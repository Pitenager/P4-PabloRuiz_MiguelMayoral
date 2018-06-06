test:
	sh -c '. venv/bin/activate; nosetests project/analyzerapp/tests/*.py'
    
coverage: 
    sh -c '. venv/bin/activate; nosetests project/analyzerapp/tests/*.py --with-coverage'

bootstrap: venv
	venv/bin/pip install -e .
ifneq ($(wildcard requirements.txt),)
	venv/bin/pip install -r requirements.txt
endif

venv:
	python3 -m venv venv
	venv/bin/pip install --upgrade pip
	venv/bin/pip install --upgrade setuptools
