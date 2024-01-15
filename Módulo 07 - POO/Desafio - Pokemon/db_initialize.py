"""Inicializador de tabelas"""
import sqlite3

class DatabaseInitialize:
    """DatabaseInitialize representa o banco de dados.

    Attributes:
        db_name: Nome do banco de dados.
    """

    def __init__(self, db_name: str):
        self.db_name = db_name

    def create_tables(db_name: str):
        """Cria as tabelas no banco de dados.

        Args:
            db_name (str): Nome do banco de dados.
        """
        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()
        cursor.executescript("""
            CREATE TABLE IF NOT EXISTS pokemon (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                health INT NOT NULL,
                type TEXT NOT NULL
            );
            
            CREATE TABLE IF NOT EXISTS effect (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                duration INT NOT NULL
            );
            
            CREATE TABLE IF NOT EXISTS attack (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                damage INT NOT NULL,
                type TEXT NOT NULL,
                effect_id INTEGER,
                FOREIGN KEY (effect_id) REFERENCES effect (id)
            );
            
            CREATE TABLE IF NOT EXISTS pokemon_attack (
                pokemon_id INT,
                attack_id INT,
                PRIMARY KEY (pokemon_id, attack_id),
                FOREIGN KEY (pokemon_id) REFERENCES pokemon (id),
                FOREIGN KEY (attack_id) REFERENCES attack (id)
            );
        """)
        connection.commit()
        connection.close()

    def populate_table(db_name: str):
        """Populando as tabelas do banco de dados."""
        connection = sqlite3.connect(db_name)
        cursor = connection.cursor()
        cursor.executescript("""
            INSERT INTO pokemon (name, health, type) VALUES ('Mewtwo', 150, 'Psychic');
            INSERT INTO pokemon (name, health, type) VALUES ('Rayquaza', 180, 'Dragon');
            INSERT INTO pokemon (name, health, type) VALUES ('Dragonite', 160, 'Dragon');
            INSERT INTO pokemon (name, health, type) VALUES ('Gyarados', 140, 'Water');
            INSERT INTO pokemon (name, health, type) VALUES ('Alakazam', 130, 'Psychic');
            INSERT INTO pokemon (name, health, type) VALUES ('Tyranitar', 155, 'Rock');
            INSERT INTO pokemon (name, health, type) VALUES ('Gengar', 125, 'Ghost');
            INSERT INTO pokemon (name, health, type) VALUES ('Snorlax', 180, 'Normal');
            INSERT INTO pokemon (name, health, type) VALUES ('Arcanine', 145, 'Fire');
            INSERT INTO pokemon (name, health, type) VALUES ('Lapras', 155, 'Water');
            INSERT INTO pokemon (name, health, type) VALUES ('Machamp', 135, 'Fighting');


            INSERT INTO effect (name, duration) VALUES ('Burn', 4);
            INSERT INTO effect (name, duration) VALUES ('Paralysis', 3);
            INSERT INTO effect (name, duration) VALUES ('Poison', 5);
            INSERT INTO effect (name, duration) VALUES ('Sleep', 6);
            INSERT INTO effect (name, duration) VALUES ('Confusion', 4);
            INSERT INTO effect (name, duration) VALUES ('Freeze', 3);
            INSERT INTO effect (name, duration) VALUES ('Flinch', 2);
            INSERT INTO effect (name, duration) VALUES ('Confuse Ray', 5);
            INSERT INTO effect (name, duration) VALUES ('Leech Seed', 4);
            INSERT INTO effect (name, duration) VALUES ('Toxic', 6);


            INSERT INTO attack (name, damage, type, effect_id) VALUES ('Thunderbolt', 90, 'Electric', 1);
            INSERT INTO attack (name, damage, type, effect_id) VALUES ('Vine Whip', 45, 'Grass', 6);
            INSERT INTO attack (name, damage, type, effect_id) VALUES ('Flamethrower', 95, 'Fire', 4);
            INSERT INTO attack (name, damage, type, effect_id) VALUES ('Water Gun', 40, 'Water', 2);
            INSERT INTO attack (name, damage, type, effect_id) VALUES ('Psybeam', 65, 'Psychic', 5);
            INSERT INTO attack (name, damage, type, effect_id) VALUES ('Fire Blast', 110, 'Fire', 4);
            INSERT INTO attack (name, damage, type, effect_id) VALUES ('Solar Beam', 120, 'Grass', 6);
            INSERT INTO attack (name, damage, type, effect_id) VALUES ('Blizzard', 100, 'Ice', 7);
            INSERT INTO attack (name, damage, type, effect_id) VALUES ('Thunder Punch', 75, 'Electric', 1);
            INSERT INTO attack (name, damage, type, effect_id) VALUES ('Surf', 90, 'Water', 2);
            INSERT INTO attack (name, damage, type, effect_id) VALUES ('Rock Slide', 75, 'Rock', NULL);
            INSERT INTO attack (name, damage, type, effect_id) VALUES ('Aerial Ace', 60, 'Flying', NULL);
            INSERT INTO attack (name, damage, type, effect_id) VALUES ('Iron Tail', 100, 'Steel', NULL);
            INSERT INTO attack (name, damage, type, effect_id) VALUES ('Dark Pulse', 80, 'Dark', NULL);
            INSERT INTO attack (name, damage, type, effect_id) VALUES ('Dragon Claw', 85, 'Dragon', NULL);
            INSERT INTO attack (name, damage, type, effect_id) VALUES ('Hyper Beam', 150, 'Normal', 5);
            INSERT INTO attack (name, damage, type, effect_id) VALUES ('Ice Fang', 65, 'Ice', 7);
            INSERT INTO attack (name, damage, type, effect_id) VALUES ('Thunder Wave', 0, 'Electric', 3);
            INSERT INTO attack (name, damage, type, effect_id) VALUES ('Toxic', 0, 'Poison', 2);
            INSERT INTO attack (name, damage, type, effect_id) VALUES ('Confuse Ray', 0, 'Ghost', 6);
            INSERT INTO attack (name, damage, type, effect_id) VALUES ('Tackle', 40, 'Normal', NULL);
            INSERT INTO attack (name, damage, type, effect_id) VALUES ('Scratch', 40, 'Normal', NULL);
            INSERT INTO attack (name, damage, type, effect_id) VALUES ('Quick Attack', 40, 'Normal', NULL);
            INSERT INTO attack (name, damage, type, effect_id) VALUES ('Gust', 40, 'Flying', NULL);


            -- Relacionamento entre Pokémon e seus ataques na tabela pokemon_attack
            -- Mewtwo
            INSERT INTO pokemon_attack (pokemon_id, attack_id) VALUES (1, 1); 
            INSERT INTO pokemon_attack (pokemon_id, attack_id) VALUES (1, 5); 
            INSERT INTO pokemon_attack (pokemon_id, attack_id) VALUES (1, 9); 
            INSERT INTO pokemon_attack (pokemon_id, attack_id) VALUES (1, 20);
            
            -- Rayquaza
            INSERT INTO pokemon_attack (pokemon_id, attack_id) VALUES (2, 15);
            INSERT INTO pokemon_attack (pokemon_id, attack_id) VALUES (2, 16);
            INSERT INTO pokemon_attack (pokemon_id, attack_id) VALUES (2, 1); 
            INSERT INTO pokemon_attack (pokemon_id, attack_id) VALUES (2, 12);
            
            -- Dragonite
            INSERT INTO pokemon_attack (pokemon_id, attack_id) VALUES (3, 21);
            INSERT INTO pokemon_attack (pokemon_id, attack_id) VALUES (3, 22);
            INSERT INTO pokemon_attack (pokemon_id, attack_id) VALUES (3, 23);
            INSERT INTO pokemon_attack (pokemon_id, attack_id) VALUES (3, 24);
            
            -- Gyarados
            INSERT INTO pokemon_attack (pokemon_id, attack_id) VALUES (4, 13);
            INSERT INTO pokemon_attack (pokemon_id, attack_id) VALUES (4, 14);
            INSERT INTO pokemon_attack (pokemon_id, attack_id) VALUES (4, 15);
            INSERT INTO pokemon_attack (pokemon_id, attack_id) VALUES (4, 16);
            
            -- Alakazam
            INSERT INTO pokemon_attack (pokemon_id, attack_id) VALUES (5, 1); 
            INSERT INTO pokemon_attack (pokemon_id, attack_id) VALUES (5, 5); 
            INSERT INTO pokemon_attack (pokemon_id, attack_id) VALUES (5, 9); 
            INSERT INTO pokemon_attack (pokemon_id, attack_id) VALUES (5, 20);
            
            -- Tyranitar
            INSERT INTO pokemon_attack (pokemon_id, attack_id) VALUES (6, 11);
            INSERT INTO pokemon_attack (pokemon_id, attack_id) VALUES (6, 13);
            INSERT INTO pokemon_attack (pokemon_id, attack_id) VALUES (6, 14);
            INSERT INTO pokemon_attack (pokemon_id, attack_id) VALUES (6, 18);

            -- Gengar
            INSERT INTO pokemon_attack (pokemon_id, attack_id) VALUES (7, 17);
            INSERT INTO pokemon_attack (pokemon_id, attack_id) VALUES (7, 18);
            INSERT INTO pokemon_attack (pokemon_id, attack_id) VALUES (7, 19);
            INSERT INTO pokemon_attack (pokemon_id, attack_id) VALUES (7, 24);
            
            -- Snorlax
            INSERT INTO pokemon_attack (pokemon_id, attack_id) VALUES (8, 21);
            INSERT INTO pokemon_attack (pokemon_id, attack_id) VALUES (8, 22);
            INSERT INTO pokemon_attack (pokemon_id, attack_id) VALUES (8, 23);
            INSERT INTO pokemon_attack (pokemon_id, attack_id) VALUES (8, 24);
            
            -- Arcanine
            INSERT INTO pokemon_attack (pokemon_id, attack_id) VALUES (9, 3); 
            INSERT INTO pokemon_attack (pokemon_id, attack_id) VALUES (9, 6); 
            INSERT INTO pokemon_attack (pokemon_id, attack_id) VALUES (9, 20);
            INSERT INTO pokemon_attack (pokemon_id, attack_id) VALUES (9, 25);

            -- Lapras
            INSERT INTO pokemon_attack (pokemon_id, attack_id) VALUES (10, 4);
            INSERT INTO pokemon_attack (pokemon_id, attack_id) VALUES (10, 9);
            INSERT INTO pokemon_attack (pokemon_id, attack_id) VALUES (10, 10);
            INSERT INTO pokemon_attack (pokemon_id, attack_id) VALUES (10, 16);
            
            -- Machamp
            INSERT INTO pokemon_attack (pokemon_id, attack_id) VALUES (11, 11);
            INSERT INTO pokemon_attack (pokemon_id, attack_id) VALUES (11, 17);
            INSERT INTO pokemon_attack (pokemon_id, attack_id) VALUES (11, 18);
            INSERT INTO pokemon_attack (pokemon_id, attack_id) VALUES (11, 19);

        """)
        connection.commit()
        connection.close()