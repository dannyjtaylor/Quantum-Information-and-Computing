from qiskit import QuantumCircuit, QuantumRegister, ClassicalRegister #shriraj helped me to make my code more efficient, didnt know there was a quantum reg/classical reg module
from qiskit_aer import AerSimulator
from qiskit import transpile



#so we know sqrt(Z) = P(pi/2), which is the S gate
#from directions, we can act on q0 by calling qc.s(q0)
#sqrt(X) is done by H * (sqrt(Z)) * H
#from directions,we call sqrt(X) as qc.sx(q0)
#we need sqrt(X) for the 3-qbit doubly controlled NOT gate, ccX_ijk.
#ccX_ijk = (c sqrt(X)_jk) * (cX_ij) * (c sqrt(X)^dagger_jk) * (cX_ij) * c (sqrt(X)_ik)
#ccX_ijk = (c sqrt(X)_jk) * (cX_ij) * (c sqrt(X)^dagger_jk) * (cX_ij) * c (sqrt(X)_ik)
#we know that sqrt(x) = H * sqrt(Z) * H
#since sqrt(Z) = S, we can say that sqrt(X) = H * S * H

# PART 8.
#therefore, sqrt(X)^dagger = H * S^dagger * H
#i did it here in the code since i didnt know how to show it from scratch paper to the .py files


#so we need to figure out how to implement controlled (sqrt(X)^dagger) gate

def my_ccx(qc: QuantumCircuit, control_i: int, control_j: int, target_k: int, target: int):


    #controlled sqrt(X)_jk
    qc.h(target_k)
    qc.cs(control_j, target_k)
    qc.h(target_k)

    #cX_ij
    qc.cx(control_i, control_j)

    #the hard one: c sqrt(X)^dagger_jk ( so we do H controlled S^dagger H)
    qc.h(target_k)
    qc.csdg(control_j, target_k) #constrolled S dagger
    qc.h(target_k)

    #cX_ij
    qc.cx(control_i, control_j)

    #controlled sqrt(X)_ik
    qc.h(target_k)
    qc.cs(control_i, target_k)
    qc.h(target_k)


#print truth table
print("ccX truth table:")
print("i j k | ccX |")
    
#iterate over all possible values of i, j, and k, so we need a triple nested loop
for i in range(2): # range 2 because we have 0 or 1
    for j in range(2):
        for k in range(2):
            #use quantumreg/classicalreg modules to help create the qc
            quantum_bits = QuantumRegister(3)
            classical_bits = ClassicalRegister(3)
            qc = QuantumCircuit(quantum_bits, classical_bits)

            #use X gates to get initial state
            if i == 1:
                qc.x(quantum_bits[0])
            if j == 1:
                qc.x(quantum_bits[1])
            if k == 1:
                qc.x(quantum_bits[2])

            my_ccx(qc, quantum_bits[0], quantum_bits[1], quantum_bits[2], classical_bits[2])
            qc.measure(quantum_bits, classical_bits)

            #simulate
            simulator = AerSimulator()
            qc = transpile(qc, simulator)
            result = simulator.run(qc).result()
            counts = result.get_counts(qc)
            measured = list(counts.keys())[0]
            output = int(measured[0])
            print(f"{i} {j} {k} |  {output}  |")

#for context the expected truth table should be something like this if the 2 cbits control, and the quantum is target
# i j k | ccX |       (remember its like (I*J) XOR K)
# 0 0 0 |  0  | 
# 0 0 1 |  1  |
# 0 1 0 |  0  |
# 0 1 1 |  1  |
# 1 0 0 |  0  |
# 1 0 1 |  1  |
# 1 1 0 |  1  |
# 1 1 1 |  0  |

# i love quantum
# too