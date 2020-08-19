def parcela_5(cinco_vz):
    return cinco_vz /5

def parcela_10(dez_vz):
    return dez_vz / 10

def main():
    compra = float(input('Preço do Produto: R$ '))
    vista = compra - (compra * (9/100))
    dez_vz = compra +(compra * (17/100))
    pac_5 = parcela_5(compra)
    pac_10 = parcela_10(dez_vz)
    print(f'Pagamento à vista com desconto de 9%: R${vista:.2f} reais.')
    print(f'Prestação para pagamento em 5 vezes sem juros: R${pac_5:.2f} reais.')
    print(f'Prestação para pagamento em 10 vezes, com 17% de juros: R${pac_10:.2f} reais.')

if __name__=='__main__':
    main()
