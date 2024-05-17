# Prolog IPython magic

- Extension to add a magick which helps defining some shell commands to be ran before the kernel start.

- Can be useful if you wish to define some environment variables or use [lmod](https://lmod.readthedocs.io/en/latest/) in the context of HPC


## Installation

`pip install jupyter-prolog`


## Usage

Use it in your Jupyter lab/notebook with IPython kernel:

```
In [1]: %load_ext jupyter-prolog                                       

In [2]: %%prolog 
   ...: module load PyTorch/2.1.2-foss-2023a-CUDA-12.1.1
```
