import random

m=5
n=4
a=0
x=1
y=0
pos=0
col_s=0
roll_again ="y"

print "Your initial position is 0,0"
while (roll_again=="y" and a==0):
	print "Rolling Dice ....."
	rnd=(int)(((random.random()*100)%6)+1)
	print ("Dice value is %d" %rnd)
	
	if(pos+rnd>m*n):
		print ("Cannot add the dice value \n")
	else:
		pos=pos+rnd
		y=y+rnd
		
		if(y>n):
			y=y%n
			x=x+1
		if(x%2==0):
			col_s=n+1-y
		else:
			col_s=y

	print ("Your current position is %d,%d" %(x-1,col_s-1))
	roll_again = input("Enter yes if you want to roll again :")
	if(pos==m*n):
		a=1;
		print ("final")

print ("Your final position is %d,%d" %(x-1,col_s-1))