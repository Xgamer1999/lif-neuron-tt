# defaults
SIM ?= icarus
TOPLEVEL_LANG ?= verilog
SRC_DIR := $(PWD)/../src

# >>> Only your RTL files here (no duplicates, no old top)
PROJECT_SOURCES = \
  LIF_Accumulator.v \
  LIF_neuron_FSM.v \
  top_lvl.v /
  tt_um_Xgamer1999_LIF.v /
  LIF_neuron.v

# RTL simulation
SIM_BUILD := sim_build/rtl
VERILOG_SOURCES := $(addprefix $(SRC_DIR)/,$(PROJECT_SOURCES))

# Gate-level simulation (DO NOT add your RTL here)
GATES ?= no
ifeq ($(GATES),yes)
  SIM_BUILD := sim_build/gl
  COMPILE_ARGS += -DGL_TEST
  COMPILE_ARGS += -DFUNCTIONAL
  COMPILE_ARGS += -DSIM
  VERILOG_SOURCES += $(PDK_ROOT)/ihp-sg13g2/libs.ref/sg13g2_io/verilog/sg13g2_io.v
  VERILOG_SOURCES += $(PDK_ROOT)/ihp-sg13g2/libs.ref/sg13g2_stdcell/verilog/sg13g2_stdcell.v
endif

# Include the testbench sources
TOPLEVEL = tt_um_top_lvl
MODULE   = test

include $(shell cocotb-config --makefiles)/Makefile.sim
