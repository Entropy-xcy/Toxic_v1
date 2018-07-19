# Toxic ISA Specifications 
## Features
Each instruction is equal in length(4 bits) and the length of opcode may vary from 2 bits to 4 bits.
## Registers:
R0: General register and Content register (See memory operation)
R1: General register and Address register (See memory operation)
## ISA
#### identifiers
i: instruction opcode
d: destination register
f: function
m: immediate number
***
#### ADD (with immediate number)
##### Format: 00dm
opcode(00)/destination register(d)/immediate number(m)
##### Description 
if 3rd bit is 0 then this instruction means R0 = R1 + m
if 3rd bit is 1 then means R1 = R0 + m
the 4th bit is the immediate number which is m.
##### Example: 0000
R0 = R1 + 0; (We can implement MOV use this instruction)
***
#### ADD (without immediate number)
##### Format: 0100
opcode(0100)
##### Description and example
R0 = R1 + R0;
***
#### NAND
##### Format: 0101
opcode(0101)
##### Description and example
R0 = R1 NAND R0;
***
#### LD&ST (Load and Store)
##### Format: 011f
opcode(011)/function(f)
##### Description
Store the content in R0 at address R1 if the 4th bit is 1
Read the content at address R1 to R0 if the 4th bit is 0
##### Example: 0110
R0 = Mem[R1];
##### Example: 0111
Mem[R1] = R0;
***
#### JMP
##### Format: 10ff

