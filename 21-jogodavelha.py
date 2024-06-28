#Autor: joão cavanhas
#Data: 25/06/2024
#Versão 1.0
#Descrição: Joga da velha
#=====================================================

idosa = [['1', '2', '3'],
         ['4', '5', '6'],
         ['7', '8', '9']]
rodadas = 0
jogador = 'X'

def mostrar_vencedor(vencedor):
    print('temos um vencedor!', vencedor)
    return True 

while rodadas < 9:                                                        #Determina que quando chegar a 9 rodadas o sistema para
    posicao = input(f'jogador {jogador} escolha uma posição: ')
    posicao_encontrada = False
    for linha in range(3):
        linhaC = ''
        for coluna in range(3):
            if posicao == idosa[linha][coluna]:
                idosa[linha][coluna] = jogador
                posicao_encontrada = True
            linhaC += ' | ' + idosa[linha][coluna] + ' | '
        print(f'{linhaC}')
    if posicao_encontrada == True:
        rodadas = rodadas + 1
        if jogador == 'X':
            jogador = 'O'
        else:
            jogador = 'X'
    else:
        print('posição não encontrada')

    #soma = soma + 1 -> soma += 1
    #linha_completa = linha_completa + idosa[linha][coluna] + ' | '

    if idosa[0][0] == idosa[0][1] == idosa[0][2]: #linha 1
        houve_vencedor = mostrar_vencedor(idosa[0][0])
        break

    elif idosa[1][0] == idosa[1][1] == idosa[1][2]: #linha 2
        houve_vencedor = mostrar_vencedor(idosa[1][0])
        break

    elif idosa[2][0] == idosa[2][1] == idosa[2][2]: #linha 3
       houve_vencedor =  mostrar_vencedor(idosa[2][0])
       break

    elif idosa[0][0] == idosa[1][0] == idosa[2][0]: #coluna 1
        houve_vencedor = mostrar_vencedor(idosa[0][0])
        break
    
    elif idosa[0][1] == idosa[1][1] == idosa[2][1]: #coluna 2 
        houve_vencedor = mostrar_vencedor(idosa[0][1])
        break

    elif idosa[0][2] == idosa[1][2] == idosa[2][2]: #coluna 3
        houve_vencedor = mostrar_vencedor(idosa[0][2])
        break

    elif idosa[0][0] == idosa[1][1] == idosa[2][2]: #diagonal 1
        houve_vencedor = mostrar_vencedor(idosa[0][0])
        break

    elif idosa[0][2] == idosa[1][1] == idosa[2][0]: #diagonal 2
        houve_vencedor = mostrar_vencedor(idosa[0][2])
        break

    else:
        houve_vencedor = False

        if posicao_encontrada == True:
         rodadas = rodadas + 1
        if jogador == 'X':
            jogador = 'O'
        else:
            jogador = 'X'

    if(houve_vencedor == False):
        print('deu idosa!')

