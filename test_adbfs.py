# -*- coding: utf-8 -*-
import os
from importlib.util import spec_from_loader, module_from_spec
from importlib.machinery import SourceFileLoader
import unittest
from unittest import mock


module_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'adbfs')
spec = spec_from_loader("adbfs", SourceFileLoader("adbfs", module_path))
adbfs = module_from_spec(spec)
spec.loader.exec_module(adbfs)

LISTING = '''\
-rw-rw----  1 0  1015  0 01/01/2010 22:11:01 /storage/emulated/0/Grüß Gott
-rw-rw----  1 0  1015  0 01/01/2010 22:11:01 /storage/emulated/0/\x80
-rw-rw----  1 0  1015  0 01/01/2010 22:11:01 /storage/emulated/0/Γεια σας
-rw-rw----  1 0  1015  0 01/01/2010 22:11:01 /storage/emulated/0/Здравствуйте
-rw-rw----  1 0  1015  0 01/01/2010 22:11:01 /storage/emulated/0/שָׁלוֹם
-rw-rw----  1 0  1015  0 01/01/2010 22:11:01 /storage/emulated/0/السَّلامُ عَلَيْكُمْ
-rw-rw----  1 0  1015  0 01/01/2010 22:11:01 /storage/emulated/0/გამარჯობა
-rw-rw----  1 0  1015  0 01/01/2010 22:11:01 /storage/emulated/0/こんにちは。
-rw-rw----  1 0  1015  0 01/01/2010 22:11:01 /storage/emulated/0/안녕하십니까
'''  # noqa


class TestCheckOutput(unittest.TestCase):

    @mock.patch('subprocess.check_output')
    def test_check_output(self, out):
        """
        As for Python2 (and its last version: 2.7), subprocess.check_output
        always return string like objects, contrary to bytes - no conversion
        to string is needed.
        Python3 treats string as unicode objects, but subprocess.check_output
        returns bytes object, which is equvalend for py2 string… annoying.
        """
        out.return_value = bytes(LISTING, 'utf-8')
        result = adbfs.check_output(None)
        self.assertEqual(result, LISTING)

    @mock.patch('subprocess.check_output')
    def test_check_output_py3_invalid_char(self, out):
        """
        Special case for py3. We have bytes with some weird character - like
        some system write something with codepage, instead of utf8.
        """
        line = (b'-rw-rw----  1 0  1015  0 01/01/2010 22:11:01 '
                b'/storage/emulated/0/\xe2\n')  # Latin 1 char â
        out.return_value = bytes(line)
        result = adbfs.check_output(None)
        self.assertEqual(result, line.decode('iso-8859-1'))


if __name__ == "__main__":
    unittest.main()
