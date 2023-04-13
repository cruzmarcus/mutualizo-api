# Mutualizo API

## 1. Concept 
This project was conceptualized based on the Mutualizo test.

## 2. Development

### 2.1 Getting Started
The service uses python version 3.10.

To create a development environment.
```bash
make create-dev-env
```

Another option to run the application is with the docker.
```bash
make run-container-api
```

To clean up the container application.
```bash
make cleanup-container
```

### 2.2 Running Tests
You must set up your local environment for e2e and integration tests.

```bash
make setup
make run-tests
make cleanup
```


### 2.3 Tests Coverage

To see the test coverage of the project, do the command below. This will show the coverage for *src* directory and the percentage coverage for each module inside the src.

To generate coverage for an _xml_ file, do the command below. With this *xml* test coverage file, it is possible to use an extension on VSCode to see the coverage in lines for each file. 
The extension 'Coverage Gutters' provides support for this functionality.

```bash
make generate-tests-coverage-src
```

The project has test coverage equal 100 % in the current version.

### 2.4 Poetry Troubleshooting
If there is a poetry in the local machine and had a problem finding the Dynamox packages when recreating a development environment or updating some package. Here is a step-by-step to solve this problem.

Uninstall the current poetry.
```bash
make poetry-uninstall
```

Removing poetry config in the cache.
```bash
cd ~/.config/pypoetry && rm poetry.lock pyproject.toml
```

Creating the project development environment again.
```bash
create-dev-env
```
