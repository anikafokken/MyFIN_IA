from abc import ABC, abstractmethod


class UserRule:
    def __init__(self, name, mode, extractor, min_value=0.0, max_value=0.0, operator=None, weight=1.0, minimize=False, data_type="NUMERIC"):
        self.name = name
        self.mode = mode
        self.min_value = min_value
        self.max_value = max_value
        self.weight = weight
        self.extractor = extractor
        self.operator = operator
        self.minimize = minimize
        self.data_type = data_type

class Constraint():
    def is_satisfied(self, student, program) -> bool:
        pass

class Factor(ABC):
    def __init__(self, weight: float = 1.0):
        self.weight = weight
    
    @abstractmethod
    def score(self, assignment) -> float: # in range 0-1
        pass

class ComparisonConstraint(Constraint):
    # extractor gets the values, operator compares them
    def __init__(self, extractor, operator):
        self.extractor = extractor
        self.operator = operator
    
    def is_satisfied(self, student, program):
        left, right = self.extractor(student, program)
        return self.operator(left, right) # i.e. operator.ge (greater or equal to)

class NumericPreferenceFactor(Factor):
    def __init__(self, extractor, name, min_value, max_value, weight=1.0, minimize=False):
        self.extractor = extractor
        self.name = name
        self.weight = weight
        self.minimize = minimize
        self.min_value = min_value
        self.max_value = max_value
    
    def normalize(self, value):
        if self.min_value == self.max_value:
            return 0
        norm = (value - self.min_value) / (self.max_value - self.min_value)
        if self.minimize:
            norm = 1 - norm
        
        return max(0, min(1, norm))

    def score(self, student, program):
        raw_value = self.extractor(student, program)
        normalized_value = self.normalize(raw_value)
        return self.weight * normalized_value

class SelectionPreferenceFactor(Factor):
    def __init__(self, name, extractor, weight=1.0):
        self.extractor = extractor
        self.name = name
        self.weight = weight
    
    def score(self, student, program):
        value = self.extractor(student, program)
        return self.weight * value

