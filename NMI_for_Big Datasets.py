from numpy import loadtxt
from sklearn.metrics.cluster import normalized_mutual_info_score
# dataset_name is: amazon, dblp, youtube, livejournal

dataset_name = 'dataset_name'
nodes_map = loadtxt("./groundtruth/nodes_map/" + dataset_name + "_nodes_map.txt", comments="#", delimiter="\t", unpack=False)
results = loadtxt("./part-00000", comments="#", delimiter=",", unpack=False)

nodes_final_label = []
for i in nodes_map:
    nodes_final_label.append(results[int(i)])
    
real_labels= loadtxt("./groundtruth/"+dataset_name+"_real_labels.txt", comments="#", delimiter="\t", unpack=False)
normalized_mutual_info_score(nodes_final_label,real_labels)