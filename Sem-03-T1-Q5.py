def media_f(a, b, c):
  return (a + b + c) / 3
def main():
  nota1 = int(input())
  nota2 = int(input())
  nota3 = int(input())
  media = media_f(nota1,nota2,nota3)
  if nota3 > 8:
    media_final =  1
    media = media + media_final
    if media > 10:
      media = 10
    

  print(f'{media:0.2f}')

if __name__=='__main__':
  main()
