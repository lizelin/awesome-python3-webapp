import asyncio
import orm
from models import User, Blog, Comment

loop = asyncio.get_event_loop()
async def test():
    await orm.create_pool(user='wxuser', password='Mynormal12#', db='awesome', host="www.linvx.net", port=3306)
    u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')
    print(u)
    await u.save()

loop.run_until_complete(test())
