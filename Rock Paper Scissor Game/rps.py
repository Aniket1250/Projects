import random

options=['Rock','Paper','Sissor']
computer=random.choice(options)

print('ENTER ANY VALUES TO PLAY THE GAME')
print('1=Rock 2=Paper 3=Sissor')
player=int(input('CHOOSE THE NO ='))

if player==1:
    player='Rock'
elif player==2:
    player='Paper'
elif player==3:
    player='Sissor'
else:
    print('!......You entered wrong no.....!')

print(f'Computer chooses the ={computer}')
print(f'You chooses the ={player}')

if(computer=='Rock' and player=='Paper'):
    print('Player is Win')
elif(computer=='Paper' and player=='Sissor'):
    print('Player is Win')
elif(computer=='Sissor' and player=='Rock'):
    print('Player is Win')
else:
    print('You loose....Better luck next time....!')

