import random

zahl = input("Gib eine Zahl ein: ")
for i in range(int(zahl)):
    wurf = random.randint(1, 6)
    print(f"Wurf {i+1}: {wurf}")