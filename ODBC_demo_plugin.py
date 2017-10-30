'''
Created on Oct 17, 2017

@author: lauthjo
'''
import requests
import json
import logging
from ruxit.api.base_plugin import BasePlugin
from ruxit.api.snapshot import pgi_name

class ODBCDemoPlugin(BasePlugin):
    def query(self, **kwargs):
        pgi = self.find_single_process_group(pgi_name('odbc_python_demo.py'))
        pgi_id = pgi.group_instance_id
        stats_url = "http://localhost:8770"
        stats = json.loads(requests.get(stats_url).content.decode())
        self.results_builder.absolute(key='value', value=stats['5'], entity_id=pgi_id)