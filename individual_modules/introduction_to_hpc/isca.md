# Exeter supported HPC facilities

## Learning Objectives

At the end of this lesson you will be able to:

- Describe the HPC infrastructure at Exeter.
- What other systems are potentially available.
- Learn how to gain access to HPC systems at Exeter.

## ISCA HPC
The University of Exeter has it's own central HPC facility (_ISCA_) to enable intensive computational research. It represents a multi-million £ investment by the University, designed to serve the advanced computing requirements of all research disciplines. ISCA usage is free at point-of-use for all research groups from all campuses. In order to access to ISCA, one needs to

1. Request access to the system, preferably through the IT ticketing [system](https://uoeitservicedesk-apps.easyvista.com/s/selfservice#!?page=58a2df66258c1)
2. Be on the University of Exeter campus network, either physically or using the VIA VPN (info [here](https://www.exeter.ac.uk/departments/it/howdoi/vpn/))
3. Have an application like `ssh` or Putty that enables remote system login

### Specifications

ISCA consists of a range of compute resources: 
- Dozens of the traditional cluster (128GB & 256GB nodes) 
- Large memory (3TB) nodes
- Xeon Phi accelerator nodes and GPU (Tesla K80) compute nodes.

For a total of ~6000 Intel CPU cores in nodes connected with 40Gbps high-speed fiber networking. It is important to stress that the storage on ISCA is **not** backed up, so we recommend you keeping copies off important results & software elsewhere for safe keeping.

<img src="../fig/IMG20221207130751.jpg" alt="ISCA row A" width="600"/>

#### Hardware & Software WIP
**TBC**, none of these features are yet in production but they are worth mentioning anyways.

- Additional NVIDIA GPU nodes with multiple A100 cards per box
- Enable web-client based [OpenOnDemand](https://openondemand.org/) interface for ISCA.
- Upgrading the operating system to RHEL 9

## ISCA OpenStack
In addition to the traditional HPC resources, the OpenStack system offers users an infinitely customizable virtual workstation/server experience. It has just been doubled in size to a total of ~2500 cores with multiple Petabytes of image storage.

### Use Cases
- Teaching modules with niche requirements
- Developing in an isolated custom environment
- Testing tools on custom defined software platforms

<img src="../fig/IMG20221207130813.jpg" alt="OpenStack row B" width="400"/>

## Working with Projects

One way ISCA might be different to other HPC systems you've used is that to run a job on the system you need to be a member of a project. Projects are generally aligned to grants, the grant PI is typically the admin of the project and can manage the addition of new members. They can also add other admins. 

Each project has a unique ID, that you will need to specify when submitting a compute job to the system. Projects also come with shared storage. We will look at identifying which projects you are a member of once we have logged in shortly.

## Fair Usage

There are major benefits in terms of capacity and capability to using a central HPC system. There are also logistical and practical challenges that arise when using a shared resource. There are two elements of the system that are shared, the storage and compute. Schedulers deal with the allocation and protection of compute, and we will cover these in more detail later on. Storage might be managed by applying file quotas to user folders. It is likely there is also a fair usage policy in action designed to ensure everyone can get access to a compute node within a reasonable period of time. Essentially, whereas on your computer you can use it how you want, when you want with no imapct of others, with a HPC system, you may need to be patient at times and be considerate of other users. 

## Citing use of ISCA

Please use the following when acknowledging the use of ISCA in research papers:

```
The authors would like to acknowledge the use of the University of Exeter High-Performance Computing (HPC) facility in carrying out this work.
```
Also, when you submit your paper or article to Symplectic please add ARC - ISCA as an Unclassified Label.

## Additional Systems

### Cornwall Clusters
For those researchers based in Cornwall, you have access to the Athena and Carson clusters, whose details can be found on Sharepoint [here](https://universityofexeteruk.sharepoint.com/sites/CornwallARC).

### Isambard
The University of Exeter is a member of the GW4 consortium, which along with the Met Office, supports the ARM-based [Isambard](https://gw4-isambard.github.io/docs/) Tier-2 supercomputer. It is one of a dozen Tier-2 national facilities that provide access to larger quantities of computing resources than what is normally found in a single campus (Tier-3) system. If you do find that your needs are beyond what Exeter itself can provide, please contact Research IT so they can direct you to the computing resource that is most appropriate for your needs. 

There are a number of HPC facilities that are available to the UK academic research community. The [hpc-uk](https://www.hpc-uk.ac.uk/about/accessibility.html) website is a useful resource in this regard.

## External Funding
- Research IT is no longer supporting a "priority queue" on ISCA
- If your group would like to *purchase* new hardware, please consider helping Research IT expand its capabilities.
