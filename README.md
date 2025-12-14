# 🍔 Food Orders vs Weather Dashboard

A Streamlit web application that analyzes the correlation between weather conditions and food ordering patterns using synthetic Zomato-style data and real-time weather information.

![Dashboard Preview](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)

## 🌟 Features

- **Multi-City Analysis**: Compare food ordering patterns across Bengaluru, Mumbai, Delhi, and Chennai
- **Interactive Date Selection**: Analyze custom date ranges with real-time validation
- **Weather Integration**: Fetches historical weather data using Open-Meteo API
- **Visual Analytics**: 
  - Line charts showing daily orders vs temperature trends
  - Bar charts comparing rainy vs non-rainy day ordering patterns
- **Smart Insights**: Automated calculation of weather impact on ordering behavior
- **Error Handling**: Graceful handling of missing data and API failures

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- Internet connection (for weather data)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/ShriyaRao16/food-weather-dashboard.git
   cd food-weather-dashboard
   ```

2. **Set up virtual environment**
   ```bash
   python -m venv .venv
   
   # On Windows
   .venv\Scripts\activate
   
   # On macOS/Linux
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

5. **Open your browser**
   - ## Access the live Streamlit app here:  
🔗 https://food-order-weather-dashboard-mrkfvvocueqdxwjthycz9t.streamlit.app/
- If not, navigate to the URL shown in your terminal
- ## 📘 Technical Blog
Read the full project write-up on AWS Builder Center:  
https://builder.aws.com/content/36psm4eSqb0feyjUqv4v3VVk4bW/exploring-the-impact-of-weather-on-food-orders-using-an-interactive-dashboard



## 📊 How It Works

1. **Select a City**: Choose from four major Indian cities
2. **Pick Date Range**: Select start and end dates for analysis
3. **View Insights**: Explore visualizations and automated insights
4. **Analyze Patterns**: Understand how weather affects food ordering

## 🏗️ Project Structure

```
food-weather-dashboard/
├── .kiro/                    # Kiro IDE specifications
│   └── specs/
│       └── weather-dashboard/
│           ├── requirements.md
│           ├── design.md
│           └── tasks.md
├── app.py                    # Main Streamlit application
├── util.py                   # Weather API integration
├── zomato_orders_2025.csv    # Sample order data
├── requirements.txt          # Python dependencies
└── README.md                # This file
```

## 🔧 Technical Details

### Data Sources
- **Order Data**: Synthetic CSV data mimicking Zomato-style food orders
- **Weather Data**: Historical weather from [Open-Meteo API](https://open-meteo.com/)

### Key Technologies
- **Streamlit**: Web application framework
- **Pandas**: Data manipulation and analysis
- **Matplotlib**: Data visualization
- **Requests**: HTTP API integration

### API Integration
The application uses the Open-Meteo Archive API for historical weather data:
- No API key required
- Supports historical data from 1940 onwards
- Provides temperature and precipitation data

## 📈 Sample Insights

The dashboard automatically generates insights such as:
- "🌧️ Food orders increase by 15.3% on rainy days"
- "🌡️ Average temperature: 24.5°C"
- "📦 Total orders in period: 1,247"

## 🛠️ Development

This project was developed using Kiro IDE's spec-driven development methodology. The complete development process is documented in the `.kiro/specs/` directory, including:

- **Requirements**: Detailed user stories and acceptance criteria
- **Design**: System architecture and correctness properties
- **Tasks**: Step-by-step implementation plan

### Running Tests

```bash
# Install test dependencies
pip install pytest hypothesis

# Run tests
pytest tests/
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Open-Meteo](https://open-meteo.com/) for providing free weather data API
- [Streamlit](https://streamlit.io/) for the excellent web app framework
- Sample data inspired by food delivery platforms like Zomato

## 📞 Support

If you encounter any issues or have questions:
1. Check the [Issues](https://github.com/yourusername/food-weather-dashboard/issues) page
2. Create a new issue with detailed description
3. Include error messages and steps to reproduce

---


**Made with ❤️ using Kiro IDE and Streamlit**

