# rad-phy2vcf
Scripts were modified from [stevemussman/phy2vcf](https://github.com/stevemussmann/phy2vcf) to accommodate RAD-seq data.

## Overview
The primary script, `rad-phy2vcf`, converts a PHYLIP alignment into a synthetic single-chromosome VCF with invariant sites retained. This output is suitable for downstream tools such as [pixy](https://pixy.readthedocs.io/en/latest/index.html).

### Installation
Simply clone the repository into desired directory:
```
git clone https://github.com/innessim/rad-phy2vcf.git /path/to/software/rad-phy2vcf
```
### Basic usage
Can be used from inside the repository directory:
```
rad-phy2vcf --help
```
> Note: If running from other directories, you will need to specify the full path to the script or have it in your `PATH`

### Optional usage (recommended)
To run the software conveniently from anywhere, create a dedicated conda environment and symlink the scripts into its `bin` directory:
```
conda create -n rad-phy2vcf
conda activate rad-phy2vcf

mkdir -p $CONDA_PREFIX/bin
ln -s /path/to/software/rad-phy2vcf/*.py "$CONDA_PREFIX/bin/"
ln -s /path/to/software/rad-phy2vcf/rad-phy2vcf "$CONDA_PREFIX/bin/rad-phy2vcf"
```
Now you can run the software from any directory while the conda environment is active:
```
rad-phy2vcf --help
```

> - The “chromosome” in the output VCF is synthetic — derived from the single concatenated sequence of loci present in the input PHYLIP alignment.
> - Positions are made unique and continuous to avoid compatibility issues with tools that reject identical positions.
