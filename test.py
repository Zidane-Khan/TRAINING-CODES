import random
print('Entering Team Name.......')
Team1 = str(input(f"Enter {1} team name: "))
print(f'Your team 1 is {Team1}')
Team2 = str(input(f"Enter {2} team name: "))
print(f'Your team 2 is {Team2}')

print('Going into toss......\n')
print('Both teams captain please come for toss\n')

print('please enter which team captain will call the toss first......')
call_toss=input(f"Choose between {Team1} or {Team2} who will call the toss first: ")
while call_toss!=Team1 and call_toss !=Team2:  # Ensure valid role input
        print('Invalid team doesn"t match the previous team you entered')
        call_toss=input(f"Choose between {Team1} or {Team2} who will call the toss first: ")
toss_team1 = {}
toss_team2 = {}

if call_toss==Team1:

    tos1 = input(f'Choose heads or tails for {Team1}: ')
    while tos1!='heads' and tos1 !='tails':  # Ensure valid role input
        print('Invalid input, type properly heads or tails')
        tos1 = input(f'Choose heads or tails for {Team1}: ')
    if tos1 == 'heads':
        toss_team1.update({Team1: tos1})
        toss_team2.update({Team2:'tails'})
    elif tos1 == 'tails':
        toss_team1.update({Team1: tos1})
        toss_team2.update({Team2:'heads'})

    print(f'{Team1} has choosen {list(toss_team1.values())}')
    print(f'{Team2} has choosen {list(toss_team2.values())}')

if call_toss==Team2:

    tos2 = input(f'Choose heads or tails for {Team2}: ')
    while tos2!='heads' and tos2 !='tails':  # Ensure valid role input
      print('Invalid input, type properly heads or tails')
      tos2 = input(f'Choose heads or tails for {Team2}: ')

    if tos2== 'heads':
        toss_team2.update({Team2: tos2})
        toss_team1.update({Team1:'tails'})
    elif tos2 == 'tails':
        toss_team2.update({Team2: tos2})
        toss_team1.update({Team1:'heads'})
    
    print(f'{Team1} has choosen {list(toss_team1.values())}')
    print(f'{Team2} has choosen {list(toss_team2.values())}')



r1 = random.choice(['heads', 'tails'])
print(f'Let’s flip the Coin!!!')
print(f"Congratulations, its {r1}")

team1_choosen = []
team2_choosen = []

# Handling team1's toss choice
for tos in toss_team1.values():
    if tos == r1:
        print(f"{Team1} wins the toss")
        choosing = input(f"Please {Team1}, choose between batting and field: ")
        while choosing!='batting' and choosing !='field':  # Ensure valid role input
           print('Invalid input, type properly batting or field')
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
        while choosing1!='batting' and choosing1 !='field':  # Ensure valid role input
           print('Invalid input, type properly batting or field')
           choosing1 = input(f"Please {Team1}, choose between batting and field: ")
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

print(f"{Team1} has chosen: {team1_choosen}")
print(f" {Team2} has chosen: {team2_choosen}")


No_Team_players = 5
Members1 = {}
Members2 = {}

for i in range(No_Team_players):
    Member = input(f'Enter name of member no {i+1} for {Team1} Team: ')
    position = input(f'Enter {Member} playing choose between baller, batsman, or allrounder: ')
    while position not in ['batsman', 'baller', 'allrounder']:  # Ensure valid role input
        print("Invalid role. Please enter either 'batsman', 'baller', or 'allrounder'.")
        position = input(f'Enter {Member} playing role (choose between batsman, baller, or allrounder): ').lower()
    Members1.update({Member: position})
print(Members1)

for i in range(No_Team_players):
    Member1 = input(f'Enter name of member no {i+1} for {Team2} Team: ')
    position1 = input(f'Enter {Member1} playing choose between baller, batsman, or allrounder: ')
    while position1 not in ['batsman', 'baller', 'allrounder']:  # Ensure valid role input
        print("Invalid role. Please enter either 'batsman', 'baller', or 'allrounder'.")
        position1 = input(f'Enter {Member1} playing role (choose between batsman, baller, or allrounder): ').lower()
    Members2.update({Member1: position1})
