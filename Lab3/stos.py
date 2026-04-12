stos =[]
stos.append(10)
stos.append(20)
stos.append(30)
print("Stos: ", stos)
print("Szczyt stosu: ", stos[-1])
print("Elament usunięty: ", stos.pop())

if not stos:
    print("Pusty")
else:
    print("Stos nie jest pusty")