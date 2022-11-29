# Find employees who are earning more than their managers. 
# Output the employee's first name along with the corresponding salary.

# Import your libraries
import pandas as pd

# Start writing code
employee.head()

df = employee.merge(employee, left_on = 'manager_id',right_on = 'id')

df[df['salary_x'] > df['salary_y']] [['first_name_x','salary_x']]

