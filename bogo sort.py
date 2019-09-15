from random import randint,shuffle

def create_array(size=10,max=50):
	return [randint(0,max) for _ in range(size)]

def is_sorted(a):
	for i in range(1,len(a)):
		if a[i]<a[i-1]: return False
	return True

def bogo_sort(a):
	ct=0
	while not is_sorted(a):
		shuffle(a)
		ct+=1
	return ct,a

a=create_array(10,10)
print ("Unsorted:",a)
ct,s=bogo_sort(a)
print ("Sorted:  ",s)
print("Number of iteration: %d"%ct)