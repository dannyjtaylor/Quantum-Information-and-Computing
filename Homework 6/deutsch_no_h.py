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

#Apply X and Haddamard to output qubit
qc.x(1)
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
#apply hadamard gate ONLY to the output bit, not to the input!!
qc.h(1)

#measure only input bit
qc.measure(0,0)
print(qc.draw())
simulator = AerSimulator()
qc = transpile(qc, simulator)
result = simulator.run(qc).result()
counts = result.get_counts(qc)
print("Measurement Results: ", counts)


#Print Statements for Question 2
#"Explain why we can no longer draw any helpful conclusions from the circuit"
print("Conclusion: ")
print("The state measured is a superposition of |01> and |00> when it's f(1), around a 50% chance for both. (Probably a linear combo of bell states?)")
print("The state measured is a superposition of |01> and |00> when it's f(3), around a 50% chance for both. (Probably a linear combo of bell states?)")
print("The state measured is a superposition of |01> and |00> when it's f(0), around a 50% chance for both. (Probably a linear combo of bell states?)")
print("The state measured is a superposition of |01> and |00> when it's f(2), around a 50% chance for both. (Probably a linear combo of bell states?)")


print("This also means that the input qubit is in a superposition of |0> and |1> regardless if f(x) is balanced (f1,f2) or constant (f3,f0)")
print("U_f is hard to analyze here since we can't know which formula (f0/f1/f2/f3) is used. (Unless you know the inside of the black box of course)")
print("The measurement also tells us that all the counts aren't equal, but are roughly like a 50% chance")
print("This makes me think this is a lienar combo of bell states")