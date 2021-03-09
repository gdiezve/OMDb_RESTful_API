from api import *
from data_cleaning import *
import memcache

# Ask for the title to search
inp = input('Insert the title you want to search:\n')

# Clean input data
inp_clean = get_clean_input(inp)

client = memcache.Client([('localhost', 8080)])
result = client.get(inp_clean)

if result is None:
    print('Sending request to OMDb API...\n')
    # Request title to OMDb API
    result = get_data(inp)

    # Cache the result for next time
    client.set(inp_clean, result)
else:
    print('Title obtained from cache.\n')

print(result)
