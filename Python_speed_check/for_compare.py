import time

def loop_check(max_num):
	start = time.time()
	i=0
	sumation=0
	while(i<max_num):
	    sumation += i
	    i+=1
	elapsed_time = time.time() - start
	print ("while_time:{0}".format(elapsed_time) + "[sec]")

	start = time.time()
	i=0
	sumation=0
	for i in range(max_num):
	    sumation+=i
	elapsed_time = time.time() - start
	print ("for_time:{0}".format(elapsed_time) + "[sec]")


def reference_check(max_num):
	temp=[1,2,3,4,5,6,7,8,9,10]

	start = time.time()
	for j in range(max_num): 
	    for i in temp:
	        sumation += i
	elapsed_time = time.time() - start
	print ("for_non_reference_time:{0}".format(elapsed_time) + "[sec]")

	start = time.time()
	for j in range(max_num): 
	    for i in range(10):
	        sumation+=temp[i]
	elapsed_time = time.time() - start
	print ("for_reference_time:{0}".format(elapsed_time) + "[sec]")


def length_check():
	image = [[y,x] for y in range(1000) for x in range(1000) ]
	#1
	start = time.time()
	sumation=0
	for i in range(len(image)): 
	    for j in range(len(image[0])):
	        sumation += i
	elapsed_time = time.time() - start
	print ("for_use_length_time:{0}".format(elapsed_time) + "[sec]")

	#2
	start = time.time()
	sumation=0
	lengthY=len(image)
	lengthX=len(image[0])
	for i in range(lengthY): 
	    for j in range(lengthX):
	        sumation += i
	elapsed_time = time.time() - start
	print ("for_don't_use_length_time:{0}".format(elapsed_time) + "[sec]")

def list_make_check():
	start = time.time()
	list1=[]
	for y in range(1000):
	    for x in range(1000):
	        list1.append([y,x])
	elapsed_time = time.time() - start
	print ("don't_use_naihou_hyouki_time:{0}".format(elapsed_time) + "[sec]")

	start = time.time()
	list1 = [[y,x] for y in range(1000) for x in range(1000) ]
	elapsed_time = time.time() - start
	print ("use_naihou_hyouki_time:{0}".format(elapsed_time) + "[sec]")

def naihou_if_check():
	start = time.time()
	list1=[]
	for y in range(1000):
	    for x in range(1000):
	        if (y+x)%2==0:
	            list1.append([y,x])
	elapsed_time = time.time() - start
	print ("don't_use_naihou_if_hyouki_time:{0}".format(elapsed_time) + "[sec]")

	list1=None

	start = time.time()
	list1 = [[y,x] for y in range(1000) for x in range(1000) if (y+x)%2==0]
	elapsed_time = time.time() - start
	print ("use_if_naihou_hyouki_time:{0}".format(elapsed_time) + "[sec]")
