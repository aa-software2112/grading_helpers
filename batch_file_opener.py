import glob

# Fetches a directory of files, opens only pdfs, docx/doc, and .txt files
# Creates a "completed" folder, moves files there once display is complete
DIR = r"C:\Users\anthonya\Downloads\a2w"
files = glob.glob(f"{DIR}\*.*")
files = list(filter(lambda f: any([file_type in f for file_type in [".pdf", ".docx", ".doc", ".txt"]]), files))
print("**** FILES TO OPEN ****")
for file in files:
    print(file)

import os
COMPLETED_DIR = f"{DIR}\completed"
try:
    os.mkdir(COMPLETED_DIR)
except: # Assume already created
    pass

import subprocess, shutil
ADOBE_READER = r"C:\Program Files (x86)\Adobe\Acrobat Reader DC\Reader\AcroRd32.exe"
WORD = r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.exe"
TXT = r"C:\Program Files\Notepad++\notepad++.exe"

print("\n", "**** OPENING FILES ****")
import time
for file in files:

    EXE = None
    if file.endswith(".pdf"):
        EXE = ADOBE_READER
    elif any([file.endswith(f) for f in [".docx", "doc"]]):
        EXE = WORD
    elif file.endswith(".txt"):
        EXE = TXT

    print("OPENING ----->", file)
    p = subprocess.Popen([EXE, file])
    d = input()
    p.terminate()
    time.sleep(0.750)
    try:
        shutil.move(file, COMPLETED_DIR)
    except Exception as e:
        print(e)
        