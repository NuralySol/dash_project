from dash import html
import dash_bootstrap_components as dbc
import bar_chart, pie_chart, scatter, age_bar_chart

def create_layout(app, data):
    heading = html.H1(
        "Chipotle Best Seller",
        className="bg-primary text-white text-center p-3 mb-4 rounded",
        style={"font-weight": "bold"}
    )

    return dbc.Container(
        fluid=True,  # Make the container fluid to span full-width on large screens
        children=[
            heading,
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.H4("Top Items Sold (Pie Chart)", className="text-center mt-3 mb-3"),
                            pie_chart.render(app, data)
                        ],
                        lg=6,
                        className="p-3"
                    ),
                    dbc.Col(
                        [
                            html.H4("Revenue by Item (Bar Chart)", className="text-center mt-3 mb-3"),
                            bar_chart.render(app, data)
                        ],
                        lg=6,
                        className="p-3"
                    ),
                ],
                className="mb-4"
            ),
            dbc.Row(
                [
                    dbc.Col(
                        [
                            html.H4("Sales Distribution (Scatter Plot)", className="text-center mt-3 mb-3"),
                            scatter.render(app, data)
                        ],
                        lg=6,
                        className="p-3"
                    ),
                    dbc.Col(
                        [
                            html.H4("H Bar Chart", className="text-center mt-3 mb-3"),
                            age_bar_chart.render(app, data)
                        ],
                        lg=6,
                        className="p-3"
                    ),
                ],
                className="mb-4"
            ),
        ],
        style={"max-width": "1200px", "margin": "auto"}  
    )