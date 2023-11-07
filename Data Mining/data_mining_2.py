"""
Your task is to build a model1 which can predict y-coordinate.
You can pass tests if predicted y-coordinates are inside error margin.


You will receive train set which should be used to build a model.
After you build a model tests will call function predict and pass x to it.


Error is going to be calculated with RMSE.


Side note: Points in test cases are from different polynomials (up to 5th degree).




Easier version: Data mining #1




Blocked libraries: sklearn, pandas, tensorflow, numpy, scipy

Explanation
[1] A mining model is created by applying an algorithm to data, but it is more than an algorithm
or a metadata container: it is a set of data, statistics, and patterns that can be applied to new data
to generate predictions and make inferences about relationships.
"""

"""
up to n**5 polynomials - we will need polynomial regression.

f(x) = c_0 + c_1 * x + c_2 * x**2 + c_3 * x**3 + c_4 * x**4 + c_5 * x**5 + ... + c_n * x**n


We have two approaches - we can assume that every polynomial can be fit to the 5th degree,
or we can use cubic splines to fit the data irrespective of the degree of the polynomial.
"""
    

test_data = [(1,4),(4,4),(2,2),(3,2),(5,2)]

class Datamining5thPolynomial:
    # had to use Co-Pilot for the transform section...
    DEGREE = 5
    
    def __init__(self, train_set, learning_rate=0.01, iterations=10):
        self.train_set = train_set
        self.learning_rate = learning_rate
        self.iterations = iterations
        
        self.elements = len(train_set)
        
        #initialise mutables
        self.weights = [0] * (self.DEGREE + 1)
        
        #manage data
        x_train = [x for x, y in train_set]
        y_train = [y for x, y in train_set]
        x_train_transformed = self.transform(x_train)
        x_train_normalised = self.normalise(x_train_transformed)
        
        self.fit(x_train_transformed, y_train)
        

        
    def fit(self, x_normalised, y_train):
        
        for iteration in range(self.iterations):
            print("-----------------------")
            print("Iteration:", iteration)
            hat = self.predict(x_normalised)
            error = [hat_i - y_i for hat_i, y_i in zip(hat, y_train)]
            
            
            # Transpose of x_normalised
            # The * operator is used to unpack the lists in x_normalised
            # The zip function then pairs up the corresponding elements from each list
            # The map function applies the list function to each pair, converting the pairs back into lists
            # The result is a new list of lists, where the i-th list contains the i-th element from each original list
            # This effectively transposes the original list of lists
            x_normalised_transpose = list(map(list, zip(*x_normalised)))

            # Dot product of x_normalised_transpose and error
            # For each row in x_normalised_transpose, we pair up the elements in the row with the elements in error
            # We then multiply each pair of elements together and sum the results
            # The result is a new list, where the i-th element is the dot product of the i-th row of x_normalised_transpose and error
            dot_product = [sum(x * e for x, e in zip(row, error)) for row in x_normalised_transpose]

            # Update weights
            # For each weight and corresponding element in the dot product, we subtract the product of the learning rate, the reciprocal of the number of elements, and the dot product element from the weight
            # The result is a new list of weights
            print("Weights Prior", self.weights)
            self.weights = [weight - self.learning_rate * (1 / self.elements) * dot_product_element for weight, dot_product_element in zip(self.weights, dot_product)]
            print("Weights Post", self.weights)
        return self
        

    
    def transform(self, X_input):
        
        # If X_input is a single number, convert it to a list
        if isinstance(X_input, (int, float)):
            X_input = [X_input]
            
        # Initialize an empty list to store the transformed data
        transformed_data = []

        # Check if X_input is a list of lists
        if all(isinstance(i, list) for i in X_input):
            # Loop over each data point in the dataset
            for datapoint in X_input:
                # Initialize an empty list to store the transformed features for this data point
                transformed_datapoint = []

                # Loop over each feature in the data point
                for feature in datapoint:
                    # Transform the feature by raising it to the power of each degree
                    transformed_feature = [feature ** degree for degree in range(self.DEGREE + 1)]

                    # Add the transformed feature to the list of transformed features for this data point
                    transformed_datapoint.extend(transformed_feature)

                # Add the transformed data point to the list of transformed data
                transformed_data.append(transformed_datapoint)
        else:
            # Loop over each data point in the dataset
            for datapoint in X_input:
                # Transform the x feature by raising it to the power of each degree
                transformed_feature = [datapoint ** degree for degree in range(self.DEGREE + 1)]

                # Add the transformed feature to the list of transformed data
                transformed_data.append(transformed_feature)

        return transformed_data
    
    def normalise(self, X_transformed) -> list:
        
        def mean(X):
            return sum(X) / len(X)
        
        def std_dev(X):
            return (sum([(x - mean(X))**2 for x in X]) / len(X))**0.5
        
        
        # Initialize an empty list to store the normalized data
        normalized_data = []

        # Loop over each data point in the dataset
        for i in range(len(X_transformed)):
            # Initialize an empty list to store the normalized features for this data point
            normalized_data_point = []
            
            # Loop over each feature of this data point
            for j in range(len(X_transformed[i])):
                # Calculate the mean and standard deviation of the j-th feature across all data points
                feature_values = [x[j] for x in X_transformed]
                feature_mean = mean(feature_values)
                feature_std_dev = std_dev(feature_values)
                
                # Check if standard deviation is zero
                if feature_std_dev == 0:
                    feature_std_dev = 1e-7  # add a small constant to avoid division by zero
                
                # Normalize the j-th feature of the i-th data point
                normalized_feature = (X_transformed[i][j] - feature_mean) / feature_std_dev
                
                # Add the normalized feature to the list of normalized features for this data point
                normalized_data_point.append(normalized_feature)
            
            # Add the normalized data point to the list of normalized data
            normalized_data.append(normalized_data_point)
        
        print("normalised data:", normalized_data)
        return normalized_data
    
        
        
    def predict(self, x) -> list:
        # should return predicted y
        x_transformed = self.transform(x)
        x_normalised = self.normalise(x_transformed)
        
        # Dot product of x_normalised and weights
        # For each row in x_normalised, we pair up the elements in the row with the elements in weights
        # We then multiply each pair of elements together and sum the results
        # The result is a new list, where the i-th element is the dot product of the i-th row of x_normalised and weights
        dot_product = [sum(x * w for x, w in zip(row, self.weights)) for row in x_normalised]
        
        return dot_product
        
    

        
