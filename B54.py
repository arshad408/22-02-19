def main():
	try:
		x=int(input())
		if x%2!=0:
			x-=1
		print(x)
	except:
		print('invalid')
main()
