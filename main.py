import random

h_score = 0
c_score = 0
round = 0

for round in range(1, 6):
  c = int(random.randint(0,2))
  h = input("entre your choice \n s for snake \n w for water \n g for gun \n :").lower()
  s = ["D","W","L"]
  w = ["L","D","W"]
  g = ["W","L","D"]
  if h == "s":
    print(s[c])
    if s[c] == "W":
        h_score += 1
    elif s[c] == "L":
        c_score += 1
    else:
        pass
  elif h == "W":
    print(w[c])
    if w[c] == "W":
      h_score += 1
    elif w[c] == "L":
      c_score += 1
    else:
      pass
  elif h == "g":
    print(g[c])
    if g[c] == "W":
      h_score += 1
    elif g[c] == "L":
      c_score += 1
    else:
      pass
    round += 1
  else:
    print("wrong input")
print(f"your score is {h_score} and computer score is {c_score}")
if h_score > c_score:
  print("you win")
elif h_score < c_score:
  print("you lose")
else :
  print("draw")


    
