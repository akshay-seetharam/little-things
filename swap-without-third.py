while True:
	a = input("a: ")
	b = input("b: ")
	print("Initial")
	print("a:", a)
	print("b:", b)
	
	b += a
	a = b[:b.rindex(a)]
	b = b[b.index(a)+len(a):]
	print("Swapped")
	print("a:", a)
	print("b:", b)
