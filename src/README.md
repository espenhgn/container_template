# Source files

## Singularity containers

This repository is used to develop and document [Singularity](https://docs.sylabs.io/guides/3.5/user-guide/index.html#) containers with various software and analytical tools.

## Software versions

  Below is the list of tools included in the different Dockerfiles and installer bash scripts for each container.
  Please keep up to date (and update the main `<container_template>/README.md` when pushing new container builds):
  
  | container               | OS/tool             | version
  | ------------------------| ------------------- | ----------------------------------------
  | container_template.sif  | ubuntu              | 20.04
  | container_template.sif  | python              | 3.8.10

## Feedback

If you face any issues, or if you need additional software, please let us know by creating an [issue](https://github.com/espenhgn/container_template/issues/new).

## Build instructions

## Testing container builds

Some basic checks for the functionality of the different container builds are provided in `<container_template>/tests/`, implemented in Python.
The tests can be executed using the [Pytest](https://docs.pytest.org) testing framework. 

In case `singularity` is not found in `PATH`, tests will fall back to `docker`. 
In case `docker` is not found, no tests will run.

To install Pytest in the current Python environment, issue:

```
pip install pytest  # --user optional
```

New virtual environment using [conda](https://docs.conda.io/en/latest/index.html):

```
conda create -n pytest python=3 pytest -y  # creates env "pytest"
conda activate pytest  # activates env "pytest"
```

Then, all checks can be executed by issuing:

```
cd <container_template>
py.test -v tests  # with verbose output
```

Checks for individual containers (e.g., `container_template.sif`) can be executed by issuing:

```
py.test -v tests/test_container_template.py
```

Note that the proper container files (*.sif files) corresponding to the different test scripts must exist in `<container_template>/containers/`,
not only git LFS pointer files.
