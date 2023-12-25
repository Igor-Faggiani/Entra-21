from db_initialize import DatabaseInitialize

if __name__ == "__main__":
    db_name = "pokemon.sqlite"
    
    db = DatabaseInitialize(db_name)
    db.create_tables()
    db.populate_table()