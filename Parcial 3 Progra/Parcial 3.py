print("Conversor de unidades S.I. Longitud.")
opcion = int(input("***Menú****  \n 1. Pulgadas a milimetros \n 2. Yardas a metros \n 3. Millas a kilometros \n\n"" Ingrese la opción que desea: "))

if opcion == 1:
    Pulgadas = int(input("Ingrese la cantidad de pulgadas a convertir: "))
    milimetros = pul*25.40
    print(f"{Pulgadas} Pulgadas equivalen a {milimetros} milimetros") 
elif opcion == 2:
    print("-------------------------------------------------")
    Yardas = int(input("Ingrese la cantidad de yardas a convertir: "))
    metros = Yardas*0.9144
    print(f"{Yardas} Yardas equivalen a {metros} metros")
elif opcion == 3:
    millas = int(input("Ingrese la cantidad de millas a convertir: "))
    kilometros = millas*1.6093
    print(f"{millas} Millas equivalen a {kilometros} kilometros")
else:
    print("La opción no es válida")