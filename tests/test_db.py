import pytest
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
from server.Db import Db

db = Db('testDatabse.db')

def setup_module(module):
    db.create()

def teardown_module(module):
    os.remove("testDatabse.db")

def test_insert():
    db.insert('test')
    assert 'test' == db.select('all')[0][1]

def test_delete():
    dbSel = db.select('all')
    for i in range(0, len(dbSel)):
        db.delete(dbSel[i][0])
    assert [] == db.select('all')

