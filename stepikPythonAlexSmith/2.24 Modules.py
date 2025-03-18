from mod import moduleHello
import math
import random
from mod.math_functions import summ
from mod import math_functions as mf

moduleHello.some()

print(math.pi)

r = random.randrange(0, 10)
user = 'User'
user_random = f'{user}{r}'
print(user_random)

summ(5, 3)
mf.sub(5, 3)