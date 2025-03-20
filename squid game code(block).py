# N = 2  
# T = []  
# team_data = {}

# # Input team data
# for i in range(N):
#     team_name = input("Enter team name: ")
#     T.append(team_name)

# for team in T:
#     team_members = {}  # Dictionary to store each member's energy level for the current team
#     M = 3  # Number of members per team
#     for j in range(M):
#         member_name = input(f"Enter member name for team {team}: ")
#         energy_level = int(input(f"Enter energy level for member {member_name} in team {team}: "))
#         team_members[member_name] = energy_level
#     team_data[team] = team_members

# eliminated_teams = set()
# remaining_players = {}  # To store the remaining players along with their energy

# # Step 1: Process energy reduction and elimination
# for team, members in team_data.items():
#     # Sort members by energy level in descending order, but check the first member
#     sorted_members = dict(sorted(members.items(), key=lambda item: item[1], reverse=True))

#     # Get the first player (with the highest energy), if their energy reaches 0, the team is eliminated
#     first_player = next(iter(sorted_members))
#     energy = sorted_members[first_player] - 1  # Reduce energy of the first player

#     if energy == 0:
#         print(f"{first_player} from team {team} has been eliminated.")  # First player is eliminated
#         eliminated_teams.add(team)  # Mark the entire team as eliminated
#     else:
#         remaining_players[first_player] = energy  # The first player remains with reduced energy

# # Step 2: Print remaining players and eliminated teams
# print("\nRemaining players and their energy levels:")
# for player, energy in remaining_players.items():
#     print(f"{player}: {energy}")

# print("\nTeams whose players were eliminated:")
# for team in eliminated_teams:
#     print(team)

# Number of teams
N = 2  

# Store team names and their members' energy
teams = []  # List of team names
team_data = {}  # Dictionary to store members and their energy levels for each team

# Input team names and members' energy levels
for i in range(N):
    team_name = input("Enter team name: ")
    teams.append(team_name)
    
    members = {}
    for j in range(3):  
        member_name = input(f"Enter member name for team {team_name}: ")
        energy_level = int(input(f"Enter energy level for {member_name} in team {team_name}: "))
        members[member_name] = energy_level
    
    team_data[team_name] = members

# Track eliminated teams
eliminated_teams = set()

# Start the game
rounds = 0  # Counter for rounds

while len(eliminated_teams) < N:
    rounds += 1
    print(f"\nRound {rounds}:")
    
    for team, members in team_data.items():
        if team not in eliminated_teams:
            print(f"Team {team} energy levels:")
            # Reduce energy by 1 for each player in the team
            for player, energy in members.items():
                members[player] = energy - 1
                print(f"{player}: {members[player]}")
            
            # Check if all players in the team are eliminated
            if all(energy <= 0 for energy in members.values()):
                eliminated_teams.add(team)  # Eliminate the team
                print(f"Team {team} is eliminated.")
    
    # Check if only one team remains
    if len(eliminated_teams) == N - 1:
        for team in team_data:
            if team not in eliminated_teams:
                print(f"\nThe winning team is {team}!")
                break

# Game over message
print("\nGame Over!")
