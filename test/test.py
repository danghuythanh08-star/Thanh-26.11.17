import cocotb
from cocotb.clock import Clock
from cocotb.triggers import FallingEdge


@cocotb.test()
async def test_project(dut):
    dut._log.info("Bat dau kiem tra chip dem so")

    clock = Clock(dut.clk, 10, "us")
    cocotb.start_soon(clock.start())

    # Bam reset, tat cong tac dem
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    for _ in range(5):
        await FallingEdge(dut.clk)

    # Tha reset -> chip phai o so 0
    dut.rst_n.value = 1
    await FallingEdge(dut.clk)
    assert int(dut.uo_out.value) == 0

    # Bat cong tac dem, cho 10 tieng tich -> phai ra so 10
    dut.ui_in.value = 1
    for _ in range(10):
        await FallingEdge(dut.clk)
    assert int(dut.uo_out.value) == 10

    # Tat cong tac -> chip phai dung yen o so 10
    dut.ui_in.value = 0
    for _ in range(5):
        await FallingEdge(dut.clk)
    assert int(dut.uo_out.value) == 10

    dut._log.info("Chip dem dung!")
