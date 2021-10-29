print()
relatorio_acerto= (' ')
relatorio_erro= (' ')
print('Perguntas e Respostas e Fornecimento de feedback corretivo')
perguntas = {
    'pergunta1': {
        'pergunta':'Marque a alternativa que apresenta um exemplo de algoritmo balanceamento de carga:',
        'resposta': {
            'a':'Round Robin',
            'b':'Stanford Metodology Algorithm',
            'c':'Markov Balanced',
            'd':'Ultra Balanced Round Algorithm',
            'd':'Balanced Scored Card',
        },
        'resposta_certa': 'a',
    },
    'pergunta2': {
        'pergunta':'Marque a alternativa que apresenta um tipo de cluster: ',
        'resposta': {
            'a':'Disponibilidade de balaceamento',
            'b':'Disponibilidade redundante',
            'c':'Alta carga',
            'd':'Alta disponibilidade',
            'd':'Alto balanceamento',
        },
        'resposta_certa': 'd',
    },    
}
print()
for pergunta_id, pergunta_dados in perguntas.items():
    print(f'{pergunta_id}: {pergunta_dados["pergunta"]}')
    
    for resposta_id, resposta_dados in pergunta_dados['resposta'].items():
        print(f'[{resposta_id}]: {resposta_dados}')

    respostas_usuario = input ('Sua Resposta: ')
    if respostas_usuario == pergunta_dados['resposta_certa']:
        print('Parabéns você acertou, continue assim!')
        relatorio_acerto = (relatorio_acerto + pergunta_dados["pergunta"]+'\n'
        +'A resposta certa seria: '+ pergunta_dados["resposta_certa"] +'\n'
        +'O aluno respondeu: '+ respostas_usuario +'\n\n')
    else:
        print('Infelizmente não foi dessa vez! Continue tentando!')
        relatorio_erro = (relatorio_erro + pergunta_dados["pergunta"]+'\n'
        +'A resposta certa seria: '+ pergunta_dados["resposta_certa"] +'\n'
        +'O aluno respondeu: '+ respostas_usuario +'\n\n')
    print()
print('Lista de questões certas:\n '+relatorio_acerto+'\n')
print('Lista de questões erradas:\n' + relatorio_erro)

arquivo = open('resultado.txt','a')
arquivo.write(relatorio_acerto + relatorio_erro)
arquivo.close()