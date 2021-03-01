"""
Faça um programa que leia o horário (hora, minuto e segundo) de inicio e a duração em segundos,
de uma experiência biológica. O programa deve resultar com o novo horário (hora, minuto e segundo)
do término da mesma.

"""
hora = 8
minuto = 30
segundo = 0
print(f'O evento inciará as {hora} hora(s), {minuto} minuto(s) e {segundo} segundo(s)')
duracao = int(input('digite a duração do evento em segundos: '))

segundo_duracao = duracao % 60
minuto_duracao = (duracao // 60) % 60
hora_duracao = (duracao // 60) // 60

hora_termino = hora + hora_duracao
minuto_termino = minuto + minuto_duracao
segundo_termino = segundo + segundo_duracao

if segundo_termino > 60:
    segundo_termino = minuto_termino + 1
    segundo_termino = segundo_termino - 60

elif minuto_termino > 60:
    hora_termino = hora_termino + 1
    minuto_termino = minuto_termino - 60


print(f'o evento termina as {hora_termino} hora(s), {minuto_termino} minutos() e {segundo_termino} segundo(s).')
