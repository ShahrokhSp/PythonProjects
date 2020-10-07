#A Black Jack Game v2
import random
cards = {2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,'J':10,'Q':10,'K':10,'Ace':11}
Dealer_card = []
Player_card = []
#############Chosing two Cards#################
def Chosing_card():
    c = random.sample(set(cards.keys()),1)
    return c[0]
        
#################Displaying the Cards#####################
def Display(a):
    sp = 'Player: '
    for i in range(len(Player_card)):
        sp += (str(Player_card[i]) +' ')
    print(sp)
    sd = 'Dealer: '
    if a == 1:
        for i in range(len(Dealer_card)):
            sd += (str(Dealer_card[i]) + ' ')
        print(sd)
    else:
        sd += '? '
        for i in range(1,len(Dealer_card)):
            sd += (str(Dealer_card[i]) + ' ')
        print(sd)
####################Sum up###########################
def Sum_Player():
    s=0
    flag = 0
    for i in Player_card:
        if cards[i] == 11:
            flag = 1
            continue
        else:
            s += cards[i]
    if flag == 0:
        return s
    elif s + 11 >21:
        s += 1
        return s
    elif s + 11 <21:
        s += 11
        return s
def Sum_Dealer():
    s=0
    flag = 0
    for i in Dealer_card:
        if cards[i] == 11:
            flag = 1
            continue
        else:
            s += cards[i]
    if flag == 0:
        return s
    elif s + 11 >21:
        s += 1
        return s
    elif s + 11 <21:
        s += 11
        return s
####################Players Actions####################
def Hit():
    Player_card.append(Chosing_card())
    Dealer_card.append(Chosing_card())
    Display(0)
def Stay():
    Winner()
#################Restart of the Game##############
def Restart():
    Dealer_card.clear()
    Player_card.clear()
    Game()
    
#################Start of the Game#####################
def Game():
    while len(Dealer_card) != 2:
        Dealer_card.append(Chosing_card())
    while len(Player_card) != 2:
        Player_card.append(Chosing_card())
    Display(0)
    ###########Checking for Black Jack###############
    if Sum_Player() == 21:
            Diplay(0)
            print('Black Jack')
            if Sum_Dealer() == 21:
                print('Unfortunately it\'s a draw')
                Display(1)
                Restart()
            else:
                print('You have won')
                Display(0)
                Restart()
    while True:
        a = input('Choose Stay or Hit: ')
        if a == 'Stay' or a == 'stay':
            Stay()
        elif a == 'Hit' or a == 'hit':
            Hit()
            Bust()
       
        

##################Winner????###################
    
def Winner():
    Bust()
    if Sum_Player() > Sum_Dealer():
        Display(1)
        print('You have won')
        Restart()
    elif Sum_Player() < Sum_Dealer():
        Display(1)
        print('You have lost')
        Restart()
    elif Sum_Player() == Sum_Dealer():
        Display(1)
        print('It\'s a draw')
        Restart()
#############Bust??????????##############
def Bust():
     if Sum_Player() > 21 or Sum_Dealer() > 21:
        print('You have Lost')
        Display(1)
        Dealer_card.clear()
        Player_card.clear()
        return Restart()
    
##################Let the Magic Begins###############
Game()    


    
    
