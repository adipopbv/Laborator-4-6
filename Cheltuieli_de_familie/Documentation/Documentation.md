# Cheltuieli de familie #

## Cerința:

> Scrieți o aplicație care gestionează cheltuielile de familie efectuate într-o lună. Pentru o cheltuială se vor reține ziua (din lună), suma, tipul cheltuielii (5 categorii: mâncare, întreținere, îmbrăcăminte, telefon, altele).

## Lista de funcționalități:

### 1.Adaugă cheltuială:

 - adaugă o nouă cheltuială(se specifică ziua, suma, tipul)
 - actualizează cheltuială(se specifică ziua, suma, tipul)

### 2.Ștergere:

 - Șterge toate cheltuielile pentru ziua dată
 - Ștergecheltuielile pentru un interval de timp (se dă ziua de început și sfârșit, se ștergtoate cheltuielile pentru perioada dată)
 - Șterge toate cheltuielile de un anumit tip

### 3.Căutări:

 - Tipărește toate cheltuielile mai mari decât o sumă dată
 - Tipărește toate cheltuielile efectuate înainte de ozi dată și mai mici decât o sumă (se dă suma și ziua, se tipăresc toate cheltuielile mai mici ca suma dată și efectuate înainte de ziua specificată)
 - tipărește toate cheltuielile de un anumit tip.

### 4.Rapoarte:

 - Tipărește suma totală pentru un anumit tip de cheltuială
 - Găsește ziua în care suma cheltuită e maximă
 - Tipărește toate cheltuielile ce au o anumită sumă
 - Tipărește cheltuielile sortate după tip

### 5.Filtrare:

 - Elimină toate cheltuielile de un anumit tip
 - Elimină toate cheltuielile mai mici decâto sumă dată

### 6.Undo:

 - Reface ultima operație (lista de cheltuieli revine ce exista înainte de ultima operație care a modificat lista).

## Planul de iterații:

### Prima iterație:

 - 1.a.
 - 1.b.
 - 3.a.
 - 4.a.
 - 5.a.

### A doua iterație:

 - 2.a.
 - 2.b.
 - 2.c.
 - 3.b.
 - 4.b.

### A treia iterație:

 - 3.c.
 - 4.c.
 - 4.d.
 - 5.b.
 - 6.a.

## Scenarii de rulare:

| Utilizator | Aplicatia | Actiune |
| --- | --- | --- |
|  | Afisare meniu | Se afisaza meniul de comenzi |
| Comanda 1 |  | Adaugarea unei noi cheltuieli |
|  | Adaugare cheltuiala | Se adauga o noua cheltuiala in lista |
| Comanda 2 |  | Actualizarea unei cheltuieli |
|  | Actualizare cheltuiala | Se actualizeaza cheltuiala dorita |
| Comanda 3 |  | Stergerea tuturor cheltuielilor dintr-o zi |
|  | Stergere cheltuieli| Se sterg cheltuielile din ziua introdusa |
| Comanda 4 |  | Stergerea cheltuielilor dintr-un interval dat de timp | 
|  | Stergere cheltuieli | Se sterg cheltuielile din intervalul de timp dat |
| Comanda 5 |  | Stergerea tuturor cheltuielilor de un anumit tip |
|  | Stergerea cheltuielilor | Se sterg cheltuielile de tipul introdus |
| Comanda 6 |  | Cheltuielile mai mari decat o anumita suma |
|  | Tiparirea cheltuielilor cerute | Se tiparesc cheltuielile mai mari decat suma introdusa |
| Comanda 7 |  | Cheltuielile de dinaintea unei zile si mai mici decat o suma |
|  | Tiparirea cheltuielilor cerute | Se tiparesc cheltuielile de dinaintea zilei date si mai mici decat suma data |
| Comanda 8 |  | Cheltuielile de un anumit tip |
|  | Tiparirea cheltuielilor cerute | Se tiparesc toate cheltuielile de tipul dat |
| Comanda 9 |  | Suma totala pentru un anumit tip de cheltuiala |
|  | Tiparirea sumei | Se tipareste suma totala pentru tipul de cheltuiala introdusa |
| Comanda 10 |  | Ziua in care se afla suma maxima cheltuita |
|  | Tiparirea zilei | Se tipareste ziua in care se afla suma maxima cheltuita |
| Comanda 11 |  | Toate cheltuielile ce au o anumita suma |
|  | Tiparirea cheltuielilor | Se tiparesc cheltuielile ce au o anumita suma |
| Comanda 12 |  | Cheltuielile sortate dupa tip |
|  | Tiparirea cheltuielilor | Se tiparesc cheltuielile sortate dupa tip |
| Comanda 13 |  | Elimina cheltuielile de un anumit tip |
|  | Tiparirea cheltuielilor | Se tiparesc cheltuielile care nu sunt de tipul introdus |
| Comanda 14 |  | Elimina cheltuielile mai mici decat o suma data |
|  | Tiparirea cheltuielilor | Se tiparescc cheltuielile mai mari sau egale cu suma introdusa |
| Comanda 15 |  | Refacerea ultimei operatii |
|  | Refacerea operatiei | Se reface ultime operatie efectuata asupra listei de cheltuieli |
| Comanda 16 |  | Iesirea din aplicatie |
|  | Iesire | Se incheie rularea aplicatiei |