import argparse
import os

parser = argparse.ArgumentParser(description='Script to find commits.')
parser.add_argument("--start-rev", type=str, default=1)
parser.add_argument("--end-rev", type=str, default='HEAD')
parser.add_argument("--svn-repo-path", type=str, default='https://svn.code.sf.net/p/codeblocks/code/trunk')
args = parser.parse_args()
opt1_value = args.start_rev
opt2_value = args.end_rev
opt3_value = args.svn_repo_path

line = f"svn log -r {opt1_value}:{opt2_value} {opt3_value} -l 15"

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


os.system(f'{line} > //home/dmitry/Desktop/output.log')
write()