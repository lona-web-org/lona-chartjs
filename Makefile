SHELL=/bin/bash
PYTHON=python3

PYTHON_ENV_ROOT=envs
PYTHON_DEV_ENV=$(PYTHON_ENV_ROOT)/$(PYTHON)-dev
PYTHON_PACKAGING_ENV=$(PYTHON_ENV_ROOT)/$(PYTHON)-packaging-env

.PHONY: clean doc sdist test ci-test shell freeze

# development environment #####################################################
$(PYTHON_DEV_ENV)/.created: REQUIREMENTS.dev.txt
	rm -rf $(PYTHON_DEV_ENV) && \
	$(PYTHON) -m venv $(PYTHON_DEV_ENV) && \
	. $(PYTHON_DEV_ENV)/bin/activate && \
	pip install pip --upgrade && \
	pip install -r ./REQUIREMENTS.dev.txt && \
	date > $(PYTHON_DEV_ENV)/.created

dev-env: $(PYTHON_DEV_ENV)/.created

# packaging environment #######################################################
$(PYTHON_PACKAGING_ENV)/.created: REQUIREMENTS.packaging.txt
	rm -rf $(PYTHON_PACKAGING_ENV) && \
	$(PYTHON) -m venv $(PYTHON_PACKAGING_ENV) && \
	. $(PYTHON_PACKAGING_ENV)/bin/activate && \
	pip install --upgrade pip && \
	pip install -r REQUIREMENTS.packaging.txt
	date > $(PYTHON_PACKAGING_ENV)/.created

packaging-env: $(PYTHON_PACKAGING_ENV)/.created

# environment helper ##########################################################
clean:
	rm -rf $(PYTHON_ENV_ROOT)

shell: dev-env
	. $(PYTHON_DEV_ENV)/bin/activate && \
	rlpython

freeze: dev-env
	. $(PYTHON_DEV_ENV)/bin/activate && \
	pip freeze

# server ######################################################################
server: dev-env
	. $(PYTHON_DEV_ENV)/bin/activate && \
	python test_script.py

# packaging ###################################################################
sdist: packaging-env
	. $(PYTHON_PACKAGING_ENV)/bin/activate && \
	rm -rf dist *.egg-info && \
	./setup.py sdist

_release: sdist
	. $(PYTHON_PACKAGING_ENV)/bin/activate && \
	twine upload --config-file ~/.pypirc.fscherf dist/*
