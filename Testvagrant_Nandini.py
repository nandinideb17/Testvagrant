import pandas as pd

ind = []
for i in range (1,11):
    ind.append(i)
  
ipl = {
    'S. NO.' : ind,
    'TEAM' : ['GT', 'LSG', 'RR', 'DC', 'RCB', 'KKR', 'PBKS', 'SRH', 'CSK', 'MI'],
    'POINTS' : [20, 18, 16, 14, 14, 12, 12, 12, 8, 6],
    'LAST 5' : [[1,1,0,0,1], [1,0,0,1,1], [1,0,1,0,0], [1,1,0,1,0], [0,1,1,0,0],
                [0,1,1,0,1], [0,1,0,1,0], [1,0,0,0,0], [0,0,1,0,1], [0,1,0,1,1]]
}
  
df = pd.DataFrame(ipl)
df.set_index('S. NO.', inplace = True)
print (df)

s = a = 0

n = 2
#This is a general solution and will display the teams that have n consecutive losses for any n. Just modify the value of n accordingly in the above statement.

print ("\nThe teams that have",n,"consecutive losses are:")

for i in range(1,len(df)+1):
    
    c = 0
    x = df._get_value(i, 'LAST 5')
    
    for j in range (len(x)-1):
        
        if x[j] == 0 and x[j+1] == 0:
        #For finding consecutive wins, the 0s in the above statement must be changed to 1s.
            
            c+=1
                
    if c==n-1:
            
        print (df._get_value(i, 'TEAM'))
        s = s + df._get_value(i, 'POINTS')
        a += 1
        
print ("\nThe average points of these teams is:",s/a)