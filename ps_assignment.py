def display(x1):
    for i in range(len(x1)):
        print("location",i+1,end="")
        for j in x1[i]:
            print("--->",j+1,end="")
        print()
            
def placedlocations(mapping,n,l,loc):
    placed=[False for i in range(n)]
    placedlocation=[[]for i in range(l)]
    for i in range(n):
        for x in range(l):
                y=mapping[i][x]
                if(loc[ y ]>0):
                    loc[y]=loc[y]-1
                    placed[i]=True
                    placedlocation[y].append(i)
                    break; 
    return placedlocation



n,l=map(int,input().split()) #n-Num of candidates , l-Num of locations
mapping=[]   
for i in range(n):
    l1=list(map(int,input().split()))
    mapping.append(l1)  #matrix contains candidates and their location preferences
    
loc=list(map(int,input().split())) #Num of vacancies in each location 
x1=placedlocations(mapping,n,l,loc)
display(x1)

    