print(Members2)


batsman = []
# Find the batsmen
for player, position in Members1.items():
    if position.lower() == 'batsman':
        batsman.append(player)
    elif position.lower() == 'allrounder':
        batsman.append(player)
    elif position.lower() == 'baller':
        batsman.append(player)

# Ensure at least 2 batsmen are present
if len(batsman) < 2:
    print("Not enough batsmen! Exiting game. FRIST one")
    exit()

batsman2 = []
# Find the batsmen
for player1, position1 in Members2.items():
    if position1.lower() == 'batsman':
        batsman2.append(player1)
    elif position1.lower() == 'allrounder':
        batsman2.append(player1)
    elif position1.lower() == 'baller':
        batsman2.append(player1)

# Ensure at least 2 batsmen are present
if len(batsman2) < 2:
    print("Not enough batsmen! Exiting game. SECON ONE")
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

print(f" {batsman} are the batsman of {Team1}")
print(f"{batsman2} are the batsman of {Team2}")


print(f" {baller} are the baller of {Team1}")
print(f" {baller2} are the baller of {Team2}")

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
    baller_wickets={wicket:0 for wicket in baller2}
    # batsman_scores2={player:0 for player in batsman2}

    for i in range(overs):
        print(f'Over {i+1} started')
        print(f'{striker}* is now on strike')

        on_over_baller2 = choose_bowler(baller2)
        print(f'{on_over_baller2} is now balling')

        for j in range(balls_per_over):
            print(f'{j+1} ball of the over')

            experience = input(f'Enter the experience for {striker} on this ball: ')
            while experience.lower() not in ['out', 'wide', '0', '1', '2', '3', '4', '6'] and not experience.isdigit():
                print("Invalid input, please enter a valid number (0, 1, 2, 3, 4, 6), 'out', or 'wide'.")
                experience = input(f'Enter the experience for {striker} on this ball: ')
 

            if experience.lower() == 'out':
                print(f'{striker} is out!')
                # Remove the current striker from the list
                baller_wickets[on_over_baller2]+=1
                print(baller_wickets)
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
                        print(f'{striker} hits a four!')
                        score += 4
                        batsman_scores[striker]+=runs
                        print(batsman_scores)
                        print(f'{striker}* striker')
            
                    elif runs == 2:
                        print('its a double!')
                        score += 2
                        batsman_scores[striker]+=runs
                        print(batsman_scores)
                        print(f'{striker}* striker')

                    elif runs == 3:
                        print('Wow good running between three runs!')
                        score += 3
                        batsman_scores[striker]+=runs
                        print(batsman_scores)
                        print(f'{striker}* striker')

                    elif runs == 1:

                        print('its a Singe!')
                        score += 1
                        batsman_scores[striker]+=runs
                        print(batsman_scores)
                        striker, non_striker = non_striker, striker
                        print(f'{striker}* striker')
                    
                    elif runs == 0:
                        print(f' Its a dot')
                        print(batsman_scores)
                        print(f'{striker}* striker')
        
                    else:
                        score += runs
                        print(f'Score: {score}')
                except ValueError:
                    print("Invalid input, please enter a valid number or 'out'/'wide'.")
        striker, non_striker = non_striker, striker
        baller2.append(baller2.pop(0))  # Rotate the bowler
        print(f'Score of {Team1} from {i+1} over is {score}')
    
    print(f'Scores of batsman from first inning: {batsman_scores}')   
    print(f'Final Score for {Team1} is {score}')
 #--------------------------------------------------------------------------------------------------------------------
    if team2_choosen[0]=='field':
            batsman_scores2={player:0 for player in batsman2}
            baller_wickets2={wicket:0 for wicket in baller}
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
                        baller_wickets[on_over_baller1]+=1
                        print(baller_wickets)
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
                                print(f'{striker1} hits a SIX!')
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
                                print(f'{striker1} its a double!')
                                score1+= 2
                                batsman_scores2[striker1]+=runs
                                print(batsman_scores2)
                                print(f'{striker1}* striker')
                            elif runs == 3:
                                print('Wow good running between three runs!')
                                score += 3
                                batsman_scores[striker]+=runs
                                print(batsman_scores)
                                print(f'{striker}* striker')

                            elif runs == 1:

                                print('its a Singe!')
                                score += 1
                                batsman_scores[striker]+=runs
                                print(batsman_scores)
                                striker, non_striker = non_striker, striker
                                print(f'{striker}* striker')
                            
                            elif runs == 0:
                                print(f' Its a dot')
                                print(batsman_scores)
                                print(f'{striker}* striker')
                            else:
                                score1 += runs
                                print(f'Score: {score}')
                        except ValueError:
                            print("Invalid input, please enter a valid number or 'out'/'wide'.")
            striker, non_striker = non_striker, striker
            baller2.append(baller2.pop(0))  # Rotate the bowler
            print(f'Score of {Team1} from {i+1} over is {score}')
        
    print(f'Scores of batsman from first inning: {batsman_scores}')   
    print(f'Final Score for {Team1} is {score}')


