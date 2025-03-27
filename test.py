
# import random

# print('Entering Team Name.......')
# Team1 = str(input(f"Enter {1} team name: "))
# print(f'Your team 1 is {Team1}')
# Team2 = str(input(f"Enter {2} team name: "))
# print(f'Your team 2 is {Team2}')

# print('Going into toss......\n')
# print('Both teams captain please come for toss\n')
# toss_team1 = {}
# toss_team2 = {}

# tos1 = input(f'Enter heads or tails for {Team1}: ')
# if tos1 == 'heads':
#     toss_team1.update({Team1: tos1})
# else:
#     toss_team1.update({Team1: tos1})

# tos2 = input(f'Enter heads or tails for {Team2}: ')
# if tos2 == 'heads':
#     toss_team2.update({Team2: tos2})
# else:
#     toss_team2.update({Team2: tos2})

# r1 = random.choice(['heads', 'tails'])
# print(f'Let’s flip!!! Congratulations, it’s {r1}')

# team1_choosen = []
# team2_choosen = []

# # Handling team1's toss choice
# for tos in toss_team1.values():
#     if tos == r1:
#         print(f"{Team1} wins the toss")
#         choosing = input(f"Please {Team1}, choose between batting and field: ")
#         print(f"{Team1} has chosen {choosing}")
#         if choosing == 'batting':
#             team1_choosen.append('batting')
#             team2_choosen.append('field')
#             print(f"{Team1} please come forward for batting")
#             print(f"{Team2} please come forward for fielding")
#         elif choosing == 'field':
#             team1_choosen.append('field')  # **Fix: Corrected appending here**
#             team2_choosen.append('batting')  # **Fix: Corrected appending here**
#             print(f"{Team1} please come forward for fielding")
#             print(f"{Team2} please come forward for batting")

# # Handling team2's toss choice
# for tos1 in toss_team2.values():
#     if tos1 == r1:
#         print(f"{Team2} wins the toss")
#         choosing1 = input(f"Please {Team2}, choose between batting and field: ")  # **Fix: Renamed `choosing1` here**
#         print(f"{Team2} has chosen {choosing1}")
#         if choosing1 == 'batting':
#             team2_choosen.append('batting')
#             team1_choosen.append('field')
#             print(f"{Team2} please come forward for batting")
#             print(f"{Team1} please come forward for fielding")
#         elif choosing1 == 'field':
#             team2_choosen.append('field')  
#             team1_choosen.append('batting')  
#             print(f"{Team2} please come forward for fielding")
#             print(f"{Team1} please come forward for batting")

# print(f"Team 1 has chosen: {team1_choosen}")
# print(f"Team 2 has chosen: {team2_choosen}")



import random

print('Entering Team Name.......')
Team1 = str(input(f"Enter {1} team name: "))
print(f'Your team 1 is {Team1}')
Team2 = str(input(f"Enter {2} team name: "))
print(f'Your team 2 is {Team2}')

print('Going into toss......\n')
print('Both teams captain please come for toss\n')
toss_team1 = {}
toss_team2 = {}

tos1 = input(f'Enter heads or tails for {Team1}: ')
if tos1 == 'heads':
    toss_team1.update({Team1: tos1})
else:
    toss_team1.update({Team1: tos1})

tos2 = input(f'Enter heads or tails for {Team2}: ')
if tos2 == 'heads':
    toss_team2.update({Team2: tos2})
else:
    toss_team2.update({Team2: tos2})

r1 = random.choice(['heads', 'tails'])
print(f'Lets flip!!! Congratulations, its {r1}')

team1_choosen = []
team2_choosen = []

# Handling team1's toss choice
for tos in toss_team1.values():
    if tos == r1:
        print(f"{Team1} wins the toss")
        choosing = input(f"Please {Team1}, choose between batting and field: ")
        print(f"{Team1} has chosen {choosing}")
        if choosing == 'batting':
            team1_choosen.append('batting')
            team2_choosen.append('field')
            print(f"{Team1} please come forward for batting")
            print(f"{Team2} please come forward for fielding")
        elif choosing == 'field':
            team1_choosen.append('field')  
            team2_choosen.append('batting')  
            print(f"{Team1} please come forward for fielding")
            print(f"{Team2} please come forward for batting")

