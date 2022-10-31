"""
OOP Basic Statistics
author: Math & Physics Fun With Gus

A class that computes various
statistical meausrements
"""

class Stats:
    
    def __init__(self, data: list[float]):  
        
        # Run validations to the received arguments
        assert isinstance(data, list[float]), 'Please input a list for x of type int and or float.'

        # data statistics
        self.x = data
        self.n = len(data)
        self.sum = sum(data)
        self.av = self.sum / self.n
        self.vari = sum([(x - self.av)**2 for x in self.x]) / (self.n - 1)
        self.std = self.vari ** (1/2)
    
    # mean calculator
    def mean(self): 
        return self.av
    
    # sample variance calculator
    def var(self): 
        return self.vari
        
    # sample standard deviation calculator
    def sd(self): 
        return self.std
    
    # dictionary summary of data
    def summary(self):
        sum_dict = {'sum': self.sum,
                    'length': self.n,
                    'mean': self.av,
                    'variance': self.vari,
                    'standard_deviation': self.std
                    }
        return sum_dict
    
    # representing class assignement as data
    def __repr__(self) -> str:
        return f"{self.x}"
            
    
"""Dual Statistic calculator"""
class Dual_Stat(Stats):
    
    def __init__(self, data1: list[float], data2: list[float]):
        
        # Run validations to the received arguments
        assert isinstance(data1, list[float]), 'Please input a list for x of type int and or float.'
        assert isinstance(data2, list[float]), 'Please input a list for y of type int and or float.'
        # Check lengths of lists
        assert len(data1) == len(data2), 'Your lists are of different lengths.'
        
        # Length of data sets
        self.n = len(data1)
        
        # data set 1 statistics
        self.x = data1
        self.sum_x = sum(data1)
        self.av_x = self.sum_x / self.n
        self.var_x = sum([(x - self.av_x)**2 for x in self.x]) / (self.n - 1)
        self.sd_x = self.var_x ** (1/2)
        
        # y data set 2 statistics
        self.y = data2
        self.sum_y = sum(data2)
        self.av_y = self.sum_y / self.n
        self.var_y = sum([(y - self.av_y)**2 for y in self.y]) / (self.n - 1)
        self.sd_y = self.var_y ** (1/2)


    # coveriance calculator
    def cov(self):
        
        vars_mean = [(x - self.av_x) * (y - self.av_y) for x,y in zip(self.x, self.y)]
        coveriance = sum(vars_mean) / (self.n - 1)
        
        return coveriance
    
    
    # correlation calculator
    def cor(self): 
        return self.cov() / (self.sd_x * self.sd_y)
    
    
    # dictionary summary of data sets
    def summary(self):
        sum_dict = {'sum_x': self.sum_x,
                    'length_x': self.n,
                    'mean_x': self.av_x,
                    'variance_x': self.var_x,
                    'standard_deviation_x': self.sd_x,
                    'sum_y': self.sum_y,
                    'length_y': self.n,
                    'mean_y': self.av_y,
                    'variance_y': self.var_y,
                    'standard_deviation_y': self.sd_y,
                    'covariance': self.cov(),
                    'correlation': self.cor()
                    }
        return sum_dict
    
    
    # representing class assignement as data sets
    def __repr__(self) -> str:
        return f"Data 1: {self.x}\nData 2: {self.y}"
    
            
# Test here!
a = [1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 10.5]
b = [105.1, 105.2, 88.5, 84.5, 73.5]

x = [1.5, 2.5, 3.5, 4.5, 5.5]
y = [105.1, 105.2, 88.5, 84.5, 73.5]

a, b = Stats(a),  Stats(b)
relationship = Dual_Stat(x, y)

print(a, b, '\n')
print(relationship, '\n')

print(f"a summary -> {a.summary()}\n\
      b summary -> {b.summary()}\n\
      x, y summary -> {relationship.summary()}\
      \n")

print(f'Mean a = {a.mean()} and mean b = {b.mean()}\n')
print(f'Standard deviation a = {a.sd()} and for b = {b.sd()}\n')
print(f'Covariance = {relationship.cov()}')
print(f'Correlation = {relationship.cor()}')