#-------------------------------------------------------------------------------------------------------------
if team1_choosen[0]=='field':
    batsman_scores2={player:0 for player in batsman2}
    baller_wickets2={wicket:0 for wicket in baller}
    
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
                        baller_wickets2[on_over_baller1]+=1
                        # Remove the current striker from the list
                        batsman2.remove(striker1)
                        print(baller_wickets2)
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
                                print(f'{striker1} hits a SIX!')
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
                                print(f'Its a double!')
                                score1+= 2
                                batsman_scores2[striker1]+=runs
                                print(batsman_scores2)
                                print(f'{striker1}* striker')

                            elif runs == 3:
                                print('Wow good running between three runs!')
                                score += 3
                                batsman_scores[striker]+=runs
                                print(batsman_scores)
                                print(f'{striker}* striker')

                            elif runs == 1:

                                print('its a Singe!')
                                score += 1
                                batsman_scores[striker]+=runs
                                print(batsman_scores)
                                striker, non_striker = non_striker, striker
                                print(f'{striker}* striker')
                            
                            elif runs == 0:
                                print(f' Its a dot')
                                print(batsman_scores)
                                print(f'{striker}* striker')
        
                
                            else:
                                score1 += runs
                                print(f'Score: {score}')
                        except ValueError:
                            print("Invalid input, please enter a valid number or 'out'/'wide'.")
                baller.append(baller.pop(0))       
                print(f'Score of {Team2} from {i+1} over is {score}')
                striker, non_striker = non_striker, striker

    print(f'Scores of batsman from first inning: {batsman_scores2}')   
    print(f'Final Score for {Team2} is {score}')



    

    
 #----------------------------------------------------------------------------------------------------------------
    if team2_choosen[0]=='batting':
        batsman_scores={player:0 for player in batsman}
        baller_wickets={wicket:0 for wicket in baller2}
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
                    baller_wickets[on_over_baller2]+=1
                    print(baller_wickets)
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
                                print(f'Its a double!')
                                score1+= 2
                                batsman_scores2[striker1]+=runs
                                print(batsman_scores2)
                                print(f'{striker1}* striker')

                        elif runs == 3:
                                print('Wow good running between three runs!')
                                score += 3
                                batsman_scores[striker]+=runs
                                print(batsman_scores)
                                print(f'{striker}* striker')

                        elif runs == 1:

                                print('its a Singe!')
                                score += 1
                                batsman_scores[striker]+=runs
                                print(batsman_scores)
                                striker, non_striker = non_striker, striker
                                print(f'{striker}* striker')
                            
                        elif runs == 0:
                                print(f' Its a dot')
                                print(batsman_scores)
                                print(f'{striker}* striker')
            
                        else:
                            score += runs
                            print(f'Score: {score}')
                    except ValueError:
                        print("Invalid input, please enter a valid number or 'out'/'wide'.")
                        striker, non_striker = non_striker, striker
         
            baller2.append(baller2.pop(0))       
            print(f'Score of {Team2} from {i+1} over is {score}')

    print(f'Scores of batsman from first inning: {batsman_scores2}')   
    print(f'Final Score for {Team2} is {score}')

