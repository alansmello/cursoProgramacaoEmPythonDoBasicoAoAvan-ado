"""
RECEBENDO DADOS DO USUÁRIO.
"""
# Entrada de dados

nome = input("Qual é o seu nome?")
idade = input("qual sua idade?")

# Processamento

# Saída de dados
    # exemplo de print antigo
# print("Seja bem vindo %s" %nome)
# print("vc tá velho com %s anos einh" % idade )

# print a partir da versão 3.x do python

#print('Seja Bem Vindo {0}'.format(nome))


#print('Vc tá velho einh {0} com {1} anos. ' .format(nome, idade))

#Print Mais Atual

print(f'Seja Bem vindo {nome}, vc ja ta velho com {idade} anos einh cara')

print(f'O {nome} nasceu em {2020-int(idade)}') # todo dado recebido via input é do tipo String, por isso o int(idade),
                                               # para tranformar em inteiro  Isso se chama CAST

# EXEMPLO DE CAST NO INPUT
num = int(input("digite um numero: "))
num2 = int(input("digite outro numero: "))
print(f'a soma é {num+num2}')
