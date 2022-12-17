# $pip install alpha_vantage
# $python download_stock_quote.py SYMBOL
import sys
from alpha_vantage.timeseries import TimeSeries
API_KEY = 'FS3N5NXJX1IXR3EI' # get it free from https://www.alphavantage.co/

symbol = sys.argv[1]

ts = TimeSeries(key=API_KEY, output_format='pandas')
data, meta_data = ts.get_daily(symbol, outputsize='full')
data.to_csv(f'./datasets/stocks/{symbol}.csv')
