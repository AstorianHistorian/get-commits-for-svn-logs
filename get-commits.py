#! /usr/bin/python3
import argparse
import os

parser = argparse.ArgumentParser(description='Script to find commits.')
parser.add_argument("--start-rev", type=str, default=1)
parser.add_argument("--end-rev", type=str, default='HEAD')
parser.add_argument("--svn-repo-path", type=str, default='https://svn.code.sf.net/p/codeblocks/code/trunk')
parser.add_argument("--file-name", type=str, default='')
args = parser.parse_args()
opt_value1 = args.start_rev
opt_value2 = args.end_rev
opt_value3 = args.svn_repo_path
opt_value4 = args.file_name

line = f"svn log -r {opt_value1}:{opt_value2} {opt_value3} {opt_value4} -l 15"

def write():
        with open('//home/dmitry/Desktop/output.log','r') as f:
            ln = f.readlines()

        with open('//home/dmitry/Desktop/output.log','w') as f:
            for line in ln:
                if "|" in line:
                    line = line.split("|")
                    f.write(f"@{line[1]}\n")
                elif ("---" in line) or (line == '\n'):
                    pass
                else:
                    f.write(f"  -{line}")

if opt_value4 != '':
    os.system(f"svn blame {opt_value3}> //home/dmitry/Desktop/outputfile.log")
os.system(f'{line} > //home/dmitry/Desktop/output.log')
write()