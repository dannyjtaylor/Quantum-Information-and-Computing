from qiskit import QuantumCircuit, transpile
from qiskit.quantum_info import Statevector
from numpy.random import randint
from qiskit_aer import AerSimulator

#part 1- initialization o 2-bit grovers algorithm
qc = QuantumCircuit(3,2)
#2 cbits for measurement
#input register, 2 bits
qc.h(0)
qc.h(1)
#output register, 1 bit
qc.x(2)
qc.h(2)

qc.barrier()
#part 2 - V gate (or the oracle gate)
#generate random 2-bit string that is 0 or 1
randNum1 = randint(0,2)
randNum2 = randint(0,2)
print(f"Random 2-bit string: {randNum1}{randNum2}")

#in the black box you NOT any bit that is regernated to be 1, then ccX those bits with output bit, and then re-NOT the bit that was NOTTED before
if randNum1 == 1:
    qc.x(0)
if randNum2 == 1:
    qc.x(1)
qc.ccx(0,1,2)
if randNum1 == 1:
    qc.x(0)
if randNum2 == 1:
    qc.x(1) 

qc.barrier()

#part 3, -W gate
# haddamard + x layer on input register, but most significant input register is control Z'd

qc.h(0)
qc.h(1)
qc.x(0)
qc.x(1)
qc.cz(0,1)
qc.x(1)
qc.x(0)
qc.h(1)
qc.h(0)
qc.barrier()

#part 4, -WV gate, looks like for 2-qubit we don't really need to do this beside measure
#measure input register bits w/ the cbits
qc.measure([0,1], [0,1])

#draw
print(qc.draw())

#use simulator
simulator = AerSimulator()
qc = transpile(qc, simulator)
result = simulator.run(qc).result()
counts = result.get_counts(qc)
print("Measurement Results With Counts: ", counts)

#to make it percentages, realize counts is a python dict. the values are the numbers, and the key is the state
print("Measurement Results as Percentages: ")
for key,count in counts.items():
    percent = (count/1024)*100
    print(f"{key}: {percent:.2f}%")