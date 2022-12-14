f = open(r'Python\GetStarted\TextFile\writefile.txt', 'w')
print('This is line 1.', file=f)
print('This is line 2.', file=f)
f.close()