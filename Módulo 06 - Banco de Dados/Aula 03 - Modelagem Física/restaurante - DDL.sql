CREATE TABLE IF NOT EXISTS public.usuarios (
	id SERIAL PRIMARY KEY,
	clientes VARCHAR(256) NOT NULL,
	numero VARCHAR(256) NOT NULL,
	email VARCHAR(256) NOT NULL
);

CREATE TABLE IF NOT EXISTS public.restaurantes (
	id SERIAL PRIMARY KEY,
	telefone VARCHAR(256) NOT NULL,
	tipo_cozinha VARCHAR(256) NOT NULL
);

CREATE TABLE IF NOT EXISTS public.mesas (
	id SERIAL PRIMARY KEY,
	num_mesas NUMERIC(50) NOT NULL,
	localizacao VARCHAR(256) NOT NULL,
	disponibilidade BOOL NOT NULL
);

CREATE TABLE IF NOT EXISTS public.reservas (
	id SERIAL PRIMARY KEY,
	id_restaurante SERIAL NOT NULL,
	id_cliente SERIAL NOT NULL,
	data TIMESTAMP NOT NULL,
	num_pessoas VARCHAR(12) NOT NULL,
	status_reserva VARCHAR(256) NOT NULL
);

CREATE TABLE IF NOT EXISTS public.avaliacoes (
	id SERIAL PRIMARY KEY,
	id_cliente SERIAL NOT NULL,
	id_restaurante SERIAL NOT NULL,
	data TIMESTAMP NOT NULL,
	avaliacao VARCHAR(5) NOT NULL,
	cometario VARCHAR(256) NOT NULL
);

CREATE TABLE IF NOT EXISTS public.enderecos (
	id SERIAL PRIMARY KEY,
	id_restaurante SERIAL NOT NULL,
	cidade VARCHAR(256) NOT NULL,
	bairro VARCHAR(256) NOT NULL,
	rua VARCHAR(256) NOT NULL
);

CREATE TABLE IF NOT EXISTS public.funcionarios (
	id SERIAL PRIMARY KEY,
	id_restaurante SERIAL NOT NULL,
	nome VARCHAR(256) NOT NULL,
	telefone VARCHAR(256) NOT NULL,
	email VARCHAR(256) NOT NULL
);

CREATE TABLE IF NOT EXISTS public.reservas_mesas (
	reserva_id INT,
	mesa_id INT,
	PRIMARY KEY (reserva_id, mesa_id)
);

-- Adicionando as Chaves-Estrangeiras
ALTER TABLE IF EXISTS public.reservas_mesas
ADD FOREIGN KEY (reserva_id)
REFERENCES public.reservas (id)
ON UPDATE CASCADE
ON DELETE CASCADE;

ALTER TABLE IF EXISTS public.reservas_mesas
ADD FOREIGN KEY (mesa_id)
REFERENCES public.mesas (id)
ON UPDATE CASCADE
ON DELETE CASCADE;

ALTER TABLE IF EXISTS public.reservas
ADD FOREIGN KEY (id_restaurante)
REFERENCES public.restaurantes (id)
ON UPDATE CASCADE
ON DELETE NO ACTION;

ALTER TABLE IF EXISTS public.reservas
ADD FOREIGN KEY (id_cliente)
REFERENCES public.usuarios (id)
ON UPDATE CASCADE
ON DELETE CASCADE;

ALTER TABLE IF EXISTS public.avaliacoes
ADD FOREIGN KEY (id_cliente)
REFERENCES public.usuarios (id)
ON UPDATE CASCADE
ON DELETE CASCADE;

ALTER TABLE IF EXISTS public.avaliacoes
ADD FOREIGN KEY (id_restaurante)
REFERENCES public.restaurantes (id)
ON UPDATE CASCADE
ON DELETE CASCADE;

ALTER TABLE IF EXISTS public.enderecos
ADD FOREIGN KEY (id_restaurante)
REFERENCES public.restaurantes (id)
ON UPDATE CASCADE
ON DELETE CASCADE;

ALTER TABLE IF EXISTS public.funcionarios
ADD FOREIGN KEY (id_restaurante)
REFERENCES public.restaurantes (id)
ON UPDATE CASCADE
ON DELETE CASCADE;

--INSERINDO DADOS NA TABELA (USUARIOS)
INSERT INTO usuarios (clientes, numero, email) VALUES
('João Silva', '+55123456789', 'joao.silva@email.com'),
('Maria Santos', '+5511987654321', 'maria.santos@email.com'),
('Pedro Oliveira', '+5522998765432', 'pedro.oliveira@email.com'),
('Ana Souza', '+5533887654321', 'ana.souza@email.com'),
('Carlos Ferreira', '+5544998765432', 'carlos.ferreira@email.com'),
('Julia Rodrigues', '+555577776666', 'julia.rodrigues@email.com'),
('Fernando Costa', '+5566999888777', 'fernando.costa@email.com'),
('Laura Pereira', '+5577888999000', 'laura.pereira@email.com'),
('Rafaela Alves', '+5588111222333', 'rafaela.alves@email.com'),
('Diego Gomes', '+5599222333444', 'diego.gomes@email.com'),
('Camila Carvalho', '+55123456789', 'camila.carvalho@email.com'),
('Gabriel Martins', '+5511987654321', 'gabriel.martins@email.com'),
('Amanda Santos', '+5522998765432', 'amanda.santos@email.com'),
('Lucas Oliveira', '+5533887654321', 'lucas.oliveira@email.com'),
('Isabela Souza', '+5544998765432', 'isabela.souza@email.com'),
('Marcos Ferreira', '+555577776666', 'marcos.ferreira@email.com'),
('Carolina Rodrigues', '+5566999888777', 'carolina.rodrigues@email.com'),
('Guilherme Costa', '+5577888999000', 'guilherme.costa@email.com'),
('Mariana Alves', '+5588111222333', 'mariana.alves@email.com'),
('Thiago Gomes', '+5599222333444', 'thiago.gomes@email.com');

SELECT * FROM usuarios