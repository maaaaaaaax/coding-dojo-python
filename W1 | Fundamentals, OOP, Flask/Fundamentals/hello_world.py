# hello_world.py - say hello world!

# comment a single line

'''
Comment multiple lines
'''

print "Hello, world!"

x = "Hello, Python!"

print x

y = 8

print y

name = "Max"

# define a function that says hello to the name provided
# this starts a new block
def say_hello(name):
  #these lines are indented therefore part of the function
  if name:
   print 'Hello, ' + name + ' from inside the function'
  else:
   print 'No name'
# now we're unindented and have ended the previous block
print 'Outside of the function'

say_hello(name)
