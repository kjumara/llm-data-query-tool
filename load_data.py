"""
Utility Script to:
1. Load a CSV dataset into a Pandas DataFrame, handling encoding issues
2. Perform basic queries (filter by product, year, and country)
3. Generates summary insights from filtered results

Intended for demonstration in the LLM-Powered Data Query Tool project
"""

import pandas as pd

def load_data(file_path) -> pd.DataFrame:
    """
    Load a CSV dataset into a Pandas DataFrame
    Args: file_path (str): Path to the CSV file
    Returns: pd.DataFrame: The loaded DataFrame. Returns an empty DataFrame if loading fails.
    """
    for encoding in ['utf-8', 'ISO-8859-1', 'latin-1']:
        try:
            df = pd.read_csv(file_path, encoding=encoding)
            print(f"Data loaded successfully with encoding: {encoding}")
            return df
        except UnicodeDecodeError:
            print(f"Failed to load data with encoding: {encoding}")
            print("Trying next encoding...")
        except FileNotFoundError:
            print(f"File not found at path: {file_path}")
            return pd.DataFrame()
        except Exception as e:
            print(f"Error loading data: {str(e)}")
            return pd.DataFrame()
    print("All encodings failed. Returning empty DataFrame.")
    return pd.DataFrame()

def query_data(
    data: pd.DataFrame,
    product: str = None,
    year: int = None,
    country: str = None,
) -> pd.DataFrame:
    """
    Perform basic queries on the DataFrame
    Args:
        data (pd.DataFrame): The DataFrame to query
        product (str, optional): The product name to filter by.
        year (int, optional): The year to filter by.
        country (str, optional): The country to filter by.
    Returns: pd.DataFrame: The filtered DataFrame
    """
    filtered_df = data.copy()
    if product:
        filtered_df = filtered_df[filtered_df['PRODUCTLINE'] == product]
    # Filter by year
    if year:
        filtered_df = filtered_df[filtered_df['YEAR_ID'] == year]
    # Filter by country
    if country:
        filtered_df = filtered_df[filtered_df['COUNTRY'] == country]
    return filtered_df

def summarize_data(df: pd.DataFrame) -> None:
    """
    Print key insights from the filtered dataset

    Args: df: pd.DataFrame: The filtered dataset.
    """
    if df.empty:
        print("No data available for the selected filters.")
        return

    # Ensure ORDERDATE is datetime for proper summarization
    df_sum = df.copy()
    df_sum['ORDERDATE'] = pd.to_datetime(df_sum['ORDERDATE'], errors='coerce')
    df_sum = df_sum.dropna(subset=['ORDERDATE'])

    total_sales = (df_sum['SALES'].sum() if 'SALES' in df_sum.columns else None)
    unique_customers = (df_sum['CUSTOMERNAME'].nunique() if 'CUSTOMERNAME' in df_sum.columns else None)
    date_min = df_sum['ORDERDATE'].min().strftime('%Y-%m-%d')
    date_max = df_sum['ORDERDATE'].max().strftime('%Y-%m-%d')

    print("\nSummary Insights:")
    if total_sales is not None:
        print(f"- Total sales: ${total_sales:,.2f}")
    if unique_customers is not None:
        print(f"- Unique customers: ${unique_customers}")
    print(f"- Date Range: {date_min} to {date_max}")

    if 'PRODUCTCODE' in df_sum.columns and 'SALES' in df_sum.columns:
        top_products = (
            df_sum.groupby('PRODUCTCODE')['SALES'].sum().sort_values(ascending=False).head(5)
        )
    print(f"Top 5 Products by Sales:")
    for product_code, sales in top_products.items():
        print(f"- {product_code}: ${sales:.2f}")

if __name__ == "__main__":
    file = "sales_data_sample.csv"
    df = load_data(file)
    
    if not df.empty:
        # Filters dataframe by product line
        print("\nAvailable Product Lines:")
        product_lines = sorted(df["PRODUCTLINE"].dropna().unique())
        for index, item in enumerate(product_lines, start=1):
            print(f"{index}. {item}")

        product_choice = input("\nEnter product number to filter by (or press enter to skip):").strip()
        product_filter = None
        if product_choice.isdigit():
            if 0 < int(product_choice) <= len(product_lines):
                product_filter = product_lines[int(product_choice)-1]
            else:
                print("Product number not found. Filter skipped.")

        # Filters dataframe by year
        year_choice = input("\nEnter year (2003, 2004, or 2005) to filter by (or press enter to skip):").strip()
        year_filter = None
        if year_choice.isdigit():
            if year_choice in range(2003, 2005):
                year_filter = year_choice
            else:
                print("Year out of range. Filter skipped.")
        else:
            print("Invalid year. Filter skipped.")

        # filters dataframe by country
        print("\nCountries to filter:")
        countries = sorted(df["COUNTRY"].dropna().unique())
        for index, country in enumerate(countries, start=1):
            print(f"{index}. {country}")

        country_choice = input("\nEnter country number (or press enter to skip):").strip()
        country_filter = None
        if country_choice.isdigit():
            if 0 < int(country_choice) <= len(countries):
                country_filter = countries[int(country_choice)-1]
            else:
                print("Country number not found. Filter skipped.")
        else:
            print("Country number not found. Filter skipped.")
        results = query_data(df, product=product_filter, year=year_filter, country=country_filter)

        print(results.head())
        summarize_data(results)