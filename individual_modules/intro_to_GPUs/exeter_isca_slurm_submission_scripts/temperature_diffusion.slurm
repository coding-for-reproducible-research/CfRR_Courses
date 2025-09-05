#!/bin/bash
#
# SLURM batch script to run the Temperature Diffusion experiment end-to-end
#
# Usage:
#   sbatch run_temperature_diffusion.sh
#
# Steps performed:
#   1) Load Spack environment (`gpu_course`) for compilers/libs
#   2) Install Python dependencies via Poetry
#   3) Verify GPU access with a quick cuda_check + nvidia-smi dump
#   4) Execute the temperature diffusion benchmark script
#
# Outputs:
#   - STDOUT → temperature_diffusion-<jobid>.out.log
#   - STDERR → temperature_diffusion-<jobid>.err.log
#

#SBATCH --job-name=temperature_diffusion  # Job name shown in scheduler
#SBATCH --output=%x-%j.out.log            # STDOUT → <job-name>-<jobid>.out.log
#SBATCH --error=%x-%j.err.log             # STDERR → <job-name>-<jobid>.err.log
#SBATCH --partition=gpu                   # GPU partition/queue
#SBATCH --nodes=1                         # Number of nodes to allocate
#SBATCH --ntasks=16                       # Number of tasks (unused by this script)
#SBATCH --cpus-per-task=1                 # CPU cores per task (for threading/IO)
#SBATCH --gres=gpu:1                      # Number of GPUs to reserve
#SBATCH -A Research_Project-RSATeam       # Research Project
#SBATCH --time=0:10:00                    # Designated Wall Time

####-------------------------------------------------------------------####
#### 1) Load Required Modules (Without Spack)
####-------------------------------------------------------------------####
module load nvidia-cuda/12.1.1
module load Python/3.11.3

####-------------------------------------------------------------------####
#### 2) Poetry virtualenv & dependency installation                   
####-------------------------------------------------------------------####
echo "===== Poetry setup ====="
# Ensure Poetry’s user‐install bin directory is on PATH
export PATH="$HOME/.local/bin:$PATH"

# Show which Poetry executable will be used
echo "Using poetry from: $(command -v poetry || echo '<not found>')"

# Exit if Poetry is not installed
if ! command -v poetry &> /dev/null; then
    echo "ERROR: poetry not found; please install Poetry in ~/.local/bin"
    exit 1
fi

# Change into project directory (adjust if necessary)
cd "${SCRIPT_DIR:-$(pwd)}"

# Install project dependencies into the Poetry-managed venv,
# suppressing interactive prompts and ANSI coloring
poetry install --no-interaction --no-ansi

# Print the path to the active virtual environment for verification
echo "Poetry venv path: $(poetry env info --path)"
echo

####-------------------------------------------------------------------####
#### 3) Quick CUDA sanity checks                                      
####-------------------------------------------------------------------####
echo "===== Running CUDA check ====="
# Verify GPU visibility/count using your cuda_check script
poetry run cuda_check
echo "cuda_check exit code: $?"
echo

echo "===== GPU info (nvidia-smi) ====="
# Dump GPUs’ index, name, driver version, total/used memory, utilization
if command -v nvidia-smi &> /dev/null; then
    nvidia-smi \
      --query-gpu=index,name,driver_version,memory.total,memory.used,utilization.gpu \
      --format=csv
else
    echo "nvidia-smi not found in PATH"
fi
echo

####-------------------------------------------------------------------####
#### 4) Run the Temperature Diffusion experiment                       
####-------------------------------------------------------------------####
echo "===== Running Temperature Diffusion Experiment ====="
# Print current working directory for logging/debugging purposes
pwd

# Execute the diffusion benchmarking script under Poetry’s venv
poetry run python ../content/temperature_diffusion_experiment.py

echo "===== Experiment complete ====="
