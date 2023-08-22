import random
while True:
 numberofbombs=input("enter a number between 1 and 10 for the number of bombs you'd like to have in game:")
 try:
    int(numberofbombs)
    break
 except:
    pass
bombs=[]
players=2
chosen_number=[]
playerposition=[0,0]
home=list(range(1,51))
for number in range(int(numberofbombs)):
    y=random.randint(1,51)
    bombs.append(y)
print(bombs)

def bombgame_simulator(theplayer):
        while True:
            try: 
                playerposition[theplayer]=int(input(f"player {theplayer} choose a number between 1 and 50 that you think doesn't have bomb:"))
                break
            except:pass

        
        if playerposition[theplayer] not in chosen_number:
                for value in bombs:
                    if playerposition[theplayer]==value:
                        return f"player {theplayer} you chose a bomb.you died!"
                chosen_number.append(playerposition[theplayer])
                return 'good'
        else:
            print('invalid value')
            return bombgame_simulator(theplayer)








        

while True:          
  for player in range( players):
         a=bombgame_simulator(player)
         if a !='good':
            print(a)
            exit()