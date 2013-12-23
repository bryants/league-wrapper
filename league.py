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
        return uri

    """Get summoner basic info by summoner name"""
    def get_summoner_by_name(self, region, name):
        path = 'summoner/by-name/%s' % name
        uri = craft_uri(region, '1.2') % path
        return uri

    """Get summoner's masteries by summoner id"""
    def get_summoner_masteries(self, region, summoner_id):
        path = 'summoner/%s/masteries' % summoner_id
        uri = craft_uri(region, '1.2') % path
        return uri

    """Get summoner's runes by summoner id"""
    def get_summoner_runes(self, region, summoner_id):
        path = 'summoner/%s/runes' % summoner_id
        uri = craft_uri(region, '1.2') % path
        return uri

    """Get summoner's statistical summary"""
    def get_summoner_stats_summary(self, region, summoner_id):
        path = 'stats/by-summoner/%s/summary' % summoner_id
        uri = craft_uri(region, '1.2') % path
        return uri

    """Get summoner's ranked statistics"""
    def get_summoner_ranked_stats(self, region, summoner_id):
        path = 'stats/by-summoner/%s/ranked' % summoner_id
        uri = craft_uri(region, '1.2') % path
        return uri

    """Get summoner's recent game data"""
    def get_summoner_games(self, region, summoner_id):
        path = 'game/by-summoner/%s/recent' % summoner_id
        uri = craft_uri(region, '1.2') % path
        return uri

    """Get champion data"""
    def get_champion_data(self, region):
        path = 'champion' % summoner_id
        uri = craft_uri(region, '1.1') % path
        return uri

    """Get summoner's league data"""
    def get_summoner_league(self, region, summoner_id):
        path = 'league/by-summoner/%s' % summoner_id
        uri = craft_uri(region, '2.2') % path
        return uri

    """Get summoner's team data"""
    def get_summoner_team(self, region, summoner_id):
        path = 'team/by-summoner/%s' % summoner_id
        uri = craft_uri(region, '2.2') % path
        return uri


