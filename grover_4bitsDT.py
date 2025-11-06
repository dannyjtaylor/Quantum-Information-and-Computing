from qiskit import QuantumCircuit, transpile
from qiskit.quantum_info import Statevector
from numpy.random import randint
from qiskit_aer import AerSimulator


#part 1- initialization o 2-bit grovers algorithm
qc = QuantumCircuit(5,4)
#2 cbits for measurement
#input register, 2 bits
qc.h(0)
qc.h(1)
qc.h(2)
qc.h(3)
#output register, 1 bit
qc.x(4)
qc.h(4)
qc.barrier()



#part 2 - V gate (or the oracle gate)
#generate random 2-bit string that is 0 or 1
randNumList = [0,0,0,0]
for i in range(0,4):
    randNumList[i] = randint(0,2)
print(f"Random 4-bit string: {randNumList[3]}{randNumList[2]}{randNumList[1]}{randNumList[0]}") #done in this way (lil endian)

#in the black box you NOT any bit that is regernated to be 1, then ccX those bits with output bit, and then re-NOT the bit that was NOTTED before
for i in range(4):
    if randNumList[i] == 1:
        qc.x(i)
#multi controlled X gate, controls are all input bits, target is output bit
qc.mcx([0, 1, 2], 4)
for i in range(4):
    if randNumList[i] == 1:
        qc.x(i)
qc.barrier()



#part 3, -W gate
# haddamard + x layer on input register, but most significant input register is control Z'd
for i in range(4):
    qc.h(i)
    qc.x(i)
#4-bit multi controlled Z gate. can go H, MCX, and H
qc.h(3)
qc.mcx([0, 1, 2], 3)
qc.h(3)

for i in range(4):
    qc.x(i)
    qc.h(i)
qc.barrier()



#part 4, -WV gate, for a 4-qubit gate measure input register bits w/ the cbits
#do it p-1 times! if p is around sqrt(2^n) * pi/4, that means it's sqrt(16) * pi/4 = 4pi/4 = pi. pi is 3.14, 3.14 - 1 = 2.
#so perform -WV gate twice
#V gate again
pminusOne = 2
for i in range(pminusOne):
    for i in range(4):
        if randNumList[i] == 1:
            qc.x(i)
    #multi controlled X gate, controls are all input bits, target is output bit
    qc.mcx([0, 1, 2], 4)
    for i in range(0,4):
        if randNumList[i] == 1:
            qc.x(i)
    #-W gate again
    for i in range(4):
        qc.h(i)
        qc.x(i)
        
    #4-bit multi controlled Z gate. can go H, MCX, and H
    qc.h(3)
    qc.mcx([0, 1, 2], 3)
    qc.h(3)

    for i in range(4):
        qc.x(i)
        qc.h(i)
    qc.barrier()

#finally measure
qc.measure(range(4), range(4))

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