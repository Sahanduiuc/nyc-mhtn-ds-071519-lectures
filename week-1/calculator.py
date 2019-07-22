class Calculator():
    def __init__(self, data):
        print(data)
        self.update_stats(data)
        
    # updates the current date set with newly added data if any    
    def update_stats(self, data):
        self.data = data
        self.length = len(data)
        self.mean = self.calc_mean()
        self.median = self.calc_med()
        self.variance = self.calc_variance()
        self.standev = self.std_dev()
        
    def calc_mean(self):
        data = self.data
        return float(sum(data)/len(data))
    
    
    def calc_med(self):
        data = self.data
        if len(data) % 2 == 0:
            m = int(len(data)/2)
            ans = (data[m-1]+data[m])/2
        elif len(data) % 2 != 0:
            ans = data[int((len(data)-1)/2)]
        return ans
    
    def calc_variance(self):
        data = self.data
        mean = self.mean
        return sum([(i-mean)**2 for i in data])/(len(data)-1)

    def std_dev(self):
        return self.variance**0.5
    
    def add_data(self, data):
        self.data.append(data)
        self.update_stats(self.data)
        
    def remove_data(self, data):
        self.data.remove(data)
        self.update_stats(self.data)
        
    