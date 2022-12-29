# Find the rate of processed tickets for each type.

# Import your libraries
import pandas as pd

# Start writing code
facebook_complaints.head()
df = facebook_complaints

a = df.groupby('type').sum()['processed'].reset_index()
b = df.groupby('type').count()['processed'].reset_index()

new_df = a.merge(b, on='type')
new_df['processed_rate'] = new_df['processed_x'] / new_df['processed_y']

new_df.drop(['processed_x','processed_y'],axis=1)
