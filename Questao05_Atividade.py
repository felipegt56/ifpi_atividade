def a_vista(p):
    return p - (p * (9/100))

def parcela_5(cinco_vz):
    return cinco_vz /5

def parcela_10(dez_vz):
    return (dez_vz + (dez_vz * (17/100))) / 10
            
def main():
    compra = float(input('Preço do Produto: R$ '))
    vista = a_vista(compra)
    pac_5 = parcela_5(compra)
    pac_10 = parcela_10(compra)
    print(f'Pagamento à vista com desconto de 9%: R${vista:0.2f} reais.')
    print(f'Prestação para pagamento em 5 vezes sem juros: R${pac_5:0.2f} reais.')
    print(f'Prestação para pagamento em 10 vezes, com 17% de juros: R${pac_10:0.2f} reais.')

if __name__=='__main__':
    main()
