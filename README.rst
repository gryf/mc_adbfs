===========================================
Midnight Commander adbfs external fs plugin
===========================================

This is Midnight Commander extfs plugin for browsing Android device through
``adb`` interface written in Python.

Rquirements
===========

* Python 2.7
* An Android device or emulator preferably rooted
* Busybox installed and available in the path on the device

Make sure, that issuing from command line::

   $ adb shell busybox ls

should display files from root directory on the device.

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

License
=======

This software is licensed under 3-clause BSD license. See LICENSE file for
details.
