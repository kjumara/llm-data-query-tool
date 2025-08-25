"""
Utility Script to:
1. Automatically generate charts from numeric columns in a DataFrame using Matplotlib
2. Facilitate quick debugging and visualization

Intended for demonstration in the LLM-Powered Data Query Tool project
"""
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

from load_data import load_data

def choose_axes(df):
    """
    Chooses x and y_axis axes based on column types:
    x: first non-numeric column
    y_axis: first numeric column
    """

    numeric_cols = df.select_dtypes(include='number').columns.tolist()
    non_numeric_cols = df.select_dtypes(exclude='number').columns.tolist()

    if not numeric_cols:
        return None, None # In this case, there is nothing to plot

    # Handle time field cases
    if 'ORDERDATE' in df.columns:
        x_axis = 'ORDERDATE'
    elif 'YEAR_ID' in df.columns:
        x_axis = 'YEAR_ID'
        if 'YEAR_ID' in numeric_cols:
            numeric_cols.remove('YEAR_ID') # don't use as y_axis
    elif non_numeric_cols:
        x_axis = non_numeric_cols[0]
    else:
        x_axis = df.index.name if df.index.name else df.index

    # First numeric column for y_axis
    y_axis = numeric_cols[0] if numeric_cols else None
    return x_axis, y_axis

def choose_chart_type(df, x_axis, y_axis):
    """
    Chooses chart type based on x-axis type:
    - Line chart for time series (ORDERDATE)
    - Bar chart for time aggregation (YEAR_ID) or categorical
    - Scatter as fallback
    """

    if x_axis == "ORDERDATE":
        return "line"
    if x_axis == "YEAR_ID":
        return "bar"
    if df[x_axis].dtype == "object" or df[x_axis].dtype.name == "category":
        return "bar"

    return "scatter"

def format_numbers(value, position):
    return f"{int(value):,}"

def auto_chart(df, save_path: str=None):
    """
    Generate a simple chart for the first numeric column in the given DataFrame
    """

    if df.empty:
        print("DataFrame is empty. Nothing to plot.")
        return

    x_axis, y_axis = choose_axes(df)
    if x_axis is None or y_axis is None:
        print("No numeric column to plot.")
        return

    chart_type = choose_chart_type(df, x_axis, y_axis)
    print(f"Plotting {chart_type} chart: x='{x_axis}', y='{y_axis}'")

    fig, ax = plt.subplots(figsize=(8,5))

    if chart_type == "line":
        ax.plot(df[x_axis], df[y_axis],marker='o')
    else: #default to bar
        ax.bar(df[x_axis].astype(str), df[y_axis])

    ax.set_xlabel(x_axis)
    ax.set_ylabel(y_axis)
    ax.set_title(f"{chart_type.capitalize()} Chart: {y_axis} by {x_axis}")
    ax.tick_params(axis="x",rotation=45)
    ax.yaxis.set_major_formatter(FuncFormatter(format_numbers))

    # Save PNG if path is provided
    if save_path:
        plt.savefig(save_path, dpi=300, bbox_inches="tight")
        print(f"Chart saved as {save_path}")

    plt.show()

if __name__ == "__main__":
    df = load_data("sales_data_sample.csv")
    df_smaller = df.groupby('YEAR_ID')['SALES'].sum().reset_index()
    auto_chart(df_smaller, "test")