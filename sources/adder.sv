`timescale 1ns/1ps

module simple_adder (
    input wire clk,
    input wire [7:0] a,
    input wire [7:0] b,
    output reg [7:0] sum
);
    // TODO: Implement addition logic

    always @(posedge clk) begin
        // 8-bit synchronous adder, modulo 256
       sum <= a + b;
       
    end

endmodule