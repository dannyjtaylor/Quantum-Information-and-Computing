from qiskit import QuantumCircuit, transpile
from qiskit.quantum_info import Statevector
from numpy.random import randint
from math import pi
from qiskit_aer import AerSimulator

qc = QuantumCircuit(3)

# controlled s
qc.cs(0,1)

# haddamard qubit 1
qc.h(1)

# controlled t gate, doesn't exist
# but it is just phase gate w/ phase = pi/4
# qc.ct(0,2)

qc.cp(pi/4, 0,2)

qc.cx(1,2)

print(qc.draw())


# Circuit #2
qc2 = QuantumCircuit(6)

qc2.cx(1,3)
qc2.cx(1,4)
qc2.cx(5,3)
qc2.cx(2,4)
qc2.ccx(0,4,2)
qc2.cx(2,4)
qc2.ccx(0,3,5)

print(qc2.draw())


# simulate measurements

# Circuit #3
# qc3 = QuantumCircuit(5,5) number of Qbits, number of Cbits
# qc.measure(range(5), range(5))   range just makes a list of bits 0-4
# measure 5 quantum bits, store into 5 classical bits.

qc3 = QuantumCircuit(5,5)
qc3.x(0)
qc3.x(1)
qc3.x(4)

qc3.measure(range(5), range(5))
print(qc3.draw())
# print(qc3.clbits)

simulator = AerSimulator()
# transpile circuit
qc3 = transpile(qc3, simulator)

# run and get counts
result = simulator.run(qc3).result()
counts = result.get_counts(qc3)

# print Cbit values
print("Measurement Results: ", counts)
# written in random order i guess? 0-4
# this just draws it tho. now u have to use qiskit aer to actually simulate it

