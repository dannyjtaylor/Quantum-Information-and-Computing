from qiskit import QuantumCircuit, transpile
from qiskit.quantum_info import Statevector
from numpy.random import randint
from math import pi
from qiskit_aer import AerSimulator

#1. Implement Circuit for Deutsch's Algorithm
qc = QuantumCircuit(2,1)

#Apply X and Haddamard Gate to Input Qubit
qc.x(0)
qc.h(0)

#Apply X and Haddamard to output qubit
qc.x(1)
qc.h(1)

#unitary Encoding Function 
#generate random ints from 0 to 3
num = randint(0,4)
print("Random Int: ", num, " so Function Chosen: f(", num, ")")
#case statement for the random int to apply to its corresponding f
match num:
    case 0:
        #f0
        #same regardless of input
        qc.id(1)
    case 1:
        #f1
        #1 if the output is 0
        qc.cx(0,1)
    case 2:
        #f2
        #0 if the output is 1
        qc.x(1)
        qc.cx(0,1)
    case 3:
        #f3
        #0 regardless of input
        qc.x(1)
#apply hadamard layer
qc.h(0)
qc.h(1)

#measure only input bit
qc.measure(0,0)
print(qc.draw())
simulator = AerSimulator()
qc = transpile(qc, simulator)
result = simulator.run(qc).result()
counts = result.get_counts(qc)
print("Measurement Results With Counts: ", counts)

# to make it percentages, realize counts is a python dict. the values are the numbers, and the key is the state
print("Measurement Results as Percentages: ")
for key,count in counts.items():
    percent = (count/1024)*100

    # #use numShots when finding percent since i'm not using 1024 default
    # percent = (count/numShots)*100

    #format print to print the keys w 2 decimal places
    print("Input Qubit measured as:", sep ="")
    print(f"{key}: {percent:.2f}%")


#Print Statements for Question 2
#"Explain the conclusion that we may draw from the results of the measurement"
print("Conclusion: ")
print("The input qubit is measured as 0 100% of the time when it's f(1), f(2) (U_f is balanced),")
print("and as 1 100% of the time when f(3),f(0) (U_f is constant)")
# hi

