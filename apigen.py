import os
import xml.etree.ElementTree
from collections import namedtuple
#import langs.ClassWriter
#import langs.PHPClassWriter

class APIClass:
    def __init__(self,access='',name=''):
        self.access = access
        self.name = name
        
class PHPFile:
    def __init__(self,path):
        self.indent = 0
        self.code_string = ''
        self.file_handle = open(path,'w')
        
    def open_php(self):
        self.code_string += '<?php\n\n'
    
    def open_class(self,name):
        self.code_string += '%sclass %s {\n' % ('\t'*self.indent,name)
        self.indent += 1
    
    def close_class(self):
        self.indent -= 1
        self.code_string += '%s}\n\n' % ('\t'*self.indent)
        
    def close_block(self):
        self.code_string += '?>'

    def write(self):
        self.file_handle.write(self.code_string)
        
if(not os.path.isdir('cpp') and  not os.path.isfile('cpp')):
    os.mkdir('cpp')
if(not os.path.isdir('php') and not os.path.isfile('php')):
    os.mkdir('php')
if(not os.path.isdir('js') and not os.path.isfile('js')):
    os.mkdir('js')
if(not os.path.isdir('sql') and not os.path.isfile('sql')):
    os.mkdir('sql')
    
xml = xml.etree.ElementTree.parse('input.xml').getroot()

a = PHPFile('test.php')

a.open_php()
a.open_class('a')
a.open_class('b')
a.close_block()
a.close_block()
a.close_php()
a.write()

APIVariable = namedtuple('APIVariable','global access type name value size')
APIClass = namedtuple('APIClass','access name abstract members methods parents implements')
APINamespace = namedtuple('APINamespace','name classes methods members')

for a_namespace in xml.findall('api/namespace'):
    namespace_path = a_namespace.find('name').text.split('.')
    php_namespace_path = "\\".join(namespace_path)
    for a_class in a_namespace.findall('class'):
        php_api_file = open('php/rest/' + a_class.find('name').text + '.php','w')
        php_class_file = open('php/' + a_class.find('name').text + '.php','w')
        js_class_file = open('js/' + a_class.find('name').text + '.js','w')
        sql_class_file = open('sql/' + a_class.find('name').text + '.sql','w')
        php_class_file.write('<?php\n\nnamespace '+php_namespace_path +';\n\n')
        php_class_file.write('class ' + a_class.find('name').text + ' {\n') 
        js_class_file.write('function '+ a_class.find('name').text + '() {\n')
        sql_class_file.write('CREATE TABLE ' + a_class.find('name').text.lower() + '(\n')
        for a_member in a_class.findall('member'):
            php_class_file.write('\t$' + a_member.find('name').text +' = '+a_member.find('value').text+';\n')
            js_class_file.write('\tthis.'+ a_member.find('name').text + ' = '+a_member.find('value').text+';\n')
            sql_class_file.write(a_member.find('name').text + ' varchar(255) not null default \'\'\n') 
        php_class_file.write('}\n')
        js_class_file.write('}\n')
        sql_class_file.write(');\n')
        php_class_file.close()
        js_class_file.close()
        sql_class_file.close() 