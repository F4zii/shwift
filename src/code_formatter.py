import subprocess
import os

discore_dir = os.listdir(".")

files = [f for f in discore_dir if os.path.splitext(f)[1] == ".py"]


for f in files:
    try:
        subprocess.call(["black", f])
    except:
        pass
