class Pessoa:
    def __init__(self, *filhos ,nome = None,idade = 22):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {self.nome}'


if __name__ == '__main__':
    leonardo= Pessoa(nome='Leonardo')
    pedro = Pessoa(leonardo,nome='Pedro')
    print(Pessoa.cumprimentar(pedro))
    print(id(pedro))
    print(pedro.cumprimentar())
    print(pedro.nome)
    pedro.idade = 67
    print(pedro.idade)
    for filhos in pedro.filhos:
        print(filhos.nome)

    pedro.sobrenome = 'Santos'
    del pedro.filhos
    print(pedro.sobrenome)
    print(pedro.nome)
    print(pedro.__dict__)
    print(leonardo.__dict__)