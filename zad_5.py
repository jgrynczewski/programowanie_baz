from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table

engine = create_engine('sqlite:///census.sqlite')
connection = engine.connect()

metadata = MetaData()

# Zaimportuj funkcję select
from sqlalchemy import select

# Odbij tabelę census
census = Table('census', metadata, autoload=True, autoload_with=engine)

# Zbuduj zapytanie select na tabeli census
stmt = select([census])

# Wyświetl instrukcję, w celu sprawdzenia wygenerowanej sqlki
print(stmt)

# Wykonaj instrukcję na połąceniu i pobierz tylko 10 wpisów
results = connection.execute(stmt).fetchmany(size=10)

# Wykonaj instrukcję i wyświetl wynik.
print(results)