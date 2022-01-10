import os 
import threading
import time 

t = time.time()
files = os.listdir()
def thread_render(file):
	print(file)
	os.system(f"manim {file}")

threads = []
for f in files:
	if f[-1] == 'y' and f[-2] == 'p' and f[-3] == '.' and f != "renderAll.py":
		thread = threading.Thread(target=thread_render, args=(f,))
		threads.append(thread)

for thread in threads:
	thread.start()

for thread in threads:
	thread.join()

print(f"Rendered {len(files)} files in {time.time() - t} seconds")