"""
War is a card game played between two players. Each player gets a variable number of cards of the beginning of the game: that's the player's deck. Cards are placed face down on top of each deck.
 
Step 1 : the fight
At each game round, in unison, each player reveals the top card of their deck – this is a "battle" – and the player with the higher card takes both the cards played and moves them to the bottom of their stack. The cards are ordered by value as follows, from weakest to strongest:
2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K, A.
 
Step 2 : war
If the two cards played are of equal value, then there is a "war". First, both players place the three next cards of their pile face down. Then they go back to step 1 to decide who is going to win the war (several "wars" can be chained). As soon as a player wins a "war", the winner adds all the cards from the "war" to their deck.
 
Special cases:
If a player runs out of cards during a "war" (when giving up the three cards or when doing the battle), then the game ends and both players are placed equally first.
The test cases provided in this puzzle are built in such a way that a game always ends (you do not have to deal with infinite games)
Each card is represented by its value followed by its suit: D, H, C, S. For example: 4H, 8C, AS.

When a player wins a battle, they put back the cards at the bottom of their deck in a precise order. First the cards from the first player, then the one from the second player (for a "war", all the cards from the first player then all the cards from the second player).

For example, if the card distribution is the following:
Player 1 : 10D 9S 8D KH 7D 5H 6S
Player 2 : 10H 7H 5C QC 2C 4H 6D
Then after one game turn, it will be:
Player 1 : 5H 6S 10D 9S 8D KH 7D 10H 7H 5C QC 2C
Player 2 : 4H 6D

Game Input
Input
Line 1: the number N of cards for player one.

N next lines: the cards of player one.

Next line: the number M of cards for player two.

M next lines: the cards of player two.

Output
If players are equally first: PAT
Otherwise, the player number (1 or 2) followed by the number of game rounds separated by a space character. A war or a succession of wars count as one game round.
Constraints
0 < N, M < 1000
"""
p1_cards = []
p2_cards = []
cards_value = {'2': 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, '9': 8, '10': 9, 'J': 10, 'Q': 11, 'K': 12, 'A': 13}
round_num = 0
is_pat = False

# GIVEN CODE:
#------------------------------------------------------------------------------
n = int(input())
for i in range(n):
    cardp_1 = input()
    p1_cards.append(cardp_1[:-1])
m = int(input())
for i in range(m):
    cardp_2 = input()
    p2_cards.append(cardp_2[:-1])
#------------------------------------------------------------------------------

def getBattleCard(cards, played):
    card = cards.pop(0)
    played.append(card)
    return card

while len(p1_cards) > 0 and len(p2_cards) > 0:
    round_num += 1
    p1_played = []
    p2_played = []
    p1_battle = getBattleCard(p1_cards, p1_played)
    p2_battle = getBattleCard(p2_cards, p2_played)
    winner = None

    while winner == None:
        if cards_value[p1_battle] > cards_value[p2_battle] :
            winner = 'P1'
        elif cards_value[p1_battle] < cards_value[p2_battle] :
            winner = 'P2'
        else:
            if len(p1_cards) < 4 or len(p2_cards) < 4:
                is_pat = True
                break
            else:
                p1_played += p1_cards[:3]
                del p1_cards[:3]
                p2_played += p2_cards[:3]
                del p2_cards[:3]
                p1_battle = getBattleCard(p1_cards, p1_played)
                p2_battle = getBattleCard(p2_cards, p2_played)
                if cards_value[p1_battle] > cards_value[p2_battle] :
                    winner = 'P1'
                elif cards_value[p1_battle] < cards_value[p2_battle] :
                    winner = 'P2'
                else:
                    continue

    if winner == 'P1':
        p1_cards += p1_played + p2_played
    elif winner == 'P2':
        p2_cards += p1_played + p2_played
    else:
        break

if is_pat:
    print("PAT")
elif len(p1_cards) > 0:
    print("1 " + str(round_num))
elif len(p2_cards) > 0:
    print("2 " + str(round_num))
