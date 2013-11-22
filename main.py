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
plaintext = raw_input('Please enter 16 characters to be encrypted: ')
if len(plaintext) != 16:
    print "Error! Input must be 16 characters long."
