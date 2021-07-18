from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import select

# Wracamy do lokalnej kopii
engine = create_engine('sqlite:///census.sqlite')
metadata = MetaData()
census = Table('census', metadata, autoload=True, autoload_with=engine)

# Create a select query: stmt
stmt = ____

# Add a where clause to filter the results to only those for New York : stmt_filtered
stmt = stmt.____

# Execute the query to retrieve all the data returned: results
results = ____

# Loop over the results and print the age, sex, and pop2000
for ___ in ____:
    print(result.age, ____, ____)
