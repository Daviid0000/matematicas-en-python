import json
import random
import statistics

población = (json.load(open("edades.json")))

edades = []
muestra = []


for individuo in población:
  edades.append(individuo["age"])


sumaTotal = sum(edades)
longitudTotal = len(edades)
promedio = sumaTotal/longitudTotal
print("Muestreo probabilístico aleatorio simple")
print(f"La suma total de las dedades es de: {sumaTotal}")
print(f"La cantidad de edades es de: {longitudTotal}")
print(f"El promedio de edades es de : {promedio}")

edades_auxiliar = edades.copy()

for _ in range(0, 20):
  indice_random = random.randint(0, len(edades_auxiliar)-1)
  valor = edades_auxiliar.pop(indice_random)
  muestra.append(valor)

promedioMuestra = sum(muestra)/len(muestra)

acc = 0
cant_muestra = 20

k = round(len(edades)/cant_muestra)
i = random.randint(1, k)

muestra_sistematica = []
muestra_sistematica.append(edades[i])

print("----------------------------------------------")
print("Muestreo probabilístico sistemático")

for j in range(0, 20):
  acc = i + (j*k)
  print(acc)

  if acc <= len(edades)-1:
    muestra_sistematica.append(edades[acc])
  else:
    muestra_sistematica.append(edades[acc - len(edades)])

valor_promedio = statistics.mean(muestra_sistematica)
print(f"El promedio de edades es de: {valor_promedio}")




#con open() se utiliza para abrir/importar archivos en modo de solo lectura
#con json.load() se utiliza para cargar el contenido del archivo que se está importando con open()
#con la lirberia 'stadistics' se puede sacar el promedio de algo con pocos pasos. Ej: print(stadistics.mean(muestra))