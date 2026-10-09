import scanpy as sc

# 1. Load a standard single-cell dataset (built into scanpy)
adata = sc.datasets.pbmc3k()

# 2. Preprocess the genomic data
sc.pp.filter_cells(adata, min_genes=200)      # Remove poor-quality cells
sc.pp.filter_genes(adata, min_cells=3)        # Remove inactive genes
sc.pp.normalize_total(adata, target_sum=1e4)  # Normalize read counts
sc.pp.log1p(adata)                            # Log-transform the data

# 3. Dimensionality Reduction (PCA)
# Gene data has 20,000+ dimensions; PCA compresses it down
sc.tl.pca(adata, svd_solver='arpack')

# 4. Clustering (Using the Louvain or Leiden algorithm)
sc.pp.neighbors(adata, n_neighbors=10, n_pcs=40)
sc.tl.leiden(adata)  # Groups cells based on gene expression profiles

# 5. Visualize the discovered cell clusters in 2D space
sc.tl.umap(adata)
sc.pl.umap(adata, color=['leiden'])
