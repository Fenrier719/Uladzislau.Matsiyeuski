from abc import ABC, abstractmethod

class Init(ABC):

    def __init__(self, list_of_keys, list_of_values):
        for key in list_of_keys:
            value = list_of_values[list_of_keys.index(key)]
            setattr(self, key, value)

    @abstractmethod
    def convert(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass


class CSV2Json(Init):

    def __repr__(self):
        string_data = ''
        for key in vars(self):
            string_data += '\t\t"' + key + '": ' + self.is_list(key) + ',\n'
        return '\t{\t\n'+ string_data[:-2] + '\n\t}'

    def is_list(self, key):
        if ',' in getattr(self, key):
            return '[' + ','.join(self.is_number(key).split(sep = ',')) +']'
        return self.is_number(key)

    def is_number(self, key):
        try:
            float(getattr(self, key))
        except:
            return '"' + getattr(self, key) + '"'
        return getattr(self, key)

    @classmethod
    def convert(cls):
        input_file_name = "test.csv"
        output_file_name = "file.json"
        with cls.open(input_file_name, 'r') as file_to_convert, cls.open(output_file_name, 'w') as converted_file:
            cls.write(converted_file, '[\n')
            list_of_keys = cls.get_keys(file_to_convert)
            cls.get_values(file_to_convert, converted_file, list_of_keys)
            cls.write(converted_file, '\n]')

    @classmethod
    def get_keys(cls, file_to_convert):
        string_of_data = cls.read(file_to_convert)
        list_of_keys = string_of_data[:-1].split(sep = ';')
        return list_of_keys

    @classmethod
    def get_values(cls, file_to_convert, converted_file, list_of_keys):
        separator = ''
        string_of_data = cls.read(file_to_convert)
        while string_of_data:
            list_of_values = string_of_data[:-1].split(sep = ';')
            cls.write(converted_file, separator + cls.is_out_of_range(list_of_keys, list_of_values))
            separator = ',\n'
            string_of_data = cls.read(file_to_convert)

    @classmethod
    def is_out_of_range(cls, list_of_keys, list_of_values):
        if len(list_of_keys) == len(list_of_values):
            class_instance = cls(list_of_keys, list_of_values)
            return repr(class_instance)
        else:
            raise Exception("The number of values in your file doesn't match the number of keys")

    @staticmethod
    def open(file_name, a):
        try:
            file = open(file_name, a)
        except:
            raise Exception("Can't open file!")
        else:
            return file

    @staticmethod
    def read(file_to_convert):
        try:
            string_of_data = file_to_convert.readline()
        except:
            raise Exception("Can't read anything from file!")
        else:
            return string_of_data

    @staticmethod
    def write(converted_file, string_of_converted_data):
        try:
            converted_file.write(string_of_converted_data)
        except:
            raise Exception("Can't write anything in file!")

if __name__ == '__main__':
    CSV2Json.convert()
