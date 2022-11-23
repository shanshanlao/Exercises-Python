# Interview Question by Dropbox

# Write a query that calculates the difference between the highest salaries found in the marketing and engineering departments. 
# Output just the absolute difference in salaries.

# Import your libraries
import pandas as pd

# Start writing code
db_employee.head()

df = pd.merge(db_employee, db_dept, left_on = 'department_id', right_on = 'id')

max_marketing = max(df['salary'][df['department'] == 'marketing'])
max_engineering = max(df['salary'][df['department'] == 'engineering'])

abs(max_marketing - max_engineering)

