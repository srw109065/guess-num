import random
r = random.randint(1,100)

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
		if r - number < 5:
			print("很接近囉")
	elif number > r:

		print("數字太大囉!")
		if number - r < 5:
			print("很接近囉")
	print("你猜測" , count , "次")

	 
		