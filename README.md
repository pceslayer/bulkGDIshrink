# bulkGDIshrink
A Simple Python Script to recursive GDI shrink all Dreamcast .GDI images in a directory and its subfolders.

Requires latest gditools.py and iso9660.py from https://sourceforge.net/projects/dcisotools/

Milage may vary depending on how image was dumped.


How to Use:

Drop gditools.py, iso9660.py and bulkGDIshrink.py in the root folder containing the sub directories of GDI images and execute bulkGDIshrink.py.

Known Issues:

Shrunk images do not work with the USB-GDROM ODE by 3DO Renovation

Currently only works properly in the root of a drive.
Requires Python 2.7
