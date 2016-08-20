from pwn import *
from time import sleep

def remove_last_line_from_string(s):
    return s[:s.rfind('\n')]

r = remote('52.88.137.165', '8000')
# EXPLOIT CODE GOES HERE
for round in range (1, 32):
	print r.recvuntil('-> Round '+str(round), timeout=10)
	bin = r.recvuntil('You got it?', timeout=10)	
	bin = remove_last_line_from_string(bin)
	f = open("bin.a", "w")
	f.write(bin)
	f.close()

	answer = subprocess.Popen("strings bin.a | head -n 17 | tail -1", shell=True, stdout=subprocess.PIPE).stdout.read()
	if '[]A\A]A^A_' in answer:
		print 'weird case'	#sometimes this happens lmao
		answer = subprocess.Popen("strings bin.a | head -n 18 | tail -1", shell=True, stdout=subprocess.PIPE).stdout.read()
	print answer
	r.send(answer)
	sleep(0.5)


		
r.interactive()

