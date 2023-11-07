"""Your task is to build a model1 which can predict y-coordinate.
You can pass tests if predicted y-coordinates are inside error margin.


You will receive train set which should be used to build a model.
After you build a model tests will call function predict and pass x to it.


Error is going to be calculated with RMSE.




Blocked libraries: sklearn, pandas, tensorflow, numpy, scipy

Explanation
[1] A mining model is created by applying an algorithm to data, but it is more than an
algorithm or a metadata container: it is a set of data, statistics, and patterns that
can be applied to new data to generate predictions and make inferences about relationships."""

class Datamining:

    def __init__(self, train_set):
        self.train_set = train_set
        # should build a linear regression model
        
        
        x_train = [x for x, y in train_set]
        y_train = [y for x, y in train_set]
        
        x_train_mean = sum(x_train) / len(x_train)
        y_train_mean = sum(y_train) / len(y_train)
        
        self.a = self.get_a(x_train, x_train_mean, y_train, y_train_mean)
        self.b = self.get_b(x_train_mean, y_train_mean, self.a)
        
        

    def linear(self, x, a, b):
            return a*x + b
        
    def get_a(self, x_i, x_mean, y_i, y_mean):
        x_variances = sum([(x - x_mean)**2 for x in x_i])
        xy_covariances = sum([(x - x_mean) * (y - y_mean) for x, y in zip(x_i, y_i)])
        
        return xy_covariances / x_variances
    
    def get_b(self, x_mean, y_mean, a):
        return y_mean - a * x_mean
    

    def predict(self, x):
        y_hat = self.linear(x, self.a, self.b)
        return y_hat