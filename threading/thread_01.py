import time
def countdown(n):
	while n > 0:
		print('T-minus', n)
		n -= 1
		time.sleep(5)

from threading import Thread
'''
t = Thread(target=countdown, args=(10,))

t.start()

# create thread object not work, must apply start() functions.

if t.is_alive():
	print('Still runing!')
else:
	print('Wirk overing!')
'''

class CountdownTask:
	def __init__(self):
		self._running = True

	def terminate(self):
		self._running = False

	def run(self, n):
		while self._running or n > 0:
			print('Tminus', n)
			n -= 1
			time.sleep(5)

def main_count():
	c = CountdownTask()
	t = Thread(target = c.run, args = (10,))
	t.start()
	c.terminate()
	t.join()
	print('All work done!')

def IOTask:
	def terminate(self):
		self._running = False

	
if __name__ == '__main__':
	#main_count()