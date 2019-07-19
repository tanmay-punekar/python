def match(S1,S2): 
    
    if len(S1) == 0 and len(S2) == 0: 
         return True
  
    if len(S2) > 1 and S2[0] == '*' and  len(S1) == 0: 
          return False

    
    if (len(S2) > 1 and S2[0] == '.') or (len(S2) != 0
        and len(S1) !=0 and S1[0] == S2[0]): 
          return match(S1[1:],S2[1:])
        
    if len(S2) !=0 and S2[0] == '*':
         return match(S1,S2[1:]) or match(S1[1:],S2)
    
    if len(S2) != 0 and len(S1) !=0 and S1[0] != S2[0]:
         return match(S1,S2[1:])

    return False

def test(S1,S2): 
    if match(S1,S2): 
        print("True")
    else: 
        print("False")

test("aba","*ab")
test("aa","a*")
test("ab",".*")
test("ab",".")
test("aab","c*a*b")
test("aaa","a*")