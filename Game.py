def cards():
    import random
    print("******The Legends of Ramayana and Mahabharata******")
    A1 = input('Player 1 Enter your Name : ')
    A2 = input('Player 2 Enter your Name : ')
    Rama = ["Rama",95,80,85,70]
    Ravana = ["Ravana",90,72,90,69]
    Lakshmana = ["Lakshmana",81,62,61,73]
    Jatayu = ["Jatayu",70,52,63,90]
    Hanuman = ["Hanuman",92,78,55,92]
    Vibheeshana = ["Vibheeshana",75,69,81,66]
    Kumbhakarna = ["Kumbhakarna",85,55,41,35]
    Indrajit = ["Indrajit",87,73,78,61]
    Angada = ["Angada",79,76,59,83]
    Vali = ["Vali",83,67,68,52]
    Krishna = ["Krishna",96,91,97,93]
    Arjuna = ["Arjuna",98,74,80,79]
    Karna = ["Karna",91,90,84,78]
    Duryodhana = ["Duryodhana",88,68,83,65]
    Bhishma = ["Bhishma",86,61,82,51]
    Ashwatthama = ["Ashwatthama",74,92,62,63]
    Dronacharya = ["Dronacharya",84,75,67,56]
    Bhima = ["Bhima",94,77,58,64]
    Yudhishthira = ["Yudhishthira",71,70,89,62]
    Abhimanyu = ["Abhimanyu",89,64,70,67]
    cards = [Rama,Ravana,Lakshmana,Jatayu,Hanuman,Vibheeshana,Kumbhakarna,Indrajit,Angada,Vali,Krishna,Arjuna
        ,Karna,Duryodhana,Bhishma,Ashwatthama,Dronacharya,Bhima,Yudhishthira,Abhimanyu]
    random.shuffle(cards)
    P1 = cards[:len(cards)//2]
    P2 = cards[len(cards)//2:]
    P1.insert(0,A1)
    P2.insert(0,A2)
    dice = [1,2,3,4,5,6]
    a = random.sample(dice,k=2)
    input(P1[0] + " Press Enter to Throw Dice")
    print(P1[0] + " You got : ",a[0])
    input(P2[0] + " Press Enter to Throw Dice")
    print(P2[0] + " You got : ",a[1])
    return P1,P2,a

def first():
 P1,P2,a = cards()
 if a[0]>a[1] :
      Player1 = P1
      Player2 = P2
      input(Player1[0] + " press Enter to begin")
 else:
      Player1 = P2
      Player2 = P1
      input(Player1[0] + " press Enter to begin")
 c1 = 0
 c2 = 0
 print(Player1[1][0] + " : 1.Attack - " + str(Player1[1][1]) + " 2.Defense - " + str(Player1[1][2]) + " 3.Intelligence - " + str(Player1[1][3]) + " 4.Agility - "+ str(Player1[1][4]))
 c = input("Select Characteristics between 1 - 4 : ")
 d = int(c)
 print(Player1[1][0] + " Characteristics :" + str(Player1[1][d]))
 m = input(Player1[0] + " Do you want to play the God Spell ? (Y/N) ")
 if m == 'Y' :
     Player1.insert(1,1)
     Player2.insert(1,0)
     o = input("Choose the Opponent's Card Number from 1 to 10 : ")
     N = int(o) + 1
 else:
     Player1.insert(1,0)
     Player2.insert(1,0)
     N = 2
 print(Player2[0] + " , Your card is ")    
 print(Player2[N][0] + " : 1.Attack - " + str(Player2[N][1]) + " 2.Defense - " + str(Player2[N][2]) + " 3.Intelligence - " + str(Player2[N][3]) + " 4.Agility - "+ str(Player2[N][4]))
 print(Player1[2][0] + " VS " + Player2[N][0])
 if Player1[2][d]>Player2[N][d] :
     print(Player1[0] + " Wins this round")
     c1 += 1
     out = [Player1[2],Player2[N]]
     Player1.pop(2)
     Player2.pop(N)
     g = Player1
     h = Player2
     g.insert(2,0)
     h.insert(2,0)
     g.insert(3,c1)
     h.insert(3,c2)
     
 else:
     print(Player2[0] + " Wins this round")
     c2 += 1
     out = [Player1[2],Player2[N]]
     Player2.pop(N)
     Player1.pop(2)
     g = Player2
     h = Player1
     g.insert(2,0)
     h.insert(2,0)
     g.insert(3,c2)
     h.insert(3,c1)
 g.insert(4,1)
 h.insert(4,2)
 return g,h,out

import random
Pl1,Pl2,out = first()
r = Pl1[4]
s = Pl2[4]
while(len(Pl1) != 5):
     if s>r:
          x = Pl1
          y = Pl2
          input(x[0] + " press Enter to Pick Up Next Card")
     else:
         x = Pl2
         y = Pl1
         input(x[0] + " press Enter to Pick Up Next Card")
     if x[2] == 0 :
         p = input(x[0] + " Do you want to play the Resurrect Spell ? (Y/N) ")  
         if p == 'Y' :
             x[2] += 1
             random.shuffle(out)
             q = out[0]
             x.insert(5,q)
         else:
             pass 
     print(x[5][0] + " : 1.Attack - " + str(x[5][1]) + " 2.Defense - " + str(x[5][2]) + " 3.Intelligence - " + str(x[5][3]) + " 4.Agility - "+ str(x[5][4]))
     k = input("Select Characteristics between 1 - 4 : ")
     l = int(k)
     print(x[5][0] + " Characteristics :" + str(x[5][l]))
     if x[1] == 0 :
         m = input(x[0] + " Do you want to play the God Spell ? (Y/N) ")  
         if m == 'Y' :
             e = 0
             x[1] += 1
             o = input("Choose the Opponent's Card Number from 1 to " + str(len(Pl1)-5) + ": ")
             N = int(o) + 4
         else:
             e = 1
             N = 5    
     else:
          N = 5
     if y[2] == 0 and e == 1 :
         p = input(y[0] + " Do you want to play the Resurrect Spell ? (Y/N) ")  
         if p == 'Y' :
             y[2] += 1
             random.shuffle(out)
             q = out[0]
             y.insert(N,q)
         else:
             pass
     print(y[0] + " Your card is ")       
     print(y[N][0] + " : 1.Attack - " + str(y[N][1]) + " 2.Defense - " + str(y[N][2]) + " 3.Intelligence - " + str(y[N][3]) + " 4.Agility - "+ str(y[N][4]))
     print(x[5][0] + " VS " + y[N][0])
     if x[5][l]>y[N][l] :
         print(x[0] + " Wins this round")
         out.insert(len(out)+1,x[5])
         out.insert(len(out)+1,y[N])
         if s>r:
             Pl1.pop(5)
             Pl2.pop(N)
             r = 0
             s = 0
         else:
             Pl2.pop(5)
             Pl1.pop(N)
             r = 0
             s = 0
         x[3] += 1
         r = x[4]
         s = y[4]
     else:
         print(y[0] + " Wins this round")
         out.insert(len(out)+1,x[5])
         out.insert(len(out)+1,y[N])
         if s>r:
             Pl1.pop(5)
             Pl2.pop(N)
             r = 0
             s = 0
         else:
             Pl2.pop(5)
             Pl1.pop(N)
             r = 0
             s = 0
         y[3] += 1
         s = x[4]
         r = y[4]
print("Score : " + Pl1[0] + " : " + str(Pl1[3]))
print("Score : " + Pl2[0] + " : " + str(Pl2[3]))
if Pl1[3] > Pl2[3]:
     print(Pl1[0] + " is the winner")
else :
      print(Pl2[0] + " is the winner")


 

       


