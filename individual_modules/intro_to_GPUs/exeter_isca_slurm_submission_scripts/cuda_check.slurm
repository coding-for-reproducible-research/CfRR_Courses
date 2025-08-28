#!/bin/bash
#
# Example SLURM batch script for running a CUDA‐based check via Poetry in a Spack environment
#

#SBATCH --job-name=cuda_check            # A short, descriptive name for your job
#SBATCH --output=%x-%j.out.log           # STDOUT -> <job-name>-<jobid>.out.log
#SBATCH --error=%x-%j.err.log            # STDERR -> <job-name>-<jobid>.err.log
#SBATCH --partition=gpu                  # Partition/queue name (e.g., GPU partition)
#SBATCH --nodes=1                        # Number of nodes to allocate
#SBATCH --ntasks=4                       # Total number of MPI tasks (not used here, but SLURM requires it)
#SBATCH --cpus-per-task=1                # CPU cores per task (for any threading or OpenMP)
#SBATCH --gres=gpu:1                     # Number of GPUs to reserve
#SBATCH -A Research_Project-RSATeam      # Research Project
#SBATCH --time=00:10:00                  # Designated Wall Time


####-------------------------------------------------------------------####
#### 1) Load Required Modules (Without Spack)
####-------------------------------------------------------------------####
module load nvidia-cuda/12.1.1
module load Python/3.11.3

####-------------------------------------------------------------------####
#### 2) Poetry virtualenv & project setup                                
####-------------------------------------------------------------------####
echo "===== Poetry setup ====="
# Ensure your local bin (where Poetry is installed) is on PATH
export PATH="$HOME/.local/bin:$PATH"

# Show which Poetry executable we’re invoking (sanity check)
echo "Using poetry from: $(command -v poetry || echo '<not found>')"

# Exit if Poetry isn’t available
if ! command -v poetry &> /dev/null; then
    echo "ERROR: poetry not found in ~/.local/bin; please verify installation"
    exit 1
fi

# Install dependencies without interactive prompts or ANSI color codes
poetry install --no-interaction --no-ansi

# Print the path to the active virtualenv for confirmation
echo "Poetry venv: $(poetry env info --path)"
echo

####-------------------------------------------------------------------####
#### 3) Run the CUDA check                                                
####-------------------------------------------------------------------####
echo "===== Running CUDA check ====="
# This should print out how many CUDA devices Cupy sees
poetry run cuda_check

# Capture and echo the exit code for easy debugging
echo "cuda_check exit code: $?"
echo
