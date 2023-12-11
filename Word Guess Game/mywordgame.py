
letter=[['k','o','l','h','p','u','r'],
        ['j', 'a', 'y', 's', 'i', 'n', 'g', 'p', 'u', 'r']
        ]

words=[
    ['hour', 'hulk', 'pork', 'kohl', 'holk', 'lurk', 'pour', 'purl', 'polk', 'roup'],
    ['jay', 'sing', 'jar', 'nag', 'spy', 'rug', 'air', 'sun', 'gin', 'pig', 'grin', 'gain', 'spray', 'rain', 'spraygun']
]

lives=3
score=0
level=0

while level<2:
    print(f'🎯Level {level+1} ........ 😈 Lets start the game 😈...........',end='')
    
    print()
    print('.....Are you ready lets go 🏃‍♂️🏃🏃‍♂️🏃‍♂️....!')

    for i in letter[level]:
        print('\t{}'.format(i),end='')
    print()
    word=''
    oldword=''
    round=0
    match=False

    while round==0 or round<2:

        print(f'Your lives ❤ ={lives}')
        word=input('Guess the word bro:')
        

        if not word.lower() == oldword.lower():

            for i in words[level]:

                if word==i:
                    round+=1
                    score+=5
                    match=True
                    oldword=word
                    break

        if not match:
            print('😢...Wrong Guess...😢')
            lives-=1

        if lives==0:
            print(f'Thanks for playing your score is 🏆={score}')
            break

        word=''
        oldword=''
        match=False
    if lives==0:
        break
    elif level==2:
        print(f'Thanks for playing your score is 🏆={score}')
        break
    else:
        print("do you want to play again=")
        a=input('(y/n)🤨=')

        if a=='y':
            level+=1
        else:
            print(f'Thanks for playing your score is 🏆={score}')
            break
    
       

