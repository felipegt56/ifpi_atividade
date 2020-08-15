def segundos (a, b, c, d, e):
    return a, b, c, d, e

def main():
    h = int(input())
    m = int(input())
    s = int(input())
    conversao_horas = h + (m/60) + (s/3600)
    conversao_segundos = conversao_horas *3600
    print(f'{conversao_segundos:.2f}')

if __name__== '__main__':
    main()




        
    
