`default_nettype none

module tt_um_example (
    input  wire [7:0] ui_in,
    output wire [7:0] uo_out,
    input  wire [7:0] uio_in,
    output wire [7:0] uio_out,
    output wire [7:0] uio_oe,
    input  wire       ena,
    input  wire       clk,
    input  wire       rst_n
);
    reg [7:0] cnt;

    always @(posedge clk) begin
        if (!rst_n)        cnt <= 8'd0;
        else if (ui_in[0]) cnt <= cnt + 1'b1;
    end

    assign uo_out  = cnt;
    assign uio_out = 8'b0;
    assign uio_oe  = 8'b0;

    wire _unused = &{ena, uio_in, ui_in[7:1], 1'b0};
endmodule
