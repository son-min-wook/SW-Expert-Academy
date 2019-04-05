case =int(input())
for i in range(case):
    m,a = input().split()
    man1=[0 for i in range(int(m))]
    man2=[0 for i in range(int(m))]
    m1=input()
    for j in range(int(m)):
        man1[j]=m1.split(" ")[j]
    m1 = input()
    for j in range(int(m)):
        man2[j] = m1.split(" ")[j]
    ap=[0 for k in range(int(a))]
    for j in range(int(a)):
        v=input()
        ap[j]=v.split(" ")
    energy=0
    x=1
    y=1
    x1=10
    y1=10
    def check(x,y,x1,y1,energy):
        #print("x", x, "y", y, "x1", x1, "y1", y1)
        p=0
        o=0
        list=[[0 for t in range(2)] for z in range(int(a))]
        list1 = [[0 for t in range(2)] for z in range(int(a))]
        for k in range(int(a)):
            if(abs(int(ap[k][0])-int(x))+abs(int(ap[k][1])-int(y))<=int(ap[k][2])):
                list[p][0]=int(ap[k][3])
                list[p][1]=k
                p+=1
        for l in range(int(a)):
            if(abs(int(ap[l][0])-int(x1))+abs(int(ap[l][1])-int(y1))<=int(ap[l][2])):
                list1[o][0]=int(ap[l][3])
                list1[o][1]=l
                o+=1
        #print("list: ",list)
        #print("list1: ",list1)
        list.sort(reverse=True)
        list1.sort(reverse=True)
        return energy+int(dup(list,list1))
    def dup(list,list1):
        #print("dup 함수: ",list)
        #print("dup 함수: ",list1)
        if(int(list[0][1])==int(list1[0][1])and int(list[0][0]) ==int(list1[0][0]) ):
            if(len(list) ==1 and len(list1)!=1):
                #print("1: ",int(list[0][0])+int(list1[1][0]))
                return int(list[0][0])+int(list1[1][0])
            elif(len(list)!=1 and len(list1)==1):
                #print("2: ", int(list[1][0])+int(list1[0][0]))
                return int(list[1][0])+int(list1[0][0])
            elif(len(list)==1 and len(list1)==1):
                #print("3: ", int(list[0][0]))
                return int(list[0][0])
            else:
                #print("4: ",int(list[0][0])+max(int(list[1][0]),int(list1[1][0])))
                return int(list[0][0])+max(int(list[1][0]),int(list1[1][0]))
        else:
            #print("5: ", int(list[0][0])+int(list1[0][0]))
            return int(list[0][0])+int(list1[0][0])
    energy = check(x,y,x1,y1,energy)
    #print("energy: ", energy)
    for s in range(int(m)):
        if(int(man1[s])==0):
            x=x
        elif (int(man1[s]) == 1):
            y = y - 1
        elif (int(man1[s]) == 2):
            x = x + 1
        elif (int(man1[s]) == 3):
            y = y + 1
        elif (int(man1[s]) == 4):
            x = x - 1
        if(int(man2[s])==0):
            x1=x1
        elif(int(man2[s])==1):
            y1=y1-1
        elif(int(man2[s])==2):
            x1=x1+1
        elif(int(man2[s])==3):
            y1=y1+1
        elif(int(man2[s])==4):
            x1=x1-1
        energy = check(x,y,x1,y1,energy)
        #print("energy: ", energy)
    print("#"+str(i+1)+" "+str(energy))

