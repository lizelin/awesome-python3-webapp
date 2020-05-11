import os, re
from datetime import datetime

from fabric.api import *

# 服务器登录用户名
env.user = 'zlli'
env.sudo_user = 'root'
env.hosts = ['www.linvx.net']

db_user = 'wxuser'
db_password = 'Mynormal12'

_TAR_FILE = 'dist-awesome.tar.gz'

def build():
    includes = ['static', 'templates', 'transwarp', 'favicon.ico', '*.py']
    includes = ['static', 'templates', '*.py']
    excludes = ['test', '.*', '*.pyc', '*.pyo']
    local('rm -f dist/%s' % _TAR_FILE)
    with lcd(os.path.join(os.path.abspath('.'), 'www')):
        cmd = ['tar', '--dereference', '-czvf', '../dist/%s' % _TAR_FILE ]
        cmd.extend(['--exclude=\'%s\'' % ex for ex in excludes])
        cmd.extend(includes)
        local(' '.join(cmd))

_REMOTE_TMP_TAR = '/home/zlli/tmp/%s' %_TAR_FILE
_REMOTE_BASE_DIR = '/app/srv/awesome'
def deploy():
    newdir = 'www-%s' % datetime.now().strftime("%y-%m-%d_%H.%M.%S")
    # 删除已有的tar
    run('rm -f %s' % _REMOTE_TMP_TAR)
    put('dist/%s'%_TAR_FILE, _REMOTE_TMP_TAR)
    # 创建新目录
    with cd(_REMOTE_BASE_DIR):
        sudo('mkdir %s' % newdir)
    
    # 解压缩
    with cd('%s/%s' % (_REMOTE_BASE_DIR, newdir)):
        sudo('tar -xzvf %s' % _REMOTE_TMP_TAR)
    
    # 重置软链接
    with cd(_REMOTE_BASE_DIR):
        sudo('rm -f www')
        sudo('ln -s %s www' % newdir)
        sudo('chown webrun:webrun www')
        sudo('chown -R webrun:webrun %s' % newdir)
    
    #重启python服务和nginx服务器
    with settings(warn_only=True):
        sudo('supervisorctl stop awesome')
        sudo('supervisorctl start awesome')
        sudo('/etc/init.d/nginx reload')

# https://www.cnblogs.com/toutou/p/supervisor.html


