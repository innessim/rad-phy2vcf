# rad-phy2vcf
Scripts were modified from [stevemussman/phy2vcf](https://github.com/stevemussmann/phy2vcf) to accommodate RAD-seq data.
## Overview
The primary script, `rad-phy2vcf.py`, converts a PHYLIP alignment into a synthetic single-chromosome VCF suitable for downstream tools such as [pixy](https://pixy.readthedocs.io/en/latest/index.html).
### Installation
Simply `git clone` repository into desired directory.
```
git clone https://github.com/innessim/rad-phy2vcf
```
### Basic usage
### Optional usage (recommended)
Create conda environment for `rad-phy2vcf`
```
conda create -n rad-phy2vcf
```

### Notes
- The “chromosome” in the output VCF is synthetic — created from concatenated loci from the PHYLIP alignment.
- Positions are unique and continuous to avoid compatibility issues in tools that reject identical positions.
