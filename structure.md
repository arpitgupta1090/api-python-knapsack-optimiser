## Code Structure

---

The main working directory of this code base contains following files/packages:

1. 'service' package which contains most of the python code.
2. 'Dockerfile' : defines the steps to create docker image of the application.
3. 'docker-compose.yml' : contains steps to run the application on Docker.
4. 'requirements.txt' : contains list of all the libraries/packages to be installed the docker image.
5. 'README.md' and 'structure.md' : markdown files which contain details of the project/application.
6. 'openapi.json': OpenAPI specification for the application.

---

### Service Package

Service package contains following packages/modules:

1. 'api': contains 'api_router' where the endpoint is defined.
2. 'core': contains module where knapsack solver model/code is defined.
3. 'coverage_report': is generated when you run the unit test command. Please open 'index.html' for details test-case/coverage report.
4. 'exceptions':
   1. 'exception' module: defines the validators that apply on the request body.
   2. 'formater' module: defines different exception formats to be used by validators.
5. 'logger': defines the logger for the application.
6. 'mapper': defines a module to convert optimiser/solver output in response body json format.
7. 'openapi': defines OpenAPI specification for request and response body.
8. 'schema': defines model schema for request and response body.
9. 'tests':
   1. 'test_api': test cases for testing the API.
   2. 'test_core': test cases for testing the solver/optimiser.
10. 'error.log': logs when a internal error in generated.
11. 'main.py': main module where FastAPI app is defined.
