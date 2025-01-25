
import math
import accion

accion = accion


print('\nProyecto Maquina de Goldberg \n')



altura=0
peso=0
gravedad=9.8

def tiempo_caida_libre(altura, caida):
    tiempo=(math.sqrt(((altura/100)*2)/gravedad))
    print(f'Tiempo caida {caida}: {round(tiempo,3)}s - Altura: {altura}cm')
    
  
##

def mur(altura, tramo):
    tiempo=(math.sqrt(((altura/100)*2)/gravedad))
    velocidad_final=0+gravedad*tiempo
    print(f'caida {tramo}   |   {altura}cm         |   {round(tiempo,3)}s    |   {gravedad}m/s^2         |   {round(velocidad_final,3)}cm/s')
        
    
##

print("Movimiento Canica Uno")

tiempo_caida_libre(14,5)

print(f'Nombre    |   Distancia   |   Tiempo    |   Aceleración      |   Velocidad final')
mur(14,1)

print("\n \n")

print("Movimiento Canica Dos")

tiempo_caida_libre(3,1)
tiempo_caida_libre(3,2)
tiempo_caida_libre(3,3)
tiempo_caida_libre(7,4)

print(f'Nombre    |   Distancia   |   Tiempo    |   Aceleración      |   Velocidad final')


mur(3,1)
mur(3,2)
mur(3,3)
mur(7,4)


accion.movCanicaUno()
accion.movCanicaDos()
