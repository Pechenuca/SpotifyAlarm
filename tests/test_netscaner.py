import pytest
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../client_pyqt')
from NetScaner import *

def setup_module(module):
    pass

def teardown_module(module):
    pass

def test_iplist():
    ips = NetScaner().iplist(1)
    assert 2 == len(ips)

def test_portChecker():
    port = NetScaner().portChecker('127.0.0.1')
    assert port == 0

def test_scan():
    sc = NetScaner().scanIps(['122.0.0.1'])
    assert sc == 0


