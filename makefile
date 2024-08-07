# Define the name of the virtual environment
VENV := .venv

# Define the path to the requirements file
REQUIREMENTS := requirements.txt

# Define the Python command to create the virtual environment
PYTHON := python

# Create the virtual environment and install requirements
.PHONY: all setup venv install clean

all: setup

setup: venv install

venv:
	$(PYTHON) -m venv $(VENV)

install: venv
	$(VENV)/bin/pip install -r $(REQUIREMENTS)

# Clean up the virtual environment
clean:
	rm -rf $(VENV)

# Provide a help target to display available commands
help:
	@echo "Usage:"
	@echo "  make          Create virtual environment and install requirements"
	@echo "  make setup    Same as 'make'"
	@echo "  make venv     Create virtual environment"
	@echo "  make install  Install requirements"
	@echo "  make clean    Remove virtual environment"
	@echo "  make help     Show this help message"

