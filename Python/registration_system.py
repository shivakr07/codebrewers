n = int(input())
arr =  {}
for i in range(n):
	s = str(input())
	if s in arr:
		arr[s] += 1
	else:
		arr[s] = 0
	if arr[s] == 0:
		print("OK")
	else:
		print(s+str(arr[s]))