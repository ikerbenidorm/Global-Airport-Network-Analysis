# Global-Airport-Network-Analysis

## Overview
This repository analyzes the worldwide airport network using complex network theory. It collects, processes, and visualizes global airport and flight route data, with statistical calculations performed in Python and presented in interactive reports.

## Repository Structure
- **reports/**: Final reports and drafts.
- **docs/**: Interactive HTML and PNG visualizations for airport network structures and communities.
- **notebooks/**: Jupyter notebook containing all detailed calculations.
- **scripts/**: Python scripts for data download and processing:
    - `download_data.py`: Downloads OpenFlights datasets.
    - `process_data.py`: Cleans and builds the airport network graph.
- **results/**: Figures and tables output from analyses.
- **data/**: Raw and processed data files.

---

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/ikerbenidorm/Global-Airport-Network-Analysis.git
cd Global-Airport-Network-Analysis
```

### 2. Create and activate the environment with Conda
Make sure you have [Miniconda](https://docs.conda.io/en/latest/miniconda.html) or [Anaconda](https://docs.anaconda.com/anaconda/install/) installed.

Create the environment from `environment.yml`:

```bash
conda env create -f environment.yml
conda activate airport-net
```

### 3. Run scripts
- Download raw data:
```bash
python scripts/download_data.py
```
- Process and analyze data:
```bash
python scripts/process_data.py
```
- Explore results with the Jupyter notebook:
```bash
jupyter notebook notebooks/Global_Airport_Network_Analysis_November2025.ipynb
```

---

## Citation

If you use this repository, please cite as follows:

```bibtex
@misc{GlobalAirportNetworkAnalysis2025,
author = {Iker Lomas Javaloyes},
title = {Global Airport Network Analysis},
year = {2025},
howpublished = {\url{https://github.com/ikerbenidorm/Global-Airport-Network-Analysis}}
}
```
