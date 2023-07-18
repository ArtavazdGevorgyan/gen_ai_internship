from abc import ABC, abstractmethod


class Data_SS(ABC):
    @abstractmethod
    def save(self, *args):
        pass

    @abstractmethod
    def load(self, *args):
        pass

    @abstractmethod
    def delete(self, *args):
        pass


class File_Storage(Data_SS):
    def save(self, *args):
        print('save of File Storage')

    def load(self, *args):
        print('load of File Storage')

    def delete(self, *args):

        print('load of File Storage')


class DB_Storage(Data_SS):
    def save(self, *args):
        print('save of Database Storage')

    def load(self, *args):
        print('load of Database Storage')

    def delete(self, *args):
        print('load of Database Storage')
