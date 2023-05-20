import random
import sys
import time
def mengetik(s):
    for c in s  +'\n':
	sys.stdout.write(c)
	sys.stdout.flush()

	time.sleep(random.random() * 0.3)

mengetik('Jangan Lupa Subscribe channel Van Junas \nSelamat menonton\nterimakasih.')
