VENV_NAME = .venv

.PHONY: init run clean

init:
	python3 -m venv $(VENV_NAME)
	. $(VENV_NAME)/bin/activate && pip install --upgrade pip && pip install -r requirements.txt

run:
	. $(VENV_NAME)/bin/activate && jupyter notebook notebooks/

clean:
	rm -rf $(VENV_NAME)