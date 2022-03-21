#!/usr/bin/python
#*- coding: utf-8 -*-
import random
import classes

all_players = [classes.Player('Астафьев', 6, 0),
               classes.Player('Вадим', 7, 0),
               classes.Player('Валера', 9, 1),
               classes.Player('Ваня', 9, 0),
               classes.Player('Ваня от Мишы', 6, 0),
               classes.Player('Головин', 5, 1),
               classes.Player('Ден от Мишы', 8, 0),
               classes.Player('Егоров Ваня', 5, 0),
               classes.Player('Сивков Женя', 5, 1),
               classes.Player('Илюха', 8, 1),
               classes.Player('Кирилл', 8, 0),
               classes.Player('Виноградов Коля', 7, 1),
               classes.Player('Корпачан Юра', 5, 1),
               classes.Player('Крюков Коля', 5, 0),
               classes.Player('Маслов Макс', 6, 1),
               classes.Player('Мезнев', 5, 0),
               classes.Player('Миша', 9, 0),
               classes.Player('Збитнев Миша', 6, 0),
               classes.Player('Молотков Олег', 4, 0),
               classes.Player('Морозов Лёха', 6, 0),
               classes.Player('Рамиль', 10, 1),
               classes.Player('Серёга Орлов', 10, 0),
               classes.Player('Тюкин Андрей', 5, 0),
               classes.Player('Хоменко Гриша', 5, 1),
               classes.Player('Юра', 6, 1)
               ]

# random.shuffle(all_players)
# for i in all_players:
#     print (i.name)

players = [p for p in all_players if p.active == 1]

print('Заявлено игроков: '+ str(len(players)))
#players = [Player('Player1',10),Player('Player2',9),Player('Player3',9),Player('Player4',9),Player('Player5',9),Player('Player51',9),Player('Player6',8),Player('Player7',8)]
teams = []      #teams in structure: [massive playes], total lvl all playes
cnt_teams = 2   #input parameter, calculate by counе declared playes


#cur_lvl_players = [p for p in players if p.level=='2']
#print(len(cur_lvl_players))


for i in range(cnt_teams):    
    teams.append(classes.Team([],0))

#for t in teams:
#    print (str(t.list_players) + ' - '+str(t.total_level))

# start complete teams from 10 lvl to 1 lvl
current_lvl=10
while(current_lvl>0):
    cur_lvl_players = [p for p in players if p.level==current_lvl]
    random.shuffle(cur_lvl_players)
    for player in cur_lvl_players:
        teams.sort(key=lambda x: (x.number_players, x.total_level))
        teams[0].add_player(player)
    current_lvl-=1

teams.sort(key=lambda x: x.team_number)        
for t in teams:    
    print (t.name)
    #random.shuffle(t.list_players)    
    for p in t.list_players:
        print (p.name)
    print('')
