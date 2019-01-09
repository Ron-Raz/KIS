#!/usr/bin/env python2.7
from KalturaClient import *
from KalturaClient.Plugins.Core import *
from KalturaClient.Plugins.Metadata import *
from KalturaClient.Plugins.Schedule import *
import json
import datetime
import sched
import time


with open('/home/kaltura/KIS/server/config.json') as f:
    cfg = json.load(f)

s = sched.scheduler(time.time, time.sleep)

def doHeartbeat(sc):
    print 'cfg=', cfg
    config = KalturaConfiguration(cfg['partnerId'])
    config.serviceUrl = cfg['serviceUrl']
    client = KalturaClient(config)
    ks = client.session.start(
        cfg['secret'], cfg['user'], KalturaSessionType.ADMIN, cfg['partnerId'])
    client.setKs(ks)

    base_entry = KalturaBaseEntry()
    base_entry.description = '{ "heartbeatTime":"'+datetime.datetime.now().strftime(
        "%Y-%m-%dT%H:%M:%SZ")+'", "serverVersion":"1.0","cpu":"0.2","mem":"0.4","status":"No Event" }'

    result = client.baseEntry.update(cfg['sipAdminEntryId'], base_entry)
    print(result.getId(), result.getName(), result.getDescription())
    s.enter(60, 1, doHeartbeat, (sc,))

s.enter(60, 1, doHeartbeat, (s,))
s.run()
