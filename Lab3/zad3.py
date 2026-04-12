# Zadanie 3. Gra w gorącego ziemniaka.
# Typowe zastosowania kolejek to symulacje rzeczywistych sytuacji, w których dane muszą być
# przetwarzane na sposób FIFO. Przykładem może być towarzyska gra w gorącego ziemniaka. Ustawieni
# w kręgu uczestnicy przekazują sobie nawzajem (do najbliższego sąsiada) pewien element (ziemniak).
# W pewnym momencie akcja zostaje przerwana. Uczestnik, który jest akurat w posiadaniu elementu,
# odpada z gry. Akcja jest kontynuowana aż do pozostania jednego uczestnika.
# Zabawa ta to w zasadzie nowoczesna wersja problemu Józefa Flawiusza:
# https://pl.wikipedia.org/wiki/Problem_J%C3%B3zefa_Flawiusza
# Celem jest stworzenie symulacji tej gry. Wykorzystamy przy tym kolejkę, aby zaimplementować
# ustawienie uczestników w kręgu. Założymy mianowicie, że ziemniaka ma zawsze uczestnik znajdujący
# się na początku kolejki. Przekazanie ziemniaka sąsiadowi będzie odpowiadało usunięciu tego
# uczestnika z początku kolejki i wstawienie go natychmiast na koniec. Co pewien czas (po określonej
# liczbie operacji usuwania/wstawiania) będziemy usuwać uczestnika znajdującego się na początku
# kolejki na stałe. Symulacja toczy się do momentu, aż w kolejce zostanie tylko jeden uczestnik.

