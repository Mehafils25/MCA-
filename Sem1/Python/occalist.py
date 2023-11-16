names=raw_input("enter a list of first names:")
count = 0
for name in names:
	if 'z' in name:
		count+=1
print(count)
