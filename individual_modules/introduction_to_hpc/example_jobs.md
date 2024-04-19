# Running more complex jobs on a HPC system 

     Questions

        How do we run a job not written in bash?

    Objectives

        Write a job submission script to use preinstalled software

        Submit a python script to the scheduler

        Submit an R script to the scheduler


In the job we submitted to the cluster so far only included bash/UNIX commands. It is highly likely that most of what we want to do on the command line involves using other software or programming languages. In this lesson we are going to look at how we run a variety of different scripts or use a range of different software on the system. Ultimately we need to use UNIX commands to call/execute/run our script.

## Command line programmes

The first extension we will cover is how to use command line tools. If you use these frequently in your work, you will be aware that these are executables you call from a shell terminal possible with some flags or arguments. 

The example job submission script below uses a command line tool called (plink)[https://zzz.bwh.harvard.edu/plink/index.shtml] which is used in the analysis of genetic data. 

The components are the script are 

1. The SLURM commands to tell the scheduler the parameters for the job, including which queue to submit to, how many processors to use, which project, and the paths to the output/log files. 

2. Load the relevant modules. When the job gets transferred to the compute nodes, the environment is empty. As part of your job you need to load all the relevant software via the module loading system. 

3. The command(s). In this example we are just asking the plink programme to print the help pages.

```
#!/bin/sh
#SBATCH -p training # submit to the serial queue
#SBATCH --time=00:10:00 # Maximum wall time for the job.
#SBATCH -A Research_Project-HPC-Training # research project to submit under. 
#SBATCH --nodes=1 # specify number of nodes.
#SBATCH --ntasks-per-node=1 # specify number of processors per node
#SBATCH --mail-type=END # send email at job completion 
#SBATCH --output=plink.o
#SBATCH --error=plink.e
#SBATCH --job-name=plink


## print start date and time
echo Job started on:
date -u

module load PLINK

plink2 --help

## print end date and time
echo Job ended on:
date -u

```

Essentially whatever software/programme/script we want to run we have to be able to do so from the command line or via a UNIX command. Therefore if we want to use another language e.g. R, python, C, perl etc we need to write a script in that language and run it from our job submission script. Here we will look at an R and Python example

## R example

To run a job using R we need two scripts: 

1) an R script that contains all the R commands we want to run. This needs to be complete and run from top to bottom with no errors or user input. It should include all data loading, package loading, and saving of any output.
2) a job submission script that executes the R script

We are going to use a short R script that runs a for loop to calculate the squares of a list of numbers. This script is named `calc-squares.R` and can be found in the resources section. The job submission script we will use is below. You should recognise the geenral frameowkr where we have the SLURM commands at the top. There are two important lines that we need to include to run our R script.

1. `module load R` We need this to load R from the list of modules. Without it there is no R programme to interpret our R script.
2. `Rscript calc-squares.R` This is our bash command saying execute the commands in our script with R.


```
#!/bin/sh
#SBATCH -p training # submit to the serial queue
#SBATCH --time=00:10:00 # Maximum wall time for the job.
#SBATCH -A Research_Project-HPC-Training # research project to submit under. 
#SBATCH --nodes=1 # specify number of nodes.
#SBATCH --ntasks-per-node=1 # specify number of processors per node
#SBATCH --mail-type=END # send email at job completion 
#SBATCH --output=exampleRjob.o
#SBATCH --error=exampleRjob.e
#SBATCH --job-name=exampleRjob


## print start date and time
echo Job started on:
date -u

module load R

Rscript calc-squares.R

## print end date and time
echo Job ended on:
date -u
```

Note that by just using `module load R` we are not specifying a particular version of R. Often this command will load the most up-to-date version as the default, but this of course can change and might not be very reproducible.  

## Python example

Running a python script is the same as running an R script. Again we need two scripts 

1) a Python script that contains all the python commands we want to run. This needs to be complete and run from top to bottom with no errors or user input. It should include all data loading, module loading, and saving of any output.
2) a job submission script that executes the R script

We are going to use a short R script that runs a for loop to calculate the squares of a list of numbers. This script is named `calc-squares.R` and can be found in the resources section. The job submission script we will use is below. You should recognise the general framework where we have the SLURM commands at the top. There are two important lines that we need to include to run our R script.

1. `module load Python/3.10.4-GCCcore-11.3.0` We need this to load Python and specifically version 3 from the list of modules. Without it there is no Python programme to interpret our Python script.
2. `python calc-squares.py` This is our bash command saying execute the commands in our script with python.

```
#!/bin/sh
#SBATCH -p training # submit to the serial queue
#SBATCH --time=00:10:00 # Maximum wall time for the job.
#SBATCH -A Research_Project-HPC-Training # research project to submit under. 
#SBATCH --nodes=1 # specify number of nodes.
#SBATCH --ntasks-per-node=1 # specify number of processors per node
#SBATCH --mail-type=END # send email at job completion 
#SBATCH --output=examplePythonJob.o
#SBATCH --error=examplePythonJob.e
#SBATCH --job-name=examplePythonJob


## print start date and time
echo Job started on:
date -u

module load Python/3.10.4-GCCcore-11.3.0

python calc-squares.py

## print end date and time
echo Job ended on:
date -u
```

## STATA example

Similar to the R and Python examples you need to collate your stata commands into a script (called a do file). These can be created using the GUI you might be familiar with.

