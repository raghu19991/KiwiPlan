import random

def find_duplicate():
    # Generating random array of 1000 unique numbers including 1 duplicate
    a=random.sample(range(1,5000),999)
    rand=random.choice(a)
    a.append(rand)
    random.shuffle(a)
    print(a)
    # method1
    #duplicate=[i for i in a if a.count(i)>1][0]

    # method2
    #b=set(a)
    #duplicate=[x for i in a if not in b][0]

    # method3
    #for i in range(0,len(a)):
    #    if j in range(i+1,len(a)):
    #        if a[i]==a[j]:
    #            duplicate=i
    #            break
                
    # method4 (without any functions)
    
     # Creating dictionary with keys=list values and value=0 for each key
    b=dict.fromkeys(a,0)
    for i in a:
        if b[i]==0: #if value of key==0 then increment the value
            b[i]+=1
        else:
            duplicate=i #since all are unique if value if not 0 means it is the duplicate value
            break
        
    print("\nDuplicate is {}".format(duplicate))

if __name__ == "__main__":
    find_duplicate()
    input("\nPress any key to exit")
