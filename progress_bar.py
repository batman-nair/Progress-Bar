import sys
from time import sleep 

def progress_bar(val, start=0, end=100, style='percent', fill='=', size=50):
	if(val>end):
		val = end
	elif (val<start):
		val = start

	percent = int(val*100/(end-start))
	
	if(style == 'bar'):
		sys.stdout.write("Progress: [")
		for i in range(size):
			if(i<=percent*size/100):
				sys.stdout.write(fill)
			else:
				sys.stdout.write(" ")
		sys.stdout.write("]")

	#Default style is percent
	else:
		sys.stdout.write("Progress: " + str(percent) + "%")
	
	sys.stdout.write("\r")
	sys.stdout.flush()	

	if(percent>=100):
		sys.stdout.write("\n")
		sys.stdout.flush()

print("Progress bar using all options")
for i in range(21):
	sleep(0.2)
	progress_bar(i, start=0, end=20, style='bar', fill='|', size=20)

print("Simple progress bar")
for i in range(101):
	sleep(0.1)
	progress_bar(i)

print("Process over")