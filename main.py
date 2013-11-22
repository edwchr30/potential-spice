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
plain_text = raw_input('Please enter 16 characters to be encrypted: ')
while len(plain_text) != '16':
    if len(plain_text) > '16':
        print "Too big!"
        plain_text = raw_input('Please enter 16 characters top be encrypted: ')
    if len(plain_text) < '16':
        print "Too small!"
        plain_text = raw_input('Please enter 16 characters top be encrypted: ')
    else:
        print "Just right!"

##Only printing "Too Small!"
