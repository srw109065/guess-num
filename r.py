import random

x = input('決定最低數值: ')
y = input('決定最高數值: ')
x = int(x)
y = int(y)
r = random.randint(x,y)

count = 0

while True:
	number = input('請猜數字: ')
	number = int(number)
	count = count + 1
	if number == r:
		print('猜對囉!')
		print("你猜測" , count , "次")
		break
	elif number < r:
		print("數字太小囉")
		if r - number < 2:
			print("很接近囉")
	elif number > r:

		print("數字太大囉!")
		if number - r < 2:
			print("很接近囉")
	print("你猜測" , count , "次")

	 
		