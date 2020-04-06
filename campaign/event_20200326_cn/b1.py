from module.campaign.campaign_base import CampaignBase
from module.map.map_base import CampaignMap
from module.map.map_grids import SelectedGrids, RoadGrids
from module.logger import logger
from campaign.event_20200326_cn.a1 import Config

MAP = CampaignMap()
MAP.shape = 'H7'
MAP.map_data = '''
    -- ME -- ME ++ ++ SP SP
    ME -- MS -- ME -- -- SP
    ++ ME -- -- -- -- -- --
    ++ ME -- -- MS -- ME ++
    ME -- __ ME ++ -- -- --
    MB -- -- MS ++ -- ME ME
    MB MB ME -- ME -- ME --
'''
MAP.spawn_data = [
    {'battle': 0, 'enemy': 2, 'siren': 1},
    {'battle': 1, 'enemy': 1},
    {'battle': 2, 'enemy': 2},
    {'battle': 3, 'enemy': 1},
    {'battle': 4, 'boss': 1},
]


A1, B1, C1, D1, E1, F1, G1, H1, \
A2, B2, C2, D2, E2, F2, G2, H2, \
A3, B3, C3, D3, E3, F3, G3, H3, \
A4, B4, C4, D4, E4, F4, G4, H4, \
A5, B5, C5, D5, E5, F5, G5, H5, \
A6, B6, C6, D6, E6, F6, G6, H6, \
A7, B7, C7, D7, E7, F7, G7, H7, \
    = MAP.flatten()


class Campaign(CampaignBase):
    MAP = MAP

    def battle_0(self):
        if self.clear_siren():
            return True

        if self.clear_enemy(scale=(3,)):
            return True

        return self.battle_default()

    def battle_4(self):
        return self.clear_boss()
