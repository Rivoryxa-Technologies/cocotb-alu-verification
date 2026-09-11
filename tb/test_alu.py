# test_alu.py - cocotb testbench for the ALU.
import random

import cocotb
from cocotb.triggers import Timer

WIDTH = 32
MASK = (1 << WIDTH) - 1


def to_signed(v):
    return v - (1 << WIDTH) if v & (1 << (WIDTH - 1)) else v


# Reference model: opcode -> expected result (masked to WIDTH bits).
OPS = {
    0: lambda a, b: (a + b) & MASK,
    1: lambda a, b: (a - b) & MASK,
    2: lambda a, b: a & b,
    3: lambda a, b: a | b,
    4: lambda a, b: a ^ b,
    5: lambda a, b: (a << (b & 0x1F)) & MASK,
    6: lambda a, b: (a >> (b & 0x1F)) & MASK,
    7: lambda a, b: 1 if to_signed(a) < to_signed(b) else 0,
}


async def apply(dut, a, b, op):
    dut.a.value = a
    dut.b.value = b
    dut.op.value = op
    await Timer(1, unit="ns")


@cocotb.test()
async def test_directed(dut):
    """Directed corner cases."""
    cases = [
        (0, 0, 0), (MASK, 1, 0), (0, 1, 1),
        (0xFF, 0x0F, 2), (0xF0, 0x0F, 3), (0xAA, 0xFF, 4),
    ]
    for a, b, op in cases:
        await apply(dut, a, b, op)
        exp = OPS[op](a, b)
        got = int(dut.y.value)
        assert got == exp, \
            f"op={op} a={a:#x} b={b:#x} got={got:#x} exp={exp:#x}"


@cocotb.test()
async def test_random(dut):
    """Constrained-random stimulus with a simple functional-coverage tally."""
    cov = {op: 0 for op in OPS}
    for _ in range(2000):
        a = random.getrandbits(WIDTH)
        b = random.getrandbits(WIDTH)
        op = random.randint(0, 7)
        await apply(dut, a, b, op)
        exp = OPS[op](a, b)
        got = int(dut.y.value)
        assert got == exp, \
            f"op={op} a={a:#x} b={b:#x} got={got:#x} exp={exp:#x}"
        cov[op] += 1

    dut._log.info("Functional coverage (ops exercised): %s", cov)
    assert all(v > 0 for v in cov.values()), "not every opcode was covered"
