'''
Implementation of the (unsupervised) K-means clustering algorithm 
'''
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
class KMeansClustering():
    def __init__(self, X, k):
        self.X = X
        self.num_data_points = self.X.shape[0]
        self.num_features = self.X.shape[1] 
        self.k = k
        self.max_iter = 100
        self.plot_fig = True 

    def initialize_random_centroids(self, X):    
        '''
        randomly assign each cluster as one of the randomly selected data points features
        '''
        centroids = np.zeros((self.k, self.num_features))
        for i in range(self.k):
            centroids[i] = X[np.random.choice(range(self.num_data_points))]
        return centroids
    
    def create_clusters(self, X, centroids):
        '''
        assign each point to the closest cluster in Euclidean distance
        '''
        clusters = [[] for _ in range(self.k)]
       
        for i in range(self.num_data_points):
            closest_centroid = np.argmin(np.sqrt(np.sum((X[i] - centroids)**2, axis=1)))
            clusters[closest_centroid].append(i)

        return clusters

    def calclulate_new_centroids(self, clusters, X):
        '''
        calculate new cluster means
        '''
        centroids = np.zeros((self.k, self.num_features)) 
        for i in range(self.k):
            new_centroid = np.mean(X[clusters[i]], axis=0)
            centroids[i] = new_centroid
        return centroids
    def predict_cluster(self, clusters, X):
        '''
        for each point assign its cluster label
        '''
        y_pred = np.zeros((self.num_data_points))

        for i in range(len(clusters)):
            cluster = clusters[i]
            for ii in range(len(cluster)):
                sample_idx = cluster[ii]
                y_pred[sample_idx] = i
        return y_pred
    def plot_figure(self, X, y):
        '''
        plot the assigned clusters
        '''
        plt.scatter(X[:,0], X[:,1], cmap=plt.cm.Spectral, c=y, s=40)      
        plt.show()    

    def fit(self, X):
        '''
        train the clustering algorithm and iteratively improve the clusters
        '''
        centroids = self.initialize_random_centroids(X)

        for it in range(self.max_iter):
            clusters = self.create_clusters(X, centroids) 
            previous_centroids = centroids
            centroids = self.calclulate_new_centroids(clusters, X)

            diff = centroids - previous_centroids

            if not diff.any():
                print('Done')
                break 
        y_pred = self.predict_cluster(clusters, X)
        if self.plot_fig:
            self.plot_figure(X, y_pred)
        return y_pred

if __name__ == '__main__':
    np.random.seed(10)
    num_clusters = 5
    X, _ = make_blobs(n_samples=500, n_features=2, centers=num_clusters) # create some data

    Kmeans = KMeansClustering(X, num_clusters) 
    y_pred = Kmeans.fit(X)