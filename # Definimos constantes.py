
servicios = 12
minimokm = 5
CO2 = 43
contador = 0
total_km = 0
total_co2 = 0

while contador < servicios:
    distancia = float(input(f"Ingrese la distancia recorrida en el servicio {contador + 1} (mínimo {minimokm} km): "))

    if distancia < minimokm:
        print("Registro no válido. La distancia debe ser de al menos 5 km. Inténtelo nuevamente.")
        continue  

    total_km += distancia  
    total_co2 += distancia * CO2  
    contador += 1  

# Calcular el promedio de contaminación
promedio_co2 = total_co2 / servicios 

# Mostrar resultados
print("RESULTADOS")
print(f"Total de kilómetros recorridos: {total_km} km")
print(f"Total de CO2 emitido: {total_co2} gr")
print(f"Promedio de contaminación por servicio: {promedio_co2:.2f} gr de CO2")
