# Why might I want to use a HPC Cluster?

## Questions
- Why would I be interested in High Performance Computing (HPC)?
- What can I expect to learn from this course?

## Objectives
- Describe what an HPC system is.
- Identify how an HPC system could benefit your research.

## The need for High Performance Computing Systems 

Datasets are getting bigger and more complex, and we want to model biological and physical systems at increasing finer resolution or with more and more inputs. This means that our research problems require increasingly more computing power and can outgrow the desktop or laptop computer where they started:

+ A statistics student wants to do cross-validate their model. This involves running the model 1000 times — but each run takes an hour. Running on their laptop will take over a month!
+ A genomics researcher has been using small datasets of sequence data, but soon will be receiving a new type of sequencing data that is 10 times bigger. It’s already challenging to open the datasets on their computer — analyzing these larger datasets will probably crash it.
+ An engineer is using a fluid dynamics package that has an option to run in parallel. So far, they haven’t used this option on their desktop, but in going from 2D to 3D simulations, simulation time has more than tripled and it might be useful to take advantage of that feature.

In all these cases, what is needed is access to more computers that can be used at the same time. Luckily, large scale computing systems — shared computing resources with lots of computers — are available at many universities, labs, or through national networks. High Performance Computers are really clusters of hundreds (sometimes thousands) of smaller computers, typically referred to as nodes.

These resources usually compare favorably to your desktop by having
+ more central processing units(CPUs)
+ CPUs that operate at higher speeds
+ more memory
+ more storage
+ faster connections 

They are frequently called “clusters”, “supercomputers” or resources for “high performance computing” commonly abbreviated to HPC. In this lesson, we will usually use the terminology of HPC or HPC cluster. 

Using a cluster often has the following advantages for researchers:

+ **Speed**: With many more CPU cores, often with higher performance specs, than a typical laptop or desktop, HPC systems can offer significant speed up.
+ **Volume**: Many HPC systems have both the processing memory (RAM) and disk storage to handle very large amounts of data. Terabytes of RAM and petabytes of storage are available for research projects.
+ **Efficiency**: Many HPC systems operate a pool of resources that are drawn on by many users. In most cases when the pool is large and diverse enough the resources on the system are used almost constantly.
+ **Cost** Bulk purchasing and government funding mean that the cost to the research community for using these systems in significantly less that it would be otherwise.
+ **Convenience**: Maybe your calculations just take a long time to run or are otherwise inconvenient to run on your personal computer. There’s no need to tie up your own computer for hours when you can use someone else’s instead.

This is how a large-scale compute system like a cluster can help solve problems like those listed at the start of the lesson. It also creates new opportunities to address new research questions previously thought too computational intensive. 

## What does a HPC system consist of?
One way to conceptualize a HPC cluster is a three-legged stool
1. Login/Submit: where users submit their work from
2. Compute/Execute: The many machines that do the computational tasks
3. Controller/Manager: the machine that does the automated scheduling of tasks on compute resources

So these HPC systems are really clusters of hundreds (sometimes thousands) of smaller computers (nodes) connected together with high-speed networking. Our compute nodes have between 16 and 48 CPU cores each, depending on when they were purchased. For a sense of scale, your average desktop or laptop computer has between 4 and 8 CPU cores. 

Each node is likely a lot more powerful than the computer you have on your desk right now, and to look at they are very different, but inside they contain all the same basic components like processors, hard disks, memory, and an operating system. Where the true power of HPC comes in is the nodes' ability to work together. You submit your code as self-contained jobs from a login node, and the rest of the nodes, or compute nodes, are where your code actually runs. HPC systems typically use a resource manager and batch scheduler to handle the distribution of jobs to nodes.

## How do I communicate with the HPC cluster? 

Most HPC systems are built with a Unix operating system. It is rare for a HPC system to have the nice user interface, that you might be used to using on your laptop. Therefore, using HPC systems often involves the use of a shell through a command line interface (CLI) and either specialized software or programming techniques. This is often the first barrier to using the system, and can seem off-putting. While the more Unix you know, the more comfortable you will feel using the system, you only **need** to know some common commands to get started. 

The shell is a program with the special role of having the job of running other programs rather than doing calculations or similar tasks itself. What the user types goes into the shell, which then figures out what commands to run and orders the computer to execute them. (Note that the shell is called “the shell” because it encloses the operating system in order to hide some of its complexity and make it simpler to interact with.) The most popular Unix shell is Bash, the Bourne Again SHell (so-called because it’s derived from a shell written by Stephen Bourne). Bash is the default shell on most modern implementations of Unix and in most packages that provide Unix-like tools for Windows.

Interacting with the shell is done via a command line interface (CLI) on most HPC systems. In the earliest days of computers, the only way to interact with early computers was to rewire them. From the 1950s to the 1980s most people used line printers. These devices only allowed input and output of the letters, numbers, and punctuation found on a standard keyboard, so programming languages and software interfaces had to be designed around that constraint and text-based interfaces were the way to do this. A typing-based interface is often called a command-line interface, or CLI, to distinguish it from a graphical user interface, or GUI, which most people now use. The heart of a CLI is a read-evaluate-print loop, or REPL: when the user types a command and then presses the Enter (or Return) key, the computer reads it, executes it, and prints its output. The user then types another command, and so on until the user logs off.

Learning to use Bash or any other shell sometimes feels more like programming than like using a mouse. Commands are terse (often only a couple of characters long), their names are frequently cryptic, and their output is lines of text rather than something visual like a graph. However, using a command line interface can be extremely powerful, and learning how to use one will allow you to reap the benefits described above.

