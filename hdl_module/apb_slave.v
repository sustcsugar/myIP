// **********************************************************
// * Author : SHI Gang
// * Email : 1144392179@qq.com
// * Create time : 2023-03-16 14:57:23
// * Last modified :2023-03-16 14:57:23
// *
// * Filename : apb_slave.v
// * Description : generate by chatGPT (2023-03-16 14:57:44). No verification.
// * Copyright (c) : AnLab 2021. All rights reserved.
// **********************************************************


module apb_slave (
  input              pclk,
  input              presetn,

  input              psel,
  input              penable,
  input              pwrite,
  input  [31:0]      paddr,
  input  [31:0]      pwdata,
  output [31:0]      prdata
);

  // define registers
  reg [31:0] register1;
  reg [31:0] register2;
  // add more registers as needed

  // read operation
  always @(posedge pclk) begin
    if (presetn == 1'b0) begin // reset
      register1 <= 32'h0;
      register2 <= 32'h0;
      // reset other registers as needed
    end else if (psel == 1'b1 && penable == 1'b1 && pwrite == 1'b0) begin // read operation
      case(paddr[7:2])
        6'b000001: prdata <= register1; // read from register1
        6'b000010: prdata <= register2; // read from register2
        // add more cases for other registers
        default: prdata <= 32'h0; // invalid address
      endcase
    end
  end

  // write operation
  always @(posedge pclk) begin
    if (presetn == 1'b0) begin // reset
      register1 <= 32'h0;
      register2 <= 32'h0;
      // reset other registers as needed
    end else if (psel == 1'b1 && penable == 1'b1 && pwrite == 1'b1) begin // write operation
      case(paddr[7:2])
        6'b000001: register1 <= pwdata; // write to register1
        6'b000010: register2 <= pwdata; // write to register2
        // add more cases for other registers
        default: ; // invalid address
      endcase
    end
  end

endmodule