# Handling team2's toss choice
for tos1 in toss_team2.values():
    if tos1 == r1:
        print(f"{Team2} wins the toss")
        choosing1 = input(f"Please {Team2}, choose between batting and field: ")  
        print(f"{Team2} has chosen {choosing1}")
        if choosing1 == 'batting':
            team2_choosen.append('batting')
            team1_choosen.append('field')
            print(f"{Team2} please come forward for batting")
            print(f"{Team1} please come forward for fielding")
        elif choosing1 == 'field':
            team2_choosen.append('field')  
            team1_choosen.append('batting')  
            print(f"{Team2} please come forward for fielding")
            print(f"{Team1} please come forward for batting")

print(f"Team 1 has chosen: {team1_choosen}")
print(f"Team 2 has chosen: {team2_choosen}")


No_Team_players = 5
Members1 = {}
Members2 = {}


for i in range(No_Team_players):
    Member = input(f'Enter name of member no {i+1} for {Team1} Team: ')
    position = input(f'Enter {Member} playing choose between baller, batsman, or allrounder: ')
    Members1.update({Member: position})
print(Members1)

for i in range(No_Team_players):
    Member1 = input(f'Enter name of member no {i+1} for {Team2} Team: ')
    position1 = input(f'Enter {Member} playing choose between baller, batsman, or allrounder: ')
    Members2.update({Member1: position1})
print(Members2)




batsman = []
# Find the batsmen
for player, position in Members1.items():
    if position.lower() == 'batsman':
        batsman.append(player)
    if position.lower() == 'allrounder':
        batsman.append(player)

   

# Ensure at least 2 batsmen are present
if len(batsman) < 2:
    print("Not enough batsmen! Exiting game.")
    exit()

batsman2 = []
# Find the batsmen
for player, position in Members2.items():
    if position.lower() == 'batsman':
        batsman2.append(player)
    if position.lower() == 'allrounder':
        batsman.append(player)

# Ensure at least 2 batsmen are present
if len(batsman2) < 2:
    print("Not enough batsmen! Exiting game.")
    exit()


baller = []
# Find the batsmen
for player, position in Members1.items():
    if position.lower() == 'baller':
        baller.append(player)
    if position.lower() == 'allrounder':
        baller.append(player)


baller2 = []

for player, position in Members2.items():
    if position.lower() == 'baller':
        baller2.append(player)
    if position.lower() == 'allrounder':
        baller2.append(player)


# Function to choose a bowler
def choose_bowler(team_bowler_list):
    print("Available bowlers: ", team_bowler_list)
    bowler_choice = input("Select a bowler for this over: ")
    while bowler_choice not in team_bowler_list:
        print("Invalid bowler choice. Please choose a valid bowler.")
        bowler_choice = input("Select a bowler for this over: ")
    return bowler_choice



striker, non_striker = batsman[0],batsman[1]
striker1, non_striker1 = batsman2[0],batsman2[1]

overs = 2
balls_per_over = 6
score = 0
score1=0

