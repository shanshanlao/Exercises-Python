# Find the top 5 businesses with most reviews. 
# Assume that each row has a unique business_id such that the total reviews for each business is listed on each row. 
# Output the business name along with the total number of reviews and order your results by the total reviews in descending order.

# Import your libraries
import pandas as pd

# Start writing code
yelp_business.head()

yelp_business[['name','review_count']].nlargest(5, 'review_count')

