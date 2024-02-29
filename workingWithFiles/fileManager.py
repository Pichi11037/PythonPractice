class FileManager():

    def __init__(self, name) -> None:
        self.name = name

    def __enter__(self):
        print("File opened".center(30, '-'))
        self.name = open(self.name, 'r', encoding='utf8')
        return self.name
    
    def __exit__(self, exception_type, exception_value, traceback_error):
        print('File closed'.center(30, '-'))
        if self.name:
            self.name.close