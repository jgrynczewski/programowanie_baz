# Import create_engine, MetaData, and Table
from sqlalchemy import create_engine
from sqlalchemy import ____
from sqlalchemy import ____

# Create engine: engine
engine = create_engine('sqlite:///census.sqlite')

# Create a metadata object: metadata
metadata = ____

# Reflect census table from the engine: census
census = Table(____, ____, autoload=____, autoload_with=____)

# Print census table metadata
print(____)
