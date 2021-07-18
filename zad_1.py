# Zaimportuj create_engine
from sqlalchemy import create_engine

# Stwórz silnik do pliku census.sqlite
engine = create_engine('sqlite:///census.sqlite')

# Wyświetl nazwy tabel
print(engine.table_names())
