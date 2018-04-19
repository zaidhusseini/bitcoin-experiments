import bitcoin

valid_private_key = False

while not valid_private_key:
  private_key = bitcoin.random_key()
  decoded_private_key = bitcoin.decode_privkey(private_key, 'hex')
  valid_private_key = 0 < decoded_private_key < bitcoin.N

  print "Private key (hex) is:", bitcoin.random_key()
  print "Private key (decimal) is:", bitcoin.decode_privkey(private_key, 'hex')
  print "Largest possible Key size is", bitcoin.N 
  print "2^256-1 is", 2**256-1