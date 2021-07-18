from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table

engine = create_engine('sqlite:///census.sqlite')

metadata = MetaData()

# Reflect the census table from the engine: census
census = ____(____, ____, autoload=____, autoload_with=____)

# Print the column names
print(____)

# Print full metadata of census
print(repr(____))