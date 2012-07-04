print 'Practice all'

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)

print "with a start of %d" % start_point
print "we'd have %d beans, %d jars and %d crates" % (beans, jars, crates)


