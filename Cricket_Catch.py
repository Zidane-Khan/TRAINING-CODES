# print('CRICKET GAME')

# import math

# Height=float(input("Enter Height of the Player: "))
# # D=int(input("Total distace ball tavel from bat to hand"))
# Velocity=int(input("At which speed ball is travelling: "))
# Angle=int(input("AT which angle ball has been going to the boundary "))



# if 5 <=Height<=7:
#     if 10 <= Velocity <= 30:
#         if 0<=Angle<=89:
#             print('The Catch is Successfully taken')

# else:
#     print('Catch is Not Taken')


# g=9.81
# distance=(Velocity**2*math.sin(2*Angle))/g
# print(distance,"Total distace ball tavel from bat to hand")


# valid_velocities = []
# velocity_min=10
# velocity_max=30
# angle_min=0
# angle_max=89

# height_min=5
# height_max=7
# for velocity in range(velocity_min, velocity_max + 1):
#     for angle in range(angle_min, angle_max + 1):
        
#         # Check if distance is within the height range for a successful catch
#         if height_min <= distance <= height_max:
#             valid_velocities.append(velocity)
#             break  

# # Finding the range of valid velocities
# if valid_velocities:
#     valid_velocity_range = (min(valid_velocities), max(valid_velocities))
#     print(f"The range of velocities that result in a successful catch is: {valid_velocity_range[0]} to {valid_velocity_range[1]}")
# else:
#     print("No valid velocities result in a successful catch in the given range.")


import math

# Print game introduction
print('CRICKET GAME')

# Take inputs from the user
Height = float(input("Enter Height of the Player: "))
Velocity = int(input("At which speed ball is travelling: "))
Angle = int(input("At which angle ball has been going to the boundary: "))

# Check if the height, velocity, and angle are within valid ranges
if 5 <= Height <= 7:
    if 15 <= Velocity <= 30:
        if 0 <= Angle <= 89:
            print('The Catch is Successfully taken')
else:
    print('Catch is Not Taken')

# Constants
g = 9.81  # Acceleration due to gravity (m/s^2)

# Calculate the distance based on the user inputs
angle_rad = math.radians(Angle)  # Convert angle to radians
distance = (Velocity ** 2 * math.sin(2 * angle_rad)) / g
print(distance, "Total distance ball travels from bat to hand")

# Variables for valid velocity range
valid_velocities = []
velocity_min = 10
velocity_max = 30
angle_min = 0
angle_max = 89

height_min = 5
height_max = 7

# Iterate through velocities and angles to find valid velocities
for velocity in range(velocity_min, velocity_max + 1):
    for angle in range(angle_min, angle_max + 1):
        # Calculate distance for the current velocity and angle
        angle_rad = math.radians(angle)  # Convert angle to radians
        distance = (velocity ** 2 * math.sin(2 * angle_rad)) / g
        
        # Check if the distance is within the valid height range for a successful catch
        if height_min <= distance <= height_max:
            valid_velocities.append(velocity)
            break  # No need to check other angles for this velocity

# Finding the range of valid velocities
if valid_velocities:
    valid_velocity_range = (min(valid_velocities), max(valid_velocities))
    print(f"The range of velocities that result in a successful catch is: {valid_velocity_range[0]} to {valid_velocity_range[1]}")
else:
    print("No valid velocities result in a successful catch in the given range.")
