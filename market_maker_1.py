import numpy as np
rounds=4
max_spread=3.0
player_pnl=0.0
bot_pnl=0.0
for r in range(1,rounds+1):
  print(f"Round {r}")
  die=np.random.radint(1,7,size=3)
  settlement=int(np.sum(die))
  revealed_die=int(np.random.choice(die))
  print(f"Revealed die: {revealed_die}")
  expected_val=7.0+revealed_die
  player_pos=0
  player_cash=0.0
  if r<=2:
    print("You are the market maker")
    while True:
      try:
        bid=float(input("Enter your BID: "))
        ask=float(input("Enter your ASK: "))
        if ask<=bid:
          print("Ask must be greater than Bid")
          continue
        if round(ask-bid,2)>max_spread:
          print(f"Spread must be less than {max_spread}")
          continue
        break
       except ValueError:
         print("Enter numbers only")
     if ask<fair_value:
       print("Bot buys ")
       player_pos=-1
       player_cash+=ask
     elif bid>fair_value:
       print("Bot sells u")
       player_pos=1
       player_cash-=bid
    else:
      print("Bot passes")
  else:
    print("Bot is the market maker")
    bot_bid=round(fair_value-1.0,1)
    bot_ask=round(fair_value+1.0,1)
    print(f"Bid {bot_bid} | Ask {bot_ask}")
    while True:
      choice=input("Enter your choice:").strip().upper()
      if chocie=="BUY":
        player_pos=1
        player_cash-=bot_ask
        break
      elif choice=='SELL":
         player_pos=-1
         player_cash+=bot_bid
      elif choice=="PASS":
         player_pos=0
         player_cash+=0.0
         break
       else:
         print("Inavlid choice")
  round_player_pnl=player_cash+(player_pos*settlement)
    
  
      
    
    
    
      
  
