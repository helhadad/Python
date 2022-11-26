"""
Script  : test_import.py
Author  : Hesham Elhadad
ID      : L00177542
Date    : 05-Nov-22
Purpose : This script demonstrates

Tested  : Python 3.10 on Windows 10 Pro
Rev     : 0
IDE     : PyCharm CE ver 2022

"""
import logging
import os.path as op
import os
import sys
import pathlib as pl
main_path = pl.Path(__file__)
proj_path = (main_path / '../../').resolve()
print(proj_path)
# sys.path.append(str(proj_path))
# print(sys.path)
# from Lib.mylog import con_handler, file_handler
#
# logger = logging.getLogger(__name__)
# logger.addHandler(file_handler)
# logger.info("Test loggin from test_import")

# print(sys.path)
# print("dirname of file =", op.dirname(__file__))
# print("split tuple = ", op.split(op.dirname(__file__)))
# print("basename of file = ", op.basename(op.dirname(__file__)))
# print("use splitdrive = ", op.splitdrive(op.dirname(__file__)))

# cur_path = pl.Path(__file__)
# print("current Path = ", cur_path)
# rel_path1 = "Lib/"
# rel_path2 = "../../"
# fpath1 = (cur_path / rel_path1).resolve()
# fpath2 = (cur_path / rel_path2).resolve()
# print("full path1 relpath = ", fpath1)
# print("full path2 relpath = ", fpath2)
