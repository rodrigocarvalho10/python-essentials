""" Exibe relat�rio de crian�as por atividade.

Imprimir a lista de crian�as agrupadas por sala
que frequenta cada uma das atividades.
"""
__version__ = "0.1.0"

sala1 = ["Erik", "Maia", "Gustavo", "Manuel", "Sofia", "Liz", "Davi"]
sala2 = ["Joao", "Antonio", "Carlos", "Manuela", "Joana", "Lucas", "Maria"]

aula_ingles = ["Erik", "Maia", "Joana", "Carlos", "Antonio", "Lucas", "Davi"]
aula_musica = ["Erik", "Carlos", "Maria", "Davi"]
aula_danca = ["Gustavo", "Sofia", "Liz", "Joana", "Antonio"]

atividades = [
    ("Inglês", aula_ingles), 
    ("Musica",aula_musica), 
    ("Danca", aula_danca)
]

for nome_atividade, atividade in atividades:

    print(f"\nAlunos da aula de {nome_atividade}\n")
    print("-" * 60)

    atividades_sala1 = set(sala1) & set(atividade)
    atividades_sala2 = set(sala2) & set(atividade)

    for aluno in atividade:
        if aluno in sala1:
            atividades_sala1.append(aluno)
        elif aluno in sala2:
            atividades_sala2.append(aluno)

    print(f"Sala1",atividades_sala1)
    print(f"Sala2",atividades_sala2)
    print("-" * 60)