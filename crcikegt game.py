# Team1 = str(input(f"Enter {1} team name: "))
# print(f'Your team 1 is {Team1}')

# No_Team_players = 4
# Members1 = {}

# # Input player names and positions
# for i in range(No_Team_players):
#     Member = input(f'Enter name of member no {i+1} for {Team1} Team: ')
#     position = input(f'Enter {Member} playing choose between baller, batsman, or allrounder: ')
#     Members1.update({Member: position})

# print(Members1)

# batsman = []
# # Find the batsmen
# for player, position in Members1.items():
#     if position.lower() == 'batsman':
#         batsman.append(player)

# # Ensure at least 2 batsmen are present
# if len(batsman) < 2:
#     print("Not enough batsmen! Exiting game.")
#     exit()

# # Select first two batsmen as striker and non-striker
# striker, non_striker = batsman[:2]

# overs = 1
# balls_per_over = 6
# score = 0

# # Simulate the balls and experience
# for i in range(overs):
#     print(f'Over {i+1} started')

#     for j in range(balls_per_over):
#         print(f'{j+1} ball')
#         experience = input(f'Enter the experience for {striker} on this ball: ')

#         if experience.lower() == 'out':
#             print(f'{striker} is out!')
#             # Remove the current striker from the list
#             batsman.remove(striker)
#             if batsman:
#                 # Select the next available batsman as the new striker
#                 striker = batsman[0]  # This updates striker to the next batsman in the list
#                 print(f'{striker} is now on strike')
#             else:
#                 print("No more batsmen left, match ends.")
#                 break  # Game ends if no batsmen are left

#         elif experience.lower() == 'wide':
#             score += 1
#             print(f"Wide ball, no change in striker, score: {score}")

#         else:
#             try:
#                 runs = int(experience)
#                 if runs == 6:
#                     print(f'{striker} hit a six!')
#                     score += 6
#                 elif runs == 4:
#                     print(f'{striker} hit a four!')
#                     score += 4
#                 elif runs == 1:
#                     print(f'{non_striker} is now on strike')
#                     score += 1
#                     # Swap striker and non-striker if 1 run is scored
#                     striker, non_striker = non_striker, striker
#                 else:
#                     score += runs
#                     print(f'Score: {score}')
#             except ValueError:
#                 print("Invalid input, please enter a valid number or 'out'/'wide'.")

# # Final score
# print(f'Final Score for {Team1} is {score}')
LIST=[2,3,7,5]
MAX=0
for i in range(1,len(LIST)):
    if LIST[i]>LIST[MAX]:
        MAX=i
print(LIST[MAX])

second_max=0
for i in range(1,len(LIST)):
    if LIST[i]>LIST[MAX] and LIST[i]!=LIST[MAX]:
        second_max=LIST[i]
print(second_max)




LIST = [2, 3, 7, 5]

# Find the index of the maximum element
MAX = 0
for i in range(1, len(LIST)):
    if LIST[i] > LIST[MAX]:
        MAX = i

# Print the maximum element
print("Maximum:", LIST[MAX])

# Find the second maximum element using 0 (assuming all elements are positive)
second_max = 0
for i in range(len(LIST)):
    if i != MAX and LIST[i] > second_max:
        second_max = LIST[i]

# Print the second maximum element
print("Second Maximum:", second_max)


