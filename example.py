from sqlalchemy import create_engine

connection_string = 'sqlite:///chinook.sqlite'

engine = create_engine(connection_string)  # konfiguracja silnika
connection = engine.connect()  # otwarcie połączenia z bazą

# print(engine.table_names())  # lista tablic w bazie

### Odbicie ###
from sqlalchemy import MetaData
from sqlalchemy import Table

metadata = MetaData()
albums = Table(
    'albums',
    metadata,
    autoload=True,
    autoload_with=engine
)

# print(repr(albums))
# print(metadata.tables)

# print(albums.columns.get('Title'))

### SELECT
# SELECT * FROM nazwa_tabeli
# SELECT nazwa_kolumny FROM nazwa_tabeli

stmt = "SELECT * FROM albums"  # Zapytanie sformułowane relacyjnie

result_proxy = connection.execute(stmt)  # LegacyReponse
result = result_proxy.fetchall()  # List

first_row = result[0]  # LegacyRow
id = first_row[0]
# print(id)
# print(first_row['Title'])

# A obietowow?
from sqlalchemy import select

stmt = select([albums])  # to samo zapytanie sformułowane obiektowo
# print(stmt)
# result = connection.execute(stmt).fetchmany(size=10)
# print(result)

### Klauzula WHERE

result = connection.execute(stmt).fetchall()
# print(result)


stmt = select([albums]).where(albums.columns.ArtistId == 90)  # <=, >=, != - operatory logiczne
print(stmt)
result = connection.execute(stmt).fetchall()
print(result)

# Inne operatory
# in_()
# like_()
# between()

stmt = select([albums]).where(albums.columns.Title.startswith('New'))
result = connection.execute(stmt).fetchall()
print(result)

# Operatory cd.
# and_()
# or_()
# not_()

from sqlalchemy import or_

stmt = select([albums]).where(or_(
    albums.columns.ArtistId == 90,
    albums.columns.ArtistId == 50
))
results = connection.execute(stmt).fetchall()

# for result in results:
#     print(f"{result.Title} --- {result.ArtistId}")

# PĘTLA KONSUMUJE ZAPYTANIE TAK JAK TO ROBIĄ METODY FETCHALL, FETCHONE, itd

stmt = select([albums]).where(albums.columns.ArtistId == 90)
results = connection.execute(stmt)

for result in results:
    print(result)

# A co jeżeli chcemy odpytać o konkretne kolumny, a nie o wszystkie kolumny.
stmt = select([albums.columns.Title, albums.columns.ArtistId]).where(albums.columns.ArtistId == 90)
print(stmt)
