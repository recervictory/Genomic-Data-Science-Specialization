## Installing Bioconductor in R
1. To install core packages, type the following in an R command window:
   
```
if (!require("BiocManager", quietly = TRUE))
    install.packages("BiocManager")
BiocManager::install()
```
1. Install specific packages, e.g., “GenomicFeatures” and “AnnotationDbi”, with
   
```
BiocManager::install(c("GenomicFeatures", "AnnotationDbi"))
```
