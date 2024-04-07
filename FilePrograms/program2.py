# 3*3 matrix
X=[[12,7,3],[4,5,6],[7,8,9]]
# 3*4 matrix
Y=[[5,8,1,2],[6,7,3,0],[4,5,9,1]]
# resultant matrix is 3*4 
result=[[0,0,0,0],[0,0,0,0],[0,0,0,0]]
for i in range(len(X)):
    for j in range(len(Y)):
        for k in range(len(result)):
            result[i][j]+=X[i][k]*Y[k][j]

for i in range(len(result)):
    print(result[i])