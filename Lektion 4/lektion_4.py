"""

print(12 <= 15)# == , <=,<, >,>=,!=
print(5 >1500)
print(20== 20)
print(60 != 15)
print(2.3421 == 2.3421)
"""
"""
groesse_cm = int (input("Gib deine Körpergröße ein: "))
urteil = groesse_cm > 150 and groesse_cm < 215
print(urteil)
"""
"""
print(True,25<140 and not 10==100)
print(True, 100 >= 1  and not  2 > 10)
print(False, (  25 < 14  or   10 != 10))
print(False, not (-1 < 3 or 2 < 9) or 10 == 15)
print(True, not 20.05 < 12 < 10   and  -10 < 20 < 150 <= 150)
print(False, not (1 < 10   or  2 < 15)   or   -50 == 42)
print(True, not 2 == 10)
"""
"""
a = int(input("gib eine Zahl ein"))
urteil = a!= 0 and 100 / a>5
print(urteil)
"""
"""
a = int(input("Gib Zahl a ein: "))
b = int(input("Gib Zahl b ein: "))
c = int(input("Gib Zahl c ein: "))

ob_a_ist_max = a>b and a>c
ob_b_ist_max = b>c and b>a
ob_c_ist_max = not( ob_a_ist_max or ob_b_ist_max)
 
print(ob_a_ist_max,ob_b_ist_max,ob_c_ist_max)

print("Text" == "Text2")
print("Text"!= "Text2")
"""
"""
#not
not True    #=False
not False   #=True
not(not False)  #=False
not (4<10)  #=False


A B

0 1
1 0

#and
True and True   #True
True and False  #False
False and False #False
20<25 and 20 !=20

A B Y
1 1 1
1 0 0
0 1 0
0 0 0

#or
True or True    #True
True or False   #True
False or True   #True
False or False  #False
2<5 or 50 == 50.0001    #True

A B Y
1 1 1
1 0 1
0 1 1
0 0 0
"""


a = int(input("Hier stehen die Punkte des Fortnite Cups: "))

if a > 40:
    print('Deine Punktanzahl ist: ', a)
else:
    print('Deine Punkteanzahl ist: 0')

