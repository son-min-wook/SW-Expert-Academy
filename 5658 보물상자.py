case =int(input())
answer=["0" for y in range(case)]
for i in range(case):
    n,v=input().split(" ")
    size=int(n)//4
    p=input()
    password = list(p)
    #print("first password: ",password)
    com=[["0" for g in range(size)] for h in range(4)]
    output = []
    for l in range(int(n)):
        z = 0
        for j in range(4):
            for u in range(size):
                com[j][u] = password[z]
                z = z + 1
        #print("com: ",com)
        for k in range(4):
            op = ""
            for g in range(size):
                op = op + com[k][g]
            if op in output:
                continue
            else:
                output.append(op)
        password.insert(0,password[int(n)-1])
        del password[int(n)]
       # print("l: ",l)
        #print("change password: ",password)
    output.sort(reverse=True)
    #print("reverse",output)
    result=output[int(v) - 1]
    result=int(result,16)
    answer[i]=result
for i in range(case):
    print("#"+str(i+1)+" "+str(answer[i]))