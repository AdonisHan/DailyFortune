import collections as cl
from random import choice
import datetime
now = datetime.datetime.now()

def _day(func):
    Adjs = 'lively precious pleasant fun cheerful positive special charming wonderful best'.split();
    def inner():
        print('You will have "{}" today'.format(choice(Adjs)))
        func()
    return inner
def _having():
    Advs = 'diligent sincerely fun passionate heart pleasant cool warm'.split();
    print('with "{}".'.format(choice(Advs)))

draws = _day(_having)

print('<===Your {:%Y-%m-%d} Daily Fortune===>'.format(now))
draws()
print('<===Your {:%Y-%m-%d} Daily Fortune===>'.format(now))
