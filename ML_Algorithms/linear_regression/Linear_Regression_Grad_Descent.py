
import numpy as np

class LinearRegression():
    def __init__(self):
        self.learning_rate = 0.01
        self.total_iterations = 1000
    def yhat(self, X, w):
        '''
        predicted y value
        '''
        # making sure the dimensions are correct
        # predictions: yhat = w1*x1 + w2*x2  + ... - want a scalar value for each input 
        # m - # training examples, n - # features, w - nx1, y - mx1, X - n x m, add intercept b so that X: n x m + 1
        # m x n * n x 1 = m x 1, want output to be 1 x m 
        # 1 x n * n x m - w^T*X 
        return np.dot(w.T, X)


    def loss(self, yhat, y):
        '''
        compute the loss - MSE
        '''
        L = 1/self.m * np.sum(np.power(yhat - y, 2)) # divide by number of examples, sum elementwise square of differences of the yhat - predicted and y - ground truth
        return L

    def gradient_descent(self, w, X, y, yhat):
        '''
        update the weigths based on the loss
        '''
        # again make sure the dimensions are correct
        # L = (yhat - y)  # loss : 1 x m, want the output to be n x 1 - multiply  n x m by (1 x m)^T = n x 1

        dLdw = 2/self.m * np.dot(X, (yhat - y).T) # gradient of L (loss) w.r.t. w (weights) , y = x * w + b, L = 1/m sum(yhat - y)^2 = 1/m sum(yhat - x*w+b)^2, dLdw = 2* 1/m *  x*w 

        w = w - self.learning_rate * dLdw # update step, dLdw needs to be same dimension as w - nx1

        return w 

    def main(self, X, y):        
        '''
        will call the above functions for a number of iterations
        '''
        # add intercept (bias)
        x1 = np.ones((1, X.shape[1]))
        X = np.append(X, x1, axis=0) # add to features

        self.m = X.shape[1]
        self.n = X.shape[0]

        w = np.zeros((self.n, 1))

        # iterate
        for it in range(self.total_iterations + 1):
            yhat = self.yhat(X, w)
            loss = self.loss(yhat, y)

            # PRINT
            if it % 200 == 0:
                print(f'Cost at iteration: {it} is {loss}')   

            w = self.gradient_descent(w, X, y, yhat)

        return w 

if __name__ == '__main__':
    X = np.random.rand(1, 500)
    y = 3 * X + np.random.rand(1, 500) * 0.1 # add some small random Gaussian noise
    regression = LinearRegression()
    w = regression.main(X, y)