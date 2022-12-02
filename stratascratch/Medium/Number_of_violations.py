# You're given a dataset of health inspections. 
# Count the number of violation in an inspection in 'Roxanne Cafe' for each year. 
# If an inspection resulted in a violation, there will be a value in the 'violation_id' column. 
# Output the number of violations by year in ascending order.

# Import your libraries
import pandas as pd

# Start writing code
sf_restaurant_health_violations.head()
df = sf_restaurant_health_violations

# Filter Business by name
df = df[df['business_name'] == 'Roxanne Cafe']

# Extract year from date
df['year'] = df['inspection_date'].dt.year

# count the number of insepction_id and group it by year
df.groupby('year')['inspection_id'].count().reset_index().sort_values(by = 'year')
