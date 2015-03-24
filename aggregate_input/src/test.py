#!/usr/bin/env python3.4

import sys
from builtins import reversed

print('This should land on the console')

stdout_backup = sys.stdout

file_socket = open('output.log', 'w')
sys.stdout = file_socket

print('This should be written in the output.log file')

sys.stdout = stdout_backup
file_socket.close()




def banana(greetings):
    aa = 'nichts'
    print("%(greetings)%(aa)")
    
a = 'Banana'
print("blala%(a)")
banana("blala%(a)")

aa=[232, 13, 123]
bb=[1111, 321]
print(sorted(aa))
print(sorted(aa, reverse=True))
print(sorted(aa+bb, reverse=True))
print(sorted(aa+bb, reverse=True, key=lambda number: 1/number))
print(sorted(aa+bb, reverse=True, key=lambda number: str(number)[0]))

for x in bb:
    print(x)
    print('ble')
else:
    print(x)
    print('else')


bb = {'a' : 1, 'b' : 2}
bb['c'] = 3
del bb['a']
print(bb)
print(bb['b'])


zz=[('City A', 1111), ('City B', 22222), ('City CC', 333)]
for ss in sorted(zz, reverse=False, key=lambda tuplee: str(tuplee[1])[0]):
    print(ss[0], ', ', ss[1])
    
print(zz[0])


# lambda
my_sum = lambda a, b: a + b
print('my_sum(1, 2) = ' + str(my_sum(1, 2)))

decimals = (0.1, 0.01, 0.23)
def convert_to_percent(decimal):
    return decimal * 100
print(list(map(convert_to_percent, decimals)))



stderr_backup = sys.stderr

file_socket = open('output2.log', 'w')
sys.stderr = file_socket

raise Exception('Banana exception')
