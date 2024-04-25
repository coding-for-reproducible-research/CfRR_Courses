# Loading software packages on HPC

## Questions
- How do we load and unload software packages?

## Objectives
- Load and use a software package.
- Explain how the shell environment changes when the module mechanism loads or unloads packages.

On a high-performance computing system, it is seldom the case that the software we want to use is available when we log in. It is installed, but we will need to “load” it before it can run.

Before we start using individual software packages, however, we should understand the reasoning behind this approach. The three biggest factors are:

+ software incompatibilities
+ versioning
+ dependencies

Software incompatibility is a major headache for programmers. Sometimes the presence (or absence) of a software package will break others that depend on it. Two of the most famous examples are Python 2 and 3 and C compiler versions. Python 3 famously provides a python command that conflicts with that provided by Python 2. Software compiled against a newer version of the C libraries and then used when they are not present will result in a nasty 'GLIBCXX_3.4.20' not found error, for instance.

Software versioning is another common issue. A team might depend on a certain package version for their research project - if the software version was to change (for instance, if a package was updated), it might affect their results. Having access to multiple software versions allow a set of researchers to prevent software versioning issues from affecting their results.

Dependencies are where a particular software package (or even a particular version) depends on having access to another software package (or even a particular version of another software package). For example, the VASP materials science software may depend on having a particular version of the FFTW (Fastest Fourier Transform in the West) software library available for it to work.

## Environment Modules

Environment modules are the solution to these problems. A module is a self-contained description of a software package – it contains the settings required to run a software package and, usually, encodes required dependencies on other software packages.

There are a number of different environment module implementations commonly used on HPC systems: the two most common are TCL modules and Lmod. Both of these use similar syntax and the concepts are the same so learning to use one will allow you to use whichever is installed on the system you are using. In both implementations the module command is used to interact with environment modules. An additional subcommand is usually added to the command to specify what you want to do. For a list of subcommands you can use module -h or module help. As for all commands, you can access the full help on the man pages with man module.

On login you may start out with a default set of modules loaded or you may start out with an empty environment; this depends on the setup of the system you are using. On ISCA you start with an empty environment.

## Listing Available Modules

To see available software modules, use `module avail`:

![](fig/module-avail.png)

This is will give you a very long list of all software, and all versions, available to load and use. You can scroll through this list to find what you need. You can restrict this list by providing the first few characters of the software you are insterested in e.g. `module avail Py`

## Listing Currently Loaded Modules

You can use the module list command to see which modules you currently have loaded in your environment. If you have no modules loaded, you will see a message telling you so

![](fig/module-list.png)

## Loading and Unloading Software

To load a software module, use `module load`. In this example we will load Python by typing `module load python`. Note that modules are case sensitive. 

In this instance we haven't specified a specific version so let's check which one we have loaded. We can do this is two ways.

First, we will use the command `python --version`, which is a python specific command that can be used on any UNIX system to find out which version of python is used by the command python. We can see in the image below that we have loaded Python3.9.

Second, we will use the command `module list`, which lists the specific name (and therefore version) of the software we installed. We can see in the image below, that our module load command has in fact loaded 12(!) modules including Python3.9.6. When you load a module it additionally installs any other modules on which it depends.

![](fig/module-python.png)

Let’s try unloading the python package with the command `module unload Python`. We can see in this case we have only removed the specific packages we stated in the command, the other 11 modules that were loaded at the same as dependencies are still loaded.

![](fig/module-unload.png)

If we wanted to unload everything at once, we could run `module purge` (unloads everything).

![](fig/module-purge.png)

Note that this module loading process happens principally through the manipulation of environment variables like $PATH. There is usually little or no data transfer involved.

The module loading process manipulates other special environment variables as well, including variables that influence where the system looks for software libraries, and sometimes variables which tell commercial software packages where to find license servers.

The module command also restores these shell environment variables to their previous state when a module is unloaded.

## Software Versioning

So far, we’ve learned how to load and unload software packages. This is very useful. However, we have not yet addressed the issue of software versioning. At some point or other, you will run into issues where only one particular version of some software will be suitable. Perhaps a key bugfix only happened in a certain version, or version X broke compatibility with a file format you use. In either of these example cases, it helps to be very specific about what software is loaded.

Let’s examine the output of `module avail` more closely. We can restrict the output by specifying which software we are interested in at the end of the command, for example `module avail Python`.

![](fig/module-avail-python.png)

You should notice at that there are multiple different versions of Python available, denoted after a `/` including major versions (2 vs 3) and subversion (X.X).

We can load the specific version of a software by specifying it when we run `module load`  For example to load Python2 we could run `module load Python/2.7.18-GCCcore-9.3.0`

## What if the software I need is not available. 

Installing software can be a fustrating experience. As software are often interrelated, a faulty or partial installation of one piece of software can have fairly dramatic impact on other software. For this reason, the locations where software is typically installed is not writable by regular users. You will not have "admin" rights or "root" access and limits you abilty to install software in the usual manner. 

There are a couple of options if you require software that is not currently available or you require a more bespoke version. The optimal solution depends on the specific software.

+ Is it a software that needs installing, or is it just an executable that you can run? Some software come ready complied and you can download the executable file to either your home or project files. Assuming that you can identify and load all the relevant dependecies this should be very quick to do. A common issue with this method is ensuring that the "file" has the correct permissions and the shell recognises it as a programme rather than a file. 
+ Request for it to be installed. If the software needs a more involved installation process, that takes advatange of root privledges they you will need sys admin to install for you. Log an enquiry and the ISCA support team will attempt to install it for you.
+ There are package and environmental managers that makes it easy to install software even if you don't have root access. One example is Anaconda. To use Anaconda or Miniconda, you first need to load the relevant module with either 
  + `module load Miniconda` 
  + `module load Minicoda3` (for Python3)
  + `module load Anaconda`
  + `module load Anaconda3` (for Python3)
  you can then create environments as described on the [Anaconda website](https://docs.anaconda.com/navigator/tutorials/index.html)