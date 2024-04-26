import time
import threading

def calc_square(numbers):
    print("calculate square numbers")
    for n in numbers:
        print('square:',n*n)
        time.sleep(0.2)
        
        

def calc_cube(numbers):
    print("calculate cube numbers")
    for n in numbers:
        print('Cube:',n*n*n)
        time.sleep(0.2)
        
        

arr=[2,3,4,9]

t=time.time()
t1=threading.Thread(target=calc_square,args=(arr,))
t2=threading.Thread(target=calc_cube,args=(arr,))
t1.start()
t2.start()

t1.join()
t2.join()

print('done in:', time.time()-t)
print("completed")
