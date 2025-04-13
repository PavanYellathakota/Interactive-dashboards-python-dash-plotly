# %%
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio
import numpy as np

pio.renderers.default = "browser"

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


# Display the updated DataFrame to verify
print(df.head())

# %%
# Create a subplot grid (2 rows, 3 columns) for different chart types
fig = make_subplots(
    rows=2, cols=3,
    subplot_titles=(
        "Revenue by Sector (Pie)",
        "Profit Distribution by Region (Box)",
        "Employees by Funding Stage (Bar)",
        "Revenue Trend by Founded Year (Line)",
        "Revenue vs Profit (Scatter)",
        "Market Share vs Customer Count (Bubble)"
    ),
    specs=[
        [{"type": "pie"}, {"type": "box"}, {"type": "bar"}],
        [{"type": "scatter"}, {"type": "scatter"}, {"type": "scatter"}]
    ]
)

# 1. Pie Chart: Revenue by Sector
sector_revenue = df.groupby("sector")["revenue"].sum().reset_index()
fig.add_trace(
    go.Pie(labels=sector_revenue["sector"], values=sector_revenue["revenue"], textinfo="percent+label"),
    row=1, col=1
)

# 2. Box Plot: Profit Distribution by Region
for region in df["region"].unique():
    fig.add_trace(
        go.Box(y=df[df["region"] == region]["profit"], name=region),
        row=1, col=2
    )

# 3. Bar Chart: Employees by Funding Stage
funding_employees = df.groupby("funding_stage")["employees"].mean().reset_index()
fig.add_trace(
    go.Bar(x=funding_employees["funding_stage"], y=funding_employees["employees"], 
           marker_color="skyblue"),
    row=1, col=3
)

# 4. Line Chart: Revenue Trend by Founded Year
year_revenue = df.groupby("founded_year")["revenue"].mean().reset_index()
fig.add_trace(
    go.Scatter(x=year_revenue["founded_year"], y=year_revenue["revenue"], 
               mode="lines+markers", line=dict(color="purple")),
    row=2, col=1
)

# 5. Scatter Chart: Revenue vs Profit
fig.add_trace(
    go.Scatter(
        x=df["revenue"], y=df["profit"], mode="markers", 
        text=df["startup"], marker=dict(size=10, color=df["growth"], colorscale="Viridis"),
        showlegend=False
    ),
    row=2, col=2
)

# 6. Bubble Chart: Market Share vs Customer Count
fig.add_trace(
    go.Scatter(
        x=df["customer_count"], y=df["market_share"], 
        mode="markers", 
        marker=dict(size=df["revenue"]*5, color=df["employees"], colorscale="Plasma", 
                    showscale=True),
        text=df["startup"]
    ),
    row=2, col=3
)

# Update layout with a better title and styling
fig.update_layout(
    title_text="Startup Ecosystem Insights: Performance and Growth Analysis",
    title_x=0.5,
    height=800, width=1200,
    showlegend=False,
    template="plotly_white"
)

# Update axes labels for clarity
fig.update_xaxes(title_text="Customer Count", row=2, col=3)
fig.update_yaxes(title_text="Market Share (%)", row=2, col=3)
fig.update_xaxes(title_text="Revenue ($M)", row=2, col=2)
fig.update_yaxes(title_text="Profit ($M)", row=2, col=2)
fig.update_xaxes(title_text="Founded Year", row=2, col=1)
fig.update_yaxes(title_text="Average Revenue ($M)", row=2, col=1)
fig.update_xaxes(title_text="Funding Stage", row=1, col=3)
fig.update_yaxes(title_text="Average Employees", row=1, col=3)
fig.update_yaxes(title_text="Profit ($M)", row=1, col=2)

# Save the figure as HTML
fig.write_html("startup_dashboard.html")

# Show the dashboard
fig.show()


