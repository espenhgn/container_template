# container_template project

README info goes here. Modify for your own project's needs.

# Important! - Set up Git LFS

Container files may get large and one should never add large binary files (.sif, .zip, .tar.gz, .mat, .dat, etc.) in [git](https://git-scm.com) repositories directly, mainly files that can be parsed as raw text files (code files, etc.)
[**Git Large File Storage** (LFS)](https://git-lfs.github.com) should be used instead. 
Before adding new files to this project, go through step 1-3 on the Git LFS [homepage](https://git-lfs.github.com). 
Revise the `<container_template>/.gitattributes` file as necessary. Some common file formats has been added already.

## Description of available containers

* ``container_template`` - a hello-world introductory container setup

## Software versions

Below is the list of tools included in the different Dockerfile(s) and installer bash scripts for each container.
Please keep up to date (and update the main `<container_template>/README.md` when pushing new container builds):
  
  | container               | OS/tool             | version
  | ----------------------- | ------------------- | ----------------------------------------
  | container_template.sif  | ubuntu              | 20.04
  | container_template.sif  | python3             | python 3.10.6

## Building/rebuilding containers

For instructions on how to build or rebuild containers using [Docker](https://www.docker.com) and [Singularity](https://docs.sylabs.io) refer to [`<container_template>/src/README.md`](https://github.com/espenhgn/container_template/blob/main/src/README.md).

## Feedback

If you face any issues, or if you need additional software, please let us know by creating a new [issue](https://github.com/espenhgn/container_template/issues/new).
