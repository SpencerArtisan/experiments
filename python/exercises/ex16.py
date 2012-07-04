from sys import argv

script, filename = argv

print "We're going to erase %r" % filename
print "If you don't want that, hit ctrl c"
print "if you want that, hit return"

raw_input("?")

print "Opening the file..."
target = open(filename, 'w')
print "Truncating the file.  goodbye"
target.truncate()

print "Now I'm going to ask you for three lines"

line1 = raw_input("line1")
line2 = raw_input("line2")
line3 = raw_input("line3")

print "I'm going to write these to the file"

target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

print "And finally, we close it"
target.close()
