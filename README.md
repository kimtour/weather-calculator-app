# Weather & Calculator Web Apps

A simple web application bundle containing a weather app and a calculator, built with Flask and FastAPI.

## Features

### Weather App
- Real-time weather data fetching using Open-Meteo API
- Displays current weather conditions with weather emojis
- Shows temperature, humidity, wind speed, and weather description
- Responsive web interface

### Calculator App
- Simple arithmetic calculator
- Supports basic operations: +, -, *, /, %
- Parentheses support for complex expressions
- Clean, modern UI

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/weather-calculator-app.git
cd weather-calculator-app
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Weather App
```bash
python weather.py
```
Then open your browser and navigate to `http://localhost:5000`

### Calculator App
```bash
python calculator.py
```
Then open your browser and navigate to `http://localhost:8000`

## Project Structure

```
.
├── weather.py              # Flask weather app
├── calculator.py           # FastAPI calculator app
├── requirements.txt        # Python dependencies
├── static/                 # Static files (CSS, JS)
│   └── index.html         # Calculator UI
└── templates/             # HTML templates
    └── weather.html       # Weather app UI
```

## API Endpoints

### Weather App
- `GET /` - Main weather page
- `POST /api/weather` - Fetch weather data
  - Request body: `{"city": "city_name"}`
  - Response: Weather data with emoji and description

### Calculator App
- `GET /` - Calculator page
- `POST /api/calc` - Calculate expression
  - Request body: `{"expression": "2+2"}`
  - Response: `{"expression": "2+2", "result": 4}`

## Technologies

- **Backend**: Flask, FastAPI, Uvicorn
- **Frontend**: HTML, CSS, JavaScript
- **APIs**: Open-Meteo Weather API

## License

This project is open source and available under the MIT License.

## Author

Created as a practice project for web development.
