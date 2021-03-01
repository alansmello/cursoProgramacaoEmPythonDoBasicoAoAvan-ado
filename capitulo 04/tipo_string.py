"""
Tipo String

Em Python, um dado é considerado do tipo String sem que:

 - estiver entre aspas simples -> 'uma string', '234', 'a', 'True', '42.3'
 - estiver entre aspas duplas -> "uma string", "234", "a", "True", "42.3"
 - estiver entre aspas simples triplas -> '''uma string''', '''234''', '''a''', '''True''', '''42.3'''    """
#- estiver entre aspas duplas triplas -> """uma string""", """234""", """a""", """True""", """42.3"""

nome = 'Alan Mello'

print(nome.upper())
print(nome.lower())
print(nome.split())
print(nome.split()[0])
print(nome.split()[1])
print(nome[::-1]) #inverção da String
print(nome[0:7]) #Slice de String Pythônico
print(nome.replace('A', 'b')) #substitui a letra A (maiusculo) por b (minusculo)
