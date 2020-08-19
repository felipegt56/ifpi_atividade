def maximo(n1,n2,n3,n4,n5):
    return max(n1, n2 ,n3 ,n4 ,n5)

def minimo(n1,n2,n3,n4,n5):
    return min(n1, n2, n3, n4, n5)

def media_5(n1, n2, n3, n4, n5):
    return (n1 + n2 + n3 + n4 + n5) / 5

def main():
    num1 = int(input('Digite o 1° número: '))
    num2 = int(input('Digite o 2° número: '))
    num3 = int(input('Digite o 3° número: '))
    num4 = int(input('Digite o 4° número: '))
    num5 = int(input('Digite o 5° número: '))
    resultado = media_5(num1,num2,num3,num4,num5)
    maxi = maximo(num1,num2,num3,num4,num5)
    mini = minimo(num1,num2,num3,num4,num5)
    print(f'O maior número lido foi {maxi}')
    print(f'O menor número lido foi {mini}')
    print(f'A média aritmética e {resultado:.2f}')

if __name__=='__main__':
    main()
