from loader.loadbase import LoadBase
import sys
import importlib

class LoadFactory(type):

    process_classes = { }
    
    def __new__(cls, name, bases, attrs):
        new_class = super(LoadFactory, cls).__new__(cls, name, bases, attrs)
        LoadFactory.process_classes[name] = new_class
        return new_class

    @classmethod
    def build(cls, name, *args, **kwargs):
        try:
            cls.__importproc__(cls, name)
            c = cls.process_classes[name]
        except KeyError:
            raise ValueError(f'No known process {name}')
        return c(*args, **kwargs)

    def __importproc__(cls, name):
        module = f"modules.{name.lower()}"
        if name in cls.process_classes:
            importlib.reload(sys.modules[module])
        else:
            importlib.import_module(module)

        c = getattr(sys.modules[module], name)
        if issubclass(c, LoadBase):
            cls.process_classes[name] = c
