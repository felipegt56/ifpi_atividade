def data(dia, mes, ano):
    return dia, mes, ano

def main():
    dia = int(input('Dia: '))
    mes = int(input('Mês: '))
    ano = int(input('Ano: '))
    day = data(dia,mes,ano)
    print(f'{dia}/{mes}/{ano}')

if __name__=='__main__':
    main()
