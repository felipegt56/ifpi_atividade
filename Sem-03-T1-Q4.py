def caractere_1(a):
  return True
def caractere(a):
  return False

def main():
  num = input('Digite um caractere qualque: ')
  verdadeiro = caractere_1(num)
  falso = caractere(num)
  
  if num >= '0' and num <= '9':
   print(f'{verdadeiro}') 
  else:
    print(f'{falso}')

if __name__=='__main__':
  main()
