from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import select

# Wracamy do lokalnej kopii
engine = create_engine('sqlite:///census.sqlite')
connection = engine.connect()

metadata = MetaData()
census = Table('census', metadata, autoload=True, autoload_with=engine)

# Import and_
from ____ import ____

# Build a query for the census table: stmt
stmt = select(____)

# Append a where clause to select only non-male records from California using and_
stmt = stmt.where(
    # The state of California with a non-male sex
    ____(census.columns.state == ____,
         census.columns.sex != ____
         )
)

# Loop over the ResultProxy printing the age and sex
for result in ____:
    print(____, ____)