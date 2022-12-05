# Find the customer with the highest daily total order cost between 2019-02-01 to 2019-05-01. 
# If customer had more than one order on a certain day, sum the order costs on daily basis. 
# Output customer's first name, total cost of their items, and the date.

# For simplicity, you can assume that every first name in the dataset is unique.

# Import your libraries
import pandas as pd

# Start writing code
customers.head()

# Merge the two dataframes
df = customers.merge(orders, left_on = 'id', right_on = 'cust_id')

# Reformat the date 
df['order_date'] = df['order_date'].dt.strftime('%Y-%m-%d')

# Filter the orders between 2019-02-1 to 2019-05-01
df = df[(df['order_date'] >= '2019-02-01') & (df['order_date'] <= '2019-05-01')]

# Sum the order costs on daily basis
df = df.groupby(['first_name','order_date'])['total_order_cost'].sum().reset_index() 

# Return the highest cost orders
df.loc[[df['total_order_cost'].idxmax()]]

