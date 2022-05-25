from collections import Counter


def statistic_game(datas):
    timeout = sum(1 for data in datas if data['timeout'])
    rounds = sum(data['rounds'] for data in datas)

    type_player = Counter()
    for data in datas:
        type_p = data['type_player'] if data['type_player'] is not None else 'timeout'
        type_player[type_p] += 1
    print(f'''Partidas terminadas em timeout:''', f'''{timeout}''')
    print(f'''Média de rodadas''', f'''{rounds / len(datas)}''')
    print('Tipo de jogador que mais venceu foi: {0}, com {1} de vitórias'.format(
          type_player.most_common()[0][0], type_player.most_common()[0][1]))
    print('Porcentagem por tipo de jogador: ')
    for type_p, qtd in type_player.most_common():
        print("----> {0} : {1} %".format(type_p, (qtd * 100) // len(datas)))


