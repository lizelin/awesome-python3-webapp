# !/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
url handlers
'''

import re, time, json, logging, hashlib, base64, asyncio
from coroweb import get, post
from models import User, Comment, Blog, next_id

@get('/')
async def index(request):
    summary = 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'
    blogs = [
        Blog(id='1', name='Test Blog', summary=summary, created_at=time.time()-120),
        Blog(id='2', name='Something New', summary=summary, created_at=time.time()-3600),
        Blog(id='3', name='Learn Swift', summary=summary, created_at=time.time()-7200)
    ]
    return {
        '__template__': 'blogs.html',
        'blogs': blogs
    }

@get('/api/users')
async def api_get_users(*, page='1'):
    num = await User.findNumber('count(id)')
    print(" user  count is : %d" %num)
    if num ==0:
        return dict(page=1, users=())
    users = await User.findAll(orderBy='created_at desc', limit=(0, 10))
    for u in users:
        u.passwd = '******'
    return dict(page=1, users=users)

   