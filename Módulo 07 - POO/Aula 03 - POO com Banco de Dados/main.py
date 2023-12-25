from inicializador_bd import InicializadorBD
from usuario_repositorio import UsuarioRepositorio
from usuario import Usuario

DB_NOME = "exemplo.db"
InicializadorBD.criar_tabelas(DB_NOME)

usuario_repositorio = UsuarioRepositorio(DB_NOME)

usuario1 = Usuario("Igor Faggiani", "igorfaggiani07@gmail.com")

try:
    usuario_repositorio.inserir_usuario(usuario1)
except:
    print("Email já cadastrado!")

# usuarios = usuario_repositorio.obter_usuarios()
# usuario1 = usuarios[0]
# usuario1.nome = "Outro nome"
# usuario1.email = "teste@gmail.com"

# usuario_repositorio.atualizar_usuario(usuario1)

# usuario_repositorio.remover_usuario(usuario1)
#random.choice()