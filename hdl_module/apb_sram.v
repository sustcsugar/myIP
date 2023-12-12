//------------------------------------------------------------------------------
// File                     : apb_sram.v
// Author                   : FFQ
// Key Words                :
// Modification History     :
//      Date        By        Version        Change Description
//      2022-04-14  FFQ       1.0            original
//
// Editor                   : VSCode, Tab Size(4)
// Description              : Simple APB Sram.
// Source                   :https://zhuanlan.zhihu.com/p/498327411
//
//------------------------------------------------------------------------------
`timescale 1ns / 1ps

module apb_sram #(
    parameter                           SIZE_IN_BYTES = 1024
)
(
    //----------------------------------
    // IO Declarations
    //----------------------------------
    input                               PRESETn,
    input                               PCLK,
    input                               PSEL,
    input [31:0]                        PADDR,
    input                               PENABLE,
    input                               PWRITE,
    input [31:0]                        PWDATA,
    output reg [31:0]                   PRDATA
);

    //----------------------------------
    // Local Parameter Declarations
    //----------------------------------
    localparam                          A_WIDTH = clogb2(SIZE_IN_BYTES);

    //----------------------------------
    // Variable Declarations
    //----------------------------------
    reg [31:0]                          mem[0:SIZE_IN_BYTES/4-1];
    wire                                wren;
    wire                                rden;
    wire [A_WIDTH-1:2]                  addr; 
 
    //----------------------------------
    // Function Declarations
    //----------------------------------
    function integer clogb2;
        input [31:0]                    value; 
        reg [31:0]                      tmp; 
        reg [31:0]                      rt;
    begin
        tmp = value - 1;
        for (rt = 0; tmp > 0; rt = rt + 1) 
            tmp = tmp >> 1;
        clogb2 = rt;
    end
    endfunction

    //----------------------------------
    // Start of Main Code
    //----------------------------------
    // Create read and write enable signals using APB control signals
    assign wren = PWRITE && PENABLE && PSEL; // Enable Period
    assign rden = ~PWRITE && ~PENABLE && PSEL; // Setup Period

    assign addr = PADDR[A_WIDTH-1:2];
    
    // Write mem
    always @(posedge PCLK)
    begin
        if (wren)
            mem[addr] <= PWDATA;
    end

    // Read mem
    always @(posedge PCLK)
    begin
        if (rden)
            PRDATA <= mem[addr];
        else
            PRDATA <= 'h0;
    end

endmodule