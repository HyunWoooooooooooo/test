# 별 찍기 - 17

n = int(input()) 


for i in range(1,n+1) :
    if i == 1 : 
        print(" " *(n-i) + "*")
    elif i == n:
        print("*"*n+"*"*(n-1))
    else:
        print(" "*(n-i) + "*" + " "*(2*i-3) + "*" )


'''

         *
        * *
       *   *
      *     *
     *       *
    *         *
   *           *
  *             *
 *               *
*******************

'''