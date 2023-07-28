a = int(input('digite o valor de a:'))
b = int(input('digite o valor de b:'))
cond = input('soma[1] ou subtração[2]? ')

if cond == '1':
    print(f'{a} + {b} = {a+b}')
elif cond == '2':
    print(f'{a} - {b} = {a-b}')
else:
    print('comando n identificado')
