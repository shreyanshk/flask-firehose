.DEFAULT_GOAL := default

default:
	@echo 'error: No target was specified.'

devenv:
	@rm -rf venv;
	@virtualenv -p python3 venv; \
	source ./venv/bin/activate; \
	pip install -r requirements-dev.txt; \

scrub:
	@find . -regex "\(.*__pycache__.*\|*.py[co]\)" -delete; \
	rm -rf Flask_Firehose.egg-info; \

test:
	@source ./venv/bin/activate; \
	pytest

updatechk:
	@source ./venv/bin/activate; \
	pip list --outdated --format=columns; \

.PHONY: default devenv scrub test updatechk
