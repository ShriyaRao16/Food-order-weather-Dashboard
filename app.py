import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from util import get_weather_data

st.set_page_config(
    page_title="Food Orders vs Weather Dashboard",
    layout="centered"
)

st.title("🍔 Food Orders vs Weather Impact (2025)")
st.write(
    "This dashboard explores how weather conditions influence food ordering behavior "
    "using synthetic Zomato-style order data and live weather data."
)

city = st.selectbox(
    "Select City",
    ["Bengaluru", "Mumbai", "Delhi", "Chennai"]
)

try:
    # Load orders data
    orders_df = pd.read_csv("zomato_orders_2025.csv")
    
    # Aggregate to daily orders
    daily_orders = orders_df.groupby("order_date").size().reset_index(name="orders")
    daily_orders.rename(columns={"order_date": "date"}, inplace=True)
    daily_orders["date"] = pd.to_datetime(daily_orders["date"])
    
    # ------------------- DATE FILTER -------------------
    # Limit max date to yesterday (API limitation)
    yesterday = (datetime.now() - timedelta(days=1)).date()
    
    min_date = daily_orders["date"].min().date()
    max_date = min(daily_orders["date"].max().date(), yesterday)
    
    start_date = st.date_input("Start Date", min_date, min_value=min_date, max_value=max_date)
    end_date = st.date_input("End Date", max_date, min_value=min_date, max_value=max_date)
    
    # Validate date range
    if start_date > end_date:
        st.error("❌ Start date must be before end date")
        st.stop()
    
    if end_date > yesterday:
        st.warning(f"⚠️ Weather data is only available until {yesterday}. Adjusting end date.")
        end_date = yesterday
    
    # ------------------- LOAD WEATHER DATA -------------------
    with st.spinner(f"Fetching weather data for {city}..."):
        weather_df = get_weather_data(city, start_date, end_date)
    
    if weather_df is None or weather_df.empty:
        st.error("❌ Failed to fetch weather data. Please try again.")
        st.stop()
    
    # ------------------- MERGE DATA -------------------
    weather_df["date"] = pd.to_datetime(weather_df["date"])
    df = pd.merge(daily_orders, weather_df, on="date", how="inner")
    
    # Filter by date range
    filtered_df = df[(df["date"] >= pd.to_datetime(start_date)) &
                     (df["date"] <= pd.to_datetime(end_date))]
    
    if filtered_df.empty:
        st.warning("⚠️ No data available for the selected date range.")
        st.stop()
    
    # ------------------- VISUALIZATION 1 -------------------
    st.subheader("📈 Daily Food Orders vs Temperature")
    
    fig1, ax1 = plt.subplots(figsize=(12, 5))
    ax1.plot(filtered_df["date"], filtered_df["orders"], label="Orders", 
             color="orange", linewidth=2, marker='o', markersize=4)
    ax1.plot(filtered_df["date"], filtered_df["temp"], label="Temperature (°C)", 
             color="blue", linewidth=2, marker='s', markersize=4)
    ax1.set_xlabel("Date", fontsize=12)
    ax1.set_ylabel("Value", fontsize=12)
    ax1.legend(fontsize=10)
    ax1.grid(True, alpha=0.3)
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    st.pyplot(fig1)
    plt.close()
    
    # ------------------- VISUALIZATION 2 -------------------
    st.subheader("🌧️ Impact of Rain on Food Orders")
    
    rain_analysis = filtered_df.groupby("rain")["orders"].mean()
    
    fig2, ax2 = plt.subplots(figsize=(6, 4))
    
    # Fix: Properly assign colors based on rain status
    bar_colors = []
    labels = []
    for rain_val in rain_analysis.index:
        if rain_val == 0 or rain_val == 0.0:
            bar_colors.append("lightgreen")
            labels.append("No Rain")
        else:
            bar_colors.append("skyblue")
            labels.append("Rain")
    
    # Create bar chart with proper colors
    bars = ax2.bar(range(len(rain_analysis)), rain_analysis.values, color=bar_colors)
    
    ax2.set_xticks(range(len(rain_analysis)))
    ax2.set_xticklabels(labels, rotation=0)
    ax2.set_ylabel("Average Orders", fontsize=12)
    ax2.set_xlabel("Weather Condition", fontsize=12)
    ax2.grid(True, alpha=0.3, axis='y')
    
    plt.tight_layout()
    st.pyplot(fig2)
    plt.close()
    
    # ------------------- INSIGHTS -------------------
    st.subheader("🔍 Key Insights")
    
    # Calculate insights dynamically
    rainy_days = filtered_df[filtered_df['rain'] == 1]
    no_rain_days = filtered_df[filtered_df['rain'] == 0]
    
    insights = []
    
    if len(rainy_days) > 0 and len(no_rain_days) > 0:
        rainy_avg = rainy_days['orders'].mean()
        no_rain_avg = no_rain_days['orders'].mean()
        
        if rainy_avg > no_rain_avg:
            percentage = ((rainy_avg/no_rain_avg - 1) * 100)
            insights.append(f"🌧️ Food orders increase by {percentage:.1f}% on rainy days")
        else:
            percentage = ((1 - rainy_avg/no_rain_avg) * 100)
            insights.append(f"☀️ Food orders decrease by {percentage:.1f}% on rainy days")
    else:
        insights.append("• Limited rain data for analysis in this period")
    
    insights.append(f"🌡️ Average temperature: {filtered_df['temp'].mean():.1f}°C")
    insights.append(f"📦 Total orders in period: {filtered_df['orders'].sum():,}")
    insights.append(f"📅 Days analyzed: {len(filtered_df)}")
    
    for insight in insights:
        st.success(insight)
    
except FileNotFoundError:
    st.error("❌ Error: 'zomato_orders_2025.csv' file not found. Please ensure the file is in the same directory.")
except Exception as e:
    st.error(f"❌ An error occurred: {str(e)}")
    import traceback
    st.code(traceback.format_exc())