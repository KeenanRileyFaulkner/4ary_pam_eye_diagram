IN_ENV = if [ -e .venv/bin/activate ]; then . .venv/bin/activate; fi;
PYTHON311 := $(shell which python3.11)
PYTHON312 := $(shell which python3.12)

install: venv python_packages activate

venv:
ifneq "$(PYTHON312)" ""
	python3.12 -m venv .venv
else ifneq "$(PYTHON311)" ""
	python3.11 -m venv .venv
else
	python3.10 -m venv .venv
endif

python_packages:
	$(IN_ENV) python -m pip install -r requirements.txt