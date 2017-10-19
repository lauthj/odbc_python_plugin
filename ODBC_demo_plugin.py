'''
Created on Oct 17, 2017

@author: lauthjo
'''
import requests
import json
import logging
from ruxit.api.base_plugin import BasePlugin
from ruxit.api.snapshot import pgi_name

class DemoPlugin(BasePlugin):
    def query(self, **kwargs):
        pgi = self.find_single_process_group(pgi_name('C:\\users.lauthjo.workspace.ODBC_Python_Demo_Plugin.odbc_python_demo'))
        pgi_id = pgi.group_instance_id
        self.results_builder.absolute(key='value', value=pgi.get_values(), entity_id=pgi_id)