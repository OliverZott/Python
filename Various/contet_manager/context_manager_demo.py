# f = open(mode='w', file='test.txt')
# f.write("Hello, test-text.")
# f.close()

with open(mode='w', file='test.txt') as f:
    f.write('Text in context version.')
