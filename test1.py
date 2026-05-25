file=open("test.txt")
content=file.readlines()
for line in content:
	if "User" in line:
		value=line.split(":")
		print(value[1])
	if "Password" in line:
		value=line.split(":")
		print(value[1])
	if "IP" in line:
		value=line.split(":")
		print(value[1])
file.close