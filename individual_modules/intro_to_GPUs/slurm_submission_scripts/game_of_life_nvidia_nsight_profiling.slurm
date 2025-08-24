#!/bin/bash
#
# SLURM batch script to run the Game of Life experiment under NVIDIA Nsight Systems
#

#SBATCH --job-name=game_of_life_NSight      # Job name for easy identification
#SBATCH --output=%x-%j.out.log              # STDOUT to <job-name>-<jobid>.out.log
#SBATCH --error=%x-%j.err.log               # STDERR to <job-name>-<jobid>.err.log
#SBATCH --partition=ncv5                     # GPU partition/queue
#SBATCH --nodes=1                            # Number of nodes to allocate
#SBATCH --ntasks=16                          # Number of tasks (MPI ranks, not used here)
#SBATCH --cpus-per-task=1                    # CPU cores per task (for threading)
#SBATCH --gpus=1                             # Number of GPUs to reserve

####-------------------------------------------------------------------####
#### 1) Spack environment setup                                        
####-------------------------------------------------------------------####
echo "===== Spack setup ====="
# Define SPACK_ROOT (default to $HOME/spack if unset)
SPACK_ROOT="${SPACK_ROOT:-$HOME/spack}"
if [[ -f "${SPACK_ROOT}/share/spack/setup-env.sh" ]]; then
    # Source Spack’s environment to make `spack` available
    source "${SPACK_ROOT}/share/spack/setup-env.sh"
    # Activate the GPU course environment with your compiler/toolchain
    spack env activate gpu_course
    echo "Active Spack env: $(spack env status)"
else
    echo "ERROR: could not find Spack at ${SPACK_ROOT}/share/spack/setup-env.sh"
fi
echo

####-------------------------------------------------------------------####
#### 2) Poetry virtualenv & install dependencies                      
####-------------------------------------------------------------------####
echo "===== Poetry setup ====="
# Ensure Poetry is on the PATH (user-local install)
export PATH="$HOME/.local/bin:$PATH"

# Sanity check: which Poetry will run?
echo "Using poetry from: $(command -v poetry || echo '<not found>')"

# Exit early if Poetry is missing
if ! command -v poetry &> /dev/null; then
    echo "ERROR: poetry not found; please install via pipx or official installer"
    exit 1
fi

# Install project dependencies into the Poetry venv (non-interactive)
poetry install --no-interaction --no-ansi
# Show which virtualenv Poetry created/activated
echo "Poetry venv: $(poetry env info --path)"
echo

####-------------------------------------------------------------------####
#### 3) Quick CUDA sanity checks                                      
####-------------------------------------------------------------------####
echo "===== Running CUDA check ====="
# Run your earlier cuda_check command to verify GPU visibility
poetry run cuda_check
echo "cuda_check exit code: $?"
echo

echo "===== GPU info (nvidia-smi) ====="
# Print out GPU state (driver, memory, utilization)
if command -v nvidia-smi &> /dev/null; then
    nvidia-smi --query-gpu=index,name,driver_version,memory.total,memory.used,utilization.gpu \
               --format=csv
else
    echo "nvidia-smi not found in PATH"
fi
echo

####-------------------------------------------------------------------####
#### 4) Profile the Game of Life experiment with Nsight Systems        
####-------------------------------------------------------------------####
echo "===== Running Game of Life Experiment under Nsight Systems ====="
# Print current directory for debugging
pwd

# Launch Nsight Systems profiler:
#  - sample=none      : only collect traces, no statistical sampling
#  - trace=cuda,nvtx  : capture CUDA API calls and NVTX ranges
#  - -o <output>      : base name for the .qdrep/.nsys-rep files
#
# We wrap the profiled command with `poetry run` to use the project venv.
nsys profile \
    --sample=none \
    --trace=cuda,nvtx \
    -o "../output/${SLURM_JOB_NAME}_${SLURM_JOB_ID}_exp_report" \
    -- \
    poetry run game_of_life_experiment_profiled \
        --profile-gpu \
        --profile-cpu

echo "=== Nsight Systems profiling complete ==="
