class Pessoa:
    olhos = 2

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
    pedro.olhos = 1
    del pedro.olhos
    print(pedro.__dict__)
    print(leonardo.__dict__)

    print(pedro.olhos)
    print(leonardo.olhos)
    print(Pessoa.olhos)
