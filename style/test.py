def f(num):
	if num==1:
		return 1
	if num==3:
		return 3
	if num%2==0:
		return f(num/2.0)
	if num%4==1:
		num2 = (num-1)/4.0
		return 2*f(2*num2+1)-f(num2)
	else:
		num3 = (num-3)/4.0
		return 3*f(2*num3+1)-2*f(num3)

def S(n):
	return sum([f(num) for num in range (1,n+1)])

lst=[1, 5, 31, 265, 2415, 20129, 197671, 1680033, 15679899, 143488409]
lst.append(S(3**11))
print lst