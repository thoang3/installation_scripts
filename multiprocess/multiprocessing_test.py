from multiprocessing import Pool, Queue, current_process
from time import sleep

NUM_GPUS = 4
PROC_PER_GPU = 2

queue = Queue()


def foo(filename):
	gpu_id = queue.get()
	try:
		# run processsing on GPU with gpu_id
		ident = current_process().ident
		print('{}: starting process on GPU {}'.format(ident, gpu_id))
		# ... process filename
		txt_file = open(filename, 'w')
		for i in range(1000):
			sleep(0.01)
			txt_file.write(str(i) + '\n')
		txt_file.close()
		print('{}: finised'.format(ident))
	finally:
		queue.put(gpu_id)


# initialze the queue with the GPU ids
for gpu_ids in range(NUM_GPUS):
	for _ in range(PROC_PER_GPU):
		queue.put(gpu_ids)

pool = Pool(processes=PROC_PER_GPU * NUM_GPUS)
files = ['file_{}.txt'.format(i) for i in range(40)]

for _ in pool.imap_unordered(foo, files):
	pass
pool.close()
pool.join()