from functools import lru_cache, cache


import random

print('Hello')

#@cached_property
#@lru_cache()
@cache
def unclean():
    return random.randint(1,100)
for i in range(5):
    print(unclean())

print('*'*100)
