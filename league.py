import urllib2
import json

class league:

    v1_api_url = 'http://prod.api.pvp.net/api/lol/%s/%s'
    v2_api_url = 'http://prod.api.pvp.net/api/%s/%s'

    def __init__(self, api_key, region='na'):
        self.api_key = api_key
        self.region = region

    """Creates the base uri for the api call"""
    def craft_uri(self, region, version):
        if version == 'v1.1' or version == '1.2':
            base_url == self.v1_api_url
        elif version == '2.1' or version == '2.2':
            base_url == self.v2_api_url

        uri = base_url % (region, version)
        key = '?api_key=%s' % self.api_key
        return uri + '/%s/' + key

    """Get summoner basic info by summoner id"""
    def get_summoner_by_id(self, region, summoner_id):
        path = 'summoner/%s' % summoner_id
        uri = craft_uri(region, '1.2') % path

    """Get summoner basic info by summoner name"""
    def get_summoner_by_name(self, region, name):
        path = 'summoner/by-name/%s' % summoner_id
        uri = craft_uri(region, '1.2') % path

    """Get summoner's masteries by summoner id"""
    def get_summoner_masteries(self, region, summoner_id):
        path = 'summoner/%s/masteries' % summoner_id
        uri = craft_uri(region, '1.2') % path

    """Get summoner's runes by summoner id"""
    def get_summoner_runes(self, region, summoner_id):
       path = 'summoner/%s/runes' % summoner_id
        uri = craft_uri(region, '1.2') % path

    def get_summoner_name(self, region, summoner_id):
       path = 'summoner/%s' % summoner_id
        uri = craft_uri(region, '1.2') % path

    def get_summoner_name(self, region, summoner_id):
       path = 'summoner/%s' % summoner_id
        uri = craft_uri(region, '1.2') % path

    def get_summoner_name(self, region, summoner_id):
       path = 'summoner/%s' % summoner_id
        uri = craft_uri(region, '1.2') % path

    def get_summoner_name(self, region, summoner_id):
       path = 'summoner/%s' % summoner_id
        uri = craft_uri(region, '1.2') % path

    def get_summoner_name(self, region, summoner_id):
       path = 'summoner/%s' % summoner_id
        uri = craft_uri(region, '1.2') % path

    def get_summoner_name(self, region, summoner_id):
        path = 'summoner/%s' % summoner_id
        uri = craft_uri(region, '1.2') % path



