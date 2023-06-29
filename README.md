# QR Chessboard Generator
Generator for a chessboard made with QR images from a list of links


#Installation:
-    clone the repo 
-    Install the dependency "segno"  ("pip install segno" : https://pypi.org/project/segno/ - used for QR generation)
-    Install the dependency "pillow"  ("pip install pillow" : https://pypi.org/project/Pillow/ - used for image editing)
-    Edit the "chess_links.txt" with a new link on each line.
-    run "generate_chessboard.py"

This will generate an image for each of your links and add them to a chessboard, for example:

![](chessboard.png)

Note that the qrs are rotated 90 degrees, but this shouldn't be an issue
The temporary individual QR images are stored in the output_qr folder/
The chessboard.png will be outputted to the main folder

Created as a tool for a present I'm working on. Own code mixed with having a play with ChatGPT.