model = Datamining5thPolynomial(test_data)
model.predict(1)
model.predict(2)
model.predict(3)


# class DataMiningCubicSpline():
    
#     def __init__(self, train_set):
#         self.train_set = train_set
        
#         self.x = [x for x, y in train_set]
#         self.y = [y for x, y in train_set]
        
#         self.b, self.c, self.d = self.cubic_spline()
    
#     def jacobi(A, b, x0, tolerance=1e-10, max_iterations=300):
#         n = len(A)
#         x = x0[:]
#         for k in range(max_iterations):
#             x_new = x0[:]
#             for i in range(n):
#                 s = sum(A[i][j] * x[j] for j in range(n) if i != j)
#                 x_new[i] = (b[i] - s) / A[i][i]
#             if all(abs(x_new[i]-x[i]) < tolerance for i in range(n)):
#                 return x_new
#             x = x_new
#         return x

#     def cubic_spline(self):
#         n = len(self.x) - 1
#         h = [self.x[i+1] - self.x[i] for i in range(n)]
#         alpha = [3*((self.y[i+2]-self.y[i+1])/h[i+1] - (self.y[i+1]-self.y[i])/h[i]) for i in range(n-1)]
#         l = [2*(h[i]+h[i+1]) for i in range(n-1)]
#         mu = [h[i+1]/l[i] for i in range(n-1)]
#         z = [alpha[i]/l[i] for i in range(n-1)]
#         for i in range(1, n-1):
#             l[i] = l[i] - mu[i-1]*h[i]
#             z[i] = (alpha[i] - h[i]*z[i-1])/l[i]
#         b = [0]*(n+1)
#         c = [0]*(n+1)
#         d = [0]*n
#         for i in range(n-1, -1, -1):
#             c[i] = z[i] - mu[i]*c[i+1]
#             b[i] = (self.y[i+1] - self.y[i])/h[i] - h[i]*(c[i+1] + 2*c[i])/3
#             d[i] = (c[i+1] - c[i])/(3*h[i])
#         return b, c, d
        
# model = DataMiningCubicSpline(test_data)
# model.predict(1)