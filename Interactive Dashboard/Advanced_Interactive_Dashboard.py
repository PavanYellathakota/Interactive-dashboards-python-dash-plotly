# %% [markdown]
# # Advanced Interactive Dashboard using Dash

# %%
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output
import dash_bootstrap_components as dbc
import plotly.io as pio

# Dataset
df = pd.DataFrame({
    "startup": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"],
    "revenue": [6.5, 8.2, 4.8, 7.1, 9.5, 3.8, 10.2, 7.9, 8.6, 6.3, 5.9, 11.4, 4.2, 9.8, 7.4],
    "profit": [2.8, 3.9, 1.9, 3.0, 4.5, 1.4, 5.1, 3.7, 4.2, 2.9, 2.3, 5.8, 1.6, 4.9, 3.3],
    "sector": ["Fintech", "Health", "Fintech", "EduTech", "Health", "EduTech", "Fintech", "Retail", "Retail", "Health", 
               "AI", "Fintech", "EduTech", "Retail", "AI"],
    "region": ["US", "Europe", "Asia", "Asia", "US", "Europe", "Asia", "US", "Europe", "Asia", 
               "US", "Europe", "Asia", "US", "Europe"],
    "employees": [60, 150, 40, 90, 120, 50, 250, 180, 100, 70, 80, 300, 35, 200, 110],
    "funding_stage": ["Series A", "Seed", "Series B", "Series A", "Series B", "Seed", "Series A", "Series A", 
                      "Seed", "Series B", "Series A", "Series C", "Seed", "Series B", "Series A"],
    "growth": [18, 28, 15, 20, 35, 12, 40, 25, 30, 16, 22, 45, 10, 38, 24],
    "founded_year": [2018, 2020, 2019, 2017, 2016, 2021, 2015, 2018, 2019, 2020, 
                     2017, 2014, 2022, 2016, 2018],
    "customer_count": [5000, 12000, 3000, 8000, 15000, 2000, 25000, 10000, 9000, 4000, 
                      6000, 30000, 1500, 20000, 7000],
    "market_share": [5.2, 8.1, 3.4, 6.5, 10.3, 2.8, 12.7, 7.9, 6.8, 4.5, 
                     5.9, 15.4, 2.1, 11.2, 6.3]
})

# Initialize Dash app with Bootstrap
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Layout
app.layout = dbc.Container([
    html.H1("Startup Performance Dashboard", className="text-center my-4"),
    dbc.Row([
        dbc.Col([
            html.Label("Select Sector(s):"),
            dcc.Dropdown(
                id="sector-filter",
                options=[{"label": sector, "value": sector} for sector in df["sector"].unique()],
                value=df["sector"].unique().tolist(),
                multi=True
            )
        ], width=4),
        dbc.Col([
            html.Label("Select Region(s):"),
            dcc.Dropdown(
                id="region-filter",
                options=[{"label": region, "value": region} for region in df["region"].unique()],
                value=df["region"].unique().tolist(),
                multi=True
            )
        ], width=4),
        dbc.Col([
            html.Label("Select Funding Stage(s):"),
            dcc.Dropdown(
                id="funding-filter",
                options=[{"label": stage, "value": stage} for stage in df["funding_stage"].unique()],
                value=df["funding_stage"].unique().tolist(),
                multi=True
            )
        ], width=4),
    ], className="mb-4"),
    dbc.Row([
        dbc.Col(dcc.Graph(id="pie-chart"), width=6),
        dbc.Col(dcc.Graph(id="bar-chart"), width=6),
    ]),
    dbc.Row([
        dbc.Col(dcc.Graph(id="scatter-chart"), width=6),
        dbc.Col(dcc.Graph(id="bubble-chart"), width=6),
    ])
], fluid=True)

