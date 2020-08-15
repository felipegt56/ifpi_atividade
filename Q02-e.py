def medida(a, b, c, d, e, f):
    return a, b, c, d, e, f

def main():
    a = float(input())
    c = float(input())
    l = float(input())
    A_piso = l * c
    V_sala = l * c * a
    A_sala = 2 * a * l + 2 * a * c 
    print(f'{A_piso:.2f}')
    print(f'{V_sala:.2f}')
    print(f'{A_sala:.2f}')

if __name__=='__main__':
    main()
