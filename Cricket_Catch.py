print('CRICKET GAME')

import math

Height=float(input("Enter Height of the Player: "))
# D=int(input("Total distace ball tavel from bat to hand"))
Velocity=int(input("At which speed ball is travelling: "))
Angle=int(input("AT which angle ball has been going to the boundary "))



if 5 <=Height<=7:
    if 10 <= Velocity <= 30:
        if 0<=Angle<=89:
            print('The Catch is Successfully taken')

else:
    print('Catch is Not Taken')


g=9.81
distance=(Velocity**2*math.sin(2*Angle))/g
print(distance,"Total distace ball tavel from bat to hand")



Team1 = str(input(f"Enter {1} team name: "))
print(f'Your team 1 is {Team1}')

No_Team_players = 4
Members1 = {}

# Input player names and positions
for i in range(No_Team_players):
    Member = input(f'Enter name of member no {i+1} for {Team1} Team: ')
    position = input(f'Enter {Member} playing choose between baller, batsman, or allrounder: ')
    Members1.update({Member: position})

print(Members1)

batsman = []
# Find the batsmen
for player, position in Members1.items():
    if position.lower() == 'batsman':
        batsman.append(player)

# Ensure at least 2 batsmen are present
if len(batsman) < 2:
    print("Not enough batsmen! Exiting game.")
    exit()

# Select first two batsmen as striker and non-striker
striker, non_striker = batsman[0],batsman[1]

overs = 1
balls_per_over = 6
score = 0

# Simulate the balls and experience
striker_score={}
non_striker_score={}
striker_scores=0
non_striker_scores=0
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
                    print(f'{striker} hit a six!')
                    score += 6
                    if striker:
                        striker_score.update({striker:score})
                        print('striker score',striker_score)
                    elif non_striker:
                         non_striker_score.update({non_striker:score})
                         print('non-striker-svcore',non_score_striker)
                elif runs == 4:
                    print(f'{striker} hit a four!')
                    score += 4
                    if striker:
                        score_striker.update({striker:score})
                        print('striker score',score_striker)
                    elif non_striker:
                         non_score_striker.update({non_striker:score})
                         print('non-striker-svcore',non_score_striker)
                elif runs == 1:
                    striker, non_striker = non_striker, striker
                    score += 1
                    print(f'{non_striker} is now on strike')
                    # if striker:
                    score_striker.update({striker:score})
                    print('striker score',score_striker)
                    # elif non_striker:
                    #      non_score_striker.update({non_striker:score})
                    #      print('non-striker-svcore',non_score_striker)
                else:
                    score += runs
                    print(f'Score: {score}')
            except ValueError:
                print("Invalid input, please enter a valid number or 'out'/'wide'.")

# Final score
print(f'Final Score for {Team1} is {score}')
print('striker score',score_striker)
print(non_score_striker)




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


