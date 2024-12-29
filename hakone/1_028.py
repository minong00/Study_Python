from sqlalchemy.dialects.postgresql.pg_catalog import format_type

nemo=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]]
sum=0
for i in range(0,5):
    for j in range(0,i+1):
        sum+=nemo[i][j]
print(sum)


for i in range(0,5):
    for j in range(4,i,-1):
        sum+=nemo[i][j]
print(sum)