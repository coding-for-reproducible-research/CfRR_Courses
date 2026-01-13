#!/bin/bash
#
# SLURM batch script to dump allocation, system, and GPU information
#
# Usage:
#   sbatch info.sh
# Outputs:
#   - STDOUT → info-<jobid>.out.log
#   - STDERR → info-<jobid>.err.log
#

#SBATCH --job-name=info                    # Descriptive name for this job
#SBATCH --output=%x-%j.out.log             # STDOUT → <job-name>-<jobid>.out.log
#SBATCH --error=%x-%j.err.log              # STDERR → <job-name>-<jobid>.err.log
#SBATCH --partition=ndv4                   # Partition/queue to submit to
#SBATCH --nodes=1                          # Number of nodes requested
#SBATCH --ntasks=4                         # Number of tasks (MPI ranks)
#SBATCH --cpus-per-task=1                  # CPU cores per task
#SBATCH --gpus=1                           # Number of GPUs requested

####-------------------------------------------------------------------####
#### 1) Print SLURM job allocation details                             
####-------------------------------------------------------------------####
echo "===== Job allocation info ====="
# Show key SLURM environment variables (or placeholders if unset)
echo "Job ID:          ${SLURM_JOB_ID:-<none>}"
echo "Job name:        ${SLURM_JOB_NAME:-<none>}"
echo "Partition:       ${SLURM_JOB_PARTITION:-<none>}"
echo "Nodes:           ${SLURM_JOB_NUM_NODES:-<none>}"
echo "Tasks:           ${SLURM_NTASKS:-<none>}"
echo "CPUs/task:       ${SLURM_CPUS_PER_TASK:-<none>}"
echo "Nodelist:        ${SLURM_JOB_NODELIST:-<none>}"
echo "Submit dir:      ${SLURM_SUBMIT_DIR:-$(pwd)}"   # Directory where sbatch was invoked
echo "Current host:    $(hostname)"                  # Node on which this script runs
echo "Script directory:${SCRIPT_DIR:-<not set>}"     # Custom env var if you set SCRIPT_DIR
echo

####-------------------------------------------------------------------####
#### 2) CPU topology and memory usage                                  
####-------------------------------------------------------------------####
echo "===== CPU topology & memory ====="
# Print detailed CPU info and topology
lscpu
echo "----- Free memory -----"
# Show available and used RAM
free -h
echo

####-------------------------------------------------------------------####
#### 3) GPU information                                                
####-------------------------------------------------------------------####
echo "===== GPU info (nvidia-smi) ====="
# If nvidia-smi is available, query key GPU metrics
if command -v nvidia-smi &> /dev/null; then
    nvidia-smi \
      --query-gpu=index,name,driver_version,memory.total,memory.used,utilization.gpu \
      --format=csv
else
    echo "nvidia-smi not found in PATH"
fi
echo
