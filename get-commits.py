#! /usr/bin/python3
import argparse
import os
from pathlib import Path

df = "*.txt*"
home = str(Path.home())

parser = argparse.ArgumentParser(description='Script to find commits.')
parser.add_argument("--start-rev", type=str, default=1)
parser.add_argument("--end-rev", type=str, default='HEAD')
parser.add_argument("--svn-repo-path", type=str, default='http://svn.code.sf.net/p/keepass/code/trunk/')
parser.add_argument("--file-name", type=str, default=f'{df}')
args = parser.parse_args()
opt_value1 = args.start_rev
opt_value2 = args.end_rev
opt_value3 = args.svn_repo_path
opt_value4 = args.file_name

def write():
        with open(f'/{home}/Desktop/logs/output.log','r') as f:
            ln = f.readlines()

        with open(f'/{home}/Desktop/logs/output.log','w') as f:
            for line in ln:
                if "|" in line:
                    line = line.split("|")
                    f.write(f"@{line[1]}\n")
                elif ("---" in line) or (line == '\n'):
                    pass
                else:
                    f.write(f"  -{line}")

os.system("mkdir $HOME/Desktop/logs/")

if opt_value4 != '':
    os.system(f"svn log --search {opt_value4} -r {opt_value1}:{opt_value2} {opt_value3} > $HOME/Desktop/logs/output.log")
else:    
    os.system(f"svn log -r {opt_value1}:{opt_value2} {opt_value3} > $HOME/Desktop/logs/output.log")
write()
