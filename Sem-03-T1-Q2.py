def numero(n):
  return n%2

def main():
  num = int(input('Digite para saber se é um número ímpar: '))
  impar = numero(num)

  if impar == 1:
    print(impar == 1)
  else:
    print(impar != 0)


if __name__=='__main__':
  main()
