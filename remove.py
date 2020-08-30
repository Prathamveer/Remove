import os, time, sys

path = r"/Users/mandeepsinghchahal/Desktop/Py"

now = time.time()

for f in os.listdir(path):

 if os.stat(f).st_mtime < now - 7 * 86400:

  if os.path.isfile(f):

   os.remove(os.path.join(path, f))