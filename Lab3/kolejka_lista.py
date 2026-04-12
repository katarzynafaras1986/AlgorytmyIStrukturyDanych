class KolejkaLista:
    def __init__(self):
        self.kolejka = []
    def enqueue(self, element):
        """Dodaje element na koniec kolejki"""
        self.kolejka.append(element)
    def dequeue(self):
        """Usuwa i zwraca element z początku kolejki"""
        if not self.is_empty():
            return self.kolejka.pop(0)
        raise IndexError("Kolejka jest pusta!")
    def front(self):
        """Podgląda pierwszy element kolejki bez usuwania"""
        if not self.is_empty():
            return self.kolejka[0]
        return None
    def is_empty(self):
        """Sprawdza, czy kolejka jest pusta"""
        return len(self.kolejka) == 0
    def size(self):
        """Zwraca rozmiar kolejki"""
        return len(self.kolejka)

# Przykład użycia
kolejka = KolejkaLista()
kolejka.enqueue(10)
kolejka.enqueue(20)
kolejka.enqueue(30)
print(kolejka.dequeue()) # 10
print(kolejka.front()) # 20
print(kolejka.size()) # 2