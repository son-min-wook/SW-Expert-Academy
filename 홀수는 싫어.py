a=int(input())
move_x=[0,0,-1,1]
move_y=[1,-1,0,0]
for i in range(a):
    size=int(input())
    field=[[0 for j in range(size)] for k in range(size)]   #홀수인지 짝수인지 받는테이블
    visit = [[0 for j in range(size)] for k in range(size)]  #들리면 1
    visit[0][0]=1              #시작은 1
    depth=[[0 for j in range(size)] for k in range(size)]
    depth[0][0]=1
    value = [[0 for j in range(size)] for k in range(size)]      #누적 표. 몇을 소비해서 가는지
    for j in range(size):
        aa = input()
        for k in range(size):
            aaa=int(aa.split(" ")[k])
            if(aaa%2==1):
                field[j][k] = 1
            else:
                field[j][k] = 0            #인풋 끝

    def compare(xx,yy):
        for k in range(4):
            xxx = xx + move_x[k]
            yyy = yy + move_y[k]
            if xxx >= 0 and yyy >= 0 and xxx < size and yyy < size:
                if visit[xxx][yyy] == 0 or value[xxx][yyy] > value[xx][yy] + field[xxx][yyy]:
                    if(value[xxx][yyy] > value[xx][yy] + field[xxx][yyy]):
                        value[xxx][yyy] = value[xx][yy] + field[xxx][yyy]
                        depth[xxx][yyy] = depth[xx][yy] + 1
                        visit[xxx][yyy] = 1
                        compare(xxx,yyy)
                    else:
                        value[xxx][yyy] = value[xx][yy] + field[xxx][yyy]
                        depth[xxx][yyy] = depth[xx][yy] + 1
                        visit[xxx][yyy] = 1
    for j in range(size):
        xx=0
        yy=j
        while(yy>=0):
            compare(xx,yy)
            xx+=1
            yy-=1
    for j in range(1,size-1):
        xx = j
        yy = size-1
        while (xx <size):
            compare(xx, yy)
            xx += 1
            yy-=1
    print("#%d %d %d" % (i+1, value[size-1][size-1],depth[size-1][size-1]-value[size-1][size-1]))