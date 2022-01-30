# Calculadora em Python

print('********************* Python Calculator *********************\n\n') 


print('Selecione o número da operação desejada: \n')

print('1 - Soma')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão\n')

a = int(input('Digite sua opção (1/2/3/4):  '))

x = int(input('\nDigite o primeiro número:  '))

y = int(input('\nDigite o segundo número:  ')) 


if a == 1:
    somar = x + y
    print(f'\n{x} + {y} = {somar}')

    
elif a == 2:
    subtrair = x - y
    print(f'\n{x} - {y} = {subtrair}')

elif a == 3:
    multiplicar = x * y
    print(f'\n{x} * {y} = {multiplicar}')

elif a == 4:
    dividir = x/y
    print(f'\n{x} / {y} = {dividir}')

else: print ('\nA opção escolhida é inválida!') 
