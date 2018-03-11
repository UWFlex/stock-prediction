import urllib.request
import constants
import os

basePath = os.path.dirname(os.path.realpath('__file__'))
print(basePath)


def urlBuilder(list) -> str:
    url = constants.BASEURL
    separator = '&'
    restOfURL = separator.join(list)
    url = url + restOfURL
    return url


# x = os.path.join(basePath, 'inputs\\symbol')
# print(x)
with open(os.path.join(basePath, 'inputs\\symbols'), 'r') as f:
    read_data = f.read()
f.closed

formatted_data = str(read_data).split()

for item in formatted_data:
    paramList = [
        constants.TIME_SERIES_DAILY_ADJUSTED, 'symbol=' + item,
        constants.OUTPUTSIZE_COMPACT, constants.DATATYPE_CSV, constants.API_KEY
    ]

    url = urlBuilder(paramList)
    print(url)

    urllib.request.urlretrieve(
        url, os.path.join(basePath,
                          'outputs\\test\\raw\\test_' + item + '.csv'))
