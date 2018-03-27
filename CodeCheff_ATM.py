input_ = raw_input()
a,b = input_.split(" ")[:2]
a = float(a)
b = float(b)
if a%5 == 0 and b > a + 0.5:
	b = b - a
	b = b - 0.50
print("%.2f" % b)

