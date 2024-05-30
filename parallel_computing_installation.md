# Parallel Computing Course Installation Instructions
## Installing MPI

The *Message Passing Interface* (MPI) is a standard for passing messages between multiple networked processes running a parallel program. As MPI is a standard, rather than a piece of software, there is not a single software package that you need to install. There are a few different 'flavours' of MPI, and the majority of HPC systems will have their own versions which are tuned for their specific systems. It is highly recommended that you use a system's built-in MPI libraries if they are available, but if not let's go through the process of installing an MPI library.

> **Requirements**
> For this workshop you will need a multi-core machine which can run a unix-based terminal (i.e. Linux/WSL or Mac).

## MacOS installation
MPI can be easily installed with Homebrew. Check your machine has homebrew installed with
```
$ which brew
```
If this returns the location of the `brew` executable, then you can proceed with:
```
$ brew install open-mpi
```

## Linux/WSL installation
An easy way to install MPI on Linux or WSL platforms is using the Spack package manager (this can also be done for MacOS but requires some additional steps).

### Using Spack package manager (multi-platform)
In our case, we can install OpenMPI, which is a free and open source MPI implementation. OpenMPI can be installed in a number of different ways, but the recommended way is to use the Spack HPC package manager, which is in a class of its own in the way it handles different MPI implementations.

Spack is really simple to install, all you need to need to do is clone the Spack repository:
```
$ git clone --depth=100 --branch=releases/v0.21 https://github.com/spack/spack.git ~/spack
```
and `source` the included setup script:
```shell
$ source ~/spack/share/spack/setup-env.sh
```
Every time you want to use Spack you will need to `source` this script, so it may be easier to add this to your shell login script, (i.e. ~/.bashrc, ~/.zshrc, etc.).
We need to let Spack find any compilers in our system, which we can do with:
```
$ spack compiler find
```

### Installing MPI with spack
> **Note:**
> This method requires you to have a working set of compilers for C and Fortran. If you don't have these on your system the simplest way to get them is to [install the GNU compiler collection (GCC)](https://gcc.gnu.org/install).

We can use Spack to install an MPI library, which will default to installing OpenMPI. If we run
```
$ spack spec mpi
```
we can see what Spack will install, and we can use
```
$ spack install mpi
```
to execute the installation. Once this is done, we can load the new mpi module with
```
$ spack load mpi
```
and check the installation with
```
$ which mpirun
```
This command tells us where the `mpirun` command has been installed, which is the primary way that we can launch an executable across multiple process with MPI. With the installation complete we are ready to run some programs with MPI.

# Installing Python

Python is required for the first section of the course. If you do now have a working Python installation on your machine (you can check this with ```which python```), you can follow the [installation instructions from the CFRR Intro to Python course here](https://uniexeterrse.github.io/intro-to-python/setup.html).

## Installing Python with Spack

Alternatively, Python can be installed with Spack, using a similar method to the MPI spack installation above. We need to run:
```
$ spack spec python
```
to see which version is available to be installed by default. We can then use
```
$ spack install python
```
to execute the installation. Once this is done, we can load the new Python module with
```
$ spack load python
```
and check the installation with
```
$ which python
```