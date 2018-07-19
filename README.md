# Toxic v1
A 4-bit RISC CPU written in Verilog HDL
## Introduction
We call it Toxic since if we say something is "Toxic" in Chinese, we mean that such thing is strange or mind-fucking. Indeed, Toxic is one of the strangest ISA in the 21-century's. In Toxic ISA, you will not be able to use so many modern features of modern CPUs, you will not have a bunch of  but just two multi-functional general-specific registers. Even to the extent that each instruction is 4-bit long which means in the best case you have in all 2^4 =16 possible instructions including register address and immediate numbers. Have fun coding it.
## Instruction Set Architecture (ISA)
In Toxic_v1, each instruction is 4-bit long and the length of opcode may vary from 2-bit to 3-bit. For specific implementation see [Toxic ISA specifications](Toxic_ISA_specifications_v1.md)
## Hardware Implementations
Verilog HDL is used in this project. This project will try to construct the simplest CPU ever in the world with the lowest gate count.
## Simulators, Assemblers and Compilers
This project will include a behavior simulator written in python. Assemblers and Compilers will not be provided soon since this ISA is toxic.

