
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio

# ============================================
# 1. LOAD DATA INTO PANDAS DATAFRAMES
# ============================================
print("Loading data...")

# Dataset 1: HTTP Status Summary
status_data = {
    'Status Code': ['200 OK', '301 Redirect', '404 Not Found', '500 Server Error'],
    'Count': [120, 30, 15, 5]
}
df_status = pd.DataFrame(status_data)

# Dataset 2: Requests Over Time
time_data = {
    'Day': ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5'],
    'Total Requests': [50, 60, 55, 70, 60],
    'Error Requests': [5, 7, 6, 8, 4]
}
df_time = pd.DataFrame(time_data)

print(" Data loaded successfully")
print(f"Status Summary:\n{df_status}")
print(f"\nRequests Over Time:\n{df_time}")

# ============================================
# 2. DEFINE COLOR MAP DICTIONARY
# ============================================
color_map = {
    '200 OK': 'green',
    '301 Redirect': 'blue', 
    '404 Not Found': 'orange',
    '500 Server Error': 'red'
}

print(f"\n Color mapping defined: {color_map}")

# Create color list for consistent coloring
status_colors = [color_map[code] for code in df_status['Status Code']]

# ============================================
# 3. CREATE SUBPLOT FIGURE WITH SPECIFIED LAYOUT
# ============================================
print("\nCreating dashboard layout...")

# Create subplots with specified layout
fig = make_subplots(
    rows=2, 
    cols=2,
    subplot_titles=(
        '<b>HTTP Status Code Distribution - Bar Chart</b>',
        '<b>HTTP Status Code Distribution - Pie Chart</b>',
        '<b>Requests Over Time - Line Chart</b>'
    ),
    specs=[
        [{"type": "bar"}, {"type": "pie"}],
        [{"type": "xy", "colspan": 2}, None]
    ],
    row_heights=[0.5, 0.5],
    vertical_spacing=0.15,
    horizontal_spacing=0.2
)

print(" Subplot layout created")

# ============================================
# 4. ADD BAR CHART (Row 1, Col 1)
# ============================================
fig.add_trace(
    go.Bar(
        x=df_status['Status Code'],
        y=df_status['Count'],
        name='Status Codes',
        marker=dict(
            color=status_colors,
            line=dict(color='black', width=1)
        ),
        text=df_status['Count'],
        textposition='outside',
        textfont=dict(size=14, color='black'),
        hovertemplate='<b>%{x}</b><br>Count: %{y}<extra></extra>'
    ),
    row=1, col=1
)

print(" Bar chart added")

# ============================================
# 5. ADD PIE CHART (Row 1, Col 2)
# ============================================
fig.add_trace(
    go.Pie(
        labels=df_status['Status Code'],
        values=df_status['Count'],
        name='Status Distribution',
        marker=dict(colors=status_colors),
        textinfo='percent+label',
        textfont=dict(size=13),
        hole=0.3,
        hovertemplate='<b>%{label}</b><br>Count: %{value}<br>Percentage: %{percent:.1%}<extra></extra>',
        pull=[0.05, 0.05, 0.05, 0.1]  # Slight pull for emphasis
    ),
    row=1, col=2
)

print(" Pie chart added")

# ============================================
# 6. ADD LINE CHART (Row 2, spanning both columns)
# ============================================
# Total Requests line (points + lines)
fig.add_trace(
    go.Scatter(
        x=df_time['Day'],
        y=df_time['Total Requests'],
        mode='lines+markers',
        name='Total Requests',
        line=dict(color='blue', width=3),
        marker=dict(
            size=12,
            color='blue',
            symbol='circle',
            line=dict(color='white', width=2)
        ),
        hovertemplate='<b>%{x}</b><br>Total Requests: %{y}<extra></extra>'
    ),
    row=2, col=1
)

