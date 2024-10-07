import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots

df = pd.read_csv('GlobalTemperatures.csv')
df['dt'] = pd.to_datetime(df['dt'])

fig = make_subplots(rows=1, cols=1)

fig.add_trace(go.Scatter(
    x=df['dt'], 
    y=df['LandAverageTemperature'], 
    mode='lines+markers',
    name='Land Average Temperature'
))

fig.add_trace(go.Scatter(
    x=df['dt'],
    y=df['LandAverageTemperatureUncertainty'],
    mode='lines+markers',
    name='Temperature Uncertainty',
    line=dict(dash='dash')
))

fig.update_layout(
    title="Temperature Dashboard",
    xaxis_title="Date",
    yaxis_title="Temperature (°C)",
    template="plotly_dark"
)

fig.show()