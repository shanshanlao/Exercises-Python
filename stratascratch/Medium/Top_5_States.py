# Find the top 5 states with the most 5 star businesses. 
# Output the state name along with the number of 5-star businesses and order records by the number of 5-star businesses in descending order. 
# In case there are ties in the number of businesses, return all the unique states. 
# If two states have the same result, sort them in alphabetical order.

# Import your libraries
import pandas as pd

# Select the 5-star business
df = yelp_business[yelp_business['stars'] == 5]

# Count the number of 5-star business in each state
df = df.groupby('state')['business_id'].count().reset_index()

# Rank the state based on the number of 5-star business
df['rank'] = df['business_id'].rank(ascending = False, method = 'min')
df = df.sort_values(by = ['rank','state'])

# Select the top 5 state
df[['state', 'business_id']][df['rank'] <= 5] 
