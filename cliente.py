class Cliente:

    def __init__(self, nome, idade, ):
        self.__nome = nome
        self.idade = idade
    @property
    def nome(self):
        print("chamando @property nome()")
        return self.__nome.title()

    @nome.setter
    def nome(self, nome):
        print("chamando @property nome()")
        self.__nome = nome
