#program to evenly distribute and count remaining apples
N=int(input("How many students are there?"))
K=int(input("How many apples are there?"))
print("Each students will get " +str(K//N)+"apples")
print( ""+str(K%N)+"apples will  remain in the basket")