# Error Requests line (must be red)
fig.add_trace(
    go.Scatter(
        x=df_time['Day'],
        y=df_time['Error Requests'],
        mode='lines+markers',
        name='Error Requests',
        line=dict(color='red', width=3, dash='solid'),
        marker=dict(
            size=12,
            color='red',
            symbol='diamond',
            line=dict(color='white', width=2)
        ),
        hovertemplate='<b>%{x}</b><br>Error Requests: %{y}<extra></extra>'
    ),
    row=2, col=1
)

print(" Line chart added with two traces")

# ============================================
# 7. UPDATE LAYOUT FOR PROFESSIONAL APPEARANCE
# ============================================
print("\nApplying final formatting...")

fig.update_layout(
    title=dict(
        text='<b>NetTrack Analytics - Web Server Monitoring Dashboard</b><br><span style="font-size:16px">For DevOps Team: Request Status & Traffic Analysis</span>',
        font=dict(size=24, family='Arial, sans-serif'),
        x=0.5,
        xanchor='center',
        y=0.98
    ),
    height=900,
    width=1200,
    showlegend=True,
    legend=dict(
        title=dict(text='<b>Legend</b>'),
        orientation='h',
        yanchor='bottom',
        y=1.02,
        xanchor='center',
        x=0.5,
        bgcolor='rgba(255,255,255,0.9)',
        bordercolor='black',
        borderwidth=1
    ),
    template='plotly_white',
    plot_bgcolor='rgba(240,240,240,0.8)',
    paper_bgcolor='rgba(250,250,250,0.9)',
    hovermode='x unified'
)

# ============================================
# 8. UPDATE AXES AND ANNOTATIONS
# ============================================
# Bar chart axes
fig.update_xaxes(
    title_text='<b>HTTP Status Code</b>',
    title_font=dict(size=14),
    row=1, col=1
)
fig.update_yaxes(
    title_text='<b>Request Count</b>',
    title_font=dict(size=14),
    row=1, col=1,
    gridcolor='lightgray',
    gridwidth=1
)

# Line chart axes
fig.update_xaxes(
    title_text='<b>Day</b>',
    title_font=dict(size=14),
    row=2, col=1,
    gridcolor='lightgray',
    gridwidth=1
)
fig.update_yaxes(
    title_text='<b>Number of Requests</b>',
    title_font=dict(size=14),
    row=2, col=1,
    gridcolor='lightgray',
    gridwidth=1
)

# Update pie chart title position
fig.update_annotations(
    font=dict(size=16, family='Arial, sans-serif')
)

# Add annotations for key insights
fig.add_annotation(
    x=0.25, y=1.08,
    xref="paper", yref="paper",
    text=" 200 OK: Successful Responses",
    showarrow=False,
    font=dict(size=14, color="green")
)

fig.add_annotation(
    x=0.75, y=1.08,
    xref="paper", yref="paper",
    text=" 404/500: Client/Server Errors",
    showarrow=False,
    font=dict(size=14, color="red")
)

print(" Final formatting applied")

# ============================================
# 9. DISPLAY AND SAVE DASHBOARD
# ============================================
# Save as HTML file
html_filename = 'nettrack_analytics_dashboard.html'
fig.write_html(html_filename)
print(f"\n Dashboard saved as '{html_filename}'")

# Try to save as PNG screenshot (for deliverables)
try:
    # Install kaleido if not present: pip install kaleido
    pio.kaleido.scope.mathjax = None  # Disable MathJax for faster export
    fig.write_image(
        'dashboard_screenshot.png',
        width=1200,
        height=900,
        scale=2
    )
    print(" Screenshot saved as 'dashboard_screenshot.png'")
except Exception as e:
    print(f"  To save as PNG, install: pip install kaleido")
    print(f"   Error: {e}")

# Display the figure
print("\n Dashboard generation complete!")
print("=" * 50)
print("DELIVERABLES:")
print(f"1. Python program: {__file__}")
print(f"2. Dashboard HTML: {html_filename}")
print(f"3. Screenshot: dashboard_screenshot.png ")
print("=" * 50)

# Show the dashboard
fig.show()