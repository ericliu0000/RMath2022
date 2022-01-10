import os 
import threading
import time 
from constants import *

t = time.time()
files = os.listdir()
def thread_render(file):
	print(file)
	os.system(f"manim {file}")

threads = []
for f in files:
	if f[-3:] == ".py" and f != "renderAll.py" and os.path.isfile(f) and f not in EXCLUDE_FILES:
		thread = threading.Thread(target=thread_render, args=(f,))
		threads.append(thread)

for thread in threads:
	thread.start()

for thread in threads:
	thread.join()

print(f"Rendered {len(files)} files in {time.time() - t} seconds.")