from qiskit import QuantumCircuit, transpile
from qiskit.quantum_info import Statevector
from numpy.random import randint
from math import pi
from qiskit_aer import AerSimulator

# generate five random classical bits (0 or 1)
bits = {}
for i in range(0,4):
    bits[i] = randint(0,2)
    print(f"{bits[i]}")

print(f"{bits}")