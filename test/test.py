import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge

@cocotb.test()
async def test_project(dut):
    cocotb.start_soon(Clock(dut.clk, 10, units="ns").start())

    # enable tile + reset
    dut.ena.value   = 1
    dut.rst_n.value = 0
    dut.ui_in.value = 0
    await RisingEdge(dut.clk)
    await RisingEdge(dut.clk)
    dut.rst_n.value = 1

    # pulse ui_in[0] (this feeds your core's signal_in via the wrapper)
    for _ in range(8):
        dut.ui_in[0].value = 1
        await RisingEdge(dut.clk)
        dut.ui_in[0].value = 0
        await RisingEdge(dut.clk)

    # sanity: wrapper output bit is defined
    assert dut.uo_out[0].value.is_resolvable, "uo_out[0] is X/Z"

