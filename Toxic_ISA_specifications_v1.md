# Toxic ISA Specifications 
## Features
Each instruction is equal in length(4 bits) and the length of opcode may vary from 2 bits to 4 bits. No hardware stack control!
## Registers:
R0: General register and Content register (See memory operation) <br>
R1: General register and Address register (See memory operation)
## RAM
in total 8 bits of addressing capability controlled by a page register (Not accessible in arithmetic operations) and R1. Each address(page+R1) corresponds to half byte (4 bits) of data.
## ISA
#### identifiers
i: instruction opcode <br>
d: destination register <br>
f: function <br>
m: immediate number
***
#### ADD (with immediate number)
##### Format: 00dm
opcode(00)/destination register(d)/immediate number(m)
##### Description 
if 3rd bit is 0 then this instruction means R0 = R1 + m <br>
if 3rd bit is 1 then means R1 = R0 + m <br>
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
##### Description and Example (0101):
R0 = R1 NAND R0;
***
#### LD&ST (Load and Store)
##### Format: 011f
opcode(011)/function(f)
##### Description
Store the content in R0 at address R1 if the 4th bit is 1 <br>
Read the content at address R1 to R0 if the 4th bit is 0
##### Example: 0110
R0 = Mem[R1];
##### Example: 0111
Mem[R1] = R0;
***
#### JMP
##### Format: 10ff
opcode(10)/function(ff)
##### Description
for the following case of ff <br>
ff==00: jump to R1 if R0 is postive <br>
ff==01: jump to R1 if R0 is zero <br>
ff==10: jump to R1 if R0 is negative <br>
##### Example: 1001
Jump to R1 if R0 is zero
***
#### NOP
##### Format: 1011
##### Description and Example (1011):
Do nothing for this cycle.
***
#### STP (Set Page)
##### Fotmat: 1100
##### Description and Example (1100):
Set the page register of RAM to R1
***
#### GTP(Get Page)
##### Format:1101
##### Description and Example (1101):
Get the current page number to R1
***
#### TRAP(111m)
Reserved
