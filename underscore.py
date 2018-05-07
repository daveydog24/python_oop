class Underscore(object):
    def map(self, list, x):
        self.new_array = filter(x, list)
        return self.new_array

    def reduce(self, list, x):
        self.list = list
        self.sum = 0
        for i in self.list:
            if x(i) == True:
                self.sum += self.list[i-1]
        return self.sum

    def find(self, list, x):
        for i in list:
            if x(i) == True:
                return i
        return undefined

    def filter(self, list, x):
        self.new_list =[]
        for i in list:
            if x(i) == True:
                self.new_list.append(i)
        return self.new_list

    def reject(self, passed_list, x):
        self.new_list = []
        for i in passed_list:
            if x(i) == False:
                self.new_list.append(i)
        return self.new_list

_ = Underscore()
mapped = _.reduce([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
reduced =  _.reduce([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
find = _.find([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
evens = _.filter([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
reject_odds = _.reject([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)
print mapped, reduced, find, evens, reject_odds