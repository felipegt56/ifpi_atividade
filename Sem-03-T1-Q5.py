def media(a, b, c):
  return (a + b + c) / 3

def main():
  nota1 = int(input('Primeira nota: '))
  nota2 = int(input('Segunda nota: '))
  nota3 = int(input('Terceira nota: '))
  media_nota = media(nota1, nota2, nota3)

  if (nota1 + nota2 + nota3) / 3 == media_nota:
    media_f = media_nota
    if nota3 > 8:
      media_f = media_nota + 1
      if media_f > 10:
        media_f -= 1
    print(f'{media_f:0.2f}')
if __name__=='__main__':
  main()
