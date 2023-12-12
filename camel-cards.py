
def getCardsCount(hand):
    card_counts = {}
    for card in hand:
        card_counts[card] = card_counts.get(card, 0) + 1

    return card_counts

def getHandType(hand,card_counts):
# Determine the type of hand
     
    card_order = "AKQJT98765432 "
    
    #get the positions of each card in Hand
    pos1 = card_order[::-1].index(hand[0])
    pos2 = card_order[::-1].index(hand[1])
    pos3 = card_order[::-1].index(hand[2])
    pos4 = card_order[::-1].index(hand[3])
    pos5 = card_order[::-1].index(hand[4])


    if pos1 < 10:
        pos1 = "0" + str(pos1)

    if pos2 < 10:
        pos2 = "0" + str(pos2)

    if pos3 < 10:
        pos3 = "0" + str(pos3)

    if pos4 < 10:
        pos4 = "0" + str(pos4)

    if pos5 < 10:
        pos5 = "0" + str(pos5)    

    
    #print(hand,pos1,pos2,pos3,pos4,pos5)
    
    

    # Five, return strength = highest - 9 let say, and keep decresing
    if 5 in card_counts.values():
        return ("Five of a kind", 9, pos1,pos2,pos3,pos4,pos5)
    
    #4, return strength = 8 let say, and keep decresing
    elif 4 in card_counts.values():
        return ("Four of a kind", 8, pos1,pos2,pos3,pos4,pos5)
    
    # Full House - return strength = 7 let say, and keep decresing
    elif 3 in card_counts.values() and 2 in card_counts.values():
        return ("Full house", 7, pos1,pos2,pos3,pos4,pos5)
    
    # 3 of a kind - return strength = 6 let say, and keep decresing
    elif 3 in card_counts.values() and 1 in card_counts.values():
        return ("Three of a kind", 6, pos1,pos2,pos3,pos4,pos5)
    
    
    #2 pair return strength = 5 let say, and keep decresing
    
    elif list(card_counts.values()).count(2) == 2:
        return ("Two pair", 5, pos1,pos2,pos3,pos4,pos5)
    
    # one pair - return strength = 4 let say, and keep decresing
    elif list(card_counts.values()).count(2) == 1:
        return ("One pair", 4, pos1,pos2,pos3,pos4,pos5)
    
    # return weakest strength = 3 
    else:
        #print(hand,pos1,pos2,pos3,pos4,pos5)
        return ("High card", 3, pos1,pos2,pos3,pos4,pos5)
    
    print("\n")


data = open("/Users/sachin/camel-input", 'r')
no_of_hands = [line.split() for line in data]

handsWithStrength = []
for i in range(0,len(no_of_hands)-1):
    
    hands = no_of_hands[i][0]
    bid = no_of_hands[i][1]

    #get stregth of hand and cards together as returnOut
    handType, *returnOut = getHandType(no_of_hands[i][0],getCardsCount(hands))

    s1 = [str(i) for i in list(returnOut)]
    
    #adding the strength together 
    HandPower = int("".join(s1))

    handsWithStrength.append((hands,int(bid),HandPower))

#sorting data on Hand1Power
sorted_data = sorted(handsWithStrength, key=lambda x: x[2])

sortedHands = [(hand, value, rank) for rank, (hand, value, _) in enumerate(sorted_data, start=1)]

totalWinning = 0
for hand in sortedHands:
    totalWinning = totalWinning + hand[1]*hand[2]

print(totalWinning)
