def time(temp, h, r_h, m, r_m, s):
    return temp, h, r_h, m, r_m, s

def main():
    tempo = int(input('tempo de duração do evento(segundos): '))
    horas = tempo // 3600
    rest_horas = tempo % 3600
    minutos = rest_horas // 60
    rest_min = tempo % 60
    segundos = rest_min
    print(f'O evento da fábrica durou {horas}:{minutos}:{segundos}')

if __name__=='__main__':
    main()
