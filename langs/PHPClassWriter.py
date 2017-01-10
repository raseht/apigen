class PHPClassWriter(ClassWriter):
    def __init__():
        self.code_string = ''
    def open_class(name,access):
        self.code_string += 'class %s' % (name)
    
    def add_member(name,type,value,access):
        self.code_string += '\t%s %s $%s = %s' % (access,name,type,value)
    
    def close_class():
        self.code_string += '}'
    