# Drug Discovery in Code

A hands-on, code-along series on **computational drug discovery** — not overviews, but the
actual workflow you can run yourself. We build one running project across 10 episodes: a
virtual-screening campaign against a real drug target (**EGFR**, the receptor behind many
lung-cancer drugs), using free, open-source Python tools.

Companion videos: **Life Sciences AI Applications** on YouTube. Each episode below has a
runnable Jupyter notebook in [`notebooks/`](notebooks).

> ⚕️ Educational only — not medical advice, and nothing here is a validated drug or protocol.

## The series

| # | Notebook | What you do |
|---|----------|-------------|
| 1 | `01_the_funnel_first_molecule.ipynb` | The workflow; load a molecule from SMILES, draw it, compute properties |
| 2 | `02_how_computers_see_molecules.ipynb` | SMILES, graphs, descriptors & fingerprints |
| 3 | `03_getting_real_data_chembl.ipynb` | Pull known EGFR actives + activities from ChEMBL |
| 4 | `04_druglikeness_and_filtering.ipynb` | Lipinski Ro5, property filters, structural alerts |
| 5 | `05_similarity_search.ipynb` | Tanimoto/fingerprints — find analogs, cluster actives |
| 6 | `06_activity_model_qsar.ipynb` | Train a scikit-learn model to predict activity |
| 7 | `07_target_in_3d_docking.ipynb` | Get a structure, prep it, dock with smina/Vina |
| 8 | `08_virtual_screening_at_scale.ipynb` | Screen a library, combine ML + docking, rank hits |
| 9 | `09_admet_and_optimization.ipynb` | ADMET prediction + multi-parameter selection |
| 10 | `10_capstone_mini_campaign.ipynb` | Full target → shortlist; where to go next |

## Setup

Everything is free and open source. With **conda** (recommended, handles RDKit cleanly):

```bash
conda env create -f environment.yml
conda activate drug-discovery-in-code
jupyter lab
```

Or with **pip** (Python 3.10+):

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
jupyter lab
```

Then open `notebooks/01_the_funnel_first_molecule.ipynb` and run along with Episode 1.

## Tools we use
- [**RDKit**](https://www.rdkit.org/) — cheminformatics (loading, drawing, descriptors, fingerprints)
- [**ChEMBL**](https://www.ebi.ac.uk/chembl/) — public bioactivity data (via `chembl_webresource_client`)
- **scikit-learn** — the activity/QSAR models
- **smina / AutoDock Vina** — molecular docking (added in Ep 7)
- **pandas / matplotlib** — data wrangling and plots

## License
MIT — see [LICENSE](LICENSE). Use the code freely.
