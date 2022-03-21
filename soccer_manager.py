#!/usr/bin/python
#*- coding: utf-8 -*-
import random
import classes

all_players = [classes.Player('Астафьев', 5, 0),
               classes.Player('Вадим', 7, 0),
               classes.Player('Валера', 10, 1),
               classes.Player('Ваня', 9, 0),
               classes.Player('Ваня от Мишы', 8, 0),
               classes.Player('Головин', 5, 1),
               classes.Player('Ден от Мишы', 7, 0),
               classes.Player('Егоров Ваня', 6, 0),
               classes.Player('Сивков Женя', 6, 0),
               classes.Player('Илюха', 9, 1),
               classes.Player('Кирилл', 8, 1),
               classes.Player('Виноградов Коля', 8, 1),
               classes.Player('Корпача Юра', 4, 1),
               classes.Player('Крюков Коля', 5, 0),
               classes.Player('Маслов Макс', 8, 1),
               classes.Player('Мезнев', 5, 1),
               classes.Player('Миша', 10, 1),
               classes.Player('Збитнев Миша', 6, 0),
               classes.Player('Молотков Олег', 3, 0),
               classes.Player('Морозов Лёха', 6, 1),
               classes.Player('Рамиль', 10, 1),
               classes.Player('Серёга Орлов', 10, 1),
               classes.Player('Тюкин Андрей', 6, 1),
               classes.Player('Хоменко Гриша', 6, 1)
               ]

# random.shuffle(all_players)
# for i in all_players:
#     print (i.name)

players = [p for p in all_players if p.active == 1]

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
        
for t in teams:    
    print (t.name)    
    for p in t.list_players:
        print (p.name)
    print('')
