#A Black Jack Game
import random
cards = {2:2,3:3,4:4,5:5,6:6,7:7,8:8,9:9,'J':10,'Q':10,'K':10,'Ace':11}
Dealer_card = []
Player_card = []
def Chosing_card():
    counter = 0
    ran = random.randint(1,13)
    for c in cards:
        counter += 1
        if counter > ran:
            return c
        
######################################
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
    
#################Start of the Game#####################
while len(Dealer_card) != 2:
    Dealer_card.append(Chosing_card())
while len(Player_card) != 2:
    Player_card.append(Chosing_card())
Display(0)
##############Checking for Black Jack###############
if Sum_Player() == 21:
        Diplay(0)
        print('Black Jack')
        if Sum_Dealer() == 21:
            print('Unfortunately it\'s a draw')
            Display(1)
        else:
            print('You have won')
            Display(0)

##################Winner????###################
    
def Winner():
    if Sum_Player() > Sum_Dealer():
        Display(1)
        print('You have won')
    elif Sum_Player() < Sum_Dealer():
        Display(1)
        print('You have lost')
    elif Sum_Player() == Sum_Dealer():
        Display(1)
        print('It\'s a draw')
##################
    


    
    