if team1_choosen[0]=='batting':
    batsman_scores={player:0 for player in batsman}
    # batsman_scores2={player:0 for player in batsman2}
    for i in range(overs):
        print(f'Over {i+1} started')
        print(f'{striker}* is now on strike')

        on_over_baller2 = choose_bowler(baller2)
        print(f'{on_over_baller2} is now balling')

        for j in range(balls_per_over):
            print(f'{j+1} ball of the over')

            experience = input(f'Enter the experience for {striker} on this ball: ')

            if experience.lower() == 'out':
                print(f'{striker} is out!')
                # Remove the current striker from the list
                batsman.remove(striker)
                if len(batsman)>=2:
                    # Select the next available batsman as the new striker
                    striker = batsman[0]  # This updates striker to the next batsman in the list
                    print(f'{striker}* is now on strike')
                    non_striker = batsman[1]  # This updates striker to the next batsman in the list
                    print(f'{non_striker} is now on non-strike')
                else:
                    print("No more batsmen left, match ends.")
                    break  # Game ends if no batsmen are left

            elif experience.lower() == 'wide':
                score += 1
                print(f"Wide ball, no change in striker, score: {score}")
            else:
                try:
                    runs = int(experience)
                    if runs == 6:
                        print(f'{striker} hits a SIX!')
                        score += 6
                        batsman_scores[striker]+=runs
                        print(batsman_scores)
                        print(f'{striker}* striker')
            
                    elif runs == 4:
                        print(f'{striker} hit a four!')
                        score += 4
                        batsman_scores[striker]+=runs
                        print(batsman_scores)
                        print(f'{striker}* striker')
            
                    elif runs == 2:
                        print(f'{striker} hit a four!')
                        score += 2
                        batsman_scores[striker]+=runs
                        print(batsman_scores)
                        print(f'{striker}* striker')

                    elif runs == 1 or  runs==3:

                        score += 1
                        batsman_scores[striker]+=runs
                        print(batsman_scores)
                        striker, non_striker = non_striker, striker
                        print(f'{striker}* striker')
        
                    else:
                        score += runs
                        print(f'Score: {score}')
                except ValueError:
                    print("Invalid input, please enter a valid number or 'out'/'wide'.")
        baller2.append(baller2.pop(0))       
        print(f'Final Score for {Team1} is {score}')
 #--------------------------------------------------------------------------------------------------------------------
    if team2_choosen[0]=='field':
            batsman_scores2={player:0 for player in batsman2}
    # batsman_scores2={player:0 for player in batsman2}
            for i in range(overs):
                print(f'Over {i+1} started')
                print(f'{striker1}* is now on strike')


                on_over_baller1 = choose_bowler(baller)
                print(f'{on_over_baller1} is now balling')

                for j in range(balls_per_over):
                    print(f'{j+1} ball of the over')

                    experience = input(f'Enter the experience for {striker1} on this ball: ')

                    if experience.lower() == 'out':
                        print(f'{striker1} is out!')
                        # Remove the current striker from the list
                        batsman2.remove(striker1)
                        if len(batsman2)>=2:
                            # Select the next available batsman as the new striker
                            striker1 = batsman2[0]  # This updates striker to the next batsman in the list
                            print(f'{striker1}* is now on strike')
                            non_striker1 = batsman2[1]  # This updates striker to the next batsman in the list
                            print(f'{non_striker1} is now on non-strike')
                        else:
                            print("No more batsmen left, match ends.")
                            break  # Game ends if no batsmen are left

                    elif experience.lower() == 'wide':
                        score1 += 1
                        print(f"Wide ball, no change in striker, score: {score1}")

                    else:
                        try:
                            runs = int(experience)
                            if runs == 6:
                                print(f'{striker} hits a SIX!')
                                score1 += 6
                                batsman_scores2[striker1]+=runs
                                print(batsman_scores2)
                                print(f'{striker1}* striker')

                    
                            elif runs == 4:
                                print(f'{striker1} hit a four!')
                                score1 += 4
                                batsman_scores2[striker1]+=runs
                                print(batsman_scores2)
                                print(f'{striker1}* striker')
                    
                            elif runs == 2:
                                print(f'{striker1} hit a four!')
                                score1+= 2
                                batsman_scores2[striker1]+=runs
                                print(batsman_scores2)
                                print(f'{striker1}* striker')

                            elif runs == 1 or  runs==3:

                                score1 += 1
                                batsman_scores2[striker1]+=runs
                                print(batsman_scores2)
                                striker1, non_striker1 = non_striker1, striker1
                                print(f'{striker1}* striker')
                
                            else:
                                score1 += runs
                                print(f'Score: {score}')
                        except ValueError:
                            print("Invalid input, please enter a valid number or 'out'/'wide'.")
                baller.append(baller.pop(0))       
                print(f'Final Score for {Team2} is {score1}')

