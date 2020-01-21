import random
import seaborn as sns
import  matplotlib.pyplot as plt
import csv
import pandas as pd


num_of_deck=1
def cards_deck(num_of_deck=num_of_deck):
    """Returns the full  shuffeled deck """
    std_deck=[ 1,2, 3, 4, 5, 6, 7, 8, 9, 10,10,10,10,
               1,2, 3, 4, 5, 6, 7, 8, 9, 10,10,10,10,
               1,2, 3, 4, 5, 6, 7, 8, 9, 10,10,10,10,
               1,2, 3, 4, 5, 6, 7, 8, 9, 10,10,10,10          
             ]
    
    std_deck =std_deck*num_of_deck
    random.shuffle(std_deck)
    return std_deck

def count(cards_hand):
    """Return the sum of the card in hands with blackjack rule"""
    not_aces=[card for card in cards_hand if card != 1 ]
    aces=[card for card in cards_hand if card == 1]
    total=0
    
    for card in not_aces:
        total+=card
        
    for card in aces:
        if total <= 10:
            total +=11
        else:
            total +=1
    return total


def play_hand(deck):
    """Takes deck or card/card Returns tuple of win/loss/tie,
    player,dealer_hand  (1= player win , 0= tie , -1 = player loose"""

    new_deck=deck
    dealer_hand=[]
    player_hand=[]
        
    player_hand.append(new_deck.pop())
    dealer_hand.append(new_deck.pop())
    player_hand.append(new_deck.pop())
    dealer_hand.append(new_deck.pop()) 
 
    # deal player to 12 or higher
    
    #both dealer and plater has blackjack(21)
    if ((count(dealer_hand) ==21) and (count(player_hand)==21) ):
        return (0,player_hand,dealer_hand)
   
    #dealer has blackjack and player does not 
    elif ((count(dealer_hand) ==21) and (count(player_hand) !=21) ):
        return (-1,player_hand,dealer_hand)
    
    #player has blackjack and dealer does not 
    elif ((count(dealer_hand) !=21) and (count(player_hand) ==21) ):
        return (1,player_hand,dealer_hand)
    
    #neither dealer nor player has blackjack(21) with first 2 cards
    else:
        while count(player_hand) < 16:
            player_hand.append(new_deck.pop())

        #dealer must hit soft 17
    while sum(dealer_hand) < 18:
        exit=False
        
        if sum(dealer_hand)== 17:
            exit= True
            
            for i, card in enumerate(dealer_hand):
                
                if card==11:
                    exit=False
                    dealer_hand[1]=1
                    
        if exit:
            break
            
        dealer_hand.append(new_deck.pop())
        
    #return(p_sum,d_sum,player_hand,dealer_hand)
        
    p_sum=sum(player_hand)
    d_sum=sum(dealer_hand)
    
    # dealer bust
    if d_sum >21:
        return (1,player_hand,dealer_hand);
    #dealer tie
    if d_sum == p_sum:
        return (0,player_hand,dealer_hand);
    #dealer win
    if d_sum > p_sum:
        return (-1,player_hand,dealer_hand)
    #dealer loose
    if d_sum < p_sum:
        return (1,player_hand,dealer_hand)


# create the empty csv filw named status had headed win draw and loss:
header_name=["win","draw","loss"]
with open('status.csv', 'w') as file:
    writer = csv.DictWriter(file, fieldnames=header_name)
    writer.writeheader()

win=0
draw=0
loss=0

win_loss=[]
player_cards=[]
dealer_cards=[]

rounds=100000
num_of_deck= 2
gtype="2dealerhit17"
deck=cards_deck(num_of_deck=num_of_deck)
total_card=len(deck)  

deck=cards_deck(6)
play_hand(deck)

for i in range(rounds):
    if len(deck)> (total_card*20)/100:
        try:  
            wl,ph,dh= play_hand(deck)
            win_loss.append(wl)
            player_cards.append(ph)
            dealer_cards.append(dh)
            
            if wl==1:
                win=win+1
            if wl==0:
                draw=draw+1
            if wl== -1:
                loss=loss+1
                
            with open('status.csv', 'a') as file:
                
                writer = csv.DictWriter(file, fieldnames=header_name)
                info = {'win': win,'draw': draw,'loss': loss}                            
                writer.writerow(info)           
            
        except IndexError:
            deck=cards_deck(num_of_deck=num_of_deck)
    else:
        #print("Shuffeling the card")
        deck=cards_deck(num_of_deck=num_of_deck)

#creating dataframe         
df=pd.DataFrame()
df["win_loss"]=win_loss
df["player_cards"]=player_cards
df["dealer_cards"]=dealer_cards
#Saving Dt to Datarame folder
df.to_csv(f"dataframes/{str(num_of_deck)+gtype}",index= False)


