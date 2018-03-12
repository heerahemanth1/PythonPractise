import time
import threading

exit_flag = 0

class DemoThread(threading.Thread):
	"""
	docstring for DemoThread
	Thread arguments
	class threading.Thread(group=None,
		target=None,
		name=None,
		args=(),
		kwargs={})
	"""
	def __init__(self, threadId, name, delay):
		super(DemoThread, self).__init__()
		self.threadId = threadId
		self.name = name + str(threadId) + ' '
		self.delay = delay

	def print_name(self, threadName, delay, counter):
		print('Starting ' + threading.currentThread().getName())
		i = 0
		while counter:
			if exit_flag:
				thread.exit()
			time.sleep(delay)
			print('%s: %s' % (threadName, time.ctime(time.time())))
			counter -= 1

	def run(self):
		print('<<<Thread', self.name, 'started>>>')
		self.print_name(self.name, self.delay, 5)
		print('<<<Thread', self.name, 'ended>>>')

if __name__ == '__main__':
	t1 = DemoThread(1, 'First', 1)
	t2 = DemoThread(2, 'Second', 2)

	t1.start()
	t2.start()

	t1.join()
	t2.join()
