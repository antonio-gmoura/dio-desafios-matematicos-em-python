while True:
    try:
        n = int(input())
        if (n == 360) or (n < 90): print("Bom Dia!!")
        elif (n >= 270): print("De Madrugada!!")
        elif (n >= 180): print("Boa Noite!!")
        elif (n >= 90): print("Boa Tarde!!")
    except EOFError:
        break