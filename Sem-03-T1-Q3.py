def verde(a):
  return f'Siga'
def amarelo(b):
  return f'Atenção'
def vermelho(c):
  return f'Pare' 

def main():
  cor = str(input('Qual a cor do sinal de trânsito(V é verde/ A é amarelo / E é vermelho: ')).upper()
  sinal_v = verde(cor)
  sinal_a = amarelo(cor)
  sinal_e = vermelho(cor)

  if cor == 'V':
    print(f'{sinal_v}')
  elif cor == 'A':
    print(f'{sinal_a}')
  elif cor == 'E':
    print(f'{sinal_e}')
  else:
      print('Opção invalida, escolha entre V, A, E')

if __name__=='__main__':
  main()
