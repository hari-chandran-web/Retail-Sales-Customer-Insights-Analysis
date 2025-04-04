import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

def set_style():
    """Set the style for all visualizations."""
    plt.style.use('seaborn')
    sns.set_palette("husl")
    plt.rcParams['figure.figsize'] = (12, 8)
    plt.rcParams['font.size'] = 12

def plot_sales_trend(df):
    """
    Create a time series plot of sales over time.
    
    Args:
        df (pd.DataFrame): Cleaned dataset
    """
    set_style()
    monthly_sales = df.groupby('Order Date')['Sales'].sum().reset_index()
    
    plt.figure(figsize=(15, 7))
    plt.plot(monthly_sales['Order Date'], monthly_sales['Sales'])
    plt.title('Monthly Sales Trend')
    plt.xlabel('Date')
    plt.ylabel('Sales ($)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_category_performance(df):
    """
    Create a bar chart showing sales by category.
    
    Args:
        df (pd.DataFrame): Cleaned dataset
    """
    set_style()
    category_sales = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)
    
    plt.figure(figsize=(12, 6))
    sns.barplot(x=category_sales.index, y=category_sales.values)
    plt.title('Sales by Category')
    plt.xlabel('Category')
    plt.ylabel('Total Sales ($)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_regional_heatmap(df):
    """
    Create a heatmap showing sales performance by region and category.
    
    Args:
        df (pd.DataFrame): Cleaned dataset
    """
    set_style()
    pivot_table = df.pivot_table(
        values='Sales',
        index='Region',
        columns='Category',
        aggfunc='sum'
    )
    
    plt.figure(figsize=(12, 8))
    sns.heatmap(pivot_table, annot=True, fmt='.0f', cmap='YlOrRd')
    plt.title('Sales Heatmap by Region and Category')
    plt.tight_layout()
    plt.show()

def plot_discount_impact(df):
    """
    Create a scatter plot showing the relationship between discount and profit.
    
    Args:
        df (pd.DataFrame): Cleaned dataset
    """
    set_style()
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='Discount', y='Profit', alpha=0.5)
    plt.title('Impact of Discount on Profit')
    plt.xlabel('Discount (%)')
    plt.ylabel('Profit ($)')
    plt.tight_layout()
    plt.show()

def create_interactive_dashboard(df):
    """
    Create an interactive dashboard using Plotly.
    
    Args:
        df (pd.DataFrame): Cleaned dataset
    """
    # Sales trend
    fig1 = px.line(
        df.groupby('Order Date')['Sales'].sum().reset_index(),
        x='Order Date',
        y='Sales',
        title='Interactive Sales Trend'
    )
    
    # Category performance
    fig2 = px.bar(
        df.groupby('Category')['Sales'].sum().reset_index(),
        x='Category',
        y='Sales',
        title='Sales by Category'
    )
    
    # Regional performance
    fig3 = px.pie(
        df.groupby('Region')['Sales'].sum().reset_index(),
        values='Sales',
        names='Region',
        title='Sales Distribution by Region'
    )
    
    return [fig1, fig2, fig3] 