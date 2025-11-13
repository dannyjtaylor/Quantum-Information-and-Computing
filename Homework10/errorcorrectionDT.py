from qiskit import QuantumCircuit, transpile, QuantumRegister, ClassicalRegister
from qiskit.quantum_info import Statevector
from numpy.random import randint
from qiskit_aer import AerSimulator


#part 1
qubits = QuantumRegister(5)
clbits = ClassicalRegister(5)
qc = QuantumCircuit(qubits, clbits)
(a0,a1, q0, q1, q2) = qubits
(ca0, ca1, cq0, cq1, cq2) = clbits


#part 2
#codeword bits are q0, q1, q2
#generate random number to determine which of the three bits has it flipped, one result no flip
# so if it chooses 0, q0 flipped, chooses 1, q1 flipped, chooses 2, q2 flipped, chooses 3, no flip
randNum = randint(0,4)
if randNum == 0:
    qc.x(q0)
    print(f"Random number chosen: {randNum}, q0 flipped, codeword state is now |100>")
elif randNum == 1:
    qc.x(q1)
    print(f"Random number chosen: {randNum}, q1 flipped, codeword state is now |010>")
elif randNum == 2:
    qc.x(q2)
    print(f"Random number chosen: {randNum}, q2 flipped, codeword state is now |001>")
else:
    print(f"Random number chosen: {randNum}, no flip, codeword state is still |000>")
qc.barrier()

#part 3
#apply hadamard gates to ancillary bits
qc.h(a0)
qc.h(a1)
qc.barrier()
#apply control-ZZ gate by pair of single cZ gates for each ancillary bit
# a0 checks parity of q0 and q1
qc.cz(a0, q0)
qc.cz(a0, q1)
# a1 checks parity of q1 and q2
qc.cz(a1, q1)
qc.cz(a1, q2)
qc.barrier()

#apply hadamard gates to ancillary bits again before measuring
qc.h(a0)
qc.h(a1)
qc.barrier()

#part 4
#measure ancillary bits, this is how you determine where to place the X gate
qc.measure(a0, ca0)
qc.measure(a1, ca1)

#se nested if statements to check all combinations for error
with qc.if_test((ca0, 1)):
    with qc.if_test((ca1, 0)):
        #ca0=1, ca1=0, so error on q0
        qc.x(q0)
    with qc.if_test((ca1, 1)):
        #ca0=1, ca1=1, so error on q1
        qc.x(q1)
with qc.if_test((ca0, 0)):
    with qc.if_test((ca1, 1)):
        #ca0=0, ca1=1, so error on q2
        qc.x(q2)
    #ca0=0, ca1=0, so no error, do nothing
qc.barrier()

#part 5
#measure codeword bits
qc.measure(q0, cq0)
qc.measure(q1, cq1)
qc.measure(q2, cq2)
simulator = AerSimulator()
qc = transpile(qc, simulator)
result = simulator.run(qc).result()
counts = result.get_counts(qc)
print("\nMeasurement Results With Counts: ", counts)

#displays as q2 q1 q0 a1 a0
print("\nMeasurement Results as Percentages: ")
for key, count in counts.items():
    print(f"codeword: {key[:3]} and ancillary: {key[3:]}")
    percent = (count/1024)*100
    print(f"{key}: {percent:.2f}%")