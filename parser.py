import urllib.request
import constants

def urlBuilder (list) -> str:
    url = constants.BASEURL
    separator = '&' 
    restOfURL = separator.join(list)
    url = url + restOfURL
    return url
    
with open('inputs/symbols', 'r') as f:
    read_data = f.read()
f.closed

formatted_data = str(read_data).split()

paramList = [constants.TIME_SERIES_DAILY_ADJUSTED,
'symbol=' + formatted_data[0],
constants.OUTPUTSIZE_COMPACT,
constants.DATATYPE_CSV,
constants.API_KEY]

url = urlBuilder(paramList)
print (url)

urllib.request.urlretrieve(url,'outputs/test')
