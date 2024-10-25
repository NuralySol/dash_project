# 📊 Chipotle Best Seller Dashboard

This project is a **data visualization dashboard** built with Python's `Dash` and `Plotly`, designed to showcase key insights on Chipotle's best-selling items.

## 🚀 Project Overview

The dashboard provides interactive visualizations for exploring:

- Sales distribution and revenue by item
- Sales trends across different categories

## 🔧 Features

1. **Dynamic Visualizations**:
   - 📈 **Scatter Plot**: Displays sales distribution with customizable axes, sizes, and colors.
   - 📊 **Bar Chart**: Visualizes revenue by item and adjusts for different categories.
   - 🥧 **Pie Chart**: Shows the proportion of top items sold.
   - 📉 **Horizontal H Bar Chart**: H-Bar Chart with the horizontal bar chart in mind (color coded).

2. **Responsive Layout**:
   - Uses `Bootstrap` components for a fluid, mobile-friendly interface.
   - Modular design to easily switch between visualizations.

3. **Interactivity**:
   - Hover effects, tooltips, and color coding provide a rich user experience.
   - Dynamic resizing and customization options for each chart.

## 📁 File Structure

- `app.py` - Main application file to initialize and run the Dash server.
- `components/`
  - `bar_chart.py` - Module to render the bar chart.
  - `scatter.py` - Module to render the scatter plot.
  - `pie_chart.py` - Module to render the pie chart.
  - `h_bar_chart.py` - Module to render the horizontal age bar chart.
