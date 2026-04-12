# Implementacja stosu za pomocą listy
# Python posiada wbudowaną strukturę list, która może działać jak stos przy użyciu metod .append() i
# .pop().
class StosLista:
    def __init__(self):
        self.stos = []
    def push(self, element):
        """Dodaje element na szczyt stosu"""
        self.stos.append(element)
    def pop(self):
        """Usuwa i zwraca element ze szczytu stosu"""
        if not self.is_empty():
            return self.stos.pop()
        raise IndexError("Stos jest pusty!")
    def peek(self):
        """Podgląda element na szczycie stosu bez usuwania"""
        if not self.is_empty():
             return self.stos[-1]
        return None
    def is_empty(self):
        """Sprawdza, czy stos jest pusty"""
        return len(self.stos) == 0
    def size(self):
        """Zwraca rozmiar stosu"""
        return len(self.stos)
# Przykład użycia
stos = StosLista()
stos.push(10)
stos.push(20)
stos.push(30)
print(stos.pop()) # 30
print(stos.peek()) # 20
print(stos.size()) # 2
