import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

df = pd.read_csv('raw_pre1.csv', sep='\s+', skiprows=[1,2,3,4], index_col=False)
df['Year'] = df['Year'].astype(int)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
df['Annual_Avg'] = df[months].mean(axis=1).round(4)

df['Rolling_Avg'] = df['Annual_Avg'].rolling(window=10).mean()

baseline = df[df['Year'] <= 1950]['Annual_Avg'].mean()
df['Anomaly'] = (df['Annual_Avg'] - baseline).round(4)
df['Color'] = df['Anomaly'].apply(lambda x: 'Warning' if x > 0 else 'Cooling')

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=df['Year'], y=df['Annual_Avg'],
    mode='lines', name='Annual Avg',
    line=dict(color='orange', width=1.5, dash='solid')))

fig.add_trace(go.Scatter(
    x=df['Year'], y=df['Rolling_Avg'],
    mode='lines', name='10-Year Trend',
    line=dict(color='black', width=3)))

fig.update_layout(
    title='Indian Temperature Trend (1901-2024)',
    yaxis_title='Temperature (\u00b0C)',
    xaxis_title='Year',
    template='plotly_white',
    hovermode='x unified')
fig.write_image('annual_trend.png')
print("Professional Chart Saved!")

fig2 = px.bar(df, x='Year', y='Anomaly', 
              color='Color', 
              color_discrete_map={'Warning': 'red', 'Cooling': 'steelblue'}, 
              title='Indian Temperature Anomaly (1901 To 2024) | Baseline: 1901 To 1950') 
fig2.write_image('anomaly.png')
print("fig2 Chart Saved")
