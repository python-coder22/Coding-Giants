""""
zahl = 69           #Datentyp: int
text = "Das ist ein string."    #Datentyp: str
wahr = True         #Datentype: bool (boolean)
falsch = False      #Datentype: bool (boolean)
komma_zahl = 6.9    #Snake Case    #Datentyp: float
kommaZahl = 6.9     #Camel Case
KommaZahl = 6.9     #Pascal Case
KOMMA_ZAHL = 6.9    #Upper Case

KONSTANTE = 6.9     #Konstante

komma_zahl = komma_zahl - 1

print(komma_zahl)

datentyp_zahl = type(zahl)

print("Datentyp von der Variable zahl:", datentyp_zahl)

datentype_text = type(text)

print("Datentyp von der Variable text:", datentype_text)

datentype_wahr = type(wahr)

print("Datentyp von der Variable wahr:", datentype_wahr)

datentype_falsch = type(falsch)

print("Datentyp von der Variable falsch:", datentype_falsch)

text2 = "Das ist ein anderer string." #Datentype: str

zahl2 =100

ist_gleich = (text == text2)

print("Die Vergleichsoperation der Variable text und text2 ergibt:", ist_gleich)

text2 = "Das ist ein string."

ist_gleich2 = (text == text2)

print("Die Vergleichsoperation der Variable text und text2 ergibt:", ist_gleich2)

"""
#Variablen
n = 11
print(n)

n = 15
print(n)

n = "Test"
print(n)

m = 'Test'
print(n)

n = True
m = n
print(type(m))

#Grundlegende Variablentypen
#int
a = 10
print(a, type(a))
a = -2560
print(a, type (a))

#float 
b = 125.01238
print(b, type (b))
b = -0.9991
print(b, type(b))

#bool
c = True
print(c,type(c))
c =  False
print(c,type(c))

#str
d = "Dein Test"
print(d, type(d))

d = "23"
print(d, type(d))

d = "das ist auch ein test"
print(d, type(d))

#Konventierung von Variablen
#Konventierung in den Typ int
a = int(3.2)
print(a,type(a))

a = int(True)
print(a,type(a))

a = int(False)
print(a,type(a))

a = int('10')
print(a,type(a))


# Konvertierung in den Typ float
b = float(1)
print(b, type (b))

b = float(True)
print(b, type (b))


b = float(False)
print(b, type (b))


b = float('21.4')
print(b, type (b))


b = float('2')
print(b, type ('b'))


#Konvertierung in den Typ bool
c = bool(-1)
print(c, type(c))

c = bool(0)
print(c, type(c))

c = bool(1)
print(c, type(c))

c = bool(2)
print(c, type(c))



#Konvertierung in den Type string
d = str(16)
print(d, type(d))

d = str(1.5)
print(d, type(d))

d = str(True)
print(d, type(d))

d = str(False)
print(d, type(d))

x = input("Gib etwas ein")
try:
    x = int(x) 
    print('hat geklappt')
except:
    print('Falsche eingabe')

zahl = 3
Zahl = 4
ZAHL = 5

print(zahl, Zahl, ZAHL)

