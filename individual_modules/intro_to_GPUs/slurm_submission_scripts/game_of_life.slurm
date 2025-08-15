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
#SBATCH --partition=ncv5                   # GPU-enabled compute partition
#SBATCH --nodes=1                          # Number of nodes
#SBATCH --ntasks=16                        # Total MPI tasks (unused here but required)
#SBATCH --cpus-per-task=1                  # Threads per task (for Python/IO)
#SBATCH --gpus=1                           # GPUs per node

####-------------------------------------------------------------------####
#### 1) Spack environment setup                                        
####-------------------------------------------------------------------####
echo "===== Spack setup ====="
# SPACK_ROOT: points to your Spack installation (override with env var if needed)
SPACK_ROOT="${SPACK_ROOT:-$HOME/spack}"
if [[ -f "${SPACK_ROOT}/share/spack/setup-env.sh" ]]; then
    # Source Spack initialization to get the `spack` command
    source "${SPACK_ROOT}/share/spack/setup-env.sh"
    # Activate the named Spack environment that holds compilers + libs
    spack env activate gpu_course
    echo "Active Spack env: $(spack env status)"
else
    echo "ERROR: Spack setup script not found at ${SPACK_ROOT}/share/spack/setup-env.sh"
    exit 1
fi
echo

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
