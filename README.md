Homebrewed Homework: Part 1
===========================
changelog/updates in Notes.md

Encryption Key Retrieval
---------------------------

This program will highlight the versatility of python by using many methods
to accomplish a useful task.  I plan to accept a 16-byte string that is
entered by the user, return a cipher-text version that is unreadable, and 
then through the use of a key that has been retrieved from a Hardware 
Security Module display the unencrypted version.

Implementation
--------------------------
1. Create file ptext.txt with 16 bytes of information.
      - This will be input from the user
2. Establish SSL connection to HSM.
3. Upload ptext.txt for encryption
4. Create a symmetrical key.
5. Demonstrate that ptext.txt is encrypted and also show decrypted version.
      - concatenate ptext.txt
      - concatenate ctext.txt [the encrypted version]
      - give the user a chance to guess the key
      - show the encryption key that was used
