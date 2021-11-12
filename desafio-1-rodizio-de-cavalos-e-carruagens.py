n = int(input())
while n > 0:
    n -= 1
    #placa = input().split('-')
    placa = input()
    try:
        pos = 0
        for char in placa:
            if (pos < 3):
                if char.islower(): raise Exception ("Caracter não é letra minúscula!", char)
                if not char.isalpha(): raise Exception ("Caracter não é letra!", char)
            elif (pos == 3):
                if char != "-": raise Exception ("É esperado um hífen na quarta posição!", char)
            elif (pos < 8):
                if not char.isnumeric(): raise Exception ("Caracter não é numero!", char)
            else:
                raise Exception ("Placa com mais de oito caracteres!", placa)
            pos += 1
        r = int(placa[pos - 1])
        if r == 9 or r == 0:
            print('SEXTA')
        elif r > 6:
            print('QUINTA')
        elif r > 4:
            print('QUARTA')
        elif r > 2:
            print('TERCA')
        else:
            print('SEGUNDA')
    except Exception as e:
        print('FALHA')
