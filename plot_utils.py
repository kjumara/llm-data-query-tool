"""
Utility Script to:
1. Automatically generate charts from numeric columns in a DataFrame using Matplotlib
2. Facilitate quick debugging and visualization

Intended for demonstration in the LLM-Powered Data Query Tool project
"""
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

from load_data import load_data

def auto_chart(df, save_path: str=None):
    """
    Generate a simple chart for the first numeric column in the given DataFrame
    and return the matplotlib figure (for Streamlit inline display).
    """

    if df.empty:
        print("DataFrame is empty. Nothing to plot.")
        return None

    # Identify numeric and non-numeric columns
    numeric_cols = df.select_dtypes(include='number').columns.tolist()
    time_cols = [c for c in df.columns if c in ["ORDERDATE", "YEAR_ID"]]

    # remove x-axis from candidates for y-axis
    y_candidates = [c for c in numeric_cols if c not in time_cols]

    if not y_candidates:
        print("No numeric column to plot.")
        return None
    y_axis = y_candidates[0]

    # Priority for x-axis: datetime or year_ID
    if time_cols:
        x_axis = time_cols[0]
        chart_type = "line"
    else:
        x_axis = df.select_dtypes(exclude='number').columns[0]
        chart_type = "bar"

    # If YEAR_ID, convert to int for clean x-axis
    if x_axis == "YEAR_ID":
        df[x_axis] = df[x_axis].astype(int)

    fig, ax = plt.subplots(figsize=(8,5))

    if chart_type == "line":
        # treat YEAR_ID as categorical to avoid fractional ticks
        if x_axis == "YEAR_ID":
            ax.plot(df[x_axis].astype(str), df[y_axis],marker='o')
        else:
            ax.plot(df[x_axis], df[y_axis],marker='o')
    else: #default to bar
        ax.bar(df[x_axis].astype(str), df[y_axis])

    ax.set_xlabel(x_axis)
    ax.set_ylabel(y_axis)
    ax.set_title(f"{chart_type.capitalize()} Chart: {y_axis} by {x_axis}")
    ax.tick_params(axis="x",rotation=45)
    ax.yaxis.set_major_formatter(FuncFormatter(lambda x, _: f"{int(x):,}"))

    return fig