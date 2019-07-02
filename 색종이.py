a=input()
for i in range(int(a)):
    b=input()
    num=int(b.split(" ")[0])
    color=int(b.split(" ")[1])
    ar=input()
    arr=[]
    for j in range(num):
        arr.append(int(ar.split(" ")[j]))
    #인풋 끝

    #총 몇개의 색이 있는지 확인 다 0 이면 1개의 색으로 분류
    color_count=0
    exist=[]
    zero_count=0
    for j in range(num):
        if(arr[j] != 0 and arr[j] not in exist):
            color_count+=1
            exist.append(arr[j])
        if(arr[j]==0):
            zero_count+=1
    if(zero_count==num):
        color_count=1


    #색이 사라졌을경우
    if(color-color_count !=0):
        finding=color-color_count
        lost=[]
        for t in range(1,color+1):
            if(t not in exist):
                lost.append(t)
        zero_combo = 0
        co = arr[0]
        count = 0
        result_list = []
        adding = 0
        maxi=0
        maxcolor=0
        for j in range(num):
            if (arr[j] == 0):
                zero_combo += 1
            if (arr[j] != 0 and co == arr[j]):
                count = count + 1 + zero_combo
                zero_combo = 0
            elif (arr[j] != 0 and arr[j] != co):
                if maxi<count + zero_combo:
                    maxi=count+zero_combo
                    maxcolor=co
                co = arr[j]
                count = 1 + zero_combo
                zero_combo = 0
        if (zero_combo != 0 ):
            count = count + zero_combo
            if maxi < count :
                maxi = count
                maxcolor = arr[j]
        elif (count != 0):
            if maxi < count + zero_combo:
                maxi = count + zero_combo
                maxcolor = arr[j]
        if(maxcolor==0):
            print("#" + str(i + 1) + " " + str(maxi-finding))
        else:
            qwe=0
            for q in range(1,color+1):
                if q==maxcolor-1 or q == maxcolor+1:
                    maxi=maxi-1
            print("#" + str(i + 1) + " " + str(maxi))

    #색이 그대로일 경우
    else:
        zero_combo=0
        co=arr[0]
        count=0
        result_list=[]
        maxi=0
        adding=0
        for j in range(num):
            if(arr[j]==0):
                zero_combo+=1
            if(arr[j]!=0 and co ==arr[j]):
                count=count+1+zero_combo
                zero_combo=0
            elif(arr[j] !=0 and arr[j] !=co):
                maxi=max(maxi,count+zero_combo)
                co=arr[j]
                count=1+zero_combo
                zero_combo=0
        if(zero_combo != 0 or count!=0 ):
            count=count+zero_combo
            maxi=max(maxi,count)
        print("#"+str(i+1)+" "+str(maxi))