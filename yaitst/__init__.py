import os

def get_yaitst_path(tst_name):
    return os.path.join(os.path.dirname(__file__), "data", tst_name + ".pickle")

def get_yaitron_tst_path():
    return get_yaitst_path("yaitron_tst")

def get_tdict_tst_path():
    return get_yaitst_path("tdict_tst")
