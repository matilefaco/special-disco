segundos_str = input("Por favor, entre com o número de segundos que deseja converter: ")
total_segs = int(segundos_str)

a = total_segs // 86400
segs_restantes = total_segs % 86400
b = segs_restantes // 3600
segs_restantes = total_segs % 3600
c = segs_restantes // 60
d = segs_restantes % 60

print(a, "dias,", b, "horas,", c, "minutos e", d, "segundos.")