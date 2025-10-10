from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator
from qiskit.quantum_info import Statevector
from numpy.random import randint
from math import pi, gcd

# hey dr barker! :3 you'll see i separated the circuit into "parts", like how we looked at the time state after each gate in class


qc = QuantumCircuit(7,3)

# part 1
# haddamard gates on bit 0/1/2
# NOT/X gate on bit 6
qc.h(0)
qc.h(1) 
qc.h(2)
qc.x(6)

# part 2
# it haddamards bit 0 again, and does a controlled NOT (control is on bit 2, target is bit 4)
qc.h(0)
qc.cx(2, 4)

#part 3
#controlled NOT, control is bit 2, target is bit 5
qc.cx(2, 5)

# part 4
# controlled NOT, control is bit 6, target is bit 4
qc.cx(6, 4)

# part 5
# just a controlled NOT, control is bit 3, target is bit 5
qc.cx(3, 5)

# part 6
# toffoli gate, control bits 1 and 4, targeted on bit 6
qc.ccx(1, 4, 6)

# part 7
qc.cs(0, 1)
qc.cx(6, 4)

# part 8
qc.h(1)

# part 9
qc.cp(pi/4, 0, 2)

# part 10
qc.cx(1,2)

# part 11
# looks like just a measurement gate, done later

# part 12
qc.h(2)


# part 11/13/14, measurement gates
# measure qbits 0, 1, 2, to Cbits 0, 1, 2
qc.measure(range(3), range(3))
print(qc.draw())
simulator = AerSimulator()
# i increased number of shots cause earlier i didn't get roughly 25% for each, but apparently it made no difference. its just how shors algorithm is apparently
# numShots = 10000
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
    print(f"{key}: {percent:.2f}%")

decimal = []
for keys in counts:
    b0 = int(keys) % 10
    b1 = int(int(keys)/10) % 10
    b2 = int(int(keys)/100) % 10
    decimal.append(b2*2**2 + b1*2 + b0)
decimal.sort()
print("Decimal Values of States: ", decimal)

period = decimal[2] - decimal[1]

r = 2**3/period
factors = []
factors.append(gcd(int((2**3-1)**(r/2)+1), 15))
factors.append(gcd(int((2**3-1)**(r/2)-1), 15))

print(" ")
print(factors, "are the factors of 15")

# is 1 and 15 technically factors of 15