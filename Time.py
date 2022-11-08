import time

initial =time.time()
x=1
while (x<10):
    print("Hello im santosh")
    time.sleep(0.000000000000002)
    x+=1
print("\n")
print("While loop ran in ",time.time()-initial,"seconds")
print("\n")
     #break
initial2=time.time()
for i in range(10):
        print("Hello im santosh")
        x+=1
        print("For loop ran in ",time.time()-initial2,"seconds")
     #   break


Localtime =time.asctime(time.localtime(time.time()))
print("\nYour local time is ",Localtime)
