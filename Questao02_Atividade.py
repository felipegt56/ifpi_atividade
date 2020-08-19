def retorno(a):
    return ord(a)

def main():
    nome = input('Digite um único caractere para saber código numérico correspondente: ')
    caractere = retorno(nome)
    print(caractere)
    
if __name__=='__main__':
    main()
    
