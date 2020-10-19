import abc

class IList(metaclass=abc.ABCMeta):
    @classmethod
    def __subclasshook__(cls, subclass):
        return (hasattr(subclass, 'insert_at') and callable(subclass.insert_at) and
                hasattr(subclass, 'add_front') and callable(subclass.add_front) and
                hasattr(subclass, 'add_back') and callable(subclass.add_back) and
                hasattr(subclass, 'remove') and callable(subclass.remove) and
                hasattr(subclass, 'remove_front') and callable(subclass.remove_front) and
                hasattr(subclass, 'remove_back') and callable(subclass.remove_back) and
                hasattr(subclass, 'get') and callable(subclass.get) and
                hasattr(subclass, 'put') and callable(subclass.put) and
                hasattr(subclass, 'find') and callable(subclass.find) and
                hasattr(subclass, 'concat') and callable(subclass.concat) and
                hasattr(subclass, 'length') and callable(subclass.length) and
                hasattr(subclass, 'is_empty') and callable(subclass.is_empty) or NotImplemented)

    @abc.abstractmethod
    def insert_at(self, item, index):
        raise NotImplementedError


    @abc.abstractmethod
    def add_front(self, item):
        raise NotImplementedError


    @abc.abstractmethod
    def add_back(self, item):
        raise NotImplementedError


    @abc.abstractmethod
    def remove(self, index):
        raise NotImplementedError


    @abc.abstractmethod
    def remove_front(self):
        raise NotImplementedError


    @abc.abstractmethod
    def remove_back(self):
        raise NotImplementedError


    @abc.abstractmethod
    def get(self, index):
        raise NotImplementedError


    @abc.abstractmethod
    def put(self, item, index):
        raise NotImplementedError


    @abc.abstractmethod
    def find(self, item):
        raise NotImplementedError


    @abc.abstractmethod
    def concat(self, other):
        raise NotImplementedError


    @abc.abstractmethod
    def length(self):
        raise NotImplementedError


    @abc.abstractmethod
    def is_empty(self):
        raise NotImplementedError