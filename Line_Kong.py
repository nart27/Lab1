# WIKI  Xn+1=(a*Xn+c) mod m
def KONG():
    m = 256  # диапазон значений m>=2
    a = 5  # множитель 0<=a<=m
    c = 1  # приращение 0<=c<=m
    x0 = 0  # нач значение

    i=1
    while i<=m:

        res=((a*x0+c)%m)
        x0=res
        print(i, '  ', res)
        i+=1




    print('Worked!')
    return 0

print(KONG())