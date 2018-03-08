.DEFAULT_GOAL := default

default:
	@echo 'error: No target was specified.'

devenv:
	@rm -rf venv;
	@virtualenv -p python3 venv; \
	source ./venv/bin/activate; \
	pip install -r requirements-dev.txt; \

dockertest:
	@docker build . -t flaskfirehose; \
		printf '\n'; \
		printf ' ---> Please visit: https://localhost:8443/\n'; \
		printf ' ---> with your favourite browser to test.\n'; \
		printf ' ---> Press Ctrl+C to stop the server.\n'
	@docker run --rm -it -p 8443:443 flaskfirehose > /dev/null || true

scrub:
	@find . -regex "\(.*__pycache__.*\|*.py[co]\)" -delete; \
	rm -rf Flask_Firehose.egg-info; \

test:
	@source ./venv/bin/activate; \
	pytest

updatechk:
	@source ./venv/bin/activate; \
	pip list --outdated --format=columns; \

.PHONY: default devenv dockertest scrub test updatechk
