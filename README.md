# TradeX

A simple Django web app that pulls intraday stock prices from the Alpha Vantage API. It shows a cool line chart of closing prices, calculates stats like surge (price change %), peak, and dip prices, and displays a table with recent data.

## Features

- **Stock Form**: Enter a stock symbol (e.g., AAPL) and time interval (e.g., 5min).
- **Chart**: Line chart of closing prices using Chart.js.
- **Stats**: Shows surge (%), highest (peak), and lowest (dip) prices from the last 100 data points.
- **Table**: Lists time, closing price, and volume.
- **Sleek UI**: Dark theme with Bootstrap 5, Font Awesome, and custom CSS.
- **Error Handling**: Red error message for invalid symbols or API issues.
- **Loader**: Spinning animation while data loads.

## Prerequisites

- Python 3.8 or higher.
- An API key from [Alpha Vantage](https://www.alphavantage.co/). Grab a free one (5 API calls/minute limit).

## Installation

1. **Clone the Repo**:
   ```
   git clone <your-repo-url>
   cd tradex
   ```

2. **Set Up Virtual Environment** (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   If you have a `requirements.txt`:
   ```
   pip install -r requirements.txt
   ```
   Otherwise, install manually:
   ```
   pip install django requests pandas python-dotenv
   ```

4. **Set Up Environment Variables**:
   Create a `.env` file in the project root with your API key:
   ```
   API_KEY=your_alpha_vantage_api_key
   ```

5. **Run Migrations** (uses SQLite by default):
   ```
   python manage.py migrate
   ```

6. **Start the Server**:
   ```
   python manage.py runserver
   ```
   Open `http://127.0.0.1:8000/` in your browser.

## Usage

1. Go to `http://127.0.0.1:8000/`.
2. Enter a stock symbol (e.g., `IBM`) and interval (e.g., `5min`).
3. Hit **Track** to load data.
4. Check out the chart, stats (surge, peak, dip), and table.
5. If something’s wrong (e.g., bad symbol), you’ll see an error message.

### Example
- Symbol: `AAPL`
- Interval: `5min`
- Output: Chart of last 100 closing prices, surge (e.g., `1.23%`), peak (e.g., `$150.45`), dip (e.g., `$140.00`), and a data table.

## Project Structure

- **`views.py`**: Handles form input, fetches API data, processes it with Pandas, builds the chart, and calculates stats (surge, peak, dip).
- **`index.html`**: Django template for the form, loader, error message, stats, chart, and table.
- **`forms.py`** (assumed): Defines the form for symbol and interval.
- **Other Files**: Standard Django setup (`urls.py`, `settings.py`). Uses CDNs for Bootstrap and Chart.js.

## How It Works

- Fetches data from Alpha Vantage’s `TIME_SERIES_INTRADAY` endpoint.
- Processes the last 100 data points with Pandas.
- Renders a Chart.js line chart for closing prices.
- Calculates:
  - Surge: % change between the last two closing prices.
  - Peak: Highest closing price.
  - Dip: Lowest closing price.

## Limitations

- Free Alpha Vantage API has limits (5 calls/min, 500/day). Get a premium key for heavy use.
- Only supports intraday data (1min to 60min intervals).
- No user accounts or real-time updates (would need WebSockets).
- Basic error handling for invalid inputs or API failures.

## Troubleshooting

- **API Issues**: Check your `.env` API key. Test the API in a browser or with curl.
- **No Data**: Ensure the symbol is valid (e.g., listed on NYSE/NASDAQ).
- **Chart Not Showing**: Check if JavaScript is enabled and CDNs aren’t blocked.
- **Dependency Problems**: Run `pip list` to confirm packages are installed.
