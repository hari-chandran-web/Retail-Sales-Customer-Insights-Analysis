import pandas as pd
import numpy as np
from data_cleaning import load_data, clean_data, prepare_data_for_analysis
from visualization import (
    plot_sales_trend,
    plot_category_performance,
    plot_regional_heatmap,
    plot_discount_impact,
    create_interactive_dashboard
)

def main():
    # Load and clean data
    print("Loading and cleaning data...")
    df = load_data("data/superstore_dataset.xlsx")
    if df is None:
        print("Error: Could not load dataset")
        return
    
    df_clean = clean_data(df)
    
    # Prepare data for analysis
    print("\nPreparing data for analysis...")
    analysis_data = prepare_data_for_analysis(df_clean)
    
    # Print summary statistics
    print("\nSummary Statistics:")
    print("\nSales by Category:")
    print(analysis_data['sales_by_category'])
    
    print("\nProfit by Region:")
    print(analysis_data['profit_by_region'])
    
    print("\nCustomer Segment Analysis:")
    print(analysis_data['customer_segment'])
    
    # Create visualizations
    print("\nGenerating visualizations...")
    
    # Static plots
    plot_sales_trend(df_clean)
    plot_category_performance(df_clean)
    plot_regional_heatmap(df_clean)
    plot_discount_impact(df_clean)
    
    # Interactive dashboard
    print("\nCreating interactive dashboard...")
    dashboard_figures = create_interactive_dashboard(df_clean)
    
    # Additional insights
    print("\nKey Insights:")
    
    # Top performing products
    top_products = df_clean.groupby('Sub-Category')[['Sales', 'Profit']].sum().sort_values('Sales', ascending=False).head()
    print("\nTop 5 Products by Sales:")
    print(top_products)
    
    # Discount analysis
    avg_profit_by_discount = df_clean.groupby('Discount')['Profit'].mean()
    print("\nAverage Profit by Discount Level:")
    print(avg_profit_by_discount)
    
    # Regional performance
    regional_performance = df_clean.groupby('Region').agg({
        'Sales': 'sum',
        'Profit': 'sum',
        'Profit Margin': 'mean'
    }).round(2)
    print("\nRegional Performance Summary:")
    print(regional_performance)

if __name__ == "__main__":
    main() 