import ipdb
from lib import *

# Test your code below...


godzilla = Role("godzilla")

kevin = Audition("kevin", "chicago", godzilla)
dakota = Audition("dakota", "alaska", godzilla)
ye = Audition("ye", "chicago", godzilla)

superman =Role("superman")

cat = Audition("cat", "nj", superman)
vanessa = Audition("vanessa", "nj", superman)
kim = Audition("kim", "north carolina", superman)

# the below line allows us to stop & try stuff!
ipdb.set_trace()