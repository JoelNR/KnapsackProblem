import sys
import time
import os
from solve_greedy import solve_greedy
from solve_tabulation import solve_tabulation
from solve_memoization import solve_memoization
from utils import readFile,taken_items,total_weight



def main():
    
    if len(sys.argv) == 2 and sys.argv[1] == "-h":
        help()
    else:

        def solve(items,capacity):  
            
            def printData():
                for i in range(3,len(sys.argv)):
                    if(sys.argv[i] == "-b"):
                        print("Beneficio: " + str(value))
                    if(sys.argv[i] == "-r"):
                        print("Room: " + str(capacity - total_weight(items,taken)))
                    if(sys.argv[i] == "-t"):
                        print("Time: " + str(fin-inicio) + "seconds")
                    if(sys.argv[i] == "-dt"):
                        print(taken_items(items,taken))
                        
            if len(sys.argv) >= 4:
                for i in range(3,len(sys.argv)):
                    if(sys.argv[i] == "-sg"):
                        inicio = time.time()
                        value, taken = solve_greedy(items,capacity)        
                        fin = time.time()
                        print("GREEDY:")
                        printData()                        
                    if(sys.argv[i] == "-sm"):
                        inicio = time.time()
                        value, taken = solve_memoization(items,capacity)        
                        fin = time.time()
                        print("MEMOIZATION:")
                        printData()
                    if(sys.argv[i] == "-st"):
                        inicio = time.time()
                        value, taken = solve_tabulation(items,capacity)        
                        fin = time.time()
                        print("TABULATION:")
                        printData()
                        
                    
        if (sys.argv[1] == "-f"):
            items, capacity = readFile(sys.argv[2])
            solve(items,capacity)

        if (sys.argv[1] == "-d"):
            with os.scandir(sys.argv[2]) as ficheros: 
                for fichero in ficheros:
                    items, capacity = readFile(fichero)
                    solve(items,capacity)



main()