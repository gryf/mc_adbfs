# simple makefile for running tests for the adbfs plugin

all: test_dir py3 flake8

TEST_DIR='.test'
PY3_VENV=$(TEST_DIR)/py3
FL8_VENV=$(TEST_DIR)/flake8
TST_EXISTS=$(shell [ -e $(TEST_DIR) ] && echo 1 || echo 0)
PY3_EXISTS=$(shell [ -e $(PY3_VENV) ] && echo 1 || echo 0)
FL8_EXISTS=$(shell [ -e $(FL8_VENV) ] && echo 1 || echo 0)

py3: test_dir virtualenv3
	.test/py3/bin/python test_adbfs.py

flake8: test_dir virtualenv_flake8
	.test/flake8/bin/flake8 adbfs test_adbfs.py

ifeq ($(TST_EXISTS), 0)
test_dir:
	mkdir -p .test
else
test_dir:
endif

ifeq ($(PY3_EXISTS), 0)
virtualenv3:
	virtualenv -p python3 $(PY3_VENV)
	$(PY3_VENV)/bin/pip install six
else
virtualenv3:
endif

ifeq ($(FL8_EXISTS), 0)
virtualenv_flake8:
	virtualenv -p python3 $(FL8_VENV)
	$(FL8_VENV)/bin/pip install flake8
else
virtualenv_flake8:
endif

clean:
	rm -fr $(TEST_DIR) __pycache__ adbfsc
