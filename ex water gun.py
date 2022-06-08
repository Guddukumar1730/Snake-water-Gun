import random
ps=0
cs=0
ds=0
n=1



while(n<=10):
    print("press s,w or g")
    f = input()




    l = ["Snake", "Water", "Gun"]
    a=random.choice(l)
    print(a)


    if f=="s" and a=="Snake":
        print("WELL PLAYED!DRAW")
        ds+=1
    elif f=="w" and a=="Water":
        print("WELL PLAYED!DRAW")
        ds+=1
    elif f=="g" and a=="Gun":
        print("WELL PLAYED!DRAW")
        ds+=1
    elif f=="s" and a=="Water":
        print("YOU WON")
        ps+=1
    elif f=="w" and a=="Gun":
        print("YOU WON!")
        ps += 1
    elif f == "g" and a == "Snake":
        print('YOU WON!')
        ps += 1
    elif f=="s" and a=="Gun":
        print("YOU LOSS!")
        cs+=1
    elif f=="w" and a=="Snake":
        print("YOU LOSS!")
        cs+=1

    elif f=="g" and a=="Water":
        print("YOU LOSS!")
        cs+=1

    n=n+1
if ps>cs:
    print('CONGRATS!!! YOU WIN THE MATCH')
elif cs>ps:
    print('OOPS!!! YOU LOST THE MATCH\n','BETTER LUCK NEXT TIME')
print('your total score: ' ,ps)
print('python total score: ',cs)
print('total no. of matches draw: ', ds)



