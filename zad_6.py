from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import select

engine = create_engine('sqlite:///census.sqlite')
connection = engine.connect()
metadata = MetaData()

census = Table('census', metadata, autoload=True, autoload_with=engine)
stmt = select([census])
print(stmt)
results = connection.execute(stmt).fetchmany(size=10)

# Pobierz pierwszy wiersz wyniku używając indeksu
first_row = results[0]

# Wyświetl wartość pierwszego wiersza
print(first_row)

# Wyświetl wartość w pierwszej kolumnie pierwszego wiersza przy użyciu indeksu
print(first_row[0])

# Wyświetl wartość w pierwszej kolumnie pierwszego wiersza używając klucza
print(first_row['state'])