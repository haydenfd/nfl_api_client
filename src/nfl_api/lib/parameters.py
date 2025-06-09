from enum import Enum

'''
    Mapping for team abbreviations to team IDs
'''
class TeamID(Enum):
    ATL = 1
    BUF = 2
    CHI = 3
    CIN = 4
    CLE = 5
    DAL = 6
    DEN = 7
    DET = 8
    GB = 9
    TEN = 10
    IND = 11
    KC = 12
    LV = 13
    LAR = 14
    MIA = 15
    MIN = 16
    NE = 17
    NO = 18
    NYG = 19
    NYJ = 20
    PHI = 21
    ARI = 22
    PIT = 23
    LAC = 24
    SF = 25
    SEA = 26
    TB = 27
    WSH = 28
    CAR = 29
    JAX = 30
    BAL = 33
    HOU = 34

'''
    Mapping for season types to season values
    Season types => Preseason, Regular season, Postseason, Offseason
'''
class SeasonType(Enum):
    PRE_SEASON = 1
    REGULAR_SEASON = 2
    POST_SEASON = 3 
    OFF_SEASON = 4 

'''
    Mapping for conference types to values
    Conferences => AFC, NFC
'''
class ConferenceType(Enum):
    AFC = 8
    NFC = 9