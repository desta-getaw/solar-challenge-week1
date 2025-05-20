import pandas as pd
import streamlit as st
from . import utils
import utils
import sys
from pathlib import Path

import seaborn as sns
st.title("10 Acadamy AIM2 Data Visualization ")
st.markdown("This dashboard allows you to visualize data with various interactive features for **Solar Radiation Measurement** Data at MoonLight Energy Solutions")

# List of available datasets
datasets = {
    "Benin (Malanville)": "C:/Users/getde/Desktop/solar-challenge-week1/data/benin-malanville.csv",
    "Sierra Leone (Bumbuna)": "C:/Users/getde/Desktop/solar-challenge-week1/data/benin-malanville.csv",
    "Togo (Dapaong QC)": "../data/togo-dapaong_qc.csv"
}

st.sidebar.header("Dashboard By Desta Getaw")
selected_dataset = st.sidebar.selectbox("Select Dataset", list(datasets.keys()))
plot_type = st.sidebar.selectbox("Select Plot Type", ["Line Plot", "Scatter Plot", "Box Plot", "Histogram"])

data_path = datasets[selected_dataset]
data = pd.read_csv(data_path)
data = utils.clean_data(data)

#  plot settings
x_column = st.sidebar.selectbox("X-Axis", data.columns)
y_column = st.sidebar.selectbox("Y-Axis", data.columns)

# Render the appropriate plot based on the selection
if plot_type == "Line Plot":
    utils.generate_line_plot(data, x_column, y_column, "Line Plot")

elif plot_type == "Scatter Plot":
    hue_column = st.sidebar.selectbox("Hue", ["None"] + list(data.columns))
    hue = None if hue_column == "None" else hue_column
    utils.generate_scatter_plot(data, x_column, y_column, "Scatter Plot", hue=hue)

elif plot_type == "Box Plot":
    utils.generate_box_plot(data, x_column, "Box Plot")

elif plot_type == "Histogram":
    utils.generate_histogram(data, x_column, "Histogram")

# Summary statistics
st.header("Summary Statistics")
st.write(utils.get_summary_stats(data))