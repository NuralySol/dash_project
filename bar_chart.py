import plotly.express as px
from dash import html, dcc

def render(app, data, x="item_name", y="order_price", color=None, title="Bar Chart of the Foods", chart_id="bar-chart"):
    fig = px.bar(
        data,
        x=x,
        y=y,
        color=color,
        title=title
    )
    
    fig.update_layout(
        xaxis_title=x.replace("_", " ").title(),
        yaxis_title=y.replace("_", " ").title(),
    )
    
    return html.Div(dcc.Graph(figure=fig), id=chart_id)