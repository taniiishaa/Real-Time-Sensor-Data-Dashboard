import paho.mqtt.client as mqtt
import json
import dash
from dash import dcc, html, no_update
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go
import plotly.express as px
import threading
import pandas as pd
import datetime

# --- Configuration ---
# Note: Ensure the Broker IP is reachable on your local network
DEFAULT_BROKER = "192.168.18.16" 
DEFAULT_TOPIC = "sadatopic"
DEFAULT_PORT = 1883

mqtt_client = None
data_records = []
data_lock = threading.Lock()

# --- MQTT Logic ---
def on_message(client, userdata, message):
    global data_records
    try:
        payload = message.payload.decode("utf-8")
        data = json.loads(payload)
        
        # Expected JSON format: {"temp": 25.5, "hum": 60}
        temp_value = data.get("temp", 0)
        humidity_value = data.get("hum", 0)
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        
        with data_lock:
            data_records.append({
                "Time": timestamp, 
                "Temperature": temp_value, 
                "Humidity": humidity_value
            })
            if len(data_records) > 20:
                data_records.pop(0)
    except Exception as e:
        print(f"Data Error: {e}")

def start_mqtt(broker, port, topic):
    global mqtt_client
    if mqtt_client:
        mqtt_client.loop_stop()
        mqtt_client.disconnect()
        
    mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    mqtt_client.on_message = on_message
    mqtt_client.connect(broker, int(port), keepalive=60)
    mqtt_client.subscribe(topic)
    mqtt_client.loop_start()

# --- Dash UI Layout ---
app = dash.Dash(__name__, title="IoT Dashboard")

app.layout = html.Div([
    html.Div([
        html.H1("Real-Time IoT Sensor Dashboard", style={'color': '#2c3e50'}),
        html.P("Monitoring Temperature and Humidity via MQTT", style={'color': '#7f8c8d'})
    ], style={'textAlign': 'center', 'padding': '20px'}),

    html.Div([
        dcc.Input(id='broker', type='text', value=DEFAULT_BROKER, style={'margin': '5px'}),
        dcc.Input(id='port', type='number', value=DEFAULT_PORT, style={'margin': '5px'}),
        dcc.Input(id='topic', type='text', value=DEFAULT_TOPIC, style={'margin': '5px'}),
        html.Button('Connect', id='connect-btn', n_clicks=0, className='button-primary'),
        html.Button('Stop', id='stop-btn', n_clicks=0, style={'backgroundColor': '#e74c3c', 'color': 'white', 'marginLeft': '10px'})
    ], style={'textAlign': 'center', 'marginBottom': '30px'}),
    
    html.H4(id='date-time', style={'textAlign': 'center'}),
    dcc.Interval(id='interval-component', interval=2000, n_intervals=0), 
    
    html.Div([
        dcc.Graph(id='temp-gauge', className='six columns'),
        dcc.Graph(id='humidity-gauge', className='six columns')
    ], style={'display': 'flex'}),
    
    html.Div([
        dcc.Graph(id='temp-line', className='six columns'),
        dcc.Graph(id='humidity-line', className='six columns')
    ], style={'display': 'flex'})
], style={'fontFamily': 'Arial, sans-serif', 'backgroundColor': '#f9f9f9', 'padding': '20px'})

# --- Callbacks ---

@app.callback(
    Output('connect-btn', 'children'),
    Output('connect-btn', 'style'),
    Input('connect-btn', 'n_clicks'),
    State('broker', 'value'),
    State('port', 'value'),
    State('topic', 'value'),
    prevent_initial_call=True
)
def update_connection(n, broker, port, topic):
    if not n: return no_update, no_update
    try:
        start_mqtt(broker, port, topic)
        return "Connected ✅", {'backgroundColor': '#2ecc71', 'color': 'white'}
    except:
        return "Connection Failed (Timeout)", {'backgroundColor': '#f39c12', 'color': 'white'}

@app.callback(
    [Output('date-time', 'children'),
     Output('temp-gauge', 'figure'), Output('humidity-gauge', 'figure'),
     Output('temp-line', 'figure'), Output('humidity-line', 'figure')],
    Input('interval-component', 'n_intervals')
)
def refresh_data(n):
    now = f"Last Update: {datetime.datetime.now().strftime('%H:%M:%S')}"
    with data_lock:
        if not data_records:
            return now, go.Figure(), go.Figure(), go.Figure(), go.Figure()
        df = pd.DataFrame(data_records)

    # Gauges
    fig_t_g = go.Figure(go.Indicator(mode="gauge+number", value=df["Temperature"].iloc[-1], title={'text': "Temp °C"}, gauge={'bar': {'color': "#e74c3c"}}))
    fig_h_g = go.Figure(go.Indicator(mode="gauge+number", value=df["Humidity"].iloc[-1], title={'text': "Humidity %"}, gauge={'bar': {'color': "#3498db"}}))
    
    # Lines
    fig_t_l = px.line(df, x="Time", y="Temperature", title="Temperature Trend", template="plotly_white")
    fig_h_l = px.line(df, x="Time", y="Humidity", title="Humidity Trend", template="plotly_white")

    return now, fig_t_g, fig_h_g, fig_t_l, fig_h_l

if __name__ == "__main__":
    app.run(debug=True, use_reloader=False, host="0.0.0.0", port=8051)