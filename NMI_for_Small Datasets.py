from numpy import loadtxt
from sklearn.metrics.cluster import normalized_mutual_info_score
# dataset_name is: karate, dolphins, polbooks, football

dataset_name = 'dataset_name'
real_labels= loadtxt("./groundtruth/"+dataset_name+"_real_labels.txt", comments="#", delimiter="\t", unpack=False)
results = loadtxt("./part-00000", comments="#", delimiter=",", unpack=False)    
normalized_mutual_info_score(results,real_labels)