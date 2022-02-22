# Troubleshooting

### 1. How to Install `R` on Jupyter Notebook in using `Anaconda`?

1. Open 'Anaconda Command Prompt' & execute conda update notebook to update your Jupyter notebook to the most recent version.
2. Then install IRkernel by `conda install -c r notebook r-irkernel`
3. Now you may open R in your command prompt by running R.exe
4. Install all necessary R packages using the following lines in the R console by executing :
```{r}
install.packages(c('repr', 'IRdisplay', 'evaluate', 'crayon', 'pbdZMQ', 
'devtools', 'uuid', 'digest'))

devtools::install_github('IRkernel/IRkernel')`
```
5. Finally, make the R kernel available to your Jupyter Notebook by executing:
- Install only for the current user ➡ `IRkernel::installspec()`
- For System-wide installation(all Users) ➡ `IRkernel::installspec(user = FALSE)`
