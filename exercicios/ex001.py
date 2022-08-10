d=float(input('Qual é a distancia da sua viajem?:'))
print('Vc. vai viajar {} km.')
if d > 200:
    preço= d * 0,45
    preço= d *0,50 if d <= 200 else d * 0,45
    print(' E o preÇo da sua passagem sera R$ {:.2f}' . format (preço))
else:
    preço= d * 0,50
