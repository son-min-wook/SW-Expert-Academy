case =int(input())
for i in range(case):
    spin=int(input())
    wheel=[[0 for j in range(8)]for k in range(4)]
    for j in range(4):
        whel = input()
        for k in range(8):
            wheel[j][k]=int(whel.split(" ")[k])

    def change0(dir,main):                               #1st
       # print("first gear!!")
       # print("dir: ",dir)
        if(main !=1):
            if (wheel[0][2] != wheel[1][6]):
             #   print("0->1")
                if (int(dir) == 1):
                    change1(-1,0)
                else:
                    change1(1,0)
        if(dir ==1):
            wheel[0].insert(0, wheel[0][7])
            del wheel[0][8]
           # print("1st 시계 ",wheel[0])
        else:
           # print("1st 바꾸기 전: ",wheel[0])
            wheel[0].insert(8, wheel[0][0])
           # print("1st 넣은 후: ", wheel[0])
            del wheel[0][0]
           # print("1st 반대 ",wheel[0])

    def change1(dir,main):
       # print("second gear!!")
       # print("dir: ",dir)
       # print("main: ",main)
        if (int(main) != 2):
            #print(wheel[1])
           # print(wheel[2])
            if (wheel[1][2] != wheel[2][6]):
                #print("1->2")
                if (int(dir) == 1):
                    change2(-1,1)
                else:
                    change2(1,1)
        if(int(main) !=0):
            if (wheel[1][6] != wheel[0][2]):
              #  print("1->0")
                if (int(dir) == 1):
                    change0(-1,1)
                else:
                    change0(1,1)
        if(int(dir) ==1):
            wheel[1].insert(0, wheel[1][7])
            del wheel[1][8]
            #print("2nd 시계 ",wheel[1])
        else:
            #print("2nd 바꾸기 전: ", wheel[1])
            wheel[1].insert(8, wheel[1][0])
           # print("2nd 넣은 후: ", wheel[1])
            del wheel[1][0]
           # print("2nd 반대 ",wheel[1])


    def change2(dir, main):
        #print("third gear!!")
        #print("dir: ", dir)
        if (main !=3):
            if (wheel[2][2] != wheel[3][6]):
                #print("2->3")
                if (int(dir) == 1):
                    change3(-1, 2)
                else:
                    change3(1, 2)
        if(main !=1):
            if (wheel[2][6] != wheel[1][2]):
                #print("2->1")
                if (int(dir) == 1):
                    change1(-1, 2)
                else:
                    change1(1, 2)
        if (dir == 1):
            wheel[2].insert(0, wheel[2][7])
            del wheel[2][8]
            #print("3rd 시계 ", wheel[2])
        else:
            wheel[2].insert(8, wheel[2][0])
            del wheel[2][0]
            #print("3rd 반대 ", wheel[2])


    def change3(dir, main):  # 1st
        #print("last gear!!")
        #print("dir: ", dir)
        if (main !=2):
            #print("first is 4th")
            if (wheel[3][6] != wheel[2][2]):
                #print("3->2")
                if (int(dir) == 1):
                    change2(-1, 3)
                else:
                    change2(1, 3)
        if (dir == 1):
            wheel[3].insert(0, wheel[3][7])
            del wheel[3][8]
            #print("4th 시계 ", wheel[3])
        else:
            wheel[3].insert(8, wheel[3][0])
            del wheel[3][0]
            #print("1st 반대 ", wheel[3])

    #print(wheel)
    for k in range(spin):
        c_wheel,dir=input().split()
        if(int(c_wheel)-1 ==0):
            change0(int(dir),-1)
        if (int(c_wheel)-1 == 1):
            change1(int(dir), -1)
        if (int(c_wheel)-1 == 2):
            change2(int(dir), -1)
        if (int(c_wheel)-1 == 3):
            change3(int(dir), -1)
    result=wheel[0][0]*1+wheel[1][0]*2+wheel[2][0]*4+wheel[3][0]*8
    print("#"+str(i+1)+" "+str(result))

