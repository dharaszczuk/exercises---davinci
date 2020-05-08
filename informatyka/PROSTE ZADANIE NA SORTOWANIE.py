"""Poniżej zapisane są dwie listy słów (akurat dosyć losowych).
Połącz je i posortuj w odwrotnym porządku alfabetycznym.
Jako odpowiedź podaj wynik tych działań - kolejne słowa oddzielone przecinkami."""

lista1 = ['akwarium','zamek','kret','czeladnik','substytut','butonierka','malarz','mimoza','metamorfoza','kronika','miozyna','figlarna']
lista2 = ['holewka','alabaster','dramat','grupa','nierealny','nacja','ewolucja','orangutan','drobiazg','prawomocny']
lista3 = lista1 + lista2
lista3.sort()
lista3.reverse()

print (lista3)

