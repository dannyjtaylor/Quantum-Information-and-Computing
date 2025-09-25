from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from numpy.random import randint
from math import pi

qc = QuantumCircuit(7)

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
qc.cx(2,4)

#part 3
#controlled NOT, control is bit 2, target is bit 5

qc.cx(2,5)

# part 4
# controlled NOT, control is bit 6, target is bit 4
qc.cx(6,4)

# part 5
# just a controlled NOT, control is bit 3, target is bit 5
qc.cx(3,5)

# part 6
# toffoli gate, control bits 1 and 4, targeted on bit 6
qc.ccx(1,4,6)

# part 7
qc.cs(0,1)
qc.cx(6,4)

# part 8
qc.h(1)

# part 9
qc.cp((pi/4,0,2))

# part 10
qc.cx(1,2)

# part 11


# part 12
qc.h(2)


# part 13