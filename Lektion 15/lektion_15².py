def decimal(a):
    dec = 0
    Potenz = 0
    while(a>0):
        mod = a % 10
        a = a // 10
        dec += mod * (2 ** Potenz)
        Potenz += 1
        print(dec)

decimal(101001)