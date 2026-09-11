// alu.v - simple 8-function ALU used as the DUT for the cocotb testbench.
module alu #(
  parameter WIDTH = 32
)(
  input  wire [WIDTH-1:0] a,
  input  wire [WIDTH-1:0] b,
  input  wire [2:0]       op,
  output reg  [WIDTH-1:0] y,
  output wire             zero
);
  localparam OP_ADD = 3'd0;
  localparam OP_SUB = 3'd1;
  localparam OP_AND = 3'd2;
  localparam OP_OR  = 3'd3;
  localparam OP_XOR = 3'd4;
  localparam OP_SLL = 3'd5;
  localparam OP_SRL = 3'd6;
  localparam OP_SLT = 3'd7;

  always @(*) begin
    case (op)
      OP_ADD: y = a + b;
      OP_SUB: y = a - b;
      OP_AND: y = a & b;
      OP_OR : y = a | b;
      OP_XOR: y = a ^ b;
      OP_SLL: y = a << b[4:0];
      OP_SRL: y = a >> b[4:0];
      OP_SLT: y = ($signed(a) < $signed(b)) ? {{(WIDTH-1){1'b0}}, 1'b1}
                                            : {WIDTH{1'b0}};
      default: y = {WIDTH{1'b0}};
    endcase
  end

  assign zero = (y == {WIDTH{1'b0}});
endmodule
