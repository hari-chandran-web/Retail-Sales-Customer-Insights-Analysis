import pandas as pd
import numpy as np
from datetime import datetime

def load_data(file_path):
    """
    Load the Superstore dataset from Excel file.
    
    Args:
        file_path (str): Path to the Excel file
        
    Returns:
        pd.DataFrame: Loaded dataset
    """
    try:
        df = pd.read_excel(file_path)
        return df
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

def clean_data(df):
    """
    Clean and prepare the dataset for analysis.
    
    Args:
        df (pd.DataFrame): Raw dataset
        
    Returns:
        pd.DataFrame: Cleaned dataset
    """
    # Create a copy to avoid modifying the original
    df_clean = df.copy()
    
    # Convert date columns to datetime
    date_columns = ['Order Date', 'Ship Date']
    for col in date_columns:
        if col in df_clean.columns:
            df_clean[col] = pd.to_datetime(df_clean[col])
    
    # Handle missing values
    df_clean = df_clean.fillna({
        'Postal Code': 'Unknown',
        'Discount': 0,
        'Profit': 0
    })
    
    # Create derived metrics
    df_clean['Profit Margin'] = (df_clean['Profit'] / df_clean['Sales'] * 100).round(2)
    df_clean['Order Year'] = df_clean['Order Date'].dt.year
    df_clean['Order Month'] = df_clean['Order Date'].dt.month
    df_clean['Order Quarter'] = df_clean['Order Date'].dt.quarter
    
    return df_clean

def prepare_data_for_analysis(df):
    """
    Prepare data for specific analysis tasks.
    
    Args:
        df (pd.DataFrame): Cleaned dataset
        
    Returns:
        dict: Dictionary containing various prepared datasets
    """
    # Sales by category
    sales_by_category = df.groupby('Category')['Sales'].agg(['sum', 'mean', 'count']).round(2)
    
    # Profit by region
    profit_by_region = df.groupby('Region')['Profit'].agg(['sum', 'mean']).round(2)
    
    # Customer segment analysis
    customer_segment = df.groupby('Segment')['Sales'].agg(['sum', 'count']).round(2)
    
    # Discount impact analysis
    discount_impact = df.groupby('Discount')['Profit'].agg(['sum', 'mean']).round(2)
    
    return {
        'sales_by_category': sales_by_category,
        'profit_by_region': profit_by_region,
        'customer_segment': customer_segment,
        'discount_impact': discount_impact
    } 