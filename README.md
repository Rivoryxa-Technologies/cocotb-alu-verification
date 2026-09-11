# cocotb-alu-verification

A small, fully runnable verification example: a directed and constrained-random
testbench for a 32-bit ALU, written in Python with
[cocotb](https://www.cocotb.org/) and running on free, open-source simulators
(Icarus Verilog or Verilator). No commercial license required.

It shows the shape of a real verification effort in miniature: a reference
model, directed corner cases, constrained-random stimulus, self-checking, and a
functional-coverage tally that fails if any opcode was never exercised.

> **Verified:** passes on cocotb 2.x with Icarus Verilog (`make`): 2 tests, 0 failures.

## Layout

```
rtl/alu.v       ALU under test (add, sub, and, or, xor, sll, srl, slt)
tb/test_alu.py  cocotb tests: directed + constrained-random + coverage
Makefile        cocotb / Icarus run flow
```

## Run it

```bash
pip install cocotb
sudo apt-get install iverilog   # or: brew install icarus-verilog
make
```

You should see both tests pass and a line reporting how many times each opcode
was exercised.

## Why this exists

It is a compact demonstration of the approach we bring to larger designs:
reference-model checking, coverage-driven stimulus, and a signoff you can
reproduce. For production work we scale this up with SystemVerilog and UVM,
formal properties, and coverage closure.

---
Maintained by [Rivoryxa Technologies](https://www.linkedin.com/company/rivoryxa-technologies/).
