#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#@Software
#@Author : amay
#@File : run_all_case.py
#@Time : 2020/4/14 13:01
import pytest
if __name__ == '__main__':
    #pytest.main(['../Test_Case/test_case.py','--html=../report/report1.html','--junitxml=../report/report.xml','--alluredir','../report/reportallure/'])
    pytest.main(['../Test_Case/test_case.py','-s', '-q', '--alluredir', '../report/testreportallure/'])
