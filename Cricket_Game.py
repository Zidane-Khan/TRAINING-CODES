
# Team1=[]
# Team2=[]

Team1=str(input(f"Enter {1} team name: "))
# Team1.append(Teams)
print(f'Your team 1 is {Team1}')

Team2=str(input(f"Enter {2} team name: "))
# Team2.append(Teams)
# print(f'Your teams 2 is {Team2}')

No_Team_players=2
# Team_players_of_Team1=[]
# Team_players_of_Team2=[]
Members1={}
Members2={}

for i in range(No_Team_players):
    Member=input(f'enter name of member no {i+1} for {Team1} Team: ')
    position=input(f' Enter {Member} playing choose between baller, batsman or Allrounder')
    Members1.update({Member: position})
    # Members1[Member]=[position]

    # Team_players_of_Team1.append(Member)
        

# for j in range(No_Team_players):
#     Member=input(f'enter name of member no {j+1} for {Team2} Team: ')
#     position=input(f' Enter {Member} playing choose between baller, batsman or allrounder: ')
#     Members2.update({Member: position})
#     # Members2[Member]=[position]
    # Team_players_of_Team2.append(Member)
        
print(Members1)
# print(Members2)


batsman=[]
for player, position in Members1.items():
    if position.lower()=='batsman':
        batsman.append(player)

    if len(batsman)==2:
        break

striker,non_striker=batsman

overs=1
balls_per_over=3
score=0

# for batter in batsman:
for j in range(balls_per_over):
    print(f'{j+1}  ball')
    Experience=input(f'Enter the the experience of {j+1} this ball: ')

    if Experience=='out':
        print(f' {striker} its out')
        batsman.remove(striker)

    elif Experience=='wide':
        score=score+1

    else:
        runs=int(Experience)
        if runs==6:
            print(f'{non_striker} on strike')
            score=score+6
        elif runs==4:
            print(f'{non_striker} on strike')
            score=score+4
        # elif Experience==3:
        #     score=score+3
        elif runs==1:
            print(f' {non_striker} on strike')
            score=score+1
        # elif Experience==1:
        #     score=score+1

print(batsman)
        

#     if len(batsman)==2:
#         break

# if len(batsman)==2:
#     striker, non_striker=batsman
#     print(f'{striker}, {non_striker}')
          

    # print(position+1)
    # if position.lower()=='batsman':
    #     print(f"{player} has came to bat")
    # if position.lower()=='batsman':
    #     print(f"{player} has came to bat")
    # elif position=='baller':
    #     print(f"{player} is balling now")

    # # overs=2
# balls_per_over=3
# score=0

# for i in range(overs):
#     print(f'over {i+1} started')

#     for j in range(balls_per_over):
#         print(f'{j+1}  ball')
#         Experience=input(f'Enter the the experience of {j+1} this ball: ')

#         if Experience=='out':
#             print('its out')

#         elif Experience=='wide':
#             score=score+1

#         else:
#             runs=int(Experience)

#             if runs==6:
#                 score=score+6
#             elif runs==4:
#                 score=score+4
#             # elif Experience==3:
#             #     score=score+3
#             elif runs==2:
#                 score=score+2
#         # elif Experience==1:
#         #     score=score+1

# for player, position in Members2.items():
#     print(position)
#     if position.lower()=='batsman':
#         print(f"{player} has came to bat")
#     elif position=='baller':
#         print(f"{player} is balling now")

  

    
# overs=2
# balls_per_over=3
# score=0

# for i in range(overs):
#     print(f'over {i+1} started')

#     for j in range(balls_per_over):
#         print(f'{j+1}  ball')
#         Experience=input(f'Enter the the experience of {j+1} this ball: ')

#         if Experience=='out':
#             print('its out')

#         elif Experience=='wide':
#             score=score+1

#         else:
#             runs=int(Experience)

#             if runs==6:
#                 score=score+6
#             elif runs==4:
#                 score=score+4
#             # elif Experience==3:
#             #     score=score+3
#             elif runs==2:
#                 score=score+2
#         # elif Experience==1:
#         #     score=score+1

# print(f'First Team Score is {score}')



