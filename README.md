# PLDLS-Algorithm
PLDLS: A Novel Parallel Label Diffusion and Label Selection-based Community Detection Algorithm Based on Spark in Social Networks

This is the soure code for Spark implementation of PLDLS algorithm for fast community detection. Furthuremore at the end of the source code, we have written Parallel modularity computing which can be used in any researches to calculate time consuming modularity in a short time.

We have provided both source code and compiled file for PLDLS algorithm. After installing and configuring Spark, for testing PLDLS from the source code which is written in Scala, intellij IDE can be used and plugins related to scala should be installed.

To execute PLDLS on a cluster of computers, after installing Spark on the cluster, PLDLS.jar file can be used to execute it with spark-submit. Execution guidleins with spark-submit is prepared in "spark_submit_guide.txt" file. To execute PLDLS, 7 configurations should be applied which are as follows:

1) The path to the input file (path to datasets.)

2) Number of iteration for fast label selection step

3) Number of iteration for improved label propagation step

4) merge_flag ==> set to 1 to perform merge step ans set to 0 to not to perform merge step

5) modularity_flag ==> set to 1 to calculate step ans set to 0 to not to perform merge step

6) writeToDisk_flag

7) Path to output folder to write the RDD which contains the label of nodes

We have used neighboring list structure as the input file for algorithm. The execution of the LSMD is so simple. To execute the code, it is needed to put extracted folder of "datasets.rar" into one folder with the extracted source codes of "LSMD_CommunityDetection_Algorithm.rar". Then open "main_algorithm.m" to write dataset name in "dataset_name" variable to start execution. In some datasets it is not necessary to execute merge step which it can be controled by "merge_flag" before execution. The output of the algorithm is label array of nodes which is written in "results" folder in ascending based on nodes number.


Names of datasets are as follows and are available in "datasets" folder.

# Datasets:

karate

Dolphins

Polbooks

Football

email

email_enron

netscience

power

ca_grqc

collaboration

ca_hepth

PGP

condmat_2003

condmat_2005

DBLP

Amazon
