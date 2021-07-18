from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table

engine = create_engine('sqlite:///census.sqlite')
connection = engine.connect()

metadata = MetaData()

# Import select
from ____ import ____

# Reflect census table via engine: census
census = Table('census', metadata, autoload=True, autoload_with=engine)

# Build select statement for census table: stmt
stmt = ____

# Print the emitted statement to see the SQL string
print(stmt)

# Execute the statement on connection and fetch 10 records: result
results = ____.____(____).____(size=___)

# Execute the statement and print the results
print(results)