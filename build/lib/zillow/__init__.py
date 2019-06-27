from __future__ import absolute_import

import os
import pkg_resources as _pkg_resources
from py_zillow.zillow._version import __version__

from py_zillow.zillow.api.api import ValuationAPI
import py_zillow.zillow.config.secrets as secrets

__author__ = 'alex@freightroll.com'

os.environ['zws_id'] = secrets.zws_id()
zillow = ValuationAPI()