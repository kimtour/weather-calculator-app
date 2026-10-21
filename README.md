# Weather & Calculator Web Apps

## Project overview

Two small Python web applications share this repository: a Flask weather lookup and a FastAPI arithmetic calculator. Each has its own browser interface and can run independently.

### Purpose and users

The practical purpose is to demonstrate interactive web forms, external API calls, JSON responses and input/error handling with two Python frameworks. Intended users are people checking a city's weather or evaluating arithmetic, plus developers learning these patterns. No specific commercial customer or deployment is established.

### Inputs and outputs

The weather app accepts a city name, uses Open-Meteo geocoding to select a location, and requests its weather forecast. It returns a display name, Celsius temperature, condition/emoji, timestamp and a five-day high/low forecast for the browser. The calculator accepts an arithmetic expression and returns its result or an error. Neither application defines a database for storing user histories.

### Logic and workflow

Weather: enter city → find coordinates → request weather data → map weather codes to descriptions → display current conditions and forecast. The first geocoding result is used, so ambiguous city names may resolve unexpectedly. Calculator: enter expression → check the allowed characters → evaluate the expression → display the result or report an invalid expression/division by zero. The two flows do not depend on one another.

### Integrations

The weather app calls Open-Meteo's geocoding and forecast APIs through Requests. Flask serves its weather page, while FastAPI/Uvicorn serves the calculator and static assets. There is no external calculator service, payment integration or scheduled fetch job.

### Running, maintenance and boundaries

Start `weather.py` and/or `calculator.py` manually using the instructions below. Requests occur when users submit forms. No cloud-hosting configuration or automated test/CI pipeline is included. Local execution requires Python dependencies and internet access for weather lookup; hosting and external API usage costs/conditions depend on the chosen environment and provider. Maintain dependencies, provider response compatibility and input limits before exposing the applications publicly.

These are learning utilities, not a weather-alert service or a hardened public expression engine. The implementation does not currently request humidity or wind values despite broader UI/feature descriptions. Production authentication, resource limits, monitoring and persistent history are outside the implemented scope.

## Features

### Weather App
- Real-time weather data fetching using Open-Meteo API
- Displays current weather conditions with weather emojis
- Shows temperature, weather description and a five-day forecast
- Responsive web interface

### Calculator App
- Simple arithmetic calculator
- Supports basic operations: +, -, *, /, %
- Parentheses support for complex expressions
- Clean, modern UI

## Installation

1. Clone the repository:
```bash
git clone https://github.com/kimtour/weather-calculator-app.git
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
