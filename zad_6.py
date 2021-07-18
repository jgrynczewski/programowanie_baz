from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table

engine = create_engine('sqlite:///census.sqlite')
connection = engine.connect()
metadata = MetaData()

# Import select
from sqlalchemy import select

# Reflect census table via engine: census
census = Table('census', metadata, autoload=True, autoload_with=engine)

# Build select statement for census table: stmt
stmt = select([census])

# Print the emitted statement to see the SQL string
print(stmt)

# Execute the statement on connection and fetch 10 records: result
results = connection.execute(stmt).fetchmany(size=10)

# Get the first row of the results by using an index: first_row
first_row = ____

# Print the first row of the results
print(first_row)

# Print the first column of the first row by accessing it by its index
print(____)

# Print the 'state' column of the first row by using its name
print(____)