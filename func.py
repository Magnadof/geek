def cor(cor,texto):
    print(f'\33[{cor}m{texto}\33[0m')

celula = 'word1;word2;word3,word4.word5'

def pontuacao(x):
    
    pontuacao = [',', '.', ';']

    valor="".join(',' if teste in pontuacao else teste for teste in x)

    print(len(valor))
    valor2=valor.split(',')
    print(f'o valor 2 é {valor2}')


pontuacao(celula)








