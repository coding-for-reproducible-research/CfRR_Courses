# Context and Setup Guide

## Course Philosophy

Throughout this course, two guiding principles have been kept in mind:

1) **Complete Pipeline Approach**. Getting to the point where you can simply:

   ```python
   import cupy as cp
   ```

   is far harder in the context of using GPUs than writing code for GPUs.

2) **Focus on practical GPU use**. This is a course about **using GPUs**, not about the low-level details of **programming GPUs**.

By the end, you’ll have everything in place to leverage GPU acceleration immediately. We’ll walk you through installing the tools, configuring your environment, and running your first CUDA-powered code, so you can start leveraging the benefit of GPUs.

## University of Exeter ISCA HPC Installation Instructions

If you have not used an HPC platform before, then you may benefit from going through the material in "Helpful Auxiliary Software" on this page, as it will guide you through the process of connecting to an HPC platform, after which you can continue moving through these set-up instructions.

## Clone the Repo

To engage with all of the content within this GPU Training course, you will need to clone the repo, which can be done with

``` bash
cd /lustre/projects/Research_Project-RSATeam #This is the directory that the RSA Team will do the course in.
mkdir $USER # Create a directory for you within the project space.
cd $USER
git clone https://github.com/UniExeterRSE/GPU_Training.git
cd GPU_Training
```

### Two Ways to Run the Course Code

#### Method 1: Interactive GPU Session

If you prefer to work interactively, follow these steps:

Request an interactive session:

```bash
srun \
  --partition=gpu \
  -A Research_Project-RSATeam \
  --time=12:00:00 \
  --nodes=1 \
  --ntasks=1 \
  --gres=gpu:1 \
  --cpus-per-task=4 \
  --pty /bin/bash
```

Load required modules:

```bash
module load nvidia-cuda/12.1.1
module load Python/3.11.3
```

Install the Python requirements:

```bash
poetry install
```

Once your environment is ready, you can invoke any of the project’s entry points via Poetry. For example:

```bash
poetry run cuda_check
```

#### Method 2: Batch Submission via Slurm

All of the key Slurm submission scripts live in the
`exeter_isca_slurm_submission_scripts/` directory. You can submit a job with

```bash
cd exeter_isca_slurm_submission_scripts
sbatch <script-name>.slurm
```

## General Installation Instructions

The following provides the steps that are required to install the necessary compilers and packages to engage with the material in this course.

```{important}
Please keep in mind that nearly all of the commands used in this section will be covered in detail within the course itself. They are included here to make sure you have all of the necessary resources (e.g. a GPU and relevant compilers) to complete the whole course. **The intention is for you to run these commands and confirm the output based on the contents of this page, not to completely understand each step you are taking.** If you do get stuck and are unsure of how to proceed, please reach out to the authors, and we can help you debug.

If you are self-studying, then please read up to the section "Project: Conway's Game of Life - CPU vs GPU Implementation" to understand more about the commands that are being used. If you are taking the workshop, then these commands are here to make sure that you are able to run code on the designated platform to save time in the workshop and identify any permission errors when accessing the needed resources.
```

## Spack - Installing system-level requirements

