#Zad. 1 Wygeneruj liczby podzielne przez 4 i zapisz je do pliku.
# import random
#
# rand = []
# i = 0
# while i != 5:
#     r = random.randint(0, 256)
#     if r % 4 == 0:
#         rand.append(r)
#         i += 1
# a = open('podzielneprzez4.txt', 'a')
# for elem in rand:
#     a.write(str(elem) + '\n')
# a.close()
#
# Zad. 2 Odczytaj plik z poprzedniego zadania i wyświetl jego zawartość
# with open('podzielneprzez4.txt', 'r') as a:
#     l = a.readlines()
#     l = [elem[:-1] for elem in l]
#     print(l)
#
# Zad. 3 Wykorzystując komendę with zapisz kilka linijek tekstu do pliku a następnie wyświetl je na ekranie.
# with open('plik.txt', 'a') as a:
#     for elem in 'stokrotka':
#         a.write(elem + '\n')
#
# with open('plik.txt', 'r') as b:
#     for elem in b:
#         print(elem[:-1])
#
#Zad.4 Stwórz klasę NaZakupy, która będzie przechowywać atrybuty:
# •	nazwa_produktu, ilosc, jednostka_miary, cena_jed
# •	oraz metody:
# •	konstruktor – który nadaje wartości
# •	wyświetl_produkt() – drukuje informacje o produkcie na ekranie
# •	ile_produktu() – informacje ile danego produktu ma być czyli ilosc + jednostka_miary np. 1 szt., 3 kg itd.
# •	ile_kosztuje() – oblicza ile kosztuje dana ilość produktu np. 3 kg ziemniaków a cena_jed wynosi 2 zł/kg wówczas funkcja powinna zwrócić wartość 3*2

# class NaZakupy:
#     def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
#         self.nazwa_produktu = nazwa_produktu
#         self.ilosc = ilosc
#         self.jednostka_miary = jednostka_miary
#         self.cena_jed = cena_jed
#
#     def wyswietl_produkt(self):
#         return self.nazwa_produktu
#
#     def ile_produktu(self):
#         return f'{self.ilosc} {self.jednostka_miary}'
#
#     def ile_kosztuje(self):
#         return self.ilosc * self.cena_jed
#
# cl = NaZakupy('masło', 10, 'kg', 5)
#
# print(cl.wyswietl_produkt())
# print(cl.ile_produktu())
# print(cl.ile_kosztuje())
#
# Zad.5 Utwórz klasę, która definiuje ciągi arytmetyczne. Wartości powinny być przechowywane jako atrybut. Klasa powinna mieć metody:
#
# •	wyświetl_dane – drukuje elementy na ekran
# •	pobierz_elementy– pobiera konkretne wartości ciągu od użytkownika
# •	pobierz_parametry – pobiera pierwsza wartość i różnicę od użytkownika oraz ilość elementów ciągu do wygenerowania.
# •	policz_sume – liczy sume elementow
# •	policz_elementy – liczy elementy jeśli pierwsza wartość i różnica jest podana

# class Arytmetyczne:
#     ciag = []
#     ilosc = 0
#     pe = 0
#     r = 0
#     def wyswietl_dane(self):
#         return f'Lista elementów: {self.ciag}'
#
#     def pobierz_elementy(self):
#         Nie rozumiem polecenia
        # pass
    #
    # def pobierz_parametry(self):
    #     self.pe = int(input("Podaj pierwszy element ciągu: "))
    #     self.r = int(input("Podaj różnicę ciągu: "))
    #     self.ilosc = int(input("Podaj ilość elementów ciągu do wygenerowania: "))
    #
    # def policz_sume(self):
    #     return f'Suma elementów: {sum(self.ciag)}'
    #
    # def policz_elementy(self):
    #     self.ciag.append(self.pe)
    #     for x in range(1, self.ilosc):
    #         self.ciag.append(self.ciag[x - 1] + self.r)


# kl = Arytmetyczne()
#
# kl.pobierz_parametry()
# kl.policz_elementy()
# print(kl.wyswietl_dane())
# print(kl.policz_sume())
