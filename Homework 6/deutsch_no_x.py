from qiskit import QuantumCircuit, transpile
from qiskit.quantum_info import Statevector
from numpy.random import randint
from math import pi
from qiskit_aer import AerSimulator

#1. Implement Circuit for Deutsch's Algorithm
qc = QuantumCircuit(2,2)

#Apply X and Haddamard Gate to Input Qubit
qc.x(0)
qc.h(0)

#Apply ONLY Haddamard to output qubit, Omit the X gate!
qc.h(1)

#unitary Encoding Function 
#generate random ints from 0 to 3
num = randint(0,4)
print("Random Int: ", num)
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
print("Measurement Results: ", counts)


#Print Statements for Question 3
#"Explain the conclusion that we may draw from the results of the measurement"
print("Conclusion: ")
print("The state measured is 01 when it's f(0), f(1), f(2),f(3), ")
print("This also means that the input qubit is |1> regardless if balanced or constant")
print("U_f is pretty much useless here since you can't really tell what formula (f0/f1/f2/f3) is used. (RIP the Gators)")
print("The measurement also tells us that all the counts are equal")