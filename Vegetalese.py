def Saladinha(texto):
    print(texto)

def Javascript(condicao, acao):
    if condicao:
        acao()

def Pega_a_salada_ai(funcao):
    funcao()

def Coelho(quantidade, acao):
    for _ in range(quantidade):
        acao()

def Caixa(inicio, fim, passo=1):
    for i in range(inicio, fim, passo):
        yield i

def Explodir(valor):
    return valor

def Carvao(condicao):
    while condicao:
        condicao = False
    else:
        Carvao_ativado()

def Carvao_ativado():
    print("Carvão ativado")

def code(bloco):
    exec(bloco)

# Exemplo de uso da função code:
code("""
Saladinha("Olá, mundo!")
Javascript(True, lambda: Saladinha("Esta é uma condição verdadeira"))
Pega_a_salada_ai(lambda: Saladinha("Sempre executa esta função"))
Coelho(3, lambda: Saladinha("Repetindo três vezes"))
for i in Caixa(1, 6, 2):
    Saladinha(i)
valor = Explodir(42)
Saladinha("O valor é: " + str(valor))
Carvao(True)
""")
