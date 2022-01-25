'''
Criar um programa que calcula a quantidade de tinta necessária para pintar uma parede.
O usuário deverá fornecer as seguintes informações: Rendimento, altura e largura.
O programa deve mostrar na tela a mensagem 'Você necessita de um x latas de tinta'

'''
def calculo_tinta():
    
    rend = int(input('Qual o rendimento da tinta?: '))
    altura = int(input('Qual a altura?: '))
    largura = int(input('Qual a largura?: '))
 
    

    calculo_rend = (rend / 2)
    calculo_area = (altura * largura)
    result = (calculo_area / calculo_rend)
    print(f'Você necessita de {int(result)} latas de tinta')


calculo_tinta()
  







