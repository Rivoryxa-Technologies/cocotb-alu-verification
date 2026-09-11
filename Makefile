# cocotb + Icarus Verilog run flow.
# Usage: make            (run with Icarus)
#        make SIM=verilator
TOPLEVEL_LANG = verilog
SIM ?= icarus

VERILOG_SOURCES = $(PWD)/rtl/alu.v
TOPLEVEL = alu
MODULE = test_alu

export PYTHONPATH := $(PWD)/tb:$(PYTHONPATH)

include $(shell cocotb-config --makefiles)/Makefile.sim
