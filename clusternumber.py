
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt


data = pd.read_csv('ClusterPlot.csv') #reading in the file cluster plot using read function

data.describe()

#Scaling each feature to a given range using minmaxscalar function
#Using fit and tranform functions to transform the data to standardized version
neutral = MinMaxScaler() 
neutral.fit(data)
standardized_data = neutral.transform(data)

#Giving a specific range for the cluster k from 1 to 10
K = range(1, 8)


sumsquaredistance = []

#Using elbow Method(Kmeans) to find the number of clusters
#Using append() to modify the data until the cluster groups are found
#Using inertia to find the sum of squared error for each cluster 
for k in K:
    kvalue = KMeans(n_clusters = k)
    kvalue  = kvalue.fit(standardized_data)
    sumsquaredistance.append(kvalue.inertia_)
    

print("Number of clusters:", kvalue ) # Printing the number of clusters found 

#Plotting the graph of the clusters using plt 
plt.plot(K, sumsquaredistance, 'bx-')
plt.xlabel('No. Of Clusters')
plt.ylabel('Sum of the Squared Distances')
plt.title('Elbow Method for the Optimal k value')
plt.show()

#adding labels for each group of cluster
data['labels'] = kvalue.labels_
print(kvalue.labels_)

#Centroid values of the data for the clusters
centroids = kvalue.cluster_centers_
centroids = pd.DataFrame(centroids, columns=['V1 Centroid', 'V2 Centroid'])
print(centroids)
