# Module 1 Exam Instructions **IMPORTANT**

For all projects, you may use your own Unix-based system and, where applicable, ensure that you are running the version of the software specified in the assignments. Alternatively, you may use the VMBox virtual machine environment provided with the course materials. Instructions on how to download and use the environment can be found on the course web site. 

For the following questions, refer to the class workflow and use the data in the Online materials (`gencommand_proj1_data.tar.gz`) to answer the questions. Assume you sequenced and assembled the genome of Malus domestica (apple), and performed gene annotation. You then collected samples and ran RNA-seq experiments to determine sets of genes that are expressed in the various tissues. This information was stored, respectively, in the following files: “apple.genome”, “apple.genes”, “apple.condition{A,B,C}”. 

NOTE: The apple genome and the apple gene annotations for this project were extracted from the Rosaceae Genome Database (RGD). Actual data have then been modified, and hence may not directly reflect the information in the original RGD records.

### Question 1 : How many chromosomes are there in the genome?
> grep '>' apple.genome | wc -l

> grep -c ">" apple.genome 
### `Ans : 3`

### Question 2 : How many genes?
> cut -f1 apple.genes | sort -u | wc -l
### `Ans: 5354`

### Question 3 : How many transcript variants?
> cut -f2 apple.genes | sort -u | wc -l
### `Ans: 5456`

### Question 4 : How many genes have a single splice variant?
> cut -f1 apple.genes | sort | uniq -c | grep ' 1 ' | wc -l
### `Ans: 5450`

### Question 5 : How many genes have 2 or more splice variants?
> cut -f1 apple.genes | sort | uniq -c | grep -v ' 1 ' | wc -l
### `Ans: 3`

### Question 6 : How many genes are there on the `+` strand?
> cut -f1,4 apple.genes | sort -u | cut -f2 | sort | uniq -c
### `Ans: 2791 - 2662 +`

### Question 7 : How many genes are there on the `-` strand?
> cut -f1,4 apple.genes | sort -u | cut -f2 | sort | uniq -c
### `Ans: 2791 - 2662 +`

### Question 8: How many genes are there on chromosome chr1?
> cut -f1,3 apple.genes | sort -u | cut -f2 | sort | uniq -c
### `Ans: 1624 chr1 2058 chr2 1771 chr3`

### Question 9: How many genes are there on each chromosome chr2?
> cut -f1,3 apple.genes | sort -u | cut -f2 | sort | uniq -c
### `Ans: 1624 chr1 2058 chr2 1771 chr3`

### Question 10: How many genes are there on each chromosome chr3?
> cut -f1,3 apple.genes | sort -u | cut -f2 | sort | uniq -c
### `Ans: 1624 chr1 2058 chr2 1771 chr3`

### Question 11: How many transcripts are there on chr1?
> cut -f2,3 apple.genes | cut -f2 | sort | uniq -c
>  cut -f2,3 apple.genes | sort -u | cut -f2 | sort | uniq -c
### `Ans: `
```
    1625 chr1
    2059 chr2
    1772 chr3
```

### Question 12: How many transcripts are there on chr2?
> cut -f2,3 apple.genes | cut -f2 | sort | uniq -c
>  cut -f2,3 apple.genes | sort -u | cut -f2 | sort | uniq -c
### `Ans: `
```
    1625 chr1
    2059 chr2
    1772 chr3
```
## Question 13: How many transcripts are there on chr3?
> cut -f2,3 apple.genes | cut -f2 | sort | uniq -c
>  cut -f2,3 apple.genes | sort -u | cut -f2 | sort | uniq -c
### `Ans: `
```
    1625 chr1
    2059 chr2
    1772 chr3
```
### Question 14: How many genes are in common between condition A and condition B?
> cut -f1 apple.conditionA | sort -u > apple.condA.sorted.genes
> cut -f1 apple.conditionB | sort -u > apple.condB.sorted.genes
> comm -1 -2 apple.condA.sorted.genes apple.condB.sorted.genes | wc -l

### `Ans:  2410`

### Question 15: How many genes are specific to condition A? 
> comm -3 -1 apple.condA.sorted.genes apple.condB.sorted.genes | wc -l
### `Ans:  1205`

### Question 16: How many genes are specific to condition B? 
> comm -3 -1 apple.condA.sorted.genes apple.condB.sorted.genes | wc -l
### `Ans:  1243`

### Question 17: How many genes are in common to all three conditions?
> cut -f1 apple.conditionC | sort -u > apple.condC.sorted.genes
> cat apple.cond{A,B,C}.sorted.genes | sort | uniq -c | grep -c " 3 "
### `Ans:  1608`