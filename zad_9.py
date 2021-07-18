from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import select

# Wracamy do lokalnej kopii
engine = create_engine('sqlite:///census.sqlite')
connection = engine.connect()

metadata = MetaData()
census = Table('census', metadata, autoload=True, autoload_with=engine)

# Define a list of states for which we want results
states = ['New York', 'California', 'Texas']

# Create a query for the census table: stmt
stmt = select(____)

# Append a where clause to match all the states in_ the list states
stmt = stmt.where(____)

# Loop over the ResultProxy and print the state and its population in 2000
for ____ in connection.execute(____):
    print(____, ____)
