#!/usr/bin/env python2.7

from KalturaClient import *
from KalturaClient.Plugins.Core import *

config = KalturaConfiguration(2169841)
config.serviceUrl = "https://www.kaltura.com/"
client = KalturaClient(config)

secret = "a594c876e1c39128f5bda311088523ff"
user_id = "ron.raz@kaltura.com"
k_type = KalturaSessionType.ADMIN
partner_id = 2169841
expiry = 86400
privileges = ""

result = client.session.start(secret, user_id, k_type, partner_id, expiry, privileges)
print(result)
