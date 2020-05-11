from fabric.api import *

def look():
    local('rm a.txt')

# 命令行执行：fab -f fabcheck.py -H 127.0.0.1 'look'