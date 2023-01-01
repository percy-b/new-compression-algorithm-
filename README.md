# new-compression-algorithm-
For bjk algorithm 
Split the input file into blocks of a fixed size (e.g. 1024 bytes).
Encode each block of data as a string of hexadecimal digits.
Generate an image file with dimensions large enough to hold all of the blocks of data, using a library like Pillow.
Iterate over the blocks of data and draw a QR code for each block in a specific location on the image file.
Save the image file to disk.
To decompress the file, you can use the following algorithm:

Load the image file into memory using a library like Pillow.
Scan the image for QR codes and decode each one to recover the original blocks of data.
Convert the hexadecimal strings back into the original binary data.
Write the recovered data to a new file.
The code demonstrates how you might implement these algorithms using the Pillow library and the pyqrcode library:

For bjk2
Read the input file into memory as a bytestring.
Use a lossless image compression library (e.g. Pillow) to compress the bytestring into a JPEG or PNG image.
Save the image to disk.
To decompress the file, you can use the following algorithm:

Load the image file into memory using a library like Pillow.
Use the library to decode the image and recover the original bytestring.
Write the recovered bytestring to a new file.
