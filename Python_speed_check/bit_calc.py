import time

def bit_plus(max_num):
	#プラス
	sumation=0
	t1 = time.time()
	for i in range(1,max_num):
		sumation = sumation + 1
	print("plus_non_bit:"+str(time.time()-t1))

	#ビット
	sumation=0
	t1 = time.time()
	for i in range(1,max_num):
		sumation = sumation | 1	
	print("plus_bit:"+str(time.time()-t1))


def bit_change(max_num):
	a=12
	b=34

	#ビット
	t1 = time.time()
	temp=0
	for i in range(1,max_num):
		temp = a
		a = b
		b = temp	
	print("change_not_bit:"+str(time.time()-t1))

	#値の交換
	t1 = time.time()
	for i in range(1,max_num):
		a = a ^ b
		b = a ^ b
		a = a ^ b
	print("change_bit:"+str(time.time()-t1))


def bit_mult(max_num):
	#ビットなし
	sumation=1024
	temp=0
	t1 = time.time()
	for i in range(1,max_num):
		temp = sumation * 4
	print("mult_non_bit:"+str(time.time()-t1))

	#ビット
	sumation=0
	t1 = time.time()
	for i in range(1,max_num):
		temp = sumation << 2
	print("mult_bit:"+str(time.time()-t1))

def bit_mod(max_num):
	#ビットなし
	sumation=10246471
	temp=0
	t1 = time.time()
	for i in range(1,max_num):
		if sumation%2==0:
			temp = sumation +1
	print("mod_non_bit:"+str(time.time()-t1))

	#ビット
	sumation=0
	t1 = time.time()
	for i in range(1,max_num):
		if sumation&1==0:
			temp = sumation +1
	print("mod_bit:"+str(time.time()-t1))

