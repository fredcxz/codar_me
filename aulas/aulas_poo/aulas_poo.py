#Programção orientada a objetos
#O que é um objeto?

""""Um objeto é uma instância de uma classe. Ele é criado a partir de uma
classe e tem seus próprios valores para as propriedades definidas na classe."""

#Exemplo

class Estudantes:
    def __init__(self, aluno: str, nota: int ) :
        self.aluno = aluno
        self.nota = nota
        self.escola = "cest"

    def __str__(self) -> str:
        return f"Aluno:{self.aluno} \nNota:{self.nota} \nEscola:{self.escola}"
    
    def alterar_nome(self, aluno:str) :
        self.aluno = novo_nome


##variaveis
nome ="Fred"
novo_nome ="Pedro 77mn,n,,m"
nota=10

## Criar um estudante
aluno = Estudantes(nome, nota)

## Teste da criacao do estudante
def test_criar():
    assert str(aluno) == f"Aluno:{aluno.nome} \nNota:{aluno.nota} \nEscola:cest"


## atualize o nome do estudante
aluno.alterar_nome(novo_nome)

## Teste da criacao do estudante
def test_atualizar():
    assert str(aluno) == f"Aluno:{aluno.novo_nome} \nNota:{aluno.nota} \nEscola:cest"