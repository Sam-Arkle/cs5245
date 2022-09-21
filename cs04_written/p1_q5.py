# (a)
import mymod
print(increment(4)) # Supposed to print 5
# (b)
import mymod
print(mymod.increment(4)) # Supposed to print 5
# (c)
from mymod import increment
print(mymod.increment(4)) # Supposed to print 5
# (d)
from mymode import increment
print(increment(4)) # Supposed to print 5