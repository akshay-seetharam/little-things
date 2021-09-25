elements = ["He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn"]
for i in elements:
	if len(i) == 2:
		sum = ord(i[0]) + ord(i[1])
		print(sum/2)
	else:
		print(ord(i[0]))

