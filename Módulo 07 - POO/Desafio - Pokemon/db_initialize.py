"""Inicializador de tabelas"""
import sqlite3

class DatabaseInitialize:
    """DatabaseInitialize representa o banco de dados.

    Attributes:
        db_name: Nome do banco de dados.
    """

    def __init__(self, db_name):
        self.db_name = db_name

    def create_tables(self):
        """Cria as tabelas no banco de dados.

        Args:
            db_nome (str): Nome do banco de dados.
        """
        connection = sqlite3.connect(self.db_name)
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

    def populate_table(self):
        """Populando as tabelas do banco de dados."""
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()
        cursor.executescript("""
            INSERT INTO pokemon (name, health, type) VALUES ('Mewtwo', 150, 'Psychic');
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
            INSERT INTO pokemon_attack (pokemon_id, attack_id) VALUES (1, 1);   -- Mewtwo usando Thunderbolt
            INSERT INTO pokemon_attack (pokemon_id, attack_id) VALUES (2, 2);   -- Dragonite usando Vine Whip
            INSERT INTO pokemon_attack (pokemon_id, attack_id) VALUES (3, 3);   -- Gyarados usando Flamethrower
            INSERT INTO pokemon_attack (pokemon_id, attack_id) VALUES (4, 4);   -- Alakazam usando Water Gun
            INSERT INTO pokemon_attack (pokemon_id, attack_id) VALUES (5, 5);   -- Tyranitar usando Psybeam
            INSERT INTO pokemon_attack (pokemon_id, attack_id) VALUES (6, 6);   -- Gengar usando Fire Blast
            INSERT INTO pokemon_attack (pokemon_id, attack_id) VALUES (7, 7);   -- Snorlax usando Solar Beam
            INSERT INTO pokemon_attack (pokemon_id, attack_id) VALUES (8, 8);   -- Arcanine usando Blizzard
            INSERT INTO pokemon_attack (pokemon_id, attack_id) VALUES (9, 9);   -- Lapras usando Thunder Punch
            INSERT INTO pokemon_attack (pokemon_id, attack_id) VALUES (10, 10); -- Machamp usando Surf
            INSERT INTO pokemon_attack (pokemon_id, attack_id) VALUES (11, 11); -- Gengar usando Rock Slide
            INSERT INTO pokemon_attack (pokemon_id, attack_id) VALUES (12, 12); -- Snorlax usando Aerial Ace
            INSERT INTO pokemon_attack (pokemon_id, attack_id) VALUES (13, 13); -- Arcanine usando Iron Tail
            INSERT INTO pokemon_attack (pokemon_id, attack_id) VALUES (14, 14); -- Lapras usando Dark Pulse
            INSERT INTO pokemon_attack (pokemon_id, attack_id) VALUES (15, 15); -- Machamp usando Dragon Claw
            INSERT INTO pokemon_attack (pokemon_id, attack_id) VALUES (16, 16); -- Mewtwo usando Hyper Beam
            INSERT INTO pokemon_attack (pokemon_id, attack_id) VALUES (17, 17); -- Dragonite usando Ice Fang
            INSERT INTO pokemon_attack (pokemon_id, attack_id) VALUES (18, 18); -- Gyarados usando Thunder Wave
            INSERT INTO pokemon_attack (pokemon_id, attack_id) VALUES (19, 19); -- Alakazam usando Toxic
            INSERT INTO pokemon_attack (pokemon_id, attack_id) VALUES (20, 20); -- Tyranitar usando Confuse Ray
            INSERT INTO pokemon_attack (pokemon_id, attack_id) VALUES (21, 21); -- Gengar usando Tackle
            INSERT INTO pokemon_attack (pokemon_id, attack_id) VALUES (22, 22); -- Snorlax usando Scratch
            INSERT INTO pokemon_attack (pokemon_id, attack_id) VALUES (23, 23); -- Arcanine usando Quick Attack
            INSERT INTO pokemon_attack (pokemon_id, attack_id) VALUES (24, 24); -- Lapras usando Gust

        """)
        connection.commit()
        connection.close()