'''
Criar  um programa que dependendo da temperatura (em celsius) do steak ele retorna o ponto de cozimento em portugues. 
O usuario devera fornecer a temperatura.


Temperaturas-Cozimento  
120°F ou 48°C - Rare (Selada)
130°F ou 54°C - Medium rare (Ao ponto para o mal)
140°F ou 60°C - Medium (Ao ponto)
150°F ou 65°C - Medium well (Ao ponto para o bem)
160°F ou 71°C - Well done (Bem passada)
'''

temp = int(input('Qual a temperatura da carne?: '))

if temp < 48:
    print('Cozinhar por mais algum tempo')
elif temp in range (48,53):
    print('Selada')
elif temp in range (54,59):
    print(' Mal passada')
elif temp in range (60,64):
    print('Ao ponto' )
elif temp in range (65,70):
    print('Bem passada')
elif temp >= 71:
    print('Assada')

