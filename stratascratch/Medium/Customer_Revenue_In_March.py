# Calculate the total revenue from each customer in March 2019. 
# Include only customers who were active in March 2019.
# Output the revenue along with the customer id and sort the results based on the revenue in descending order.

# Import your libraries
import pandas as pd

# Start writing code
orders.head()

# extract month and year from date
orders['month_year'] = pd.to_datetime(orders['order_date']).dt.to_period('M')

# filter records in March 2019
df = orders[orders['month_year'] == '2019-03']

# calculate the revenue
df.groupby('cust_id')['total_order_cost'].sum().reset_index().sort_values(by='total_order_cost', ascending=False)

