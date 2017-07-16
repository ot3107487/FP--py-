'''
data si ora inceperii: 3:29PM, 10.15.2016
Features list:
F1. Citeste lista element cu element
F2. Secventa de lungime maxima cu proprietatea ca diferenta a
oricaror 2 numere consecutive este prima
F3. Secventa de lungime maxima cu proprietatea ca orice numar
se afla in intervalul [0,10]
F4. Iesire program

Plan de iteratie:
I1. F1,F4 Citeste lista element cu element/ Iesire program
I2. F2. Secventa de lungime maxima cu proprietatea ca diferenta a
oricaror 2 numere consecutive este prima
I3. F3. Secventa de lungime maxima cu proprietatea ca orice numar
se afla in intervalul [0,10]

Running scenario:
pass

Task-uri:
T1. Citirea unui numar
T2. Adaugarea unui numar in lista
T3. Verificarea daca un numar este prim
T4. Verificarea daca un numar apartine intervalului [0,10]
T5. Gasirea unui subsir de lungime maxima cu o anumita proprietate
T6. Afisarea unei liste
T7. Implementarea interfateti utilizator

T1->T2->T3/T4->T5->T7


'''
def citesteIntSecure(mesaj):
    '''
    Citeste un numarul n si verifica daca este intreg
    '''
    while True:
        try:
            n=int(input(mesaj))
            return n
        except ValueError:
            print("Mai incearca ! :)")
def adaugaElement(l,e):
    '''
    Adauga in lista l data ca parametru, elementul e
    date de intrare:
    l-lista de modificat
    e-elementul de adaugat

    date de iesire:
    lista modificata
    '''
    l.append(e)
    return l
def testAdaugaElement():
    assert adaugaElement([],2)==[2]
    assert adaugaElement([1,3],4)==[1,3,4]
#Testele sunt aici !!!!
def runTests():
    testAdaugaElement()
    testEstePrim()
    testDiferentaPrima()
    testIntervalNr()
def citesteLista(l):
    '''
    Citeste lista l element cu element, in functie de numarul de eleemente
    date de intrare:
    l-lista (vida sau nu)
    date de iesire:
    lista modificata
    '''
    n=citesteIntSecure("Introduceti 'lungimea' listei: ")
    for i in range (n):
        adaugaElement(l,citesteIntSecure("Introduceti elementul: "))
def citesteLista2(l):
    del l[:]
    citesteLista(l)
def afisareLista(l):
    for i in range(len(l)):
        print(l[i])
def estePrim(n):
    '''
    Verifica daca numarul n este prim
    Date de intrare:
    n-nr natural
    Date de iesire:
    True - n prime
    False-altfel
    
    '''
    if n<2:
        return False
    if n==2:
        return True
    if n%2==0:
        return False
    d=3
    while d*d<=n:
        if n%d==0:
            return False
        d=d+1
    return True
def diferentaPrima(a,b):
    if a>b:
        if estePrim(a-b):
            return True
        else:
            return False
    else:
        if estePrim(b-a):
            return True
        else:
            return False
def testDiferentaPrima():
    assert diferentaPrima(7,5)
    assert diferentaPrima(15,2)
    assert diferentaPrima(14,10)==False
    
def testEstePrim():
    assert estePrim(3)
    assert estePrim(7)
    assert estePrim(0)==False
    assert estePrim(-4)==False
    assert estePrim(16)==False
def intervalNr(n):
    '''
    verifica daca numarul n este in intervalul [0,10]
    date de intrare:
    n- numar intreg
    date de iesire:
    True- n apartine [0,10]
    False- altfel
    '''
    if n>=0 and n<=10:
        return True
    return False
def testIntervalNr():
    assert intervalNr(5)
    assert intervalNr(10)
    assert intervalNr(0)
    assert intervalNr(-1)==False
    assert intervalNr(11)==False

def secventaDiferentaPrima(l):
    '''
    Functia determina lungimea subsirului de lungime maxima din lista l
    care respecta proprietatea ca diferenta a oricaror 2 termeni consecutivi
    este prima.
    Parametri: - lista l
    Variabile folosite:
    pozC - pozitia curenta
    lungC - lungimea curenta
    poz - pozitia de unde incepe subsirul de lungime maxima
    p - inca o pozitie care salveaza pozitia curenta (sa nu se piarda)
    lungM - lungimea maxima
    '''
    pozC=0
    poz=0
    lungM=0
    while pozC<len(l)-lungM:
        lungC=0
        p=pozC
        for j in range(pozC,len(l)-1):
            if diferentaPrima(l[pozC],l[pozC+1]):
                lungC+=1
                pozC+=1
            else:
                break
        if lungC>lungM:
            lungM=lungC
            poz=p
        if lungC==0:
            pozC+=1
    for i in range(poz,poz+lungM+1):
        print(l[i])
    if lungM==0:
        print("Nu exista un astfel de subsir")
def secventaIntervalNr(l):
    '''
    Functia determina lungimea subsirului de lungime maxima din lista l
    care respecta proprietatea ca orice element al subsirului apartine [0,10]
    Parametri: - lista l
    Variabile folosite:
    pozC - pozitia curenta
    lungC - lungimea curenta
    poz - pozitia de unde incepe subsirul de lungime maxima
    p - inca o pozitie care salveaza pozitia curenta (sa nu se piarda)
    lungM - lungimea maxima
    '''
    pozC=0
    poz=0
    lungM=0
    while pozC<len(l)-lungM:
        lungC=0
        p=pozC
        for j in range(pozC,len(l)):
            if intervalNr(l[pozC]):
                lungC+=1
                pozC+=1
            else:
                break
        if lungC>lungM:
            lungM=lungC
            poz=p
        if lungC==0:
            pozC+=1
    for i in range(poz,poz+lungM):
        print(l[i])
    if lungM==0:
        print("Nu exista un astfel de subsir")
def meniu():
    print("\n")
    print("Take a pick ! Choose it wisely...you must: ")
    print("1.Citeste lista")
    print("2.Citeste alta lista")
    print("3.Afiseaza lista citita")
    print("4.Secventa de lungime maxima cu diferenta prima")
    print("5.Secventa de lungime maxima cu elemente de la 0 la 10")
    print("6.Iesire")

def citireComanda():
    return input("Ce vrei sa faci? \n")
def runProgram():
    l=[]
    comenzi={"1":citesteLista,"2":citesteLista2,"3":afisareLista,"4":secventaDiferentaPrima,"5":secventaIntervalNr}
    while True:
        meniu()
        cmd=citireComanda()
        if cmd=="6":
            print("De ceee?!?!?!?...")
            return
        if cmd in comenzi:
            try:
                comenzi[cmd](l)
            except ValueError as ex:
                print(ex)
        else:
            print("Command error! Introduceti ceva intre 1 si 4")
        
        
def main():
    runTests()
    runProgram()
main()

#terminat azi: 10.15.2016 9:34 PM .
#Pauzele lungi si dese ... cheia marilor succes(uri)e
