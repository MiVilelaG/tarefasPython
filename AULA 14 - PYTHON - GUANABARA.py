n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um vlaor: '))
    if n % 2 ==0:
        par += 1
    else:
        impar +=1
print('Voce digitou {} números pares e {} numeros impares!'.format(par, impar))