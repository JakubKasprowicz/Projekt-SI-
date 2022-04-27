

import pandas as pd

pd.options.mode.chained_assignment = None  # default='warn'
import random


def zwroc_najgorszy(dictlist, tab_fit):
    for i in range(10):  # elememnt najgorszy, który chcemy następnie zastępować znalezionym lepszym elementem
        if (dictlist[i].get('fitness')) == tab_fit[0]:
            rekord_najgorszy = dictlist[i].get('ktory')
            return rekord_najgorszy


HMS = 10
HM = []
tab_fit = [None] * 10
pd.options.display.max_rows = 9999
df = pd.read_csv('baza danych samochodow.csv', usecols=[0, 1, 2, 3], nrows=9999)
y = pd.read_csv('baza danych samochodow.csv', usecols=[0, 1, 2, 3], nrows=1)
j = 0
fitness = 0
for i in range(HMS):
    while j <= HMS-1:
        liczba_losowa = random.randint(1, 9999)
        bak = df.iloc[liczba_losowa][0]
        fitness = df.iloc[liczba_losowa][2] / df.iloc[liczba_losowa][
            3]  # jakością jest iloczyn mocy i spalania, warunkiem jest bak większy od 50 litrów
        # HM[0]= fitness HM[1] = caly obiekt HM[1][0] = poj baku HM[1][1] = marka HM[1][2] = moc HM[1][3] = spalanie
        if ((int(bak) > 50) and (int(fitness) > 33)):
            HM.append(round(fitness, 2))
            HM.append(df.iloc[liczba_losowa])
            # gotowa lista to fitness obiekt fitness obiekt etc..
            j = j + 1

dictlist = [dict() for x in range(10)]
for key in HM:
    print(key)
print( "HM przed znajdowaniem najlepszego rozwiazania ============================================================================")

for i in range(1_000_0):
    if (i % 500 == 0):
        print("Petla numer" + str(i))
    for i in range(10):
        dictlist[i]["fitness"] = HM[
            2 * i]  # wpisanie do slownikow wartosci fitness oraz numeru w pamieci, który zajmuje dany rekord
        dictlist[i]["ktory"] = i
        tab_fit[i] = HM[2 * i]
    tab_fit.sort()
    liczba_losowa = random.randint(1, 100)
    if int(liczba_losowa) < 30:
        temp = random.randint(0, 9)
        nowyRekord = HM[3]
        nowyRekord[0] = int(HM[2 * temp + 1][0])
        nowyRekord[1] = str(HM[2 * temp + 1][1])
        nowyRekord[2] = int(HM[2 * temp + 1][2])
        nowyRekord[3] = int(HM[2 * temp + 1][3])
        if (HM[2 * temp + 1][2] / HM[2 * temp + 1][3]) < (nowyRekord[2] / nowyRekord[3] and int(nowyRekord[0] > 50)):
            HM[2 * temp + 1] = nowyRekord
            print("zamieniam rekord o numerze " + str(2 * temp + 1))

    if 30 <= int(liczba_losowa) <= 70:
        temp = random.randint(1, 999)
        nowyRekord = df.iloc[temp]
        fitness = df.iloc[temp][2] / df.iloc[temp][3]
        if (fitness > HM[zwroc_najgorszy(dictlist, tab_fit) * 2] and int(nowyRekord[0]) > 50):
            indeks_rekordu = zwroc_najgorszy(dictlist, tab_fit)
            print("zamieniam rekord o numerze " + str(indeks_rekordu))
            HM[indeks_rekordu * 2] = fitness
            HM[(indeks_rekordu * 2) + 1] = nowyRekord
    if int(liczba_losowa) > 70:
        essa = random.randint(1, 999)
        temp = random.randint(0, 9)

        nowyRekord = df.iloc[essa]
        nowyRekord[0] = int(HM[2 * temp + 1][0])
        nowyRekord[2] = int(HM[2 * temp + 1][2])
        if (HM[2 * temp + 1][2] / HM[2 * temp + 1][3]) < (nowyRekord[2] / nowyRekord[3] and int(nowyRekord[0]) > 30):
            HM[2 * temp + 1] = nowyRekord
            print("zamieniam rekord o numerze " + str(2 * temp + 1))

for key in HM:
    print(key)
