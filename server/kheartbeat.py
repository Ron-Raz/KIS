#!/usr/bin/env python2.7
from KalturaClient import *
from KalturaClient.Plugins.Core import *
from KalturaClient.Plugins.Metadata import *
from KalturaClient.Plugins.Schedule import *
import json
import datetime
import sched
import time
import xml.etree.ElementTree as et
with open('/home/kaltura/KIS/server/config.json') as f:
    cfg = json.load(f)
print 'cfg=', cfg

s = sched.scheduler(time.time, time.sleep)
count = 0
config = KalturaConfiguration(cfg['partnerId'])
config.serviceUrl = cfg['serviceUrl']
client = KalturaClient(config)
base_entry = KalturaBaseEntry()

mdFilter = KalturaMetadataFilter()
mdFilter.metadataProfileIdEqual = cfg['metadataProfileId']
mdFilter.objectIdEqual = cfg['sipAdminEntryId']


def doHeartbeat(sc=None):
    global cfg, s, count, config, client, base_entry
    ks = client.session.start(
        cfg['secret'], cfg['user'], KalturaSessionType.ADMIN, cfg['partnerId'], cfg['kalturaSessionInSeconds'])
    client.setKs(ks)
    # get metadata to see if action is needed
    mdPager = KalturaFilterPager()
    mdResponse = client.metadata.metadata.list(mdFilter, mdPager).objects
    if len(mdResponse) == 1:
        root = et.fromstring(mdResponse[0].getXml())
        status= root.find('ServerAction').text
    else:
        status= cfg['notFound']
    # update description with heartbeat status
    base_entry.description = '{ "heartbeatTime":"'+datetime.datetime.utcnow().strftime(
        "%Y-%m-%dT%H:%M:%SZ")+'", "serverVersion":"1.0","cpu":"0.2","mem":"0.4","status":"'+status+'" }'
    result = client.baseEntry.update(cfg['sipAdminEntryId'], base_entry)
    client.session.end()
    count += 1
    print(count, result.getId(), result.getName(), result.getDescription())
    if sc is not None:
        s.enter(cfg['heartbeatIntervalInSeconds'], 1, doHeartbeat, (sc,))


doHeartbeat()
s.enter(cfg['heartbeatIntervalInSeconds'], 1, doHeartbeat, (s,))
s.run()
