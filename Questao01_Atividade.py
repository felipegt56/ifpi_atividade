def nome(nome):
    return len(nome)

def main():
    nom = str(input('Digite seu nome: ')).strip()
    nam = nome(nom)
    print(f' Seu nome possui {nam} letras.')

if __name__=='__main__':
    main()
