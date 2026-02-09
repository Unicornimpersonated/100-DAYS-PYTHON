def format_name(f_name,l_name):
    Name= f_name.title() +" "+ l_name.title()
    return Name

print(format_name("AnEri","sHaH"))

''' What is the need of return when we can just print the result '''

''' We need when the output of one function is the input of another'''
def function_1(text):
    return text+text

def function_2(text):
    return text.title()

output=function_2(function_1("hello"))
print(output)