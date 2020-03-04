# CONSTANTES
PERSONASENM2 = 4
ESPACIOGRADAS = 0.2
PRECIOESPECIAL = 0.3
PRECIOCOMUN =  0.7


# variables

totalM2 = float(input("Cantidad de metros cuadrados que tiene el estadio que contrató: "))
perGrada = int(input("Capacidad de gente en la grada: "))
porEscenario = int(input("el porcentaje de espacio ocupado por el escenario: "))

# Cantidad total de Personas
m2Grada = totalM2 * ESPACIOGRADAS
m2Escenario = totalM2 * (porEscenario/100)
m2disponibles = totalM2 - m2Grada - m2Escenario
personas = (m2disponibles * 4) + perGrada

print("Cantidad total de personas es: ", personas)


# Ganancias Totales

dineroEspecial = float(input("Ingrese el precio especial: "))
dineroComun = float(input("Ingrese el precio común: "))

precioEspecial = (personas * PRECIOESPECIAL) * dineroEspecial
precioComun = (personas * PRECIOCOMUN) * dineroComun
dineroTotal = precioEspecial + precioComun

print("Si se venden todas las entradas, ingresaría", dineroTotal, "Pesos" )
