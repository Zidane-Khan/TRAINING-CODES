Team1 = str(input(f"Enter {1} team name: "))
print(f'Your team 1 is {Team1}')
# Team2 = str(input(f"Enter {2} team name: "))
# print(f'Your team 1 is {Team1}')

# print("both team captains pease come to toss")
# Heads=0
# Tails=1
# team1_toss_select={}
# team2_toss_select={}
# toss=input(f'enter heads or tails for {Team1} ')
# toss2=input(f'enter heads or tails for {Team2} ')
# for i in toss:
#     if i=='Heads':
#         team1_toss_select.update({Team1:'Heads'})

#     else:
#         team1_toss_select.update({Team1:'Tails'})

No_Team_players = 4
Members1 = {}
Members2 = {}

# Input player names and positions
for i in range(No_Team_players):
    Member = input(f'Enter name of member no {i+1} for {Team1} Team: ')
    position = input(f'Enter {Member} playing choose between baller, batsman, or allrounder: ')
    Members1.update({Member: position})
print(Members1)

# for i in range(No_Team_players):
#     Member = input(f'Enter name of member no {i+1} for {Team1} Team: ')
#     position = input(f'Enter {Member} playing choose between baller, batsman, or allrounder: ')
#     Members2.update({Member: position})
# print(Members2)

batsman = []
# Find the batsmen
for player, position in Members1.items():
    if position.lower() == 'batsman':
        batsman.append(player)

# Ensure at least 2 batsmen are present
if len(batsman) < 2:
    print("Not enough batsmen! Exiting game.")
    exit()

# batsman2 = []
# # Find the batsmen
# for player, position in Members2.items():
#     if position.lower() == 'batsman':
#         batsman2.append(player)

# # Ensure at least 2 batsmen are present
# if len(batsman2) < 2:
#     print("Not enough batsmen! Exiting game.")
#     exit()

# Select first two batsmen as striker and non-striker
striker, non_striker = batsman[0],batsman[1]
# striker, non_striker = batsman2[0],batsman2[1]

overs = 1
balls_per_over = 6
score = 0

# Simulate the balls and experience
# striker_score={}
# non_striker_score={}
# striker_scores=0
# non_striker_scores=0

batsman_scores={player:0 for player in batsman}
# batsman_scores2={player:0 for player in batsman2}

for i in range(overs):
    print(f'Over {i+1} started')

    for j in range(balls_per_over):
        print(f'{j+1} ball')
        experience = input(f'Enter the experience for {striker} on this ball: ')

        if experience.lower() == 'out':
            print(f'{striker} is out!')
            # Remove the current striker from the list
            batsman.remove(striker)
            if batsman:
                # Select the next available batsman as the new striker
                striker = batsman[0]  # This updates striker to the next batsman in the list
                print(f'{striker} is now on strike')
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

                    # if striker:
                    #     striker_scores+=6
                    #     striker_score.update({striker:striker_scores})
                    #     print(f'{striker} hit a six!')
                    #     print('striker score',striker_score)
                    # else:
                    #      non_striker_scores+=6
                    #      non_striker_score.update({non_striker:non_striker_scores})
                    #      print(f'{non_striker} hit a six!')
                    #      print('non-striker-svcore',non_striker_score)
                elif runs == 4:
                    print(f'{striker} hit a four!')
                    score += 4
                    batsman_scores[striker]+=runs
                    print(batsman_scores)
                    print(f'{striker}* striker')
        
                    # if striker:
                    #     striker_scores+=4
                    #     striker_score.update({striker:striker_scores})
                    #     print(f'{striker} hit a six!')
                    #     print('striker score',striker_score)
                    # else:
                    #      non_striker_scores+=4
                    #      non_striker_score.update({non_striker:non_striker_scores})
                    #      print(f'{non_striker} hit a six!')
            
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

# Final score
# 
print(f'Final Score for {Team1} is {score}')
# print(f'Final Score for {Team2} is {score}')



# LIST = [2, 3, 7, 5]

# # Find the index of the maximum element
# MAX = 0
# for i in range(1, len(LIST)):
#     if LIST[i] > LIST[MAX]:
#         MAX = i
# # Print the maximum element
# print("Maximum:", LIST[MAX])
# # Find the second maximum element using 0 (assuming all elements are positive)
# second_max = 0
# for i in range(len(LIST)):
#     if i != MAX and LIST[i] > second_max:
#         second_max = LIST[i]
# # Print the second maximum element
# print("Second Maximum:", second_max)


