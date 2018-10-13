import collections


class MetaProperties(type):
    PATTERNS = {
        'get_': 'fget',
        'set_': 'fset',
        'del_': 'fdel',
    }
    PROPERTY_FACTORY = property

    def __new__(cls, name, bases, attr_dict):
        properties = cls.generate_properties(attr_dict)
        attr_dict.update(properties)
        return super().__new__(cls, name, bases, attr_dict)

    @classmethod
    def generate_properties(cls, attr_dict):
        result = collections.defaultdict(dict)
        for key, value in attr_dict.items():
            for pattern in cls.PATTERNS:
                if key.startswith(pattern):
                    property_name = key[len(pattern):]
                    name_len = len(property_name)
                    if name_len < 1:
                        raise NameError('Invalid property name.')
                    result[property_name][cls.PATTERNS[pattern]] = value
                    break
        result = {k: cls.PROPERTY_FACTORY(**kwargs)
                  for k, kwargs in result.items()}
        return result


if __name__ == '__main__':

    class TestClass(metaclass=MetaProperties):
        def __init__(self, data_1=None):
            self._data_1 = data_1
            self._data_2 = 'default'

        def get_data_1(self):
            return self._data_1

        def set_data_1(self, value):
            value *= 2
            self._data_1 = value

        def del_data_1(self):
            del self._data_1

        def get_data_2(self):
            return self._data_2

    test_intstance = TestClass(10)
    print(test_intstance.data_1)
    test_intstance.data_1 = 2
    print(test_intstance.data_1)
    del test_intstance.data_1
    print(getattr(test_intstance, '_data_1', '_data_1 - deleted'))
    print(test_intstance.data_2)
