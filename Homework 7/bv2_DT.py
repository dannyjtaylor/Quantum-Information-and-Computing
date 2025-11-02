# 1. write a script bv1.py

from re import A
from qiskit import QuantumCircuit, transpile
from qiskit.quantum_info import Statevector
from numpy.random import randint
from math import pi
from qiskit_aer import AerSimulator

#2. 5 random Cbits stored in array a

#generate five random bits (0 or 1) in an array
a = [0,0,0,0,0]
for i in range(0,5):
    a[i] = randint(0,2)
    # print(f"{bits[i]}")
print("Original bit string for A (in Python array form) ", a)


#3. 
#5 input qbits, 1 output qbit
qc = QuantumCircuit(6,5) # need 5 cbits since wem easure the 5 input bits

#4.
#no haddamards, just NOT on output bit
#NOT and haddmard the output bit
qc.x(5)

#5.
#blackbox U_f, ax
qc.barrier()
for j in range(5):
    if a[j] == 1:
        qc.cx(5,j)
qc.barrier()

#6.
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
print("\nResults:")
#youll notice here it looks reversed from the first print line, but it's python printing of an array vs the actual bit 
#string the way we typically look at it in binary
print(f"Original bit string for A (not as Python array form): {a[4]}{a[3]}{a[2]}{a[1]}{a[0]}")

#get measured bit string
measured = max(counts, key=counts.get) # key w/ highest count
print(f"Measured bit string for A (before reversing): {measured}")
measured2 = measured[::-1] #perform "reverse", since the bits are in big endian form to show it in order correctly
print(f"Measured bit string for A (after reversing): {measured2}")

print ("hi")