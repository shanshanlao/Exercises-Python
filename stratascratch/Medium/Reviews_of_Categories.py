# Interview Question by Yelp: Reviews of Categories

# Find the top business categories based on the total number of reviews. 
# Output the category along with the total number of reviews. 
# Order by total reviews in descending order.

# Import your libraries
import pandas as pd

# Start writing code
yelp_business.head()

# Get the number of records
n = yelp_business.shape[0]

cat = {}
for i in range(n):
    temp_list = yelp_business['categories'].str.split(';').tolist()
    cnt = yelp_business['review_count'][i]
    for key in temp_list[i]:
        if key in cat:
            cat[key] += cnt
        else:
            cat[key] = cnt

df = pd.DataFrame(cat.items(), columns=['categories','total_reviews'])
df.sort_values(by = ['total_reviews'], ascending = False)

