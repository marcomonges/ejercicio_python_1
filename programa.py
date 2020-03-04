metros_cuadrados = int(input("Cuantos Metros Cuadrados tiene el estadio?: "))
gente_gradas = int(input("Cantidad de gente que cabe en las gradas?: "))
escenario = int(input("Qué porcentage de espacio ocupa el escenario?: "))
precio_especial = int(input("Cuanto costará la entrada a precio especial?: ")) 
precio_comun = int(input("Cuanto costará la entrada a precio común?: "))

boletos_total = (metros_cuadrados - escenario) * 4
gente_total = (100 * gente_gradas) / 20

total_precio_especial =
total_precio_comun = 
total_precio =

print("se estiman: " + gente_total + " personas en total")
print("Tienes que imprimir: " + especial + " Boletos a precio especial, y: " + comun + " Boletos a precio común.")
print("Las ganancias se estiman de: " + total_precio + " Pesos")
