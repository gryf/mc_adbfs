===========================================
Midnight Commander adbfs external fs plugin
===========================================

This is Midnight Commander extfs plugin for browsing Android device through
``adb`` interface written in Python.


Rquirements
===========

* Python 3.x (tested on 3.5.4, 3.6 and 3.7)
* ``adb`` installed and in ``$PATH`` or provided via the config file
* An Android device or emulator preferably rooted
* ``busybox`` (``toolbox``, ``toybox``) installed and available in the path on
  the device

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

   $ cd adbfs://

under MC - after some time you should see the files and directories on your
device. For convenience you can add a bookmark (accessible under CTRL+\\) for
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
   dirs_to_skip = ["acct", "charger", "d", "dev", "proc", "sys"]
   suppress_colors = false
   root =
   adb_command = adb
   adb_connect =

where:

* ``debug`` will provide a little bit more verbose information, useful for
  debugging
* ``dirs_to_skip`` list of paths to directories which will be skipped during
  reading. If leaved empty, or setted to empty list (``[]``) will read
  everything (slow!)
* ``suppress_colors`` this option will make ``busybox`` not to display colors,
  helpful, if ``busybox ls`` is configured to display colors by default. Does
  not affect ``toolbox`` or ``toybox``.
* ``root`` root directory to read. Everything outside of that directory will be
  omitted. That would be the fastest way to access certain location on the
  device. Note, that ``dirs_to_skip`` still apply inside this directory.
* ``adb_command`` absolute or relative path to ``adb`` command. ``~/`` or
  environment variables are allowed.
* ``adb_connect`` specifies if connection to specific device needs to be
  performed before accessing shell. It is useful for *adb over network*
  feature. Typical value here is a device IP address with optional port, which
  defaults to 5555.
* ``try_su`` specifies whether or not to try to detect if ``su`` command is
  available and usable.


Contribution
============

There is a ``Makefile`` in the top directory, which is basic helper for running
the tests. Please use it, and adapt/add tests for provided fixes/functionality.
The reason why `tox`_ wasn't used is, that there is no ``setup.py`` file, and
it's difficult to install simple script, which isn't a python module (python
interpreter will refuse to import module without ``.py`` extension).

It requires GNU ``make`` program, and also ``virtualenv`` besides Python in
version 2 and 3. Using it is simple as running following command:

.. code:: shell-session

   $ make

it will run `py2`, `py3` and `flake8` jobs to check it against the code. For
running tests against Python 3:

.. code:: shell-session

   $ make py3

or Python 2:

.. code:: shell-session

   $ make py2

or flake 8:

.. code:: shell-session

   $ make flake8

Exit status on any of those means that test fail. Appropriate message/traceback
will also be visible.


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

.. _tox: https://tox.readthedocs.io
