from fabric.api import run

def look():
    run('uname -a')

# 命令行执行：fab -f fabcheck.py -H 127.0.0.1 'look'