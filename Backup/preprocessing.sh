#!/bin/bash
#SBATCH --job-name=preprocessing
#SBATCH --time=30:00:00
#SBATCH --partition=gpu-8-v100
#SBATCH --nodelist=gpunode0
#SBATCH --gres=gpu:1
#_SBATCH --exclusive

# informando ao tch-rs que desejo compilar com cuda na versão 11.7
#export TORCH_CUDA_VERSION=cu122
export TORCH_CUDA_VERSION=cu117

srun python preprocess_hubert_f0.py