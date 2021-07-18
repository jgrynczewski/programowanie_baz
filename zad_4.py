from sqlalchemy import create_engine
engine = create_engine('sqlite:///census.sqlite')

# Create a connection on engine
connection = ___

# Build select statement for census table: stmt
stmt = ____

# Execute the statement and fetch the results: results
results = ____

# Print results
print(____)