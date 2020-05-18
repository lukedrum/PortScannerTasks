# Zadanie 3
#
# Wykorzystując zdobytą wiedzę, napisz skrypt symulujący skanowanie portów w zakresie 1-1000
# używając do tego modułu threading. Sprawdź czy wykorzystanie wątków faktycznie przyspiesza działanie skryptu.
# Nie korzystaj z modułu socket. Skrypt ma tylko symulować pracę skanera.
# Wykorzystaj poniższy fragment kodu.

import threading
import queue
import time


def main():
    task_q = queue.Queue()

    # fill tasks queue with task
    # Place Your code here 
            
    #######################
   
    # create worker code here
    def worker(worker_id, task_q):
            # Place Your code here 
            
            #######################

            print(str(worker_id) + " simulating work on a task" + str(task))
            time.sleep(1)

        return True
  
    # use threads to perform worker tasks
    # Place Your code here 
    
    #####################################


if __name__ == "__main__":
    main()