Within this course, [Spack](https://spack.io/) is being used to manage system-level requirements, such as drivers. The reason for this is that a lot of system-level requirements generally require privileged permissions, such as access to `sudo`. However, as a lot of the platforms that have GPUs available are HPC platforms, `spack` allows us to install drivers that normally would require privileged access. There are also a range of other benefits to the use of `spack` that will be discussed in this course.

First, you will need to clone the `spack` repo in your user home directory at a recent stable version (extra config and depth flags suggested in spack's readme):

``` bash
git clone -c feature.manyFiles=true --depth=2 -b v0.23.1 https://github.com/spack/spack.git
```

You will then need to activate `spack` with:

```bash
source spack/share/spack/setup-env.sh
```

```{note}
You can check that `spack` has been successfully installed by running `spack --version`, which should return the version of spack that you have available.
```

You will need need to create a spack environment, which can be done with the following, creating a `spack` environment named "gpu_course":

```bash
spack env create gpu_course
```

which can then be activated with

```bash
spack env activate -p gpu_course
```

In this course, spack is being used to install system-level requirements, and so the required version of Python and the needed driver of CUDA are installed via spack with the following two commands.

```bash
spack add python@3.12
spack add cuda
```

```{note}
This step will simply say that you intend to install these packages; at this time, `spack` is still waiting for more packages to be added to the environment specification. We can check what the current specification is (e.g. package list, dependencies, compilers to be used etc.) with `spack spec`.
```

Finally, we are able to install all of the packages into our `spack` environment with

```bash
spack install
```

```{note}
On an HPC environment, we would want to put the above spack commands into a shell script and run this with the scheduler, such as `sbatch` for ISCA/Archer2.  The `install` can take on the order of hours for the above specifications.
```

```{note}
The `.spack` directory is a hidden folder in your home directory that stores user-level configuration data, caches, and environment settings for Spack. It helps Spack remember things like what packages you have installed, which mirrors you have configured, and any custom settings you have applied. Sometimes, these configuration files or caches can become outdated or inconsistent, especially if you have been experimenting with different environments, modifying package recipes, or changing `spack` versions. When a "weird" or hard-to-troubleshoot error occurs, one way to rule out bad configuration or cache data is to remove the `.spack` directory. By doing so, you essentially give Spack a clean slate: it will recreate the directory and its necessary files the next time it runs, which often resolves mysterious issues stemming from old or corrupted data. If you try to get a clean slate for spack by just removing the non-hidden `spack` directory, then it will likely not be a clean slate, and the previous experimentations data will still be present.
```

## Poetry - Installing user-level requirements

Within this course, [Poetry](https://python-poetry.org/) is used to manage the user-level requirements.

The following command will install poetry:

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

```{note}
Poetry can be uninstalled with `curl -sSL https://install.python-poetry.org | python3 - --uninstall`.
```

```{note}
`poetry install` needs to be run from within the training course repo. If you haven't, then you need to clone this repo with `git clone https://github.com/UniExeterRSE/GPU_Training.git` and then navigate to its root with `cd GPU_Training`
```

All of the user-level requirements can be installed via Poetry with the command:

```bash
poetry install
```

`````{admonition} IMPORTANT: If running locally...
:class: important
You can check that the installation has been successful by running `poetry run cuda_check`, which should return the number of CUDA devices that are currently available, such as `Number of CUDA devices: 1`. If you want to find out more information about the device that is connected, you can run a command such as `nvidia-semi` for an NVIDIA GPU.
`````

`````{admonition} IMPORTANT: If running on a HPC...
:class: important
If you are working on an HPC cluster via SLURM, submit the `cuda_check.slurm` script instead of running the commands directly. The script contain the same commands as above (e.g. `poetry run cuda_check` and `nvidia-smi`) that the `.slurm` script will run and store the output and errors in the files `out.log` and `err.log` respectively. This can be done with the command `sbatch slurm_submission_scripts/cuda_check.slurm`.
`````

## Data

### Data Download

```{note}
For the RSA Team Day the data files are available on the shared ISCA file-system.
```

To download the dataset, follow these steps:

- **Create a Copernicus Marine Account**:
  - You will need an account to access the data. Register here: [Register for Account](https://data.marine.copernicus.eu/register?redirect=%2Fproduct%2FGLOBAL_ANALYSISFORECAST_PHY_001_024%2Fdownload%3Fdataset%3Dcmems_mod_glo_phy-thetao_anfc_0.083deg_PT6H-i_202406).

- **Run the CLI Command to Download the Dataset**:
  - Use the following command to download the subset of data:

    ```bash
    poetry run download_data
    ```

  - This command will prompt you to enter your username and password. Once authenticated, the data file will download to the data directory. Please note that the download may take some time as the file size is approximately 250 MB.

### Data Description

The dataset used during the course is based on 3-dimensional Ocean Temperatures. The dataset is described in detail on the [Copernicus Marine Data Service](https://data.marine.copernicus.eu/product/GLOBAL_ANALYSISFORECAST_PHY_001_024/description)

**Filename**: `cmems_mod_glo_phy-thetao_anfc_0.083deg_PT6H-i_1730799065517.nc`

**Description**:
This dataset was downloaded from the **Global Ocean Physics Analysis and Forecast** service. It provides data for global ocean physics, focusing on seawater potential temperature.

- **Product Identifier**: `GLOBAL_ANALYSISFORECAST_PHY_001_024`
- **Product Name**: Global Ocean Physics Analysis and Forecast
- **Dataset Identifier**: `cmems_mod_glo_phy-thetao_anfc_0.083deg_PT6H-i`

**Variable Visualized**:

- **Sea Water Potential Temperature (thetao)**: Measured in degrees Celsius [°C].

**Geographical Area of Interest**:

- **Region**: Around the United Kingdom
- **Coordinates**:
  - **Northern Latitude**: 65.312
  - **Eastern Longitude**: 6.1860
  - **Southern Latitude**: 46.829
  - **Western Longitude**: -13.90

**Depth Range**:

- **Minimum Depth**: 0.49 meters
- **Maximum Depth**: 5727.9 meters

**File Size**:

- **267.5 MB**

## Helpful Auxiliary Software

This section details a number of useful pieces of software that make the development of GPU code easier. Notably, a lot of these sit within Visual Studio Code, chosen as these are what the author was exposed to when first starting in GPU development.

### Using Visual Studio Code (VSCode)

Visual Studio Code (VSCode) can be installed from [its website](https://code.visualstudio.com/).

#### Remote-SSH

This guide walks you through setting up and using **Remote-SSH** in Visual Studio Code (VSCode) to connect to a remote machine.

##### Install the Remote - SSH Extension

Install from [Remote-SSH](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh) or via the following steps:

1. Open **VSCode**.
2. Go to the **Extensions** view by clicking on the square icon in the sidebar or pressing `Ctrl+Shift+X` (Windows/Linux) or `Cmd+Shift+X` (Mac).
3. Search for "**Remote - SSH**" and install the extension from Microsoft.

##### Configure SSH on Your Local Machine

Ensure you can SSH into the remote machine from your terminal. If SSH is not already configured:

1. **Generate SSH Keys** (if not already done):
   - Open a terminal on your local machine.
   - Run the command `ssh-keygen` and follow the prompts to generate a key pair. This will create keys in `~/.ssh/` by default.

2. **Copy Your Public Key to the Remote Machine**:
   - Run the command `ssh-copy-id user@hostname`, replacing `user` and `hostname` with your remote machine’s username and IP address or hostname.
   - Enter your password when prompted. This step ensures you can log in without repeatedly typing your password.

##### Add SSH Configuration in VSCode

1. Open **VSCode**.
2. Press `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (Mac) to open the command palette.
3. Type and select **Remote-SSH: Open Configuration File**.
4. Choose the SSH configuration file (usually located at `~/.ssh/config`).

5. Add a new SSH configuration to the file, specifying the remote machine’s details. Here’s an example configuration:

   ```ssh-config
   Host my-remote-machine
       HostName <remote-ip-or-hostname>
       User <your-username>
       IdentityFile ~/.ssh/id_rsa  # Path to your SSH private key
       Port 22  # Default SSH port; change if needed
   ```

##### Connecting to remote from within VSCode

You should now be able to connect to the remote machine from within VSCode but using `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (Mac) and then selecting `Remote-SSH: Connect to host...` which should then present a list with the name of the machine you gave in the config file, in the above case `my-remote-machine`. You will then be asked for a password if you protected your ssh key. Once connected, a new VSCode window will be created, and you should have a fully functioning ID on the remote machine.

#### Live Server

As this course produces 3D outputs, some supporting code will generate interactive HTML dashboards to make exploring the output data easier. The VSCode Live Server extension makes the process of viewing these dashboards with your local web browser easier.

##### Install the Live Server Extension

Install from [Live Server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer) or via the following steps:

1. Open **VSCode**.
2. Go to the **Extensions** view by clicking on the square icon in the sidebar or pressing `Ctrl+Shift+X` (Windows/Linux) or `Cmd+Shift+X` (Mac).
3. Search for "**Live Server**" and install the extension by **Ritwick Dey**.

---

##### Start the Live Server

1. **Right-click** on the HTML file in the editor and select **Open with Live Server**.

##### View Changes in Real-Time

- As you edit and save your HTML, CSS, or JavaScript files, the browser will automatically refresh to display your changes.
- This eliminates the need to manually refresh the browser manually, speeding up development.