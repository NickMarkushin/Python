list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
kolvoigrokov=len(list_players) #Всего игроков
kolvovkomande=kolvoigrokov/2 #Игроков в одной команде
first_team=list_players[0:int(kolvovkomande)]
second_team=list_players[int(kolvovkomande):]
print(first_team)
print(second_team)