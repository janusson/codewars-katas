# try-except-finally-raise.py
# basic 'try/except' scripting
try:
    print('Try out this block of code.')
    # print(x) # add a little chaos
except TypeError:
    print('Type error.')
except NameError:
    print('A name error occurred.')
else:
    print('If that all worked, we\'re done here')
finally:
    print('And that\'s it, I suppose.')

print('One last thing...')
raise SyntaxError('Whooplas')
