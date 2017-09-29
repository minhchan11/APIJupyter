'''
CLASS: Getting Data from APIs

Exercise 1 - retrieving US Census language use data

'''
# Link to the Census Bureau language stats API description page

# Look through the API description links and examples to see what use you have avaialble

# Use the requests library to interact with a URL

import requests
# Use a URL example in a browser to see the result returned and the use request to access with python
# http://api.census.gov/data/2013/language?get=EST,LANLABEL,NAME&for=state:06&LAN=625
r = requests.get('http://api.census.gov/data/2013/language?get=EST,LANLABEL,NAME&for=state:06&LAN=625:650')

# modify the request to get languges 625 through 650 so we can see a larger sample of what is returned from the request
# Hint the syntax for more than one language number is similar to one we use for multiple elements in a list

r = requests.get('http://api.census.gov/data/2013/language?get=EST,LANLABEL,NAME&for=state:06&LAN=625:650')
# check the status: 200 means success, 4xx means error
r.status_code

# view the raw response text
r.text

# Convert to json()
r.json()
type(r.json())
r.json()[0]
# 
#look at the contents of the output of the json() method.  Most JASON returned is a dict but it looks like this one is a list of lists

# Convert the json() method output into a dataframe with the first list as the column header and the rest as rows of data
import pandas as pd
df = pd.DataFrame(r.json()[1:],columns=r.json()[0])
# Sort the dataframe decending by the number of people speaking the language
# Check the data type of 'EST', the number of people that speak the language
df['EST'] = df['EST'].map(lambda x: pd.to_numeric(x))
df.sort_values(by='EST',ascending=False)
# Now create a new request that brings in the stats for all the US and primary languages
# See the websites links for syntax for US and range of language nunbers
r2 = requests.get('http://api.census.gov/data/2013/language?get=EST,LANLABEL,NAME&&for=state:*&LAN=601:999').json()
df2 = pd.DataFrame(r2,columns=r2[0])[1:]

### Bonus
# Create a loop that will collect the counts of Spanish language speakers by state
r3 = requests.get('http://api.census.gov/data/2013/language?get=EST,LANLABEL,NAME&for=state:*&LAN=625').json()
df3 = pd.DataFrame(r3,columns=r3[0])[1:]
df3['EST'] = df3['EST'].apply(pd.to_numeric)
df3['EST'].sum()