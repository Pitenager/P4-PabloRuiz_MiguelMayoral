# P4_FINAL_PabloRuiz_MiguelMayoral

Final Pratice for Verificación y Desarrollo (Continuous Integration)

## Python Version

The program was coded in Python 3.6, so run it in same version.

## How it works

You can install the dependencies using:

```bash
make bootstrap
```

You can get the coverage with:
```
make coverage
```

There are 2 different types of tests: TDD and BDD+Selenium.

You can execute the TDD test with:
```
make test
```

For the BDD tests, you can execute them using the following method once you are in folder /tests (/project/analyzerapp/tests):

```bash
aloe features/tests.feature
```
This is to run all the selenium + aloe test automatically.

You can execute the program using the next command from the directory where manage.py is located (P4_FINAL_PabloRuiz_MiguelMayoral/project/):

```bash
python manage.py runserver
```
And visiting http://localhost:8000/index/
