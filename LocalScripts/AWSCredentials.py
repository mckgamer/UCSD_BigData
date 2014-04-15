### AWS credentials: ####
# Change entries here to match your own #
# Get values for the first two entries from the "Security crediential" Tab
# Under in the menu under your name.
aws_access_key_id='AKIAIGEJQCBR2BKJLIAA'
aws_secret_access_key='tvjWcOguyxTKlu7al1LrxsS/FfipWRikyngLnvaD'
# Get the Keypair in the EC2 Dashboard page.
keyPairFile="/home/michael/.ssh/291East.pem" # name of file keeping local key
key_name="291East" # name of keypair (not name of file where key is stored)
# Set the security group On the EC2 page (You will need to add IP addresses if
# you want to connect from a place previously unauthorized.
security_groups=['CSE 291']
### End of AWS credentials ####
