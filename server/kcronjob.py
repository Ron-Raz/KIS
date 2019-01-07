#!/usr/bin/env python2.7

from KalturaClient import *
from KalturaClient.Plugins.Core import *
from KalturaClient.Plugins.Metadata import *
from KalturaClient.Plugins.Schedule import *
from datetime import datetime
import json

# load account specific values from config file

with open('/home/kaltura/KIS/server/config.json') as f:
    cfg = json.load(f)

config = KalturaConfiguration(cfg.partnerId)
config.serviceUrl = cfg.serviceUrl
client = KalturaClient(config)
ks = client.session.start( cfg.secret, cfg.user, KalturaSessionType.ADMIN, cfg.partnerId )
client.setKs(ks)

filter = KalturaMediaEntryFilter()
filter.mediaTypeEqual = KalturaMediaType.LIVE_STREAM_FLASH
pager = KalturaFilterPager()

mdFilter = KalturaMetadataFilter()
mdFilter.metadataProfileIdEqual = cfg.metadataProfileId

lsFilter = KalturaLiveStreamScheduleEventFilter()
lsFilter.statusEqual = KalturaScheduleEventStatus.ACTIVE

objs = client.media.list(filter, pager).objects
print('len',len(objs))
for obj in objs:
	my = {}
	# get basic entry info
	my['name'] = obj.getName()
	my['id'] = obj.getId()
	my['primary'] = obj.getPrimaryBroadcastingUrl()
	my['backup'] = obj.getSecondaryBroadcastingUrl()
	my['stream'] = obj.getStreamName()
	# get sip info from custom metadata
	mdFilter.objectIdEqual = obj.getId()
	mdPager = KalturaFilterPager()
	mdResponse = client.metadata.metadata.list(mdFilter, mdPager).objects
	if len(mdResponse) == 1:
		my['sip'] = mdResponse[0].getXml()
	else:
		my['sip'] = cfg.notFound
	# get live stream shedule start/end
	lsFilter.templateEntryIdEqual = obj.getId()
	lsPager = KalturaFilterPager()
	lsResponse = client.schedule.scheduleEvent.list(lsFilter, lsPager).objects
	if len(lsResponse) == 1:
		my['start'] = datetime.fromtimestamp(lsResponse[0].getStartDate())
		my['end'] = datetime.fromtimestamp(lsResponse[0].getEndDate())
		my['eventid'] = lsResponse[0].getId()
	else:
		my['start'] = cfg.notFound
		my['end'] = cfg.notFound
	# print the properties	
	print(my)
