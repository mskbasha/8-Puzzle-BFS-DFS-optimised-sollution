import copy
import numpy as np
from numba import jit
@jit(nopython=True)
def solve(matrix=np.array([[3,2,1], [4,5,6], [8,7,0]],dtype='uint8')):
    lis=np.ones(10**9,dtype='uint8')
    queue=np.ones((181440,3,3),dtype='uint8')
    queue[0]=matrix
    a=np.array([10**(8-x) for x in range(0,9)])
    target=np.array([[1,2,3],[4,5,6],[7,8,0]],dtype='uint8')
    _=True
    ind=1
    var=0
    while _:
        ni,nj=np.where(matrix==0)
        bi,bj=ni[0],nj[0]
        possible_coordinates = list(filter(lambda x:x[0]<3 and x[0]>=0 and x[1]<3 and x[1]>=0,
                                    [[bi-1,bj],[bi+1,bj],[bi,bj-1],[bi,bj+1]]))
        for m,n in possible_coordinates:
            child=np.copy(matrix)
            child[bi][bj]=child[m][n]
            child[m][n]=0
            s=np.sum(child.reshape(1,9)[0]*a)
            if lis[s]:
                queue[ind]=child
                ind+=1
                lis[s]=False
            if (child == target).all():
                print("target found")
                _=False 
        matrix=queue[var]
        var+=1
solve()