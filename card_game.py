import numpy as np

  
def game():
  deck=np.repeat(np.arange(1,14),4)
  
  pnl=0.0
  
  for round in range(1,5):
    deck=np.random.permutation(deck)
    print(f"Round {round}")
    round_pnl=0.0
    cards=np.random.choice(deck,size=3)
    sum=np.sum(cards)
    no_of_rev=np.random.randint(0,3)
    if no_of_rev==0:
      ev=21
      print("No cards revealed !")
      err=np.random.uniform(0,5)
      market_bid=sum+err
      market_ask=sum-err
      print(f"Market bid {market_bid}")
      print(f"Market Ask {market_ask}")
      user_action=input("Enter your decision: ").strip().upper()
      if user_action=="BUY":
        round_pnl+=ev-market_ask
      elif user_action=="SELL":
        round_pnl+=market_bid-ev
      elif user_action=="PASS":
        round_pnl+=0.0
    if no_of_rev==1:
      i=np.random.randint(0,3)
      rev_card=cards[i]
      print(f"Value of the revealed card is {rev_card}")
      ev=14+int(rev_card)
      err=np.random.uniform(0,5)
      market_bid=sum+err
      market_ask=sum-err
      print(f"Market bid {market_bid}")
      print(f"Market ask {market_ask}")
      user_action=input("Enter your decision: ").strip().upper()
      if user_action=="BUY":
        round_pnl+=ev-market_ask
      elif user_action=="SELL":
        round_pnl+=market_bid-ev
      elif user_action=="PASS":
        round_pnl+=0.0
        
    if no_of_rev==2:
      i=np.random.randint(0,2)
      rev_c1=cards[i]
      rev_c2=cards[i+1]
      print(f"Value of the revealed cards is {rev_c1} and {rev_c2}")
      ev=7+int(rev_c1)+int(rev_c2)
      err=np.random.uniform(0,5)
      market_bid=sum+err
      market_ask=sum-err
      print(f"Market bid {market_bid}")
      print(f"Market ask {market_ask}")
      user_action=input("Enter your decision: ").strip().upper()
      if user_action=="BUY":
        round_pnl+=ev-market_ask
      elif user_action=="SELL":
        round_pnl+=market_bid-ev
      elif user_action=="PASS":
        round_pnl+=0.0
    pnl+=round_pnl
        
  print(f"Total pnl {pnl}")    
       
if __name__=="__main__":
  game()    
    
    
