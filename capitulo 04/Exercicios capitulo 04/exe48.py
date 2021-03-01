"""
Leia um valor em segundos, e imprima-o em horas, minutos e segundos.
"""
total_segundos = int(input('digite um valor em segundos: '))

segundo = total_segundos % 60
minuto = (total_segundos // 60) % 60
hora = (total_segundos // 60) // 60

print(f'{hora} hora(s), {minuto} minuto(s) e {segundo} segundo(s)')
