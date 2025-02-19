meta_produccion = 10  
produccion_total = 0 
vacas = 0
cabras = 0
bufalas = 0

print("Registro de producción lechera")

while produccion_total < meta_produccion:
    tipo_animal = input("Ingrese tipo de animal ordeñado (vaca, cabra, bufala): ")
    cantidad = int(input("Ingrese cuántos animales ordeñó: "))
    produccion_por_animal = float(input("Ingrese cuántos litros produjo cada animal: "))
    
    
    if 0.5 <= produccion_por_animal <= 1.5:
        produccion_obtenida = cantidad * produccion_por_animal
        produccion_total += produccion_obtenida

        
        if tipo_animal == "vaca":
            vacas += cantidad
        elif tipo_animal == "cabra":
            cabras += cantidad
        elif tipo_animal == "bufala":
            bufalas += cantidad
        else:
            print("Tipo de animal no reconocido. No se registra la producción.")
            produccion_total -= produccion_obtenida  
    else:
        print("Producción por animal fuera del rango válido. No se registra la producción.")
    
    print(f"Producción total acumulada: {produccion_total:.2f} litros")
    

print("\nMeta de producción alcanzada.")
print(f"Total de vacas ordeñadas: {vacas}")
print(f"Total de cabras ordeñadas: {cabras}")
print(f"Total de búfalas ordeñadas: {bufalas}")
print(f"Producción total registrada: {produccion_total:.2f} litros")

