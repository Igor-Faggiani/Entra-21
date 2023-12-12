"""Sintaxe das Classes"""
class NomeClasse:
    """Docstring da classe."""

    #Método construtor: Método utilizado para inicializar um objeto da classe.
    def __init__(self, parametro1: int):
        # self --> Referência ao próprio objeto.
        self.parametro1 = parametro1

        # Declarar um atributo privado.
        self.__atributo_privado = 0

    # Getters
    @property
    def atributo_privado(self):
        return self.__atributo_privado
    
    # Setters
    @atributo_privado.setter
    def atributo_privado(self, novo_valor: int):
        self.__atributo_privado = novo_valor

    # Métodos do objeto
    def metodo1(self):
        """Docstring do método."""
        print("Chamando o método do objeto")
    


if __name__ == '__main__':
    objeto_teste = NomeClasse(20)
    objeto_teste.metodo1()