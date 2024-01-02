def cor(cor,texto):
    print(f'\33[{cor}m{texto}\33[0m')


def pontuacao(x):
    
    punctuation = [',', '.', ';']
    gender="".join(',' if letter in punctuation else letter for letter in x)
    gender=gender.split(',')
    valor=len(gender)
    return(valor)
    



v='word1;word2;word3,word4.word5'


print(pontuacao(v))

