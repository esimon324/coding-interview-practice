class TempTracker:
    def __init__(self):
        self.sum = 0.0
        self.seen = 0
        self.max = -1
        self.min = 111
        self.freq = [0 for i in range(111)]
        self.mode = 0
    
    def insert(self,temp):
        if temp >= 0 and temp < 111:
            self.sum += temp
            self.seen += 1
            
            if temp > self.max:
                self.max = temp
                
            if temp < self.min:
                self.min = temp
                
            self.freq[temp] += 1
            if self.freq[temp] > self.freq[self.mode]:
                self.mode = temp
    
    def get_max(self):
        return self.max
    
    def get_min(self):
        return self.min
        
    def get_mode(self):
        return self.mode
        
    def get_mean(self):
        return self.sum / self.seen
        
    def print_tracker(self):
        print 'Max Temp:',self.get_max()
        print 'Min Temp:',self.get_min()
        print 'Mean Temp:',self.get_mean()
        print 'Mode Temp:',self.get_mode()