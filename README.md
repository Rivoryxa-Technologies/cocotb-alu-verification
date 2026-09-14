# cocotb-alu-verification

A small, fully runnable verification example: a directed and constrained random
testbench for a 32-bit ALU, written in Python with
[cocotb](https://www.cocotb.org/) and running on free, open source simulators
(Icarus Verilog or Verilator). No commercial license required.

It shows the shape of a real verification effort in miniature: a reference
model, directed corner cases, constrained random stimulus, self checking, and a
functional coverage tally that fails if any opcode was never exercised.

> **Verified:** passes on cocotb 2.x with Icarus Verilog (`make`): 2 tests, 0 failures.

## Layout

```
rtl/alu.v       ALU under test (add, sub, and, or, xor, sll, srl, slt)
tb/test_alu.py  cocotb tests: directed + constrained random + coverage
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
reference model checking, coverage driven stimulus, and a signoff you can
reproduce.

## What Rivoryxa delivers with this

This is our public reference flow for Python based verification. For clients, the block, reference model, stimulus, coverage and simulator are agreed as part of a scoped verification task. This example demonstrates an ALU simulation testbench; it contains no ACT4 or RISC-V core compliance flow.

See the [Rivoryxa profile](https://github.com/Rivoryxa-Technologies) for our full service list, or reach us on [LinkedIn](https://www.linkedin.com/company/rivoryxa-technologies/).

## Rechecked scope, 15 September 2026

A clean build with Python 3.12.12, cocotb 2.1.0 and Homebrew Icarus 13.0 on
macOS arm64 passed both tests:

```bash
make SIM_BUILD=/tmp/alu-clean COCOTB_RESULTS_FILE=/tmp/alu-clean.xml
```

Use a new build directory when changing simulator versions. Reusing an OSS CAD
Suite Icarus 14 build with Icarus 13 caused a runtime-format error in this audit;
the OSS wrapper also conflicted with the virtualenv's Python runtime. Neither
is an RTL failure. The eight operation counts are not exhaustive cross coverage
or proof over all operand combinations.

The raw output is in `evidence/audit-2026-09-15.log`.