if score > score1:
    print(f'Congratulations {Team1} wins with {score} runs!')
elif score1 > score:
    print(f'Congratulations {Team2} wins with {score1} runs!')
else:
    print(f'The match is a draw with both teams scoring {score}!')

if score == score1:
    print("It's a draw! A Super Over will decide the winner.")

    

    if team1_choosen[0]=='field':

        super_batsman_scores={player:0 for player in batsman}   
        super_baller_wickets={wicket:0 for wicket in baller2} 
    # Super Over: Team 1's Super Over
        print(f"\nSuper Over! {Team1} will bat first.")
        

        super_over_score = 0
        super_over_batsman = batsman[:2]  

        super_over_baller1 = baller2[:]  
        super_over_striker, super_over_non_striker = super_over_batsman[0], super_over_batsman[1]
        

        for i in range(1):  
            print(f"\nSuper Over: {Team1} Batting")
            print(f'{super_over_striker}* is now on strike')

            on_over_baller1 = choose_bowler(super_over_baller1)
            print(f'{on_over_baller1} is now balling')

            for j in range(balls_per_over):
                print(f'{j+1} ball of the over')
                experience = input(f'Enter the experience for {super_over_striker} on this ball: ')

                if experience.lower() == 'out':
                    print(f'{super_over_striker} is out!')
                    super_over_batsman.remove(super_over_striker)
                    if len(super_over_batsman) >= 1:
                        super_over_striker = super_over_batsman[0]
                        print(f'{super_over_striker}* is now on strike')
                        super_over_non_striker = super_over_batsman[1] if len(super_over_batsman) > 1 else None
                    else:
                        print("No more batsmen left, super over ends.")
                        break  
                elif experience.lower() == 'wide':
                    super_over_score += 1
                    print(f"Wide ball, no change in striker, super over score: {super_over_score}")
                else:
                    try:
                        runs = int(experience)
                        if runs == 6:
                            print(f'{super_over_striker} hits a SIX!')
                            super_over_score += 6
                            super_batsman_scores[super_over_striker]+=runs
                            print(super_over_batsman)
                            print(f'{super_over_striker}* striker')

                
                        elif runs == 4:
                            print(f'{super_over_striker} hit a four!')
                            super_over_score += 4
                            super_batsman_scores[super_over_striker]+=runs
                            print(super_over_batsman)
                            print(f'{super_over_striker}* striker')
                
                        elif runs == 2:
                            print(f'{super_over_striker} hit a four!')
                            super_over_score += 2
                            super_batsman_scores[super_over_striker]+=runs
                            print(super_over_batsman)
                            print(f'{super_over_striker}* striker')

                        elif runs == 1 or  runs==3:

                            super_over_score += 1
                            super_batsman_scores[super_over_striker]+=runs
                            print(super_over_batsman)
                            super_over_striker, super_over_non_striker = super_over_non_striker, super_over_striker
                            print(f'{super_over_striker}* striker')
            
                        else:
                            super_over_score += runs
                            print(f'Score: {super_over_score}')
                    except ValueError:
                        print("Invalid input, please enter a valid number or 'out'/'wide'.")
        print(f"\n{Team1}'s Super Over score: {super_over_score}")

    
        print(f"\nSuper Over! {Team2} will bat next.")

        super_batsman_scores2={player:0 for player in batsman2}
        super_over_score2 = 0
        super_over_batsman2 = batsman2[:2]  
        super_over_baller2 = baller[:]  
        super_over_striker2, super_over_non_striker2 = super_over_batsman2[0], super_over_batsman2[1]
        

        for i in range(1): 
            print(f"\nSuper Over: {Team2} Batting")
            print(f'{super_over_striker2}* is now on strike')

            on_over_baller2 = choose_bowler(super_over_baller2)
            print(f'{on_over_baller2} is now balling')

            for j in range(balls_per_over):
                print(f'{j+1} ball of the over')
                experience = input(f'Enter the experience for {super_over_striker2} on this ball: ')

                if experience.lower() == 'out':
                    print(f'{super_over_striker2} is out!')
                    super_over_batsman2.remove(super_over_striker2)
                    if len(super_over_batsman2) >= 1:
                        super_over_striker2 = super_over_batsman2[0]
                        print(f'{super_over_striker2}* is now on strike')
                        super_over_non_striker2 = super_over_batsman2[1] if len(super_over_batsman2) > 1 else None
                    else:
                        print("No more batsmen left, super over ends.")
                        break  

                elif experience.lower() == 'wide':
                    super_over_score += 1
                    print(f"Wide ball, no change in striker, super over score: {super_over_score2}")
                else:
                    try:
                        runs = int(experience)
                        if runs == 6:
                            print(f'{super_over_striker2} hits a SIX!')
                            score += 6
                            super_batsman_scores2[super_over_striker2]+=runs
                            print(super_over_batsman2)
                            print(f'{super_over_striker2}* striker')

                
                        elif runs == 4:
                            print(f'{super_over_striker2} hit a four!')
                            score += 4
                            super_batsman_scores2[super_over_striker2]+=run
                            print(super_over_batsman2)
                            print(f'{super_over_striker2}* striker')
                
                        elif runs == 2:
                            print(f'{super_over_striker2} hit a four!')
                            score += 2
                            super_batsman_scores2[super_over_striker2]+=runs
                            print(super_over_batsman2)
                            print(f'{super_over_striker2}* striker')

                        elif runs == 1 or  runs==3:

                            score += 1
                            super_batsman_scores2[super_over_striker2]+=runs
                            print(super_over_batsman2)
                            super_over_striker2, super_over_non_striker2 = super_over_non_striker2, super_over_striker2
                            print(f'{super_over_striker2}* striker')
            
                        else:
                            super_over_score += runs
                            print(f'Score: {super_over_score2}')
                    except ValueError:
                        print("Invalid input, please enter a valid number or 'out'/'wide'.")

        # Final decision on the winner after super over
        if super_over_score > super_over_score2:
            print(f'\nCongratulations {Team1} wins the Super Over with {super_over_score} runs!')
        elif super_over_score2 > super_over_score:
            print(f'\nCongratulations {Team2} wins the Super Over with {super_over_score2} runs!')
        else:
            print(f'\nThe Super Over ends in a draw! Both teams scored {super_over_score}!')
    
    if team2_choosen[0]=='field':

        print(f"\nSuper Over! {Team2} will bat next.")

        super_batsman_scores2={player:0 for player in batsman2}
        super_over_score2 = 0
        super_over_batsman2 = batsman2[:2]  
        super_over_baller2 = baller[:]  
        super_over_striker2, super_over_non_striker2 = super_over_batsman2[0], super_over_batsman2[1]
        

        for i in range(1): 
            print(f"\nSuper Over: {Team2} Batting")
            print(f'{super_over_striker2}* is now on strike')

            on_over_baller2 = choose_bowler(super_over_baller2)
            print(f'{on_over_baller2} is now balling')

            for j in range(balls_per_over):
                print(f'{j+1} ball of the over')
                experience = input(f'Enter the experience for {super_over_striker2} on this ball: ')

                if experience.lower() == 'out':
                    print(f'{super_over_striker2} is out!')
                    super_over_batsman2.remove(super_over_striker2)
                    if len(super_over_batsman2) >= 1:
                        super_over_striker2 = super_over_batsman2[0]
                        print(f'{super_over_striker2}* is now on strike')
                        super_over_non_striker2 = super_over_batsman2[1] if len(super_over_batsman2) > 1 else None
                    else:
                        print("No more batsmen left, super over ends.")
                        break  

                elif experience.lower() == 'wide':
                    super_over_score += 1
                    print(f"Wide ball, no change in striker, super over score: {super_over_score2}")
                else:
                    try:
                        runs = int(experience)
                        if runs == 6:
                            print(f'{super_over_striker2} hits a SIX!')
                            score += 6
                            super_batsman_scores2[super_over_striker2]+=runs
                            print(super_over_batsman2)
                            print(f'{super_over_striker2}* striker')

                
                        elif runs == 4:
                            print(f'{super_over_striker2} hit a four!')
                            score += 4
                            super_batsman_scores2[super_over_striker2]+=run
                            print(super_over_batsman2)
                            print(f'{super_over_striker2}* striker')
                
                        elif runs == 2:
                            print(f'{super_over_striker2} hit a four!')
                            score += 2
                            super_batsman_scores2[super_over_striker2]+=runs
                            print(super_over_batsman2)
                            print(f'{super_over_striker2}* striker')

                        elif runs == 1 or  runs==3:

                            score += 1
                            super_batsman_scores2[super_over_striker2]+=runs
                            print(super_over_batsman2)
                            super_over_striker2, super_over_non_striker2 = super_over_non_striker2, super_over_striker2
                            print(f'{super_over_striker2}* striker')
            
                        else:
                            super_over_score += runs
                            print(f'Score: {super_over_score2}')
                    except ValueError:
                        print("Invalid input, please enter a valid number or 'out'/'wide'.")

        super_batsman_scores={player:0 for player in batsman}    
    # Super Over: Team 1's Super Over
        print(f"\nSuper Over! {Team1} will bat first.")
        

        super_over_score = 0
        super_over_batsman = batsman[:2]  

        super_over_baller1 = baller2[:]  
        super_over_striker, super_over_non_striker = super_over_batsman[0], super_over_batsman[1]
        

        for i in range(1):  
            print(f"\nSuper Over: {Team1} Batting")
            print(f'{super_over_striker}* is now on strike')

            on_over_baller1 = choose_bowler(super_over_baller1)
            print(f'{on_over_baller1} is now balling')

            for j in range(balls_per_over):
                print(f'{j+1} ball of the over')
                experience = input(f'Enter the experience for {super_over_striker} on this ball: ')

                if experience.lower() == 'out':
                    print(f'{super_over_striker} is out!')
                    super_over_batsman.remove(super_over_striker)
                    if len(super_over_batsman) >= 1:
                        super_over_striker = super_over_batsman[0]
                        print(f'{super_over_striker}* is now on strike')
                        super_over_non_striker = super_over_batsman[1] if len(super_over_batsman) > 1 else None
                    else:
                        print("No more batsmen left, super over ends.")
                        break  
                elif experience.lower() == 'wide':
                    super_over_score += 1
                    print(f"Wide ball, no change in striker, super over score: {super_over_score}")
                else:
                    try:
                        runs = int(experience)
                        if runs == 6:
                            print(f'{super_over_striker} hits a SIX!')
                            super_over_score += 6
                            super_batsman_scores[super_over_striker]+=runs
                            print(super_over_batsman)
                            print(f'{super_over_striker}* striker')

                
                        elif runs == 4:
                            print(f'{super_over_striker} hit a four!')
                            super_over_score += 4
                            super_batsman_scores[super_over_striker]+=runs
                            print(super_over_batsman)
                            print(f'{super_over_striker}* striker')
                
                        elif runs == 2:
                            print(f'{super_over_striker} hit a four!')
                            super_over_score += 2
                            super_batsman_scores[super_over_striker]+=runs
                            print(super_over_batsman)
                            print(f'{super_over_striker}* striker')

                        elif runs == 1 or  runs==3:

                            super_over_score += 1
                            super_batsman_scores[super_over_striker]+=runs
                            print(super_over_batsman)
                            super_over_striker, super_over_non_striker = super_over_non_striker, super_over_striker
                            print(f'{super_over_striker}* striker')
            
                        else:
                            super_over_score += runs
                            print(f'Score: {super_over_score}')
                    except ValueError:
                        print("Invalid input, please enter a valid number or 'out'/'wide'.")
        print(f"\n{Team1}'s Super Over score: {super_over_score}")

    # Final decision on the winner after super over
        if super_over_score > super_over_score2:
            print(f'\nCongratulations {Team1} wins the Super Over with {super_over_score} runs!')
        elif super_over_score2 > super_over_score:
            print(f'\nCongratulations {Team2} wins the Super Over with {super_over_score2} runs!')
        else:
            print(f'\nThe Super Over ends in a draw! Both teams scored {super_over_score}!')

    
   