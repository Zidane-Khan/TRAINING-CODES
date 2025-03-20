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

