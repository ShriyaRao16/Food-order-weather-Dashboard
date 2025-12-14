# Food-Order-Weather-Analysis

Weather Impact on Food Orders Dashboard
A data visualization dashboard that explores the correlation between weather conditions and food ordering behavior by combining  weather data with Zomato-style order data.
# Project Overview
This project merges up two unrelated data sources:<br>
•Weather Data: Historical temperature and precipitation data from Open-Meteo API<br>
•Food Orders: Synthetic Zomato order dataset for Indian cities<br>

The dashboard reveals interesting patterns like how rainy days impact food delivery orders and how temperature correlates with ordering behavior.<br>
# Features
Interactive city selection (Bengaluru, Mumbai, Delhi, Chennai)<br>
📅 Custom date range filtering<br>
📈 Dual-axis visualization: Orders vs Temperature<br>
🌧️ Rain impact analysis with comparative bar charts<br>
🔍 Dynamic insights and statistical analysis<br>
⚡ Real-time historical weather data fetching<br>
# Tech Stack
➣Frontend: Streamlit<br>
➣Data Processing: Pandas<br>
➣Visualization: Matplotlib<br>
➣API: Open-Meteo Historical Weather API<br>
➣Language: Python 3.8+<br>
# 📦 Installation
## Prerequisites


```bash
python 3.8+
pip
```

## Setup

```bash
git clone https://github.com/ShriyaRao16/Food-Order-Weather-Analysis.git
cd Food-Order-Weather-Analysis
```
## Create virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

## Install dependencies
```bash
pip install -r requirements.txt
```
## Usage
```bash
#Run the dashboard
streamlit run app.py
```
The dashboard will open in your browser at :<br>

# How to Use:
1.)Select a city from the dropdown<br>
2.)Choose your date range<br>
3.)View visualizations and insights<br>
4.)Analyze weather impact on food orders<br>

 ## Project Structure
 ```md
weather-food-orders-dashboard/
├── .kiro/
│   └── (Kiro AI assistant cache)
├── app.py
│   └── Main Streamlit dashboard
├── util.py
│   └── Weather data fetching utilities
├── zomato_orders_2025.csv
│   └── Sample orders dataset
├── requirements.txt
│   └── Python dependencies
├── README.md
   └── Project documentation
```
# Data Sources
1. Weather Data (Open-Meteo API)

•Source: Open-Meteo Archive API<br>
•Data: Historical temperature and precipitation<br>
•Coverage: 1940 to present<br>
•Update Frequency: Daily<br>

2. Food Orders Data

•Source: Synthetic dataset (Zomato-style)<br>
•Fields: order_date, order_id, restaurant, customer<br>
•Period: January - December 2025<br>
•Cities: Bengaluru, Mumbai, Delhi, Chennai<br>
# Key Insights
Based on our analysis:

•🌧️ Food orders tend to increase by 10-15% on rainy days<br>
•🌡️ Moderate temperatures (20-25°C) correlate with higher ordering activity<br>
•📈 Weather conditions have a measurable impact on customer behavior<br>
•🏙️ Pattern varies by city due to different climate conditions<br>

# How Kiro Accelerated Development
This project was built with assistance from Kiro AI:

➣Rapid prototyping of data visualization logic<br>
➣Quick debugging of API integration issues<br>
➣Code optimization and best practices<br>
➣UI/UX improvements and error handling<br>

Read the full blog post: [Link to AWS Builder Center Blog]

# 📸 Screenshots
<img width="935" height="797" alt="image" src="https://github.com/user-attachments/assets/181b00f2-33cf-42f8-b742-80179f9edf6d" /><br>

<img width="921" height="663" alt="image" src="https://github.com/user-attachments/assets/bc37f89b-d7fc-45f1-8df7-7b5810240d40" />

<img width="888" height="412" alt="image" src="https://github.com/user-attachments/assets/36b5c367-27ec-4bc6-8575-ebf9b0ff8f07" />

# Future Enhancements
·Add more cities and weather parameters<br>
·Implement machine learning predictions<br>
·Add real-time weather updates<br>
·Include more order metrics (revenue, cuisine types)<br>
·Add export functionality for reports<br>

 # Acknowledgments
✦Open-Meteo for providing free historical weather data API<br>
✦Streamlit for the amazing dashboard framework<br>
✦AI for Bharat for organizing this workshop<br>
✦Kiro AI for accelerating the development process<br>


