from sql-alchemy import
(
create_engine, Table, Column, Float, ForeignKey, Integer, String, MetaData
)

#executing the instructions from our localhost to our ** database

db = create_engine("postgresql:///**")

meta = MetaData(db)

#queries for the database



#making the connection

with db.connect() as connection:

    #Query 1

    select_query = artist_table.select()

    results = connection.execute(select_query)

    for result in results:
        print(result)

