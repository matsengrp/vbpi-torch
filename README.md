# vbpi-torch
Pytorch Implementation of Variational Bayesian Phylogenetic Inference


## Dependencies

* [Biopython](http://biopython.org)
* [bitarray](https://pypi.org/project/bitarray/)
* [dendropy](https://dendropy.org)
* [ete3](http://etetoolkit.org)
* [PyTorch](https://pytorch.org/)

You can build and enter a conda environment with all of the dependencies built in using the supplied `environment.yml` file via:

```
conda env create -f environment.yml
conda activate vbpi-torch
```


## Preparation

Unzip `DENV4_constant_golden_run.trees.zip` in the `rooted/data/DENV4` directory.


## Running

Examples:

In the unrooted/ folder

```bash
python main.py --dataset DS1 --psp --empFreq
python main.py --dataset DS1 --psp --nParticle 20 --gradMethod rws --empFreq
python main.py --dataset flu100 --psp
python main.py --dataset flu100 --psp --supportType mcmc -cf 100000
```

In the rooted/ folder
```bash
python main.py --dataset DENV4 --burnin 2501 --coalescent_type constant --clock_type strict --init_clock_rate 1e-3 --sample_info --psp --empFreq
python main.py --dataset HCV --burnin 251 --coalescent_type skyride --clock_type fixed_rate --init_clock_rate 7.9e-4 --psp
```

## To sample trees for comparison with generalized pruning

In the unrooted/ folder

```bash
python main.py --dataset DS1 --psp --supportType long_mcmc --maxIter 200000 --sampleTrees 1000000 --outgroup 15
python main.py --dataset DS3 --psp --supportType long_mcmc --maxIter 200000 --sampleTrees 1000000 --outgroup 7
python main.py --dataset DS4 --psp --supportType long_mcmc --maxIter 200000 --sampleTrees 1000000 --outgroup 8
python main.py --dataset DS5 --psp --supportType long_mcmc --maxIter 200000 --sampleTrees 1000000 --outgroup 1
python main.py --dataset DS6 --psp --supportType long_mcmc --maxIter 200000 --sampleTrees 1000000 --outgroup 6
python main.py --dataset DS7 --psp --supportType long_mcmc --maxIter 200000 --sampleTrees 1000000 --outgroup 7
python main.py --dataset DS8 --psp --supportType long_mcmc --maxIter 200000 --sampleTrees 1000000 --outgroup 4
```

To then get the average branch length (per PCSP or SDAG edge) in a GP comparable format, we require the bito python module.
See https://github.com/phylovi/bito for installation and details. 
With this module installed, in the unrooted/ folder

```bash
python convert_vbpi_to_gp.py results/vbpi_sampled_trees_ds1.nwk data/long_mcmc/ds1/ds1.fasta results/vbpi_ds1_branch_parameters.csv results/vbpi_ds1_taxon_order.txt 
python convert_vbpi_to_gp.py results/vbpi_sampled_trees_ds3.nwk data/long_mcmc/ds3/ds3.fasta results/vbpi_ds3_branch_parameters.csv results/vbpi_ds3_taxon_order.txt
python convert_vbpi_to_gp.py results/vbpi_sampled_trees_ds4.nwk data/long_mcmc/ds4/ds4.fasta results/vbpi_ds4_branch_parameters.csv results/vbpi_ds4_taxon_order.txt
python convert_vbpi_to_gp.py results/vbpi_sampled_trees_ds5.nwk data/long_mcmc/ds5/ds5.fasta results/vbpi_ds5_branch_parameters.csv results/vbpi_ds5_taxon_order.txt
python convert_vbpi_to_gp.py results/vbpi_sampled_trees_ds6.nwk data/long_mcmc/ds6/ds6.fasta results/vbpi_ds6_branch_parameters.csv results/vbpi_ds6_taxon_order.txt
python convert_vbpi_to_gp.py results/vbpi_sampled_trees_ds7.nwk data/long_mcmc/ds7/ds7.fasta results/vbpi_ds7_branch_parameters.csv results/vbpi_ds7_taxon_order.txt
python convert_vbpi_to_gp.py results/vbpi_sampled_trees_ds8.nwk data/long_mcmc/ds8/ds8.fasta results/vbpi_ds8_branch_parameters.csv results/vbpi_ds8_taxon_order.txt
```





