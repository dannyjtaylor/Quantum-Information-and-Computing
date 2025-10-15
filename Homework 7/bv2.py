from qiskit import QuantumCircuit, transpile
from qiskit.quantum_info import Statevector
from numpy.random import randint
from math import pi
from qiskit_aer import AerSimulator

#generate five random cbits (0 or 1) in an array
bits = {}
for i in range(0,5):
    bits[i] = randint(0,2)
    print(f"{bits[i]}")
print(f"{bits}")

#5 input qbits, 1 output qbit
qc = QuantumCircuit(6,5) # need 5 cbits since wem easure the 5 input bits
#only NOT outbit bit, no haddamard on any bits
qc.x(5)

#blackbox U_f, ax
qc.barrier()
for j in range(5):
    if bits[j] == 1:
        qc.cx(5,j)
qc.barrier()

#measure input register bits
qc.measure([0,1,2,3,4], [0,1,2,3,4])

#draw
print(qc.draw())

# use simulator
simulator = AerSimulator()
qc = transpile(qc, simulator)
result = simulator.run(qc).result()
counts = result.get_counts(qc)
print("Measurement Results With Counts: ", counts)

# to make it percentages, realize counts is a python dict. the values are the numbers, and the key is the state
print("Measurement Results as Percentages: ")
for key,count in counts.items():
    percent = (count/1024)*100
    print(f"{key}: {percent:.2f}%")

#print bit string of a
print("Results:")
print(f"Original bit string: {bits[0]}{bits[1]}{bits[2]}{bits[3]}{bits[4]}")

# get measured bit string
measured = max(counts, key=counts.get) # key w/ highest count
print(f"Measured bit string (measurements): {measured}")

# apparently need big endian to show uit correctly
measured2 = measured[::-1]
print(f"new measured: {measured2}")