# Callback to update charts
@app.callback(
    [
        Output("pie-chart", "figure"),
        Output("bar-chart", "figure"),
        Output("scatter-chart", "figure"),
        Output("bubble-chart", "figure")
    ],
    [
        Input("sector-filter", "value"),
        Input("region-filter", "value"),
        Input("funding-filter", "value")
    ]
)
def update_charts(selected_sectors, selected_regions, selected_funding):
    filtered_df = df[
        (df["sector"].isin(selected_sectors)) &
        (df["region"].isin(selected_regions)) &
        (df["funding_stage"].isin(selected_funding))
    ]
    
    if filtered_df.empty:
        empty_fig = go.Figure().update_layout(
            title="No Data Available",
            xaxis={"visible": False},
            yaxis={"visible": False},
            annotations=[{"text": "No data for selected filters", "xref": "paper", "yref": "paper", "showarrow": False}]
        )
        return empty_fig, empty_fig, empty_fig, empty_fig
    
    # Pie Chart: Revenue by Sector
    sector_revenue = filtered_df.groupby("sector")["revenue"].sum().reset_index()
    pie_fig = go.Figure(
        go.Pie(
            labels=sector_revenue["sector"],
            values=sector_revenue["revenue"],
            textinfo="percent+label"
        )
    )
    pie_fig.update_layout(title="Revenue by Sector", showlegend=True)
    
    # Bar Chart: Average Employees by Funding Stage
    funding_employees = filtered_df.groupby("funding_stage")["employees"].mean().reset_index()
    bar_fig = go.Figure(
        go.Bar(
            x=funding_employees["funding_stage"],
            y=funding_employees["employees"],
            marker_color="skyblue"
        )
    )
    bar_fig.update_layout(
        title="Average Employees by Funding Stage",
        xaxis_title="Funding Stage",
        yaxis_title="Average Employees"
    )
    
    # Scatter Chart: Revenue vs Profit
    scatter_fig = px.scatter(
        filtered_df,
        x="revenue",
        y="profit",
        color="growth",
        text="startup",
        hover_data=["sector", "region"]
    )
    scatter_fig.update_traces(marker=dict(size=10), textposition="top center")
    scatter_fig.update_layout(
        title="Revenue vs Profit",
        xaxis_title="Revenue ($M)",
        yaxis_title="Profit ($M)",
        showlegend=True
    )
    
    # Bubble Chart: Market Share vs Customer Count
    bubble_fig = px.scatter(
        filtered_df,
        x="customer_count",
        y="market_share",
        size="revenue",
        color="employees",
        hover_data=["startup", "sector"],
        text="startup"
    )
    bubble_fig.update_traces(textposition="top center")
    bubble_fig.update_layout(
        title="Market Share vs Customer Count",
        xaxis_title="Customer Count",
        yaxis_title="Market Share (%)",
        showlegend=True
    )
    
    return pie_fig, bar_fig, scatter_fig, bubble_fig

# Function to generate static charts and save as HTML
def save_dashboard_html():
    # Get initial figures with default filters
    selected_sectors = df["sector"].unique().tolist()
    selected_regions = df["region"].unique().tolist()
    selected_funding = df["funding_stage"].unique().tolist()
    pie_fig, bar_fig, scatter_fig, bubble_fig = update_charts(selected_sectors, selected_regions, selected_funding)
    
    # Create HTML content
    html_content = f"""
    <html>
    <head>
        <title>Startup Performance Dashboard</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 20px; }}
            h1 {{ text-align: center; }}
            .chart-container {{ display: flex; flex-wrap: wrap; justify-content: space-between; }}
            .chart {{ width: 48%; margin-bottom: 20px; }}
        </style>
    </head>
    <body>
        <h1>Startup Performance Dashboard</h1>
        <p><b>Note:</b> This is a static snapshot of the dashboard. Interactivity (e.g., dropdown filters) requires a running Dash server.</p>
        <div class="chart-container">
            <div class="chart">{pio.to_html(pie_fig, full_html=False)}</div>
            <div class="chart">{pio.to_html(bar_fig, full_html=False)}</div>
            <div class="chart">{pio.to_html(scatter_fig, full_html=False)}</div>
            <div class="chart">{pio.to_html(bubble_fig, full_html=False)}</div>
        </div>
    </body>
    </html>
    """
    
    # Save to file with utf-8 encoding
    with open("Advanced_Interactive_Dashboard.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    print("Dashboard saved as 'Advanced_Interactive_Dashboard.html'")

# Run the app and save HTML
if __name__ == "__main__":
    save_dashboard_html()  # Save static HTML snapshot
    app.run(debug=True, port=8051)  # Use port 8051 to avoid conflict


