# Classify each business as either a restaurant, cafe, school, or other. 
## A restaurant should have the word 'restaurant' in the business name. 
## For cafes, either 'cafe', 'café', or 'coffee' can be in the business name. 
## 'School' should be in the business name for schools. All other businesses should be classified as 'other'. 
## Output the business name and the calculated classification.


# Import your libraries
import pandas as pd

# Start writing code
sf_restaurant_health_violations.head()

df = sf_restaurant_health_violations.drop_duplicates(subset=['business_name'])

business_type = [None] * len(df)
for index, string in enumerate(df['business_name']):
    if 'cafe' in string.lower():
        business_type[index] = 'cafe'
    elif 'café' in string.lower():
        business_type[index] = 'cafe'
    elif 'coffee' in string.lower():
        business_type[index] = 'cafe'
    elif 'school' in string.lower():
        business_type[index] = 'school'
    elif 'restaurant' in string.lower():
        business_type[index] = 'restaurant'
    else:
        business_type[index] = 'other'

df['business_type'] = business_type

df[['business_name','business_type']]
