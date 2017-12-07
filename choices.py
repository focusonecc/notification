# -*- coding: utf-8 -*-
# @Author: liang
# @Date:   2017-11-27 08:44:41
# @Last Modified by:   theo-l
# @Last Modified time: 2017-11-27 08:51:04

from common.base_choices import BaseChoice, ChoiceItem


class ServiceType(BaseChoice):
    UMENG = ChoiceItem(1, u'UMENG')


class PlatformType(BaseChoice):
    IOS = ChoiceItem(1, u'iOS')
    ANDROID = ChoiceItem(2, u'Android')
    WEB = ChoiceItem(3, u'Web')


class DeviceStatus(BaseChoice):
    ACTIVE = ChoiceItem(1, u'Active')
    