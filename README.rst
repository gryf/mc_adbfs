===========================================
Midnight Commander adbfs external fs plugin
===========================================

This is Midnight Commander extfs plugin for browsing Android device through
``adb`` interface written in Python.

Rquirements
===========

* Python 2.7
* ``adb`` installed and in ``$PATH``
* An Android device or emulator preferably rooted
* Busybox installed and available in the path on the device

Make sure, that issuing from command line::

   $ adb shell busybox ls

it should display files from root directory on the device.

Features
========

* Listing the directory with (default), or without skipping system dirs
  (``acct``, ``dev``, ``proc``, etc)
* Copying files from and to the device
* Creating directories
* Removing files and directories
* Symbolic links in lists are corrected to be relative to the file system
* Symbolic links also point to the right target, skipping intermediate links

Installation
============

Copy adbfs into ``~/.local/share/mc/extfs.d/`` directory and make it executable
if needed.

Usage
=====

To use it, just issue::

    cd adbfs://

under MC - after some time you should see the files and directories on your
device. For convenience you can add a bookmark (accessible under CTRL+\) for
fast access. The time is depended on how many files and directories you have on
your device and how fast it is :)

Limitations
===========

* Initial listing might be slow. Depending on how fast the device is, how many
  files are on the device and so on
* Some filenames might be still inaccessible for operating
* All files operations which needs root privileges will fail (for now)
* The implementation is experimental and it's by now working with mine device;
  while it might not work with yours

License
=======

This software is licensed under 3-clause BSD license. See LICENSE file for
details.
