def time(h, m, s):
    return f' {h}:{m}:{s}'

def main():
    tempo = int(input('tempo de duração do evento(segundos): '))
    horas = tempo // 3600
    rest_horas = tempo % 3600
    minutos = rest_horas // 60
    rest_min = tempo % 60
    segundos = rest_min
    hora = time(horas, minutos, segundos)
    print(f'O evento da fábrica durou {hora}')

if __name__=='__main__':
    main()
