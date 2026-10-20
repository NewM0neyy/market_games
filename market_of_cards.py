import random
suits=['♥', '♦', '♠', '♣']
ranks={'2':20,'3':30,'4':40,'5':50,'6':60,
       '7':70,'8':80,'9':90,'10':100,'J':110,
       'Q':120,'K':130,'A':140}
def card_value(card):
  rank,suit=card[:-1],card[-1]
  base=ranks[rank]
  return base if suit in ['Hearts','Diamonds'] else -base
deck=[f"{rank}{suit}" for rank in ranks for suit in suits]
random.shuffle(deck)
player_hand=[deck.pop(),deck.pop()]
bot_hand=[deck.pop(),deck.pop()]
center_cards=[deck.pop(),deck.pop(),deck.pop()]
max_spread=50.0
player_pos=0
player_cash=0.0
bot_pos=0
bot_cash=0.0
rev_center=[]
# strating w/the rounds
for r in range(1,4):
  rev_center.append(center_cards[r-1])
  print(f"Round {r}")
  print(f"Center revealed card {rev_center}")
  player_fair=sum(card_value(c) for c in player_hand)+sum(card_value(c) for c in rev_center)
  bot_fair=sum(card_value(c) for c in bot_hand)+ sum(card_value(c) for c in rev_center)
  # u will be the market maker in games 1 and 3 and bot will be the market maker in game 2 
  if r in [1,3]:
    print("You are the market maker")
    print(f"Your hand{player_hand}")
    while True:
      try:
        bid=float(input("Your bid: "))
        ask=float(input("Your ask: "))
        if ask<=bid:
          print("Ask must be greater than bid: ")
          continue
        if(ask-bid)>max_spread:
          print(f"Spread cannot exceed {max_spread}")
          continue
        break
      except ValueError:
        print("Invalid Input")
      if ask<bot_fair:
        print("Bot buys")
        player_pos=-1
        player_cash+=ask
        bot_pos+=1
        bot_cash-=ask
      elif bid>bot_fair:
        print("Bot sells")
        player_pos+=1
        player_cash-=bid
        bot_pos-=1
        bot_cash+=bid
      else:
        print("Bot passes")
  else:
    # for keeping the game random and not very accurate 
    # we are introducing entropy
    noise=random.randint(-15,15)
    bot_quote=bot_fair+noise
    bot_bid=round(bot_quote-20,1)
    bot_ask=round(bot_quote+20,1)
    print(f"Bid :{bot_bid} | Ask:{bot_ask}")
    while True:
      decision=input("Enter your decision: ").strip().upper()
      if decision=='BUY':
        player_pos+=1
        player_cash-=bot_ask
        bot_pos-=1
        bot_cash+=bot_ask
        break
      elif decision=='SELL':
        player_pos-=1
        player_cash+=bot_bid
        bot_pos+=1
        bot_cash-=bot_bid
        break
      elif decision=='PASS':
        break
all_cards=player_hand+bot_hand+center_cards
true_val=sum(card_value(c) for c in all_cards)
player_pnl=player_cash+(player_pos*true_val)
bot_pnl=bot_cash+(bot_pos*true_val)
print(f"Player final pnl  {player_pnl}")
print(f"Bot final pnl  {bot_pnl}")
if player_pnl>bot_pnl:
  print("You Win!")
elif player_pnl<bot_pnl:
  print("You Lost")
else:
  print("Draw")
  
