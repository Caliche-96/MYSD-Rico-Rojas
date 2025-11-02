#Andres Felipe fuertes v
print("programa descripcion por inversion")
minverso = input("Ingrese el mensaje inverso: ")

moriginal = ""

for i in range(len(minverso)):
    
    moriginal = minverso[i] + moriginal
print("El mensaje original es=", moriginal)
