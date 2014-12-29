import os
import re
import subprocess

for dir_, _, files in os.walk("."):
        for fileName in files:
                relDir = os.path.abspath(dir_)
                relFile = os.path.join(relDir, fileName)
                match = re.match(r'.*\.xml$', relFile)
                if(match):
                        f=subprocess.call(["xmllint","--noout",relFile])
                        if(f!=0):
                                print relFile

