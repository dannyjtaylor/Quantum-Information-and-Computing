from qiskit import QuantumCircuit
from qiskit.quantum_info import Statevector
from numpy.random import randint

qc = QuantumCircuit(2)
qc.h(1)

# controlled NOT on qubit 0, controlled by 1. (ij = 10)
qc.cs(1,0)

rint = randint(0,4) # 0,1,2,3
print("Chose: ", rint)

match rint:
    case 0:
        # phi plus
        qc1 = QuantumCircuit(2)
        sv = Statevector.from_instruction(qc1)

        qc1.h(1)
        qc1.cx(1,0) 

        print(qc1.draw(reverse_bits=True))
        print("Chose Phi Plus! StateVector = ", 
        str(sv[0])," |00>", str(sv[1])," |01>", str(sv[2])," |10>",  str(sv[3])," |11>")   
    case 1:
        # phi minus
        qc2 = QuantumCircuit(2)

        qc2.h(1)
        qc2.cx(1,0)
        qc2.z(1)

        print(qc2.draw(reverse_bits=True))
        print("Chose Phi Minus!")
    case 2:
        # psi plus
        qc3 = QuantumCircuit(2)

        qc3.h(1)
        qc3.cx(1,0)
        qc3.x(0)

        print(qc3.draw(reverse_bits=True))
        print("Chose Psi Plus!")
    case 3:
        # psi minus
        qc4 = QuantumCircuit(2)

        qc4.h(1)
        qc4.cx(1,0)
        qc4.x(0)
        qc4.z(1)

        print(qc4.draw(reverse_bits=True))
        print("Chose Psi Minus!")