#-------------------------------------------------------------------------------------------------------------
if team1_choosen[0]=='field':
    batsman_scores2={player:0 for player in batsman2}
    # batsman_scores2={player:0 for player in batsman2}
    for i in range(overs):
                
                print(f'Over {i+1} started')
                print(f'{striker1}* is now on strike')


                on_over_baller1 = choose_bowler(baller)
                print(f'{on_over_baller1} is now balling')

                for j in range(balls_per_over):
                    print(f'{j+1} ball of the over')

                    experience = input(f'Enter the experience for {striker1} on this ball: ')

                    if experience.lower() == 'out':
                        print(f'{striker1} is out!')
                        # Remove the current striker from the list
                        batsman2.remove(striker1)
                        if len(batsman2)>=2:
                            # Select the next available batsman as the new striker
                            striker1 = batsman2[0]  # This updates striker to the next batsman in the list
                            print(f'{striker1}* is now on strike')
                            non_striker1 = batsman2[1]  # This updates striker to the next batsman in the list
                            print(f'{non_striker1} is now on non-strike')
                        else:
                            print("No more batsmen left, match ends.")
                            break  # Game ends if no batsmen are left

                    elif experience.lower() == 'wide':
                        score1 += 1
                        print(f"Wide ball, no change in striker, score: {score1}")

                    else:
                        try:
                            runs = int(experience)
                            if runs == 6:
                                print(f'{striker} hits a SIX!')
                                score1 += 6
                                batsman_scores2[striker1]+=runs
                                print(batsman_scores2)
                                print(f'{striker1}* striker')

                    
                            elif runs == 4:
                                print(f'{striker1} hit a four!')
                                score1 += 4
                                batsman_scores2[striker1]+=runs
                                print(batsman_scores2)
                                print(f'{striker1}* striker')
                    
                            elif runs == 2:
                                print(f'{striker1} hit a four!')
                                score1+= 2
                                batsman_scores2[striker1]+=runs
                                print(batsman_scores2)
                                print(f'{striker1}* striker')

                            elif runs == 1 or  runs==3:

                                score1 += 1
                                batsman_scores2[striker1]+=runs
                                print(batsman_scores2)
                                striker1, non_striker1 = non_striker1, striker1
                                print(f'{striker1}* striker')
                
                            else:
                                score1 += runs
                                print(f'Score: {score}')
                        except ValueError:
                            print("Invalid input, please enter a valid number or 'out'/'wide'.")
                baller.append(baller.pop(0))       
                print(f'Final Score for {Team2} is {score1}')

    

    
 #----------------------------------------------------------------------------------------------------------------
    if team2_choosen[0]=='batting':
        batsman_scores={player:0 for player in batsman}
    # batsman_scores2={player:0 for player in batsman2}
        for i in range(overs):
            print(f'Over {i+1} started')
            print(f'{striker}* is now on strike')


            on_over_baller2 = choose_bowler(baller2)
            print(f'{on_over_baller2} is now balling')

            for j in range(balls_per_over):
                print(f'{j+1} ball of the over')

                experience = input(f'Enter the experience for {striker} on this ball: ')

                if experience.lower() == 'out':
                    print(f'{striker} is out!')
                    # Remove the current striker from the list
                    batsman.remove(striker)
                    if len(batsman)>=2:
                        # Select the next available batsman as the new striker
                        striker = batsman[0]  # This updates striker to the next batsman in the list
                        print(f'{striker}* is now on strike')
                        non_striker = batsman[1]  # This updates striker to the next batsman in the list
                        print(f'{non_striker} is now on non-strike')
                    else:
                        print("No more batsmen left, match ends.")
                        break  # Game ends if no batsmen are left

                elif experience.lower() == 'wide':
                    score += 1
                    print(f"Wide ball, no change in striker, score: {score}")

                else:
                    try:
                        runs = int(experience)
                        if runs == 6:
                            print(f'{striker} hits a SIX!')
                            score += 6
                            batsman_scores[striker]+=runs
                            print(batsman_scores)
                            print(f'{striker}* striker')

                
                        elif runs == 4:
                            print(f'{striker} hit a four!')
                            score += 4
                            batsman_scores[striker]+=runs
                            print(batsman_scores)
                            print(f'{striker}* striker')
                
                        elif runs == 2:
                            print(f'{striker} hit a four!')
                            score += 2
                            batsman_scores[striker]+=runs
                            print(batsman_scores)
                            print(f'{striker}* striker')

                        elif runs == 1 or  runs==3:

                            score += 1
                            batsman_scores[striker]+=runs
                            print(batsman_scores)
                            striker, non_striker = non_striker, striker
                            print(f'{striker}* striker')
            
                        else:
                            score += runs
                            print(f'Score: {score}')
                    except ValueError:
                        print("Invalid input, please enter a valid number or 'out'/'wide'.")
            baller2.append(baller2.pop(0))       
            print(f'Final Score for {Team1} is {score}')



if score > score1:
    print(f'Congratulations {Team1} wins with {score} runs!')
elif score1 > score:
    print(f'Congratulations {Team2} wins with {score1} runs!')
else:
    print(f'The match is a draw with both teams scoring {score}!')

