===========================================
Midnight Commander adbfs external fs plugin
===========================================

This is Midnight Commander extfs plugin for browsing Android device through
``adb`` interface written in Python.

Rquirements
===========

* Python 2.7
* ``adb`` installed and in ``$PATH`` or provided via the config file
* An Android device or emulator preferably rooted
* Busybox installed and available in the path on the device

Make sure, that issuing from command line:

.. code:: shell-session

   $ adb shell busybox ls
   $ # or in case of no PATH adb placement
   $ /path/to/adb shell busybox ls

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

To use it, just issue:

.. code:: shell-session

   cd adbfs://

under MC - after some time you should see the files and directories on your
device. For convenience you can add a bookmark (accessible under CTRL+\) for
fast access. The time is depended on how many files and directories you have on
your device and how fast it is :)

Configuration
=============

You can configure behaviour of this plugin using ``.ini`` file located under
``$XDG_CONFIG_HOME/mc/adbfs.ini`` (which usually is located under
``~/.config/mc/adbfs.ini``), and have default values, like:

.. code:: ini

   [adbfs]
   debug = false
   skip_dirs = true
   dirs_to_skip = ["acct", "charger", "d", "dev", "proc", "sys"]
   suppress_colors = false
   root =
   adb_command = adb

where:

* ``debug`` will provide a little bit more verbose information, useful for
  debugging
* ``dirs_to_skip`` list of paths to directories which will be skipped during
  reading. If leaved empty, or setted to empty list (``[]``) will read
  everything (slow!)
* ``suppress_colors`` this option will make ``busybox`` not to display colors,
  helpful, if ``busybox ls`` is configured to display colors by default. Does
  not affect ``toolbox``.
* ``root`` root directory to read. Everything outside of that directory will be
  omitted. That would be the fastest way to access certain location on the
  device. Note, that ``dirs_to_skip`` still apply inside this directory.
* ``adb_command`` = path to ``adb`` command.

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
