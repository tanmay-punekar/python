import numpy as pune
###############################Problem-1########################################
Arr1 = pune.array([0,1,2,3,4,5,6,7,8,9])
Arr = pune.where(Arr1%2==1,-1,Arr1)
pune.set_printoptions(threshold=10)
Arr
###############################Problem-2########################################
Arr2 = pune.arange(10).reshape(2,5)
Arr2
###############################Problem-3########################################
Arr3 = pune.array([1,2,3])
C = pune.append(pune.repeat(Arr3,3),pune.tile(Arr3,3))
C
###############################Problem-4########################################
Arr4 = pune.array([1,2,3,2,3,4,3,4,5,6])
Arr5 = pune.array([7,2,10,2,7,4,9,4,9,8])
D = pune.intersect1d(Arr4,Arr5)
D
###############################Problem-5########################################
Arr51 = pune.array([1,2,3,2,3,4,3,4,5,6])
Arr52 = pune.array([7,2,10,2,7,4,9,4,9,8])
E = pune.where(Arr51==Arr52)
E
###############################Problem-6########################################
Arr6 = pune.random.uniform(5,10,size =(5,3))
Arr6
###############################Problem-7########################################
pune.set_printoptions(threshold=5)
Arr7 = pune.arange(15)
Arr7
###############################Problem-8########################################
pune.random.seed(100)
Arr8 = pune.random.random([3,3])/1e3
pune.set_printoptions(suppress=True,precision=6)
Arr8
###############################Problem-9########################################
Arr9 = pune.arange(9).reshape(3,3)
Arr9[:,[0,1]] = Arr9[:,[1,0]]
Arr9
###############################Problem-10#######################################
Arr10 = pune.arange(9).reshape(3,3)
Arr10[[0,1]] = Arr10[[1,0]]
Arr10