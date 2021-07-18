from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import select

# Wracamy do lokalnej kopii
engine = create_engine('sqlite:///census.sqlite')
connection = engine.connect()

metadata = MetaData()
census = Table('census', metadata, autoload=True, autoload_with=engine)

# Build a query to select the state column: stmt
stmt = ____

# Order stmt by the state column
stmt = ____

# Execute the query and store the results: results
results = ____

# Print the first 10 results
print(____[:10])
