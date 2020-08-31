def Ilmo(n):
  return f'Ilmo Sr. {n}'
def Ilma(n):
  return f'Ilma Sra. {n}'

def main():
  nome = str(input('Qual é o seu nome? '))
  sexo = int(input('Defina seu sexo MASCULINO(1)/ FEMININO(2): '))
  n1 = Ilmo(nome)
  n2 = Ilma(nome)
  if sexo == 1:
    print(f'Ilmo Sr.{nome}')
  else:
    print(f'Ilma Sra.{nome}')

if __name__=='__main__':
  main()
