def compras(a, b, c, d, e):
    return a, b, c, d, e

def main():
    compra = float(input('Preço do Produto: R$ '))
    vista = compra - (compra * (9/100))
    cinco_vz = compra / 5
    dez_vz = compra +(compra * (17/100))
    parc_dez = dez_vz  / 10
    print(f'Pagamento à vista com desconto de 9%: R${vista:.2f} reais.')
    print(f'Prestação para pagamento em 5 vezes sem juros: R${cinco_vz:.2f} reais.')
    print(f'Prestação para pagamento em 10 vezes, com 17% de juros: R${parc_dez:.2f} reais.')

if __name__=='__main__':
    main()
