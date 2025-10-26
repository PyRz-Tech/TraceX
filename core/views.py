import requests
import pandas as pd
from django.shortcuts import render
from .forms import StockForm
import json
from dotenv import load_dotenv
import os

load_dotenv()

def dashboard(request):
    form = StockForm()
    context = {'form': form}
    
    if request.method == 'GET' and 'symbol' in request.GET:
        form = StockForm(request.GET)
        if form.is_valid():
            symbol = form.cleaned_data['symbol']
            interval = form.cleaned_data['interval']
            api_key = os.getenv('API_KEY')
            url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval={interval}&outputsize=full&apikey={api_key}'
            response = requests.get(url).json()
            
            if 'Time Series (' + interval + ')' in response:
                data = response['Time Series (' + interval + ')']
                df = pd.DataFrame.from_dict(data, orient='index')
                df = df.reset_index().rename(columns={'index': 'Time'})
                df.columns = ['Time', 'Open', 'High', 'Low', 'Close', 'Volume']
                df = df[['Time', 'Close', 'Volume']].tail(100)
                
                
                chart = {
                    'type': 'line',
                    'data': {
                        'labels': df['Time'].tolist(),
                        'datasets': [{
                            'label': 'Close Price',
                            'data': df['Close'].astype(float).tolist(),
                            'borderColor': '#2962FF',
                            'fill': False
                        }]
                    },
                    'options': {
                        'responsive': True,
                        'maintainAspectRatio': False
                    }
                }
                
                
                surge = ((float(df['Close'].iloc[-1]) - float(df['Close'].iloc[-2])) / float(df['Close'].iloc[-2]) * 100) if len(df) > 1 else 0
                peak = df['Close'].astype(float).max()
                dip = df['Close'].astype(float).min()
                
                context.update({
                    'symbol': symbol,
                    'table': df.to_html(classes='table table-dark table-sm', border=0),
                    'chart': json.dumps(chart),
                    'surge': f'{surge:.2f}%',
                    'peak': f'${peak:.2f}',
                    'dip': f'${dip:.2f}'
                })
            else:
                context['error'] = 'Invalid ticker or API error'
    
    return render(request, 'index.html', context)
