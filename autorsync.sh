#!/usr/bin/env bash
fswatch -o . | while read f; do rsync --progress --partial -avz server/ kaltura@centos:/home/kaltura/KIS/server/; done