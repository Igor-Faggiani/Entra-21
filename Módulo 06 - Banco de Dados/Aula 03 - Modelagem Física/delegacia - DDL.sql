CREATE TABLE IF NOT EXISTS public.criminosos (
	id SERIAL PRIMARY KEY,
	nome VARCHAR(256) NOT NULL,
	cpf VARCHAR(11) NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS public.vitimas (
	id SERIAL PRIMARY KEY,
	nome VARCHAR(256) NOT NULL,
	cpf VARCHAR(256) NOT NULL UNIQUE,
	telefone VARCHAR(20) NOT NULL
);

CREATE TABLE IF NOT EXISTS public.crimes (
	id SERIAL PRIMARY KEY,
	descricao VARCHAR(256) NOT NULL,
	data TIMESTAMP NOT NULL,
	data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS public.armas (
	id SERIAL PRIMARY KEY,
	calibre VARCHAR(20) NOT NULL,
	modelo VARCHAR(256) NOT NULL,
	fabricante VARCHAR(256) NOT NULL
);

CREATE TABLE IF NOT EXISTS public.locais (
	id SERIAL PRIMARY KEY,
	logradouro VARCHAR(256) NOT NULL,
	cidade VARCHAR(256) NOT NULL,
	bairro VARCHAR(256) NOT NULL,
	estado VARCHAR(256) NOT NULL,
	crime_id INT NOT NULL
);

CREATE TABLE IF NOT EXISTS public.armas_crimes (
	arma_id INT,
	crime_id INT,
	PRIMARY KEY (arma_id, crime_id)
);

CREATE TABLE IF NOT EXISTS public.vitimas_crimes (
	vitima_id INT,
	crime_id INT,
	PRIMARY KEY (vitima_id, crime_id)
);

CREATE TABLE IF NOT EXISTS public.crimes_criminosos (
	criminoso_id INT,
	crime_id INT,
	PRIMARY KEY (criminoso_id, crime_id)
);

-- Adicionando as Chaves-Estrangeiras
ALTER TABLE IF EXISTS public.locais
ADD FOREIGN KEY (crime_id)
REFERENCES public.crimes (id)
ON UPDATE CASCADE
ON DELETE CASCADE;

ALTER TABLE IF EXISTS public.armas_crimes
ADD FOREIGN KEY (arma_id)
REFERENCES public.armas (id)
ON UPDATE CASCADE
ON DELETE NO ACTION;

ALTER TABLE IF EXISTS public.armas_crimes
ADD FOREIGN KEY (arma_id)
REFERENCES public.armas (id)
ON UPDATE CASCADE
ON DELETE RESTRICT;

ALTER TABLE IF EXISTS public.crimes_criminosos
ADD FOREIGN KEY (crime_id)
REFERENCES public.crimes (id)
ON UPDATE CASCADE
ON DELETE SET NULL;

ALTER TABLE IF EXISTS public.crimes_criminosos
ADD FOREIGN KEY (criminoso_id)
REFERENCES public.criminosos (id);

ALTER TABLE IF EXISTS public.vitimas_crimes
ADD FOREIGN KEY (crime_id)
REFERENCES public.crimes (id);

ALTER TABLE IF EXISTS public.vitimas_crimes
ADD FOREIGN KEY (vitima_id)
REFERENCES public.vitimas (id);

-- Renomenado
-- ALTER TABLE locais RENAME TO localizacoes;

/*
Comandos DML (Data Maipulation Language)
* INSERT - Inserir dados na tabela
* UPDATE - Atualizar dados da tabela
* DELETE - Remover dados da tabela
*/

INSERT INTO armas (calibre, modelo, fabricante) VALUES
('9mm', 'Glock 17', 'Glock Ges.m.b.H.'),
('5.56mm', 'M4A1', 'Colt Defense'),
('7.62mm', 'AK-47', 'Kalashnikov Concern'),
('12 gauge', 'Mossberg 500', 'O.F. Mossberg & Sons'),
('.50 BMG', 'Barrett M82', 'Barrett Firearms Manufacturing'),
('9mm', 'SIG Sauer P320', 'SIG Sauer'),
('7.62mm', 'FN SCAR', 'FN Herstal'),
('.45 ACP', 'Colt 1911', 'Colt Manufacturing Company'),
('5.56mm', 'Steyr AUG', 'Steyr Mannlicher'),
('.338 Lapua Magnum', 'Accuracy International AS50', 'Accuracy International'),
('9mm', 'Heckler & Koch VP9', 'Heckler & Koch'),
('.45 ACP', 'Smith & Wesson M&P', 'Smith & Wesson'),
('5.56mm', 'Bushmaster ACR', 'Bushmaster Firearms International'),
('7.62mm', 'Ruger SR-762', 'Sturm, Ruger & Co.'),
('.40 S&W', 'Springfield XD', 'Springfield Armory, Inc.'),
('12 gauge', 'Remington 870', 'Remington Arms'),
('9mm', 'CZ P-10', 'Česká zbrojovka'),
('5.56mm', 'HK416', 'Heckler & Koch'),
('.308 Winchester', 'DPMS LR-308', 'DPMS Panther Arms'),
('.45 ACP', 'Para-Ordnance 1911', 'Para-Ordnance'),
('7.62mm', 'IWI Tavor X95', 'Israel Weapon Industries');

SELECT * FROM armas;

-- Atualizando os dados (UTILIZAR WHERE)
UPDATE armas 
SET calibre = '8 PSL', modelo = 'Revóvler Mod. 82'
WHERE id = 1;

-- Removendo os dados (UTILIZAR O WHERE)
DELETE FROM armas
WHERE id = 1