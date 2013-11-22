##Title##
print "This program serves to demonstrate"
print "that encryption offers protection"
print "beyond intrusion prevention.  With"
print "encryption and properly managed"
print "keys, you can protect your data"
print "even if it gets stolen/misplaced."
print "\n"
print "The steps will be explained as"
print "we go."
print "\n"
print "First we will create a file."
plain_text = "stuff"
while len(plain_text)!=16:
    plain_text = raw_input('Please enter 16 characters to be encrypted: ')
    print len(plain_text), " NOPE, try again..."
else:
    print plain_text, " is exactly 16 characters! GREAT JOB!"
#Only printing "Too Small!"
