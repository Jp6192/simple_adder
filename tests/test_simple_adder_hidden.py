import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge

@cocotb.test()
async def test_addition(dut):
    clock = Clock(dut.clk, 10, units="ns")
    cocotb.start_soon(clock.start())

    # simple stimulus
    await RisingEdge(dut.clk)
    dut.a.value = 5
    dut.b.value = 3
    await RisingEdge(dut.clk)
    await RisingEdge(dut.clk)
    assert dut.sum.value == 8, f"Expected 8, got {dut.sum.value}"

# Pytest wrapper (required by HUD guide)
def test_simple_adder_hidden_runner():
    import os
    from pathlib import Path
    from cocotb_tools.runner import get_runner

    sim = os.getenv("SIM", "icarus")
    proj_path = Path(__file__).resolve().parent.parent

    # Use sources/ (HUD format)
    sources = [proj_path / "sources/adder.sv"]

    runner = get_runner(sim)
    runner.build(
        sources=sources,
        hdl_toplevel="simple_adder",
        always=True,
    )
    runner.test(
        hdl_toplevel="simple_adder",
        test_module="test_simple_adder_hidden",
    )
