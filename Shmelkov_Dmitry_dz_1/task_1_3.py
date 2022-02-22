for n in range(101):
    if n == 0:
        continue
    elif n == 1:
        print(f'{n} процент')
    elif n > 4 and n <= 20:
        print(f'{n} процентов')
    elif n > 20:
        if str(n)[1] == "1" :
            print(f'{n} процент')
        elif str(n)[1] == "2" or str(n)[1] == "3" or str(n)[1] == "4":
            print(f'{n} процента')
        else :
            print(f'{n} процентов')
    else:
        print(f'{n} процента')