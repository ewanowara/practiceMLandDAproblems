'''
Implementation of KNN - K-Nearest Neighbors Algorithm
'''
import numpy as np

class KNearestNeighbor():
    def __init__(self, k):
        self.k = k
        
    def train(self, X, y):
        '''
        Train the model
        '''
        self.X_train = X
        self.y_train  = y
        
    def predict(self, X_test):
        '''
        Predict labels on the test set
        '''
        distances = self.compute_distance(X_test)
        y_pred = self.predict_labels(distances)
        return y_pred
    def compute_distance(self, X_test):
        '''
        Compute distance (Euclidean) between the points
        '''
        label = []
        num_train = self.X_train.shape[0]
        num_test = X_test.shape[0]
        distances = np.zeros((num_test, num_train))

        for i in range(num_test):
              distances[i,:] = np.sqrt(np.sum((self.X_train - X_test[i,:]) ** 2, axis=1))                
        return distances    

    def predict_labels(self, distances):
        '''
        Assign labels of the closest points 
        '''
        num_test = distances.shape[0]
        y_pred = np.zeros(num_test)
        
        for i in range(num_test):
            y_indices = np.argsort(distances[i,:]) 

            k_closest_classes = self.y_train[y_indices[: self.k]].astype(int)
            y_pred[i] = np.argmax(np.bincount(k_closest_classes))

        return y_pred

if __name__ == "__main__":
    X = np.loadtxt("example_data/data.txt", delimiter=",")
    y = np.loadtxt("example_data/targets.txt")

    X = np.array([[1, 1], [3, 1], [1, 4], [2, 4], [3, 3], [5, 1]])
    y = np.array([0, 0, 0, 1, 1, 1])

    KNN = KNearestNeighbor(k=1)
    KNN.train(X, y)
    y_pred = KNN.predict(X)
    print(f"Accuracy: {sum(y_pred == y) / y.shape[0]}")
