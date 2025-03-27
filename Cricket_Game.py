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

tos1 = input(f'Enter heads or tails for {Team1} ')
if tos1 == 'heads':
    toss_team1.update({Team1: tos1})
else:
    toss_team1.update({Team1: tos1})

tos2 = input(f'Enter heads or tails for {Team2} ')
if tos2 == 'heads':
    toss_team2.update({Team2: tos2})
else:
    toss_team2.update({Team2: tos2})

# Toss result
r1 = random.choice(['heads', 'tails'])
print(f'Let\'s flip!!! , Congratulations it\'s {r1}')

team1_choosen = []
team2_choosen = []

# Toss outcome for Team 1
for tos in toss_team1.values():
    if tos == r1:
        print(f"{Team1} wins the toss")
        choosing = input(f"Please {Team1} choose between batting and fielding: ")
        print(f"{Team1} has chosen {choosing}")
        if choosing == 'batting':
            team1_choosen.append('batting')
            team2_choosen.append('field')
            print(f"{Team1} please come forward for batting")
            print(f"{Team2} please come forward for fielding")
        elif choosing == 'field':
            team2_choosen.append('field')
            team1_choosen.append('batting')
            print(f"{Team1} please come forward for fielding")
            print(f"{Team2} please come forward for batting")

# Toss outcome for Team 2
for tos1 in toss_team2.values():
    if tos1 == r1:
        print(f"{Team2} wins the toss")
        choosing1 = input(f"Please {Team2} choose between batting and fielding: ")
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

# Number of players per team
No_Team_players = 4
Members1 = {}
Members2 = {}

# Input player names and positions for Team 1
for i in range(No_Team_players):
    Member = input(f'Enter name of member no {i+1} for {Team1} Team: ')
    position = input(f'Enter {Member} playing choose between baller, batsman, or allrounder: ')
    Members1.update({Member: position})

# Input player names and positions for Team 2
for i in range(No_Team_players):
    Member1 = input(f'Enter name of member no {i+1} for {Team2} Team: ')
    position1 = input(f'Enter {Member1} playing choose between baller, batsman, or allrounder: ')
    Members2.update({Member1: position1})

# Identify batsmen for Team 1
batsman = [player for player, position in Members1.items() if position.lower() == 'batsman']
if len(batsman) < 2:
    print("Not enough batsmen in Team 1! Exiting game.")
    exit()

# Identify batsmen for Team 2
batsman2 = [player for player, position in Members2.items() if position.lower() == 'batsman']
if len(batsman2) < 2:
    print("Not enough batsmen in Team 2! Exiting game.")
    exit()

# Identify bowlers for Team 1
baller = [player for player, position in Members1.items() if position.lower() == 'baller']

# Identify bowlers for Team 2
baller2 = [player for player, position in Members2.items() if position.lower() == 'baller']

# Function to choose a bowler
def choose_bowler(team_bowler_list):
    print("Available bowlers: ", team_bowler_list)
    bowler_choice = input("Select a bowler for this over: ")
    while bowler_choice not in team_bowler_list:
        print("Invalid bowler choice. Please choose a valid bowler.")
        bowler_choice = input("Select a bowler for this over: ")
    return bowler_choice

# Setup batting order
striker, non_striker = batsman[0], batsman[1]
striker1, non_striker1 = batsman2[0], batsman2[1]

# Over settings
overs = 2
balls_per_over = 6
score = 0
score1 = 0

# Team 1 batting if they chose to bat
if team1_choosen[0] == 'batting':
    batsman_scores = {player: 0 for player in batsman}
    for i in range(overs):
        print(f'Over {i+1} started')
        print(f'{striker}* is now on strike')

        # Allow Team 2 to choose a bowler
        bowler = choose_bowler(baller2)
        print(f'{bowler} is now bowling')

        for j in range(balls_per_over):
            print(f'{j+1} ball of the over')
            experience = input(f'Enter the experience for {striker} on this ball: ')

            if experience.lower() == 'out':
                print(f'{striker} is out!')
                batsman.remove(striker)
                if len(batsman) >= 2:
                    striker = batsman[0]
                    non_striker = batsman[1]
                    print(f'{striker}* is now on strike')
                    print(f'{non_striker} is now on non-strike')
                else:
                    print("No more batsmen left, match ends.")
                    break

            elif experience.lower() == 'wide':
                score += 1
                print(f"Wide ball, no change in striker, score: {score}")

            else:
                try:
                    runs = int(experience)
                    if runs == 6:
                        print(f'{striker} hits a SIX!')
                        score += 6
                        batsman_scores[striker] += runs
                    elif runs == 4:
                        print(f'{striker} hit a four!')
                        score += 4
                        batsman_scores[striker] += runs
                    elif runs == 2:
                        print(f'{striker} hit a two!')
                        score += 2
                        batsman_scores[striker] += runs
                    elif runs == 1 or runs == 3:
                        score += 1
                        batsman_scores[striker] += runs
                        striker, non_striker = non_striker, striker
                        print(f'{striker}* striker')
                    else:
                        score += runs
                    print(f'Score: {score}')
                except ValueError:
                    print("Invalid input, please enter a valid number or 'out'/'wide'.")

        print(f'End of Over {i+1}, Final Score so far for {Team1}: {score}')

        # After each over, ask the user to select a bowler again for the next over
        if i < overs - 1:
            bowler = choose_bowler(baller2)

# Team 2 batting if they chose to bat
if team2_choosen[0] == 'batting':
    batsman_scores2 = {player: 0 for player in batsman2}
    for i in range(overs):
        print(f'Over {i+1} started')
        print(f'{striker1}* is now on strike')

        # Allow Team 1 to choose a bowler
        bowler = choose_bowler(baller)
        print(f'{bowler} is now bowling')

        for j in range(balls_per_over):
            print(f'{j+1} ball of the over')
            experience = input(f'Enter the experience for {striker1} on this ball: ')

            if experience.lower() == 'out':
                print(f'{striker1} is out!')
                batsman2.remove(striker1)
                if len(batsman2) >= 2:
                    striker1 = batsman2[0]
                    non_striker1 = batsman2[1]
                    print(f'{striker1}* is now on strike')
                    print(f'{non_striker1} is now on non-strike')
                else:
                    print("No more batsmen left, match ends.")
                    break

            elif experience.lower() == 'wide':
                score1 += 1
                print(f"Wide ball, no change in striker, score: {score1}")

            else:
                try:
                    runs = int(experience)
                    if runs == 6:
                        print(f'{striker1} hits a SIX!')
                        score1 += 6
                        batsman_scores2[striker1] += runs
                    elif runs == 4:
                        print(f'{striker1} hit a four!')
                        score1 += 4
                        batsman_scores2[striker1] += runs
                    elif runs == 2:
                        print(f'{striker1} hit a two!')
                        score1 += 2
                        batsman_scores2[striker1] += runs
                    elif runs == 1 or runs == 3:
                        score1 += 1
                        batsman_scores2[striker1] += runs
                        striker1, non_striker1 = non_striker1, striker1
                        print(f'{striker1}* striker')
                    else:
                        score1 += runs
                    print(f'Score: {score1}')
                except ValueError:
                    print("Invalid input, please enter a valid number or 'out'/'wide'.")

        print(f'End of Over {i+1}, Final Score so far for {Team2}: {score1}')

        # After each over, ask the user to select a bowler again for the next over
        if i < overs - 1:
            bowler = choose_bowler(baller)

# Final result
if score > score1:
    print(f'Congratulations {Team1} wins')
elif score1 > score:
    print(f'Congratulations {Team2} wins')
else:
    print('It\'s a draw')
