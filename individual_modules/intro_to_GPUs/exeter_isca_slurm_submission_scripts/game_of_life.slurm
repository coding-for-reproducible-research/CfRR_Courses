#!/bin/bash
#
# SLURM batch script to run the Game of Life experiment end-to-end
#
# Usage:
#   sbatch run_game_of_life.sh
#
# What it does:
#   1) Loads your Spack toolchain (gpu_course env)
#   2) Installs Python deps via Poetry
#   3) Verifies GPU access with a quick cuda_check + nvidia-smi dump
#   4) Executes the Game of Life benchmark script
#
# Outputs:
#   - STDOUT → game_of_life-<jobid>.out.log
#   - STDERR → game_of_life-<jobid>.err.log
#

#SBATCH --job-name=game_of_life            # Job name shown in squeue
#SBATCH --output=%x-%j.out.log             # STDOUT → <job-name>-<jobid>.out.log
#SBATCH --error=%x-%j.err.log              # STDERR → <job-name>-<jobid>.err.log
#SBATCH --partition=gpu                    # GPU-enabled compute partition
#SBATCH --nodes=1                          # Number of nodes
#SBATCH --ntasks=16                        # Total MPI tasks (unused here but required)
#SBATCH --cpus-per-task=1                  # Threads per task (for Python/IO)
#SBATCH --gres=gpu:1                       # Number of GPUs to reserve
#SBATCH -A Research_Project-RSATeam        # Research Project
#SBATCH --time=0:10:00                     # Designated Wall Time

####-------------------------------------------------------------------####
#### 1) Load Required Modules (Without Spack)
####-------------------------------------------------------------------####
module load nvidia-cuda/12.1.1
module load Python/3.11.3

####-------------------------------------------------------------------####
#### 2) Poetry venv & dependency installation                           
####-------------------------------------------------------------------####
echo "===== Poetry setup ====="
# Ensure Poetry (often installed via pipx) is on your PATH
export PATH="$HOME/.local/bin:$PATH"

# Show which Poetry binary will run
echo "Using poetry from: $(command -v poetry || echo '<not found>')"

# Fail early if Poetry is unavailable
if ! command -v poetry &> /dev/null; then
    echo "ERROR: Poetry not found; please install via pipx or official installer"
    exit 1
fi

# Move into your project directory (adjust SCRIPT_DIR as needed)
cd "${SCRIPT_DIR:-$(pwd)}"

# Install all dependencies into Poetry’s virtualenv,
# suppressing prompts and ANSI color codes
poetry install --no-interaction --no-ansi

# Display the path to the created venv (for logging/debugging)
echo "Poetry venv path: $(poetry env info --path)"
echo

####-------------------------------------------------------------------####
#### 3) Quick CUDA sanity checks                                      
####-------------------------------------------------------------------####
echo "===== Running CUDA check ====="
# Run your cuda_check script (should print GPU count)
poetry run cuda_check
echo "cuda_check exit code: $?"
echo

echo "===== GPU details via nvidia-smi ====="
# Print GPU name, driver, memory, utilization
if command -v nvidia-smi &> /dev/null; then
    nvidia-smi \
      --query-gpu=index,name,driver_version,memory.total,memory.used,utilization.gpu \
      --format=csv
else
    echo "nvidia-smi not found in PATH"
fi
echo

####-------------------------------------------------------------------####
#### 4) Run the Game of Life experiment                               
####-------------------------------------------------------------------####
echo "===== Running Game of Life Experiment ====="
# Log current directory for traceability
pwd

# Execute the benchmark script under Poetry’s venv
poetry run python ../content/game_of_life_experiment.py

echo "===== Experiment complete ====="
