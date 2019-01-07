#!/usr/bin/env python2.7

from KalturaClient import *
from KalturaClient.Plugins.Core import *
from KalturaClient.Plugins.Metadata import *
from KalturaClient.Plugins.Schedule import *
from datetime import datetime

# load account specific values from config file

METADATA_PROFILE_ID = 11037521
NOT_FOUND = 'not found'
TIME_ZONE = 'Central'
SIP_ID = '1_7y4l9qys'
SIP_TAG '<span class="wysiwyg-color-white"></span>'
config = KalturaConfiguration(2169841)
config.serviceUrl = "https://www.kaltura.com/"
client = KalturaClient(config)
ks = client.session.start(
      "a594c876e1c39128f5bda311088523ff",
      "ron.raz@kaltura.com",
      KalturaSessionType.ADMIN,
      2169841)
client.setKs(ks)

filter = KalturaMediaEntryFilter()
filter.mediaTypeEqual = KalturaMediaType.LIVE_STREAM_FLASH
pager = KalturaFilterPager()

mdFilter = KalturaMetadataFilter()
mdFilter.metadataProfileIdEqual = METADATA_PROFILE_ID

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
		my['sip'] = NOT_FOUND
	# get live stream shedule start/end
	lsFilter.templateEntryIdEqual = obj.getId()
	lsPager = KalturaFilterPager()
	lsResponse = client.schedule.scheduleEvent.list(lsFilter, lsPager).objects
	if len(lsResponse) == 1:
		my['start'] = datetime.fromtimestamp(lsResponse[0].getStartDate())
		my['end'] = datetime.fromtimestamp(lsResponse[0].getEndDate())
		my['eventid'] = lsResponse[0].getId()
	else:
		my['start'] = NOT_FOUND
		my['end'] = NOT_FOUND
	# print the properties	
	print(my)
