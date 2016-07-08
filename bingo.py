import random
import sys

mat=6
x=1
y=0
pos=0
col_s=0
f=0
d=0
val_c=0
val_r=0
roll_again = 1

flag=[[0 for j in range(mat)] for i in range(mat)]


def check( flag ):
	count=0

	for i in range(mat):
		count=0
		for j in range(mat):
			if(flag[i][j]==1):
				count=count+1
		if(count==mat):
			print ("The row %d is a bingo\n" %i)
			return 1

	for i in range(mat):
		count=0
		for j in range(mat):
			if(flag[j][i]==1):
				count=count+1
		if(count==mat):
			print ("The column %d is a bingo\n" %i)
			return 1

	return 0


print ("Initial - 0,0")



while (roll_again==1):
	print ("ROLLING")
	rnd=(int)(((random.random()*100)%6)+1)
	print ("Dice-%d" %rnd)
	if((pos+rnd)>(mat*mat)):
		x=1
		y=0
		rnd=((pos+rnd)-(mat*mat))
		pos=0
	
	pos=pos+rnd

	x=(pos/mat)+1
	y=pos%mat

	if(y==0):
		d=1
		if(x%2==0):
			y=mat
		else:
			y=1

		x=x-1;
		
	if(x%2==0 and d==0):
		col_s=(mat+1-y)
	else:
		col_s=y

	print ("Current - %d,%d" %(x-1,col_s-1))

	flag[x-1][col_s-1]=1

	f=check(flag)
	if(f==1):
		var=input("exit?")
		quit()
	d=0
	roll_again = input("roll again ? :")

print ("Final pos - %d,%d"  %(x-1,col_s-1))
	
