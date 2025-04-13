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
import pandas as pd
import plotly.express as px
import plotly.io as pio
import json

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

# Prepare data for charts
# Bar Chart: Revenue by Startup
bar_fig = px.bar(df, x="startup", y="revenue", color="sector", title="Revenue by Startup")
bar_html = pio.to_html(bar_fig, include_plotlyjs=False, full_html=False)

# Pie Chart: Sector Distribution (based on startup count)
sector_counts = df["sector"].value_counts().reset_index()
sector_counts.columns = ["sector", "count"]
pie_fig = px.pie(sector_counts, names="sector", values="count", title="Sector Distribution")
pie_html = pio.to_html(pie_fig, include_plotlyjs=False, full_html=False)

# Convert DataFrame to JSON for JavaScript
df_json = json.dumps(df.to_dict(orient="records"))

# Create HTML with side-by-side charts and interactive filters
with open("startup_interactive_dashboard.html", "w", encoding="utf-8") as f:
    f.write(f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Startup Interactive Dashboard</title>
    <script src="https://cdn.plot.ly/plotly-2.35.2.min.js"></script>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 20px;
            background-color: #f9f9f9;
        }}
        .container {{
            max-width: 1200px;
            margin: auto;
        }}
        h1 {{
            text-align: center;
            color: #333;
        }}
        .filter-container {{
            display: flex;
            flex-wrap: wrap;
            gap: 20px;
            margin-bottom: 20px;
            justify-content: center;
        }}
        .filter-group {{
            display: flex;
            flex-direction: column;
        }}
        label {{
            margin-bottom: 5px;
            font-weight: bold;
        }}
        select {{
            padding: 8px;
            font-size: 16px;
            border-radius: 4px;
            width: 200px;
        }}
        .chart-container {{
            display: flex;
            flex-wrap: wrap;
            gap: 20px;
            justify-content: center;
        }}
        .chart {{
            flex: 1;
            min-width: 400px;
            max-width: 580px;
            background: white;
            padding: 15px;
            border-radius: 8px;
            box-shadow: 0 0 8px rgba(0,0,0,0.1);
        }}
        .error-message {{
            text-align: center;
            color: red;
            font-size: 18px;
        }}
        @media (max-width: 900px) {{
            .chart {{
                min-width: 100%;
            }}
        }}
        @media (max-width: 600px) {{
            select {{
                width: 100%;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Startup Interactive Dashboard</h1>
        <div class="filter-container">
            <div class="filter-group">
                <label for="sector-filter">Select Sector:</label>
                <select id="sector-filter" multiple>
                    <option value="all" selected>All Sectors</option>
                    {"".join(f'<option value="{sector}">{sector}</option>' for sector in df["sector"].unique())}
                </select>
            </div>
            <div class="filter-group">
                <label for="region-filter">Select Region:</label>
                <select id="region-filter" multiple>
                    <option value="all" selected>All Regions</option>
                    {"".join(f'<option value="{region}">{region}</option>' for region in df["region"].unique())}
                </select>
            </div>
        </div>
        <div class="chart-container">
            <div class="chart">
                <h2>Revenue by Startup</h2>
                <div id="bar-chart">{bar_html}</div>
            </div>
            <div class="chart">
                <h2>Sector Distribution</h2>
                <div id="pie-chart">{pie_html}</div>
            </div>
        </div>
    </div>

    <script>
        // Load data
        const data = {df_json};

        // Debug: Log data
        console.log("Loaded data:", data);

        // Cache original chart data
        const originalBarData = document.getElementById('bar-chart').plotly_data || {{ data: [], layout: {{}} }};
        const originalPieData = document.getElementById('pie-chart').plotly_data || {{ data: [], layout: {{}} }};

        // Filter function
        function updateCharts() {{
            try {{
                const sectorFilter = Array.from(document.getElementById('sector-filter').selectedOptions).map(opt => opt.value);
                const regionFilter = Array.from(document.getElementById('region-filter').selectedOptions).map(opt => opt.value);

                console.log("Sector filter:", sectorFilter);
                console.log("Region filter:", regionFilter);

                // Filter data
                let filteredData = data;
                if (!sectorFilter.includes('all') && sectorFilter.length > 0) {{
                    filteredData = filteredData.filter(row => sectorFilter.includes(row.sector));
                }}
                if (!regionFilter.includes('all') && regionFilter.length > 0) {{
                    filteredData = filteredData.filter(row => regionFilter.includes(row.region));
                }}

                console.log("Filtered data:", filteredData);

                // Update Bar Chart
                if (filteredData.length > 0) {{
                    Plotly.restyle('bar-chart', {{
                        x: [filteredData.map(row => row.startup)],
                        y: [filteredData.map(row => row.revenue)],
                        marker: {{ color: filteredData.map(row => {{
                            return row.sector === 'Fintech' ? '#636EFA' :
                                   row.sector === 'Health' ? '#EF553B' :
                                   row.sector === 'EduTech' ? '#00CC96' :
                                   row.sector === 'Retail' ? '#AB63FA' : '#FFA15A';
                        }})) }},
                        text: filteredData.map(row => row.startup)
                    }});
                    Plotly.relayout('bar-chart', {{
                        title: 'Revenue by Startup',
                        xaxis: {{ title: 'Startup' }},
                        yaxis: {{ title: 'Revenue ($M)' }}
                    }});
                }} else {{
                    Plotly.restyle('bar-chart', {{
                        x: [[]],
                        y: [[]],
                        text: []
                    }});
                    Plotly.relayout('bar-chart', {{ title: 'No Data Available' }});
                }}

                // Update Pie Chart
                const sectorCounts = {{}};
                filteredData.forEach(row => {{
                    sectorCounts[row.sector] = (sectorCounts[row.sector] || 0) + 1;
                }});
                if (Object.keys(sectorCounts).length > 0) {{
                    Plotly.restyle('pie-chart', {{
                        labels: [Object.keys(sectorCounts)],
                        values: [Object.values(sectorCounts)],
                        textinfo: 'percent+label'
                    }});
                    Plotly.relayout('pie-chart', {{ title: 'Sector Distribution' }});
                }} else {{
                    Plotly.restyle('pie-chart', {{
                        labels: [[]],
                        values: [[]]
                    }});
                    Plotly.relayout('pie-chart', {{ title: 'No Data Available' }});
                }}
            }} catch (e) {{
                console.error("Error updating charts:", e);
                document.getElementById('bar-chart').innerHTML = '<p class="error-message">Failed to update Bar Chart</p>';
                document.getElementById('pie-chart').innerHTML = '<p class="error-message">Failed to update Pie Chart</p>';
            }}
        }}

        // Attach event listeners
        try {{
            const sectorFilter = document.getElementById('sector-filter');
            const regionFilter = document.getElementById('region-filter');
            sectorFilter.addEventListener('change', () => {{
                console.log("Sector filter changed");
                updateCharts();
            }});
            regionFilter.addEventListener('change', () => {{
                console.log("Region filter changed");
                updateCharts();
            }});
            // Initial render
            console.log("Initializing charts");
            updateCharts();
        }} catch (e) {{
            console.error("Error setting up filters:", e);
        }}
    </script>
</body>
</html>
""")

# %%
import pandas as pd
import plotly.express as px
import plotly.io as pio
import json

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

# Prepare data for charts
# Bar Chart: Revenue by Startup
bar_fig = px.bar(df, x="startup", y="revenue", color="sector", title="Revenue by Startup")
bar_html = pio.to_html(bar_fig, include_plotlyjs=False, full_html=False)

# Pie Chart: Sector Distribution (based on startup count)
sector_counts = df["sector"].value_counts().reset_index()
sector_counts.columns = ["sector", "count"]
pie_fig = px.pie(sector_counts, names="sector", values="count", title="Sector Distribution")
pie_html = pio.to_html(pie_fig, include_plotlyjs=False, full_html=False)

# Convert DataFrame to JSON for JavaScript
df_json = json.dumps(df.to_dict(orient="records"))

# Create HTML with side-by-side charts and fixed filters
with open("startup_interactive_dashboard.html", "w", encoding="utf-8") as f:
    f.write(f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Startup Interactive Dashboard</title>
    <script src="https://cdn.plot.ly/plotly-2.35.2.min.js"></script>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 20px;
            background-color: #f9f9f9;
        }}
        .container {{
            max-width: 1200px;
            margin: auto;
        }}
        h1 {{
            text-align: center;
            color: #333;
        }}
        .filter-container {{
            display: flex;
            flex-wrap: wrap;
            gap: 20px;
            margin-bottom: 20px;
            justify-content: center;
        }}
        .filter-group {{
            display: flex;
            flex-direction: column;
        }}
        label {{
            margin-bottom: 5px;
            font-weight: bold;
        }}
        select {{
            padding: 8px;
            font-size: 16px;
            border-radius: 4px;
            width: 200px;
        }}
        .chart-container {{
            display: flex;
            flex-wrap: wrap;
            gap: 20px;
            justify-content: center;
        }}
        .chart {{
            flex: 1;
            min-width: 400px;
            max-width: 580px;
            background: white;
            padding: 15px;
            border-radius: 8px;
            box-shadow: 0 0 8px rgba(0,0,0,0.1);
        }}
        .error-message {{
            text-align: center;
            color: red;
            font-size: 18px;
        }}
        @media (max-width: 900px) {{
            .chart {{
                min-width: 100%;
            }}
        }}
        @media (max-width: 600px) {{
            select {{
                width: 100%;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>Startup Interactive Dashboard</h1>
        <div class="filter-container">
            <div class="filter-group">
                <label for="sector-filter">Select Sector:</label>
                <select id="sector-filter" multiple>
                    <option value="all" selected>All Sectors</option>
                    {"".join(f'<option value="{sector}">{sector}</option>' for sector in df["sector"].unique())}
                </select>
            </div>
            <div class="filter-group">
                <label for="region-filter">Select Region:</label>
                <select id="region-filter" multiple>
                    <option value="all" selected>All Regions</option>
                    {"".join(f'<option value="{region}">{region}</option>' for region in df["region"].unique())}
                </select>
            </div>
        </div>
        <div class="chart-container">
            <div class="chart">
                <h2>Revenue by Startup</h2>
                <div id="bar-chart">{bar_html}</div>
            </div>
            <div class="chart">
                <h2>Sector Distribution</h2>
                <div id="pie-chart">{pie_html}</div>
            </div>
        </div>
    </div>

    <script>
        // Load data
        const data = {df_json};

        // Debug: Log initial data
        console.log("Loaded data:", data);

        // Filter function
        function updateCharts() {{
            try {{
                // Get selected filter values
                const sectorFilter = Array.from(document.getElementById('sector-filter').selectedOptions).map(opt => opt.value);
                const regionFilter = Array.from(document.getElementById('region-filter').selectedOptions).map(opt => opt.value);

                console.log("Sector filter:", sectorFilter);
                console.log("Region filter:", regionFilter);

                // Filter data
                let filteredData = data;
                if (!sectorFilter.includes('all') && sectorFilter.length > 0) {{
                    filteredData = filteredData.filter(row => sectorFilter.includes(row.sector));
                }}
                if (!regionFilter.includes('all') && regionFilter.length > 0) {{
                    filteredData = filteredData.filter(row => regionFilter.includes(row.region));
                }}

                console.log("Filtered data:", filteredData);

                // Update Bar Chart
                const barData = filteredData.length > 0 ? [{{
                    x: filteredData.map(row => row.startup),
                    y: filteredData.map(row => row.revenue),
                    type: 'bar',
                    marker: {{ 
                        color: filteredData.map(row => {{
                            return row.sector === 'Fintech' ? '#636EFA' :
                                   row.sector === 'Health' ? '#EF553B' :
                                   row.sector === 'EduTech' ? '#00CC96' :
                                   row.sector === 'Retail' ? '#AB63FA' : '#FFA15A';
                        }})
                    }},
                    text: filteredData.map(row => row.startup),
                    textposition: 'auto'
                }}] : [{{
                    x: [],
                    y: [],
                    type: 'bar',
                    text: []
                }}];

                Plotly.newPlot('bar-chart', barData, {{
                    title: filteredData.length > 0 ? 'Revenue by Startup' : 'No Data Available',
                    xaxis: {{ title: 'Startup' }},
                    yaxis: {{ title: 'Revenue ($M)' }},
                    responsive: true
                }});

                // Update Pie Chart
                const sectorCounts = {{}};
                filteredData.forEach(row => {{
                    sectorCounts[row.sector] = (sectorCounts[row.sector] || 0) + 1;
                }});
                const pieData = Object.keys(sectorCounts).length > 0 ? [{{
                    labels: Object.keys(sectorCounts),
                    values: Object.values(sectorCounts),
                    type: 'pie',
                    textinfo: 'percent+label'
                }}] : [{{
                    labels: [],
                    values: [],
                    type: 'pie'
                }}];

                Plotly.newPlot('pie-chart', pieData, {{
                    title: Object.keys(sectorCounts).length > 0 ? 'Sector Distribution' : 'No Data Available',
                    responsive: true
                }});
            }} catch (e) {{
                console.error("Error updating charts:", e);
                document.getElementById('bar-chart').innerHTML = '<p class="error-message">Failed to update Bar Chart</p>';
                document.getElementById('pie-chart').innerHTML = '<p class="error-message">Failed to update Pie Chart</p>';
            }}
        }}

        // Attach event listeners
        try {{
            const sectorFilter = document.getElementById('sector-filter');
            const regionFilter = document.getElementById('region-filter');

            // Add event listeners
            sectorFilter.addEventListener('change', function() {{
                console.log("Sector filter changed:", this.value);
                updateCharts();
            }});
            regionFilter.addEventListener('change', function() {{
                console.log("Region filter changed:", this.value);
                updateCharts();
            }});

            // Initial render
            console.log("Initializing charts");
            updateCharts();
        }} catch (e) {{
            console.error("Error setting up filters:", e);
            document.getElementById('bar-chart').innerHTML = '<p class="error-message">Failed to initialize charts</p>';
            document.getElementById('pie-chart').innerHTML = '<p class="error-message">Failed to initialize charts</p>';
        }}
    </script>
</body>
</html>
""")


