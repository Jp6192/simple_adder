The simple_adder module is an 8-bit synchronous adder implemented in Verilog RTL. It accepts two 8-bit input operands and produces their sum as an 8-bit output. The operation is clock-driven: the sum is updated on the rising edge of the clock and stored in a register. Because the operands and output are 8 bits wide, the addition is performed modulo 2⁸, so any carry beyond bit 7 is discarded.

This design is useful as a training/teaching example of:

Synchronous (clocked) logic

Registered outputs

Simple arithmetic in RTL

Simple Adder RTL Design

To understand the behavior of the simple_adder block, the following signals are involved:

Clock signal (clk)

8-bit input operand A (a)

8-bit input operand B (b)

8-bit registered output sum (sum)

The behavior can be summarized by the equation evaluated at every positive edge of clk:

sum = (a+b) mod 2^8

a : 8-bit input operand A

b : 8-bit input operand B

sum_next : Value loaded into sum on the next rising edge of clk

The output sum holds its previous value between clock edges.

Clock-Controlled Process

The adder is controlled purely by the clock, without any explicit FSM. The operation proceeds as follows:

On every rising edge of clk:

The current values of a and b are sampled.

An 8-bit addition a + b is performed.

The result (lower 8 bits) is stored in the register sum.

Key points for RTL/training:

The block is synchronous:

Input changes do not immediately change sum.

sum changes only at posedge clk.

The combinational logic (the adder) sits before the register:

Inputs a and b → Combinational adder → sum register.

There is one clock-cycle latency from applying inputs to observing the updated sum.

Data Width and Modulo Behavior

Data width of inputs: 8 bits (a[7:0], b[7:0])

Data width of output: 8 bits (sum[7:0])

Arithmetic is modulo 2^8 = 256

This means:

    sum=(a+b)mod256

If the true arithmetic sum exceeds 255, only the lower 8 bits are kept and the carry-out is discarded.

Example of modulo behavior:

True sum: 0xF0 + 0x30 = 0x120

Stored sum: 0x20 (lower 8 bits of 0x120)

