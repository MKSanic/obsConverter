import os
from shutil import copyfile
from pathlib import Path
mkvs = set()
mp4s = set()
os.chdir(Path(__file__).parent)
os.system(os.getcwd())
for file in os.listdir():
    if(file.split(".")[len(file.split("."))-1] == "mp4"):
        mp4s.add(file)
    elif(file.split(".")[len(file.split("."))-1] == "mkv"):
        mkvs.add(file)
for v in mkvs:
    file = v.split('.')[0:len(v.split('.'))-1][0] + ".mp4"
    fs = f'ffmpeg -i "{v}" -codec copy "mp4s/{file}"'
    os.system(fs)
    copyfile(v,f"mkvs/{v}")
    os.system(f'del "{v}"')
for v in mp4s:
    copyfile(v,f"mp4s/{v}")
    os.system(f'del "{v}"')
