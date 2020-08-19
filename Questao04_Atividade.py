def num(n1, n2, n3, n4, n5, maior, menor, media):
    return max(maior), min(menor)

def main():
    num1 = int(input('Digite o 1° número: '))
    num2 = int(input('Digite o 2° número: '))
    num3 = int(input('Digite o 3° número: '))
    num4 = int(input('Digite o 4° número: '))
    num5 = int(input('Digite o 5° número: '))
    maxi = [num1,num2,num3,num4,num5]
    mini = [num1,num2,num3,num4,num5]
    medi = (num1 + num2 + num3 + num4 + num5) / 5
    print(f'O maior número lido foi {max(maxi)}')
    print(f'O menor número lido foi {min(mini)}')
    print(f'A média aritmética e {medi}')

if __name__=='__main__':
    main()
