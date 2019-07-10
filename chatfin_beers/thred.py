from threading import *
'''
def display():
    print('Main thread' ,current_thread().getName())

t=Thread(target=display)

t.start()

print('Main thread' , current_thread().getName())
'''

class Mythread(Thread):
    def run(self):
        for i in range(10):
            print('Child Thread')

t = Mythread()
t.start()

for i in range(10):
    print('Main Thread')