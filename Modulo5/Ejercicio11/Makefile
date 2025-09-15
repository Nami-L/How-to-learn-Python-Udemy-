SHELL := /bin/bash
# =============================== VARIABLES =================================
# Miscellaneous variables
CUR_DATE := $(shell date +%Y-%m-%d_%H-%M-%S)

# Guardar la fecha para cada simulacion
# := es una variable que no va a acambiar

# Directories
GIT_DIR := $(shell git rev-parse --show-toplevel)#siempre tenemos el directorio root
PYTHON_FILE = $(shell find . -name "*.py")


.PHONY: all
all: help # Si detecta si ya compiló no necesita volver a compilar



# Colors
C_RED := \033[31m
C_GRE := \033[32m
C_BLU := \033[34m
C_YEL := \033[33m
C_ORA := \033[38;5;214m
NC    := \033[0m 

#______________________________________________________________________________
.PHONY: vars
vars: ## Print Makefile variables
	@echo ""
	@echo -e "$(C_ORA)Miscellaneous variables...$(NC)"
	@echo "CUR_DATE  = $(CUR_DATE)"
	@echo ""
	@echo -e "$(C_ORA)Directory variables...$(NC)"
	@echo "PYTHON_FILE = $(PYTHON_FILE)"
	@echo "GIT_DIR   = $(GIT_DIR)"
	@echo ""
	@echo -e "$(C_ORA)File Variables...$(NC)"
	@echo ""	

.PHONY: run
run: ## Correr pyhthon
	@echo -e "$(C_ORA)Compiling project$(NC)"
	python3 $(PYTHON_FILE)


#______________________________________________________________________________ 
# ================================ TARGETS ==================================

.PHONY: help
help: ## Displays help message
	@echo ""
	@echo "======================================================================"
	@echo ""
	@echo "Usage: make <target> <variables>"
	@echo ""
	@echo "--------------------------- Targets ----------------------------------"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | \
	awk 'BEGIN {FS = ":.*?## "}; {printf "- make \033[36m%-15s\033[0m %s\n", $$1, $$2}'
	@echo ""
	@echo "--------------------------- Variables -------------------------------"
	@echo ""