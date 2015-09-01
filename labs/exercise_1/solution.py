def func():
	num=[]
	x = map(int, raw_input("Enter the numbers: ").split(' '))
	for i in x:
		if i % 33 == 0:
			num.append(i)
	return num
print func()