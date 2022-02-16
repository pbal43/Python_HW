from random import randrange
from datetime import timedelta
from datetime import datetime

def random_date(start, end):
    """
    This function will return a random datetime between two datetime
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)

d1 = datetime.strptime('1/1/2008', '%m/%d/%Y')
d2 = datetime.strptime('1/1/2009', '%m/%d/%Y')


a = random_date(d1, d2)
z = str(a)
randik = (z[0:10])





