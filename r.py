import random
r = random.randint(1,100)

while True:
	number = input('請猜數字: ')
	number = int(number)

	if number == r:
		print('猜對囉!')
		break
	elif number < r:
		print("數字太小囉", r)
		if r - number < 5:
			print("很接近囉")
	elif number > r:
		print("數字太大囉!", r)
		if number - r < 5:
			print("很接近囉")

	 
		