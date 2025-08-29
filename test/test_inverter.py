# tests/test_inverter.py
import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, Timer
import random

@cocotb.test()
async def basic_invert(dut):
    # If your top is TinyTapeout-style, you likely have:
    # clk, rst_n, ena, ui_in[7:0], uo_out[7:0], uio_in/out/oe
    cocotb.start_soon(Clock(dut.clk, 10, units="ns").start())

    # Reset (active low typical)
    dut.rst_n.value = 0
    dut.ena.value = 1
    dut.ui_in.value = 0
    await Timer(50, units="ns")
    dut.rst_n.value = 1

    # Drive a few inputs and check outputs
    for _ in range(8):
        val = random.randint(0, 255)
        dut.ui_in.value = val
        await RisingEdge(dut.clk)
        # Example: if your design outputs ~val (inverted), tweak to your logic
        expected = (~val) & 0xFF
        assert int(dut.uo_out.value) == expected, f"Expected {expected:#04x}, got {int(dut.uo_out.value):#04x}"
