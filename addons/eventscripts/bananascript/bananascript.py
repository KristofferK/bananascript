###############################
####    BANANASCRIPT by    ####
####   K-9 & The CheeTaH   ####
####     COPYRIGHT 2011    ####
###############################
import es

## Enable ticklistener (migth cause lag)
#* Required for:
#  Setting deaths
TickListener_Enabled = 0

## when someone saves:
#* 0: Continue time with a little punishment
#* 1: Stops time.
es.ServerVar("stoptime").set(1)
#* How many seconds to add when someone uses !save
#  does require stoptime on 0
#  Default: 300 (5 minutes)
es.ServerVar("savepunish").set(300)

FPS54_Starts    = 1     # where FPS 54 starts. Includes this number
FPS54_Ends      = 100   # where FPS 54 end.    Includes this number

## Server Vars
es.ServerVar("block_fps").set(0)        # 1 or 0    forces fps_max          to 300      if set to 1
es.ServerVar("block_yaw").set(1)        # 1 or 0    forces cl_yawspeed      to 210      if set to 1
es.ServerVar("block_left").set(1)       # 1 or 0    block +left/+right                  if set to 1
es.ServerVar("enable_jump").set(1)      # 1 or 0    Gives specific players jump boost   if set to 1     (check def player_jump(ev):)
## Pushing - requires enable_jump
#* push no matter fps_max
Push11FPS = ['STEAM_0:1:7589873','STEAM_0:1:34314926','STEAM_0:0:15639550','STEAM_0:0:27028253']
#* push when not over FPS54_Ends and not under FPS54_Starts
Push00FPS = ['STEAM_0:0:17632587']

## Map Difficulties
#* If a map isn't in Mediummaps NOR HardMaps, then it will be auto set as easy!
#  So we aren't even gonna bother set up bhop_eazy.. too much work.. ehh? :P
MediumMaps  = ['bhop_advi_supernova','bhop_-4-',
    'bhop_1n5an3_hard','bhop_1n5an3_harder',
    'bhop_3d','bhop_adventure_final',
    'bhop_advi_harder','bhop_advi_nova',
    'bhop_algebradude','bhop_allmap',
    'bhop_aquatic_v1','bhop_awake',
    'bhop_baltimoron_beta_v2','bhop_danmark',
    'bhop_developed_beta01','bhop_dots',
    'bhop_dtt_flo30','bhop_eazy_harder',
    'bhop_exotic_v2','bhop_forgotten_tomb',
    'bhop_hmm_brighter','bhop_larena','bhop_legion',
    'bhop_monster_jam','bhop_office_indoors',
    'bhop_overground_fix','bhop_pro_bhopper_final_fix',
    'bhop_prostyle','bhop_quist_v2','bhop_rooster','bhop_sky',
    'bhop_something','bhop_strider_v3','bhop_Tasku',
    'bhop_technologeek','bhop_tropic_v2','bhop_twisted',
    'bhop_underground_fix','bhop_unkn0wn_v2','bhop_eu_v2',
    'bhop_xtreme_final','bhop_ytt_dust','bhop_ytt_space']
HardMaps  = ['bhop_badges','bhop_absolutebhop_v4','bhop_addict_v2',
    'bhop_advi_supernova','bhop_arcane_v1','bhop_badges',
    'bhop_badges_ausbhop','bhop_challenge','bhop_cruxXx','bhop_dan',
    'bhop_exodus','bhop_factory_v2','bhop_giga_citadel_v2',
    'bhop_grandex_galaxy_v2','bhop_guly','bhop_nextgen','bhop_om_final','bhop_outback',
    'bhop_playboy','bhop_quantum_final','bhop_sahara_hard_nosound',
    'bhop_sahara_nosound','bhop_serzv1','bhop_skillz_final_3','bhop_superdooperhard',
    'bhop_tex','bhop_texturekill_beta1_3b','bhop_thc','bhop_thc_gold','bhop_thc_island',
    'bhop_waterfall','bhop_wayz','bhop_whipz','bhop_wouit_v2','bhop_together']


## Map Points
#* Syntax is: banana_top_points_NUM_diff_method
#  NUM is what his rank is on the map. It must be 3 digit when under 1000 (001,002,003...010...500...1000)
#  diff is the maps difficulty (easy,medium,hard)
#  method is how he completed it (normal,sideways,wonly)
#* easy maps completed on normal
es.ServerVar("banana_top_points_001_easy_normal").set(10)
es.ServerVar("banana_top_points_002_easy_normal").set(9)
es.ServerVar("banana_top_points_003_easy_normal").set(8)
es.ServerVar("banana_top_points_004_easy_normal").set(7)
es.ServerVar("banana_top_points_005_easy_normal").set(6)
es.ServerVar("banana_top_points_006_easy_normal").set(5)
es.ServerVar("banana_top_points_007_easy_normal").set(4)
es.ServerVar("banana_top_points_008_easy_normal").set(3)
es.ServerVar("banana_top_points_009_easy_normal").set(2)
es.ServerVar("banana_top_points_010_easy_normal").set(1)
es.ServerVar("banana_top_points_011_easy_normal").set(1)
es.ServerVar("banana_top_points_012_easy_normal").set(1)
es.ServerVar("banana_top_points_013_easy_normal").set(1)
es.ServerVar("banana_top_points_014_easy_normal").set(1)
es.ServerVar("banana_top_points_015_easy_normal").set(1)
es.ServerVar("banana_top_points_016_easy_normal").set(1)
es.ServerVar("banana_top_points_017_easy_normal").set(1)
es.ServerVar("banana_top_points_018_easy_normal").set(1)
es.ServerVar("banana_top_points_019_easy_normal").set(1)
es.ServerVar("banana_top_points_020_easy_normal").set(1)
#* easy maps completed on sideways
es.ServerVar("banana_top_points_001_easy_sideways").set(20)
es.ServerVar("banana_top_points_002_easy_sideways").set(18)
es.ServerVar("banana_top_points_003_easy_sideways").set(16)
es.ServerVar("banana_top_points_004_easy_sideways").set(14)
es.ServerVar("banana_top_points_005_easy_sideways").set(12)
es.ServerVar("banana_top_points_006_easy_sideways").set(10)
es.ServerVar("banana_top_points_007_easy_sideways").set(8)
es.ServerVar("banana_top_points_008_easy_sideways").set(6)
es.ServerVar("banana_top_points_009_easy_sideways").set(4)
es.ServerVar("banana_top_points_010_easy_sideways").set(2)
es.ServerVar("banana_top_points_011_easy_sideways").set(1)
es.ServerVar("banana_top_points_012_easy_sideways").set(1)
es.ServerVar("banana_top_points_013_easy_sideways").set(1)
es.ServerVar("banana_top_points_014_easy_sideways").set(1)
es.ServerVar("banana_top_points_015_easy_sideways").set(1)
es.ServerVar("banana_top_points_016_easy_sideways").set(1)
es.ServerVar("banana_top_points_017_easy_sideways").set(1)
es.ServerVar("banana_top_points_018_easy_sideways").set(1)
es.ServerVar("banana_top_points_019_easy_sideways").set(1)
es.ServerVar("banana_top_points_020_easy_sideways").set(1)
#* easy maps completed on W-only
es.ServerVar("banana_top_points_001_easy_wonly").set(40)
es.ServerVar("banana_top_points_002_easy_wonly").set(36)
es.ServerVar("banana_top_points_003_easy_wonly").set(32)
es.ServerVar("banana_top_points_004_easy_wonly").set(28)
es.ServerVar("banana_top_points_005_easy_wonly").set(24)
es.ServerVar("banana_top_points_006_easy_wonly").set(20)
es.ServerVar("banana_top_points_007_easy_wonly").set(16)
es.ServerVar("banana_top_points_008_easy_wonly").set(12)
es.ServerVar("banana_top_points_009_easy_wonly").set(8)
es.ServerVar("banana_top_points_010_easy_wonly").set(4)
es.ServerVar("banana_top_points_011_easy_wonly").set(2)
es.ServerVar("banana_top_points_012_easy_wonly").set(2)
es.ServerVar("banana_top_points_013_easy_wonly").set(2)
es.ServerVar("banana_top_points_014_easy_wonly").set(2)
es.ServerVar("banana_top_points_015_easy_wonly").set(2)
es.ServerVar("banana_top_points_016_easy_wonly").set(2)
es.ServerVar("banana_top_points_017_easy_wonly").set(2)
es.ServerVar("banana_top_points_018_easy_wonly").set(2)
es.ServerVar("banana_top_points_019_easy_wonly").set(2)
es.ServerVar("banana_top_points_020_easy_wonly").set(2)
#* medium maps completed on normal
es.ServerVar("banana_top_points_001_medium_normal").set(20)
es.ServerVar("banana_top_points_002_medium_normal").set(18)
es.ServerVar("banana_top_points_003_medium_normal").set(16)
es.ServerVar("banana_top_points_004_medium_normal").set(14)
es.ServerVar("banana_top_points_005_medium_normal").set(12)
es.ServerVar("banana_top_points_006_medium_normal").set(10)
es.ServerVar("banana_top_points_007_medium_normal").set(8)
es.ServerVar("banana_top_points_008_medium_normal").set(6)
es.ServerVar("banana_top_points_009_medium_normal").set(4)
es.ServerVar("banana_top_points_010_medium_normal").set(2)
es.ServerVar("banana_top_points_011_medium_normal").set(1)
es.ServerVar("banana_top_points_012_medium_normal").set(1)
es.ServerVar("banana_top_points_013_medium_normal").set(1)
es.ServerVar("banana_top_points_014_medium_normal").set(1)
es.ServerVar("banana_top_points_015_medium_normal").set(1)
es.ServerVar("banana_top_points_016_medium_normal").set(1)
es.ServerVar("banana_top_points_017_medium_normal").set(1)
es.ServerVar("banana_top_points_018_medium_normal").set(1)
es.ServerVar("banana_top_points_019_medium_normal").set(1)
es.ServerVar("banana_top_points_020_medium_normal").set(1)
#* medium maps completed on sideways
es.ServerVar("banana_top_points_001_medium_sideways").set(50)
es.ServerVar("banana_top_points_002_medium_sideways").set(45)
es.ServerVar("banana_top_points_003_medium_sideways").set(40)
es.ServerVar("banana_top_points_004_medium_sideways").set(35)
es.ServerVar("banana_top_points_005_medium_sideways").set(30)
es.ServerVar("banana_top_points_006_medium_sideways").set(25)
es.ServerVar("banana_top_points_007_medium_sideways").set(20)
es.ServerVar("banana_top_points_008_medium_sideways").set(15)
es.ServerVar("banana_top_points_009_medium_sideways").set(10)
es.ServerVar("banana_top_points_010_medium_sideways").set(5)
es.ServerVar("banana_top_points_011_medium_sideways").set(2)
es.ServerVar("banana_top_points_012_medium_sideways").set(2)
es.ServerVar("banana_top_points_013_medium_sideways").set(2)
es.ServerVar("banana_top_points_014_medium_sideways").set(2)
es.ServerVar("banana_top_points_015_medium_sideways").set(2)
es.ServerVar("banana_top_points_016_medium_sideways").set(2)
es.ServerVar("banana_top_points_017_medium_sideways").set(2)
es.ServerVar("banana_top_points_018_medium_sideways").set(2)
es.ServerVar("banana_top_points_019_medium_sideways").set(2)
es.ServerVar("banana_top_points_020_medium_sideways").set(2)
#* medium maps completed on W-only
es.ServerVar("banana_top_points_001_medium_wonly").set(100)
es.ServerVar("banana_top_points_002_medium_wonly").set(90)
es.ServerVar("banana_top_points_003_medium_wonly").set(80)
es.ServerVar("banana_top_points_004_medium_wonly").set(70)
es.ServerVar("banana_top_points_005_medium_wonly").set(60)
es.ServerVar("banana_top_points_006_medium_wonly").set(50)
es.ServerVar("banana_top_points_007_medium_wonly").set(40)
es.ServerVar("banana_top_points_008_medium_wonly").set(30)
es.ServerVar("banana_top_points_009_medium_wonly").set(20)
es.ServerVar("banana_top_points_010_medium_wonly").set(10)
es.ServerVar("banana_top_points_011_medium_wonly").set(5)
es.ServerVar("banana_top_points_012_medium_wonly").set(5)
es.ServerVar("banana_top_points_013_medium_wonly").set(5)
es.ServerVar("banana_top_points_014_medium_wonly").set(5)
es.ServerVar("banana_top_points_015_medium_wonly").set(5)
es.ServerVar("banana_top_points_016_medium_wonly").set(5)
es.ServerVar("banana_top_points_017_medium_wonly").set(5)
es.ServerVar("banana_top_points_018_medium_wonly").set(5)
es.ServerVar("banana_top_points_019_medium_wonly").set(5)
es.ServerVar("banana_top_points_020_medium_wonly").set(5)
#* hard maps completed on normal
es.ServerVar("banana_top_points_001_hard_normal").set(100)
es.ServerVar("banana_top_points_002_hard_normal").set(90)
es.ServerVar("banana_top_points_003_hard_normal").set(80)
es.ServerVar("banana_top_points_004_hard_normal").set(70)
es.ServerVar("banana_top_points_005_hard_normal").set(60)
es.ServerVar("banana_top_points_006_hard_normal").set(50)
es.ServerVar("banana_top_points_007_hard_normal").set(40)
es.ServerVar("banana_top_points_008_hard_normal").set(30)
es.ServerVar("banana_top_points_009_hard_normal").set(20)
es.ServerVar("banana_top_points_010_hard_normal").set(10)
es.ServerVar("banana_top_points_011_hard_normal").set(5)
es.ServerVar("banana_top_points_012_hard_normal").set(5)
es.ServerVar("banana_top_points_013_hard_normal").set(5)
es.ServerVar("banana_top_points_014_hard_normal").set(5)
es.ServerVar("banana_top_points_015_hard_normal").set(5)
es.ServerVar("banana_top_points_016_hard_normal").set(5)
es.ServerVar("banana_top_points_017_hard_normal").set(5)
es.ServerVar("banana_top_points_018_hard_normal").set(5)
es.ServerVar("banana_top_points_019_hard_normal").set(5)
es.ServerVar("banana_top_points_020_hard_normal").set(5)
#* hard maps completed on sideways
es.ServerVar("banana_top_points_001_hard_sideways").set(200)
es.ServerVar("banana_top_points_002_hard_sideways").set(180)
es.ServerVar("banana_top_points_003_hard_sideways").set(160)
es.ServerVar("banana_top_points_004_hard_sideways").set(140)
es.ServerVar("banana_top_points_005_hard_sideways").set(120)
es.ServerVar("banana_top_points_006_hard_sideways").set(100)
es.ServerVar("banana_top_points_007_hard_sideways").set(80)
es.ServerVar("banana_top_points_008_hard_sideways").set(60)
es.ServerVar("banana_top_points_009_hard_sideways").set(40)
es.ServerVar("banana_top_points_010_hard_sideways").set(20)
es.ServerVar("banana_top_points_011_hard_sideways").set(10)
es.ServerVar("banana_top_points_012_hard_sideways").set(10)
es.ServerVar("banana_top_points_013_hard_sideways").set(10)
es.ServerVar("banana_top_points_014_hard_sideways").set(10)
es.ServerVar("banana_top_points_015_hard_sideways").set(10)
es.ServerVar("banana_top_points_016_hard_sideways").set(10)
es.ServerVar("banana_top_points_017_hard_sideways").set(10)
es.ServerVar("banana_top_points_018_hard_sideways").set(10)
es.ServerVar("banana_top_points_019_hard_sideways").set(10)
es.ServerVar("banana_top_points_020_hard_sideways").set(10)
#* hard maps completed on W-only
es.ServerVar("banana_top_points_001_hard_wonly").set(500)
es.ServerVar("banana_top_points_002_hard_wonly").set(450)
es.ServerVar("banana_top_points_003_hard_wonly").set(400)
es.ServerVar("banana_top_points_004_hard_wonly").set(350)
es.ServerVar("banana_top_points_005_hard_wonly").set(300)
es.ServerVar("banana_top_points_006_hard_wonly").set(250)
es.ServerVar("banana_top_points_007_hard_wonly").set(200)
es.ServerVar("banana_top_points_008_hard_wonly").set(150)
es.ServerVar("banana_top_points_009_hard_wonly").set(100)
es.ServerVar("banana_top_points_010_hard_wonly").set(50)
es.ServerVar("banana_top_points_011_hard_wonly").set(20)
es.ServerVar("banana_top_points_012_hard_wonly").set(20)
es.ServerVar("banana_top_points_013_hard_wonly").set(20)
es.ServerVar("banana_top_points_014_hard_wonly").set(20)
es.ServerVar("banana_top_points_015_hard_wonly").set(20)
es.ServerVar("banana_top_points_016_hard_wonly").set(20)
es.ServerVar("banana_top_points_017_hard_wonly").set(20)
es.ServerVar("banana_top_points_018_hard_wonly").set(20)
es.ServerVar("banana_top_points_019_hard_wonly").set(20)
es.ServerVar("banana_top_points_020_hard_wonly").set(20)

## Import Modules
import os
import time
import psyco
import random
import corelib
import usermsg
import langlib
import cPickle
import vecmath
import popuplib
import services
import playerlib
import effectlib
import gamethread
from time import strftime
from usermsg import saytext2
from operator import itemgetter
psyco.full()

## Globals
started                     = []
effects                     = []
statsmenuscreated           = []
WantsPadNTimer              = {}
WantsPadNTimer['pad']       = {}
WantsPadNTimer['timer']     = {}
WantsBoostDict              = {}
WantsBoostDict[0]           = {}
WantsBoostDict[1]           = {}
WantsBoostDict[2]           = {}
fps_max_dict                = {}
deaths_list                 = {}
mapDicts                    = {}
mapDicts_W                  = {}
mapDicts_SW                 = {}
mapDicts_54                 = {}
mapDicts_W_54               = {}
mapDicts_SW_54              = {}
mapDicts_300                = {}
mapDicts_W_300              = {}
mapDicts_SW_300             = {}
JumpDict                    = {}
JumpDict["Status"]          = {}
JumpDict["LastJump"]        = {}
JumpDict["Active"]          = {}
JumpDict["Active"]["w"]     = {}
JumpDict["Active"]["a"]     = {}
JumpDict["Active"]["s"]     = {}
JumpDict["Active"]["d"]     = {}
JumpDict["Active"]["jump"]  = {}
JumpDict["Active"]["duck"]  = {}
players                     = {}
playerList = None
cp_save_max = '200'
scoutlist = []
checkpoints = {}
liste = []
infos = {}
owntext = "!info"
player_send = "all"
popup_timeout = 10
currentMap = es.ServerVar('eventscripts_currentmap')
waitTime = 0.01
dissolventMethod = 4 #0 - Energy Effect | 1 - Heavy Electrical | 2 - Light Electrical | 3 - Core Effect | 4 - Random Effect

##Script Info
info = es.AddonInfo()
info.author      = "TheCheeTaH"
info.name        = "BananaScript"
info.basename    = "bananascript"
info.version     = "3.1.5"
info.url         = "http://www.bananahop.com"
info.description = "Bunny hop timer. Counts jumps, time, and even the way you jump!"
es.ServerVar(info.basename, '%s-Private-%s' %(info.version,info.author), info.description + " ----- Made By " + info.author).makepublic()

lang = langlib.Strings(es.getAddonPath("bananascript") + "/strings.ini")
text = lambda identifier, options = {}, lang = "en" : "No strings.ini found in ../addons/eventscripts/%(basename)s/%(basename)s.py" % {"basename" : info.basename}

''' Load the dictionary '''
dictPath = os.path.join( es.getAddonPath( "bananascript" ), "data.db" )
if os.path.isfile(dictPath):
    fileStream = open(dictPath, 'rb')
    mapDicts   = cPickle.load(fileStream)
    fileStream.close()
dictPath_W = os.path.join( es.getAddonPath( "bananascript" ), "data_W.db" )
if os.path.isfile(dictPath_W):
    fileStream_W = open(dictPath_W, 'rb')
    mapDicts_W   = cPickle.load(fileStream_W)
    fileStream_W.close()
dictPath_SW = os.path.join( es.getAddonPath( "bananascript" ), "data_SW.db" )
if os.path.isfile(dictPath_SW):
    fileStream_SW = open(dictPath_SW, 'rb')
    mapDicts_SW   = cPickle.load(fileStream_SW)
    fileStream_SW.close()
dictPath_54 = os.path.join( es.getAddonPath( "bananascript" ), "data_54.db" )
if os.path.isfile(dictPath_54):
    fileStream_54 = open(dictPath_54, 'rb')
    mapDicts_54   = cPickle.load(fileStream_54)
    fileStream_54.close()
dictPath_W_54 = os.path.join( es.getAddonPath( "bananascript" ), "data_W_54.db" )
if os.path.isfile(dictPath_W_54):
    fileStream_W_54 = open(dictPath_W_54, 'rb')
    mapDicts_W_54   = cPickle.load(fileStream_W_54)
    fileStream_W_54.close()
dictPath_SW_54 = os.path.join( es.getAddonPath( "bananascript" ), "data_SW_54.db" )
if os.path.isfile(dictPath_SW_54):
    fileStream_SW_54 = open(dictPath_SW_54, 'rb')
    mapDicts_SW_54   = cPickle.load(fileStream_SW_54)
    fileStream_SW_54.close()
dictPath_300 = os.path.join( es.getAddonPath( "bananascript" ), "data_300.db" )
if os.path.isfile(dictPath_300):
    fileStream_300 = open(dictPath_300, 'rb')
    mapDicts_300   = cPickle.load(fileStream_300)
    fileStream_300.close()
dictPath_W_300 = os.path.join( es.getAddonPath( "bananascript" ), "data_W_300.db" )
if os.path.isfile(dictPath_W_300):
    fileStream_W_300 = open(dictPath_W_300, 'rb')
    mapDicts_W_300   = cPickle.load(fileStream_W_300)
    fileStream_W_300.close()
dictPath_SW_300 = os.path.join( es.getAddonPath( "bananascript" ), "data_SW_300.db" )
if os.path.isfile(dictPath_SW_300):
    fileStream_SW_300 = open(dictPath_SW_300, 'rb')
    mapDicts_SW_300   = cPickle.load(fileStream_SW_300)
    fileStream_SW_300.close()

file = es.getAddonPath('bananascript') + '/infos.db'
if os.path.isfile(file):
    file_players = open(file)
    infos = cPickle.load(file_players)
    file_players.close()

cpDict = os.path.join( es.getAddonPath( "bananascript" ), "saves.db" )
if os.path.isfile(cpDict):
    cpFile = open(cpDict, 'rb')
    checkpoints   = cPickle.load(cpFile)
    cpFile.close()
else:
    checkpoints = {}

''' Load the languages '''
langPath = os.path.join( es.getAddonPath( info.basename ), "strings.ini" )
if os.path.isfile(langPath):
    text = langlib.Strings(langPath)
''' Set up an auth check service, to return whether or not the user is authed. '''
if services.isRegistered('auth'):
    auth_service = services.use('auth')
    auth_service.registerCapability('climbtimer', auth_service.ADMIN)
    isAuthed = lambda x: auth_service.isUseridAuthorized(x, 'climbtimer')
else:
    isAuthed = lambda x: False
def load():
    SetUpStats()
    es.addons.registerClientCommandFilter(myfilter)
    save_cpdict()
    gamethread.delayedname(0.1,'MapsFix',MapsFix)
    es.msg("#multi","#darkgreenBanana Script #default(#greenv%s#default)#darkgreen has been #lightgreenloaded#darkgreen!"%info.version)
    if TickListener_Enabled:
        es.addons.registerTickListener(ticklistener)
    es.msg("TickListener: %s" %(TickListener_Enabled2(TickListener_Enabled)))
    StartValueChecker()
    es.server.queuecmd("mp_restartgame 1")
    ''' If the script is loaded halfway through a load, ensure the delays start '''
    # Say CMDS
    addMap = es.ServerVar('eventscripts_currentmap')
    if str(currentMap):
        es_map_start({'mapname':str(currentMap)})
    if not es.exists('saycommand', '!lazyshit'):
        es.regsaycmd('!lazyshit', 'bananascript/wantsboost')
    if not es.exists('saycommand', '!save'):
        es.regsaycmd('!save', 'bananascript/save')
    if not es.exists('saycommand', '!next'):
        es.regsaycmd('!next', 'bananascript/next')
    if not es.exists('saycommand', '!back'):
        es.regsaycmd('!back', 'bananascript/back')
    if not es.exists('saycommand', '!reset'):
        es.regsaycmd('!reset', 'bananascript/reset')
    if not es.exists('saycommand', '!ghost'):
        es.regsaycmd('!ghost', 'bananascript/ghost')
    if not es.exists('saycommand', '!unghost'):
        es.regsaycmd('!unghost', 'bananascript/unghost')
    if not es.exists('saycommand', '!scout'):
        es.regsaycmd('!scout', 'bananascript/giveScout')
    if not es.exists('saycommand', '!usp'):
        es.regsaycmd('!usp', 'bananascript/giveUsp')
    if not es.exists('saycommand', '!flash'):
        es.regsaycmd('!flash', 'bananascript/giveFlash')
    if not es.exists('saycommand', '!kill'):
        es.regsaycmd('!kill', 'bananascript/goDead')
    if not es.exists('saycommand', '!spec'):
        es.regsaycmd('!spec', 'bananascript/goSpec')
    if not es.exists('saycommand', '!sp'):
        es.regsaycmd('!sp', 'bananascript/goSpec')
    if not es.exists('saycommand', '!menu'):
        es.regsaycmd('!bp', 'bananascript/menu')
    if not es.exists('saycommand', '!menu'):
        es.regsaycmd('!cp', 'bananascript/menu')
    if not es.exists('saycommand', '!chee'):
        es.regsaycmd('!chee', 'bananascript/erase')

    # Client CMDS
    if not es.exists('clientcommand', '!lazyshit'):
        es.regclientcmd('!lazyshit', 'bananascript/wantsboost')
    if not es.exists('clientcommand', 'cp_save'):
        es.regclientcmd('cp_save', 'bananascript/save')
    if not es.exists('clientcommand', 'cp_next'):
        es.regclientcmd('cp_next', 'bananascript/next')
    if not es.exists('clientcommand', 'cp_back'):
        es.regclientcmd('cp_back', 'bananascript/back')
    if not es.exists('clientcommand', 'cp_reset'):
        es.regclientcmd('cp_reset', 'bananascript/reset')
    if not es.exists('clientcommand', 'cp_ghost'):
        es.regclientcmd('cp_ghost', 'bananascript/ghost')
    if not es.exists('clientcommand', 'cp_unghost'):
        es.regclientcmd('cp_unghost', 'bananascript/unghost')
    if not es.exists('clientcommand', 'cp_scout'):
        es.regclientcmd('cp_scout', 'bananascript/giveScout')
    if not es.exists('clientcommand', 'cp_usp'):
        es.regclientcmd('cp_usp', 'bananascript/giveUsp')
    if not es.exists('clientcommand', 'cp_flash'):
        es.regclientcmd('cp_flash', 'bananascript/giveFlash')
    if not es.exists('clientcommand', 'cp_kill'):
        es.regclientcmd('cp_kill', 'bananascript/goDead')
    if not es.exists('clientcommand', 'cp_spec'):
        es.regclientcmd('cp_spec', 'bananascript/goSpec')
    if not es.exists('clientcommand', 'cp_menu'):
        es.regclientcmd('cp_menu', 'bananascript/menu')

    global menu
    menu = popuplib.create("checkpoints")
    menu.addline('[- Banana Points -]')
    menu.addline(' ')
    menu.addline('->1. Save')
    menu.addline('->2. Next')
    menu.addline('->3. Back')
    menu.addline('->4. Reset')
    menu.addline('->5. Scout')
    menu.addline('->6. USP')
    menu.addline('->7. Ghost/UnGhost')
    menu.addline('->8. Flash')
    menu.addline('->9. Spec')
    menu.addline(' ')
    menu.addline('NOTICE!')
    menu.addline('Options: 6 & 7')
    menu.addline('Is only for TRIKZ maps')
    menu.addline(' ')
    menu.addline('USER PANEL')
    menu.addline('To see rank type: !wr, !wrw or !wrsw')
    menu.addline('To open menu type: !cp')
    menu.addline(' ')
    menu.addline('To bind BHOP:')
    menu.addline('Type in CONSOLE:')
    menu.addline('=> bind mwheeldown +jump')
    menu.addline('=> bind mwheelup +jump')
    menu.addline(' ')
    menu.addline('TIPS FOR BEGINNERS')
    menu.addline('By moving the mouse')
    menu.addline('=> RIGHT, hold button [D]')
    menu.addline('<= LEFT , hold button [A]')
    menu.addline(' ')
    menu.addline('->0. Close')
    menu.menuselect = menu_select
    
    global adminPopup_4
    adminPopup_4 = popuplib.create("climbtimer_admin4")
    adminPopup_4.addline("Banana Timer ADMIN [4/4]")
    adminPopup_4.addline("-" * 30)
    adminPopup_4.addline("->1. Delete Records Sideways/Player Map")
    adminPopup_4.addline("->2. Delete Records Sideways/Player Map - 54")
    adminPopup_4.addline("->3. Delete Records Sideways/Player Map - 300")
    adminPopup_4.addline(" \n "*1)
    adminPopup_4.addline("-" * 30)
    adminPopup_4.addline("->8. Back")
    adminPopup_4.addline("9. Next")
    adminPopup_4.addline("-" * 30)
    adminPopup_4.addline("0. Close")
    adminPopup_4.menuselectfb = adminPopupMenuselect4
    
    global adminPopup_3
    adminPopup_3 = popuplib.create("climbtimer_admin3")
    adminPopup_3.addline("Banana Timer ADMIN [3/4]")
    adminPopup_3.addline("-" * 30)
    adminPopup_3.addline("->1. Delete Records W Only/Player Map")
    adminPopup_3.addline("->2. Delete Records W Only/Player Map - 54")
    adminPopup_3.addline("->3. Delete Records W Only/Player Map - 300")
    adminPopup_3.addline(" \n "*1)
    adminPopup_3.addline("-" * 30)
    adminPopup_3.addline("->8. Back")
    adminPopup_3.addline("->9. Next")
    adminPopup_3.addline("-" * 30)
    adminPopup_3.addline("0. Close")
    adminPopup_3.menuselectfb = adminPopupMenuselect3
    
    global adminPopup_2
    adminPopup_2 = popuplib.create("climbtimer_admin2")
    adminPopup_2.addline("Banana Timer ADMIN [2/4]")
    adminPopup_2.addline("-" * 30)
    adminPopup_2.addline("->1. Delete Records Normal/Player Map")
    adminPopup_2.addline("->2. Delete Records Normal/Player Map - 54")
    adminPopup_2.addline("->3. Delete Records Normal/Player Map - 300")
    adminPopup_2.addline(" \n "*1)
    adminPopup_2.addline("-" * 30)
    adminPopup_2.addline("->8. Back")
    adminPopup_2.addline("->9. Next")
    adminPopup_2.addline("-" * 30)
    adminPopup_2.addline("0. Close")
    adminPopup_2.menuselectfb = adminPopupMenuselect2
    
    global adminPopup
    adminPopup = popuplib.create("climbtimer_admin")
    adminPopup.addline("Banana Timer ADMIN [1/4]")
    adminPopup.addline("-" * 30)
    adminPopup.addline("->1. Add/Move Start Position")
    adminPopup.addline("->2. Add/Move End   Position")
    adminPopup.addline("->3. Delete Records and Start/End Position")
    adminPopup.addline("->4. Update !top")
    adminPopup.addline("->5. Erase !stats")
    adminPopup.addline("-" * 30)
    adminPopup.addline("8. Back")
    adminPopup.addline("->9. Next")
    adminPopup.addline("-" * 30)
    adminPopup.addline("0. Close")
    adminPopup.menuselectfb = adminPopupMenuselect
    RemoveIdleGuns()
    
def RemoveIdleGuns():
    gamethread.cancelDelayed('RemoveIdleGuns')
    gamethread.delayedname(5,'RemoveIdleGuns',RemoveIdleGuns)
    for entity in es.createentityindexlist():
        ClassName = str(es.entitygetvalue(entity, "classname"))
        if "weapon_" in ClassName:
            howner = es.getindexprop(entity, 'CBaseEntity.m_hOwnerEntity')
            if howner != None and howner == -1:
                TargetName = str(es.entitygetvalue(entity, "targetname"))
                #es.msg("%s: %s" %(hasTrail(entity),TargetName))
                mapName = str(currentMap)
                ShallRemove = 0
                if not hasTrail(entity):
                    ShallRemove = 1
                    
                if ShallRemove:
                    es.server.queuecmd("es_xremove %s" %entity)
def hasTrail(index):
    handle = es.gethandlefromindex(index)
    for entity in es.createentityindexlist("env_spritetrail"):
        if es.getindexprop(entity, "CBaseEntity.moveparent") == handle:
            return True
    return False
def QueryClientVars(userid):
    if int(es.ServerVar("block_yaw")):
        es.queryclientvar(userid,'cl_yawspeed')
    es.queryclientvar(userid,'fps_max')
    
def myfilter(userid,text,teamonly):
    return (userid, text, teamonly)
def isTrikz():
    if str(currentMap).startswith('trikz'):
        return 1
    else:
        return 0

def addMap(mapname):
    if not mapname in checkpoints:
        checkpoints[mapname] = {}
def SetUpTop():
    es.msg("#multi","#darkgreen[Banana Hop]#default Now updating #darkgreen!top#default.")
    gamethread.delayed(0.1,SetUpTop2)
def SetUpTop2():
    global TopMenu
    mapName = str(currentMap)
    TopMenu = popuplib.easymenu("TopMenu", None, EmptyMenuDef)
    TopMenu.c_beginsep = "-"*35
    TopMenu.c_pagesep = "-"*35
    TopMenu.settitle("[Banana Records : Top]\n%s\nLast updated (Server time):\n%s\nPage:" %("-" * 35,strftime("%d-%m-%Y %H:%M:%S (%I:%M:%S %p)")))
    sortedList = mk_sortDictPoints_54_and_300()
    if sortedList:
        lx = 0
        for top in sortedList:
            lx += 1
            Name   = top[1].split("___cheesplit!_|_!cheesplit___")[1]
            Points = top[1].split("___cheesplit!_|_!cheesplit___")[0]
            if Points == '00000': return
            TopMenu.addoption(None,"#%02d:  %s - %s" %(lx, Points, Name))
    else:
        TopMenu.addoption("[No Records]",0)
def SetUpStats():
    return
    es.msg("#multi","#darkgreen[Banana Hop]#default Now updating #darkgreen!stats#default.")
    gamethread.delayed(0.1,SetUpStats2)
def SetUpStats2():
    mapName = str(currentMap)
    TheTIME = strftime("%d-%m-%Y %H:%M:%S (%I:%M:%S %p)")
    PlayersToAdd = []
    for SteamID in mapDicts[mapName]:
        if SteamID not in PlayersToAdd: PlayersToAdd.append(SteamID)
    for SteamID in mapDicts_W[mapName]:
        if SteamID not in PlayersToAdd: PlayersToAdd.append(SteamID)
    for SteamID in mapDicts_SW[mapName]:
        if SteamID not in PlayersToAdd: PlayersToAdd.append(SteamID)
    for SteamID in PlayersToAdd:
        MapsFinishedValueNO54  = MapsFinished054(SteamID,'Normal')
        MapsFinishedValueWW54  = MapsFinished054(SteamID,'W')
        MapsFinishedValueSW54  = MapsFinished054(SteamID,'SW')
        MapsFinishedValueNO300 = MapsFinished300(SteamID,'Normal')
        MapsFinishedValueWW300 = MapsFinished300(SteamID,'W')
        MapsFinishedValueSW300 = MapsFinished300(SteamID,'SW')
        Points_54    = MapsFinished_Normal_Points54(SteamID)
        Points_54_W  = MapsFinished_W_Points54(SteamID)
        Points_54_SW = MapsFinished_SW_Points54(SteamID)
        Points_54_Total = Points_54+Points_54_W+Points_54_SW
        Points_300   = MapsFinished_Normal_Points300(SteamID)
        Points_300_W = MapsFinished_W_Points300(SteamID)
        Points_300_SW= MapsFinished_SW_Points300(SteamID)
        Points_300_Total = Points_300+Points_300_W+Points_300_SW
        Points_Total_Total = Points_300_Total+Points_54_Total
        PlayersRank = PlayersRankDef(SteamID)
        StatsMenu = popuplib.create("StatsMenu_%s" %(SteamID))
        StatsMenu.addline("[Banana Records : Stats]\n%s\nAs of:\n%s\n%s" % ("-" * 35,TheTIME,"-" * 35))
        StatsMenu.addline("Player %s" %SteamID)
        StatsMenu.addline("-"*35)
        StatsMenu.addline("FINISHED FPS_MAX 54")
        StatsMenu.addline('Normal    :  %03d - %04dP'%(int(MapsFinishedValueNO54),int(Points_54)))
        StatsMenu.addline('W-Only   :  %03d - %04dP'%(int(MapsFinishedValueWW54),int(Points_54_W)))
        StatsMenu.addline('Sideways:  %03d - %04dP'%(int(MapsFinishedValueSW54),int(Points_54_SW)))
        StatsMenu.addline("-"*35)
        StatsMenu.addline("FINISHED FPS_MAX 300")
        StatsMenu.addline('Normal    :  %03d - %04dP'%(int(MapsFinishedValueNO300),int(Points_300)))
        StatsMenu.addline('W-Only   :  %03d - %04dP'%(int(MapsFinishedValueWW300),int(Points_300_W)))
        StatsMenu.addline('Sideways:  %03d - %04dP'%(int(MapsFinishedValueSW300),int(Points_300_SW)))
        StatsMenu.addline("-"*35)
        StatsMenu.addline('Total       :  %s' %(Points_Total_Total))
        StatsMenu.addline('Rank#     : %s' %(PlayersRank))
        StatsMenu.addline("-" * 11 + "\n0.Close")
def SendWRThing(userid,choice,popupid):
    ev = {}
    ev['userid'] = userid
    ev['text'] = choice
    player_say(ev)
def EmptyMenuDef(userid,choice,popupid): return
def round_start(ev):
    save_cpdict()
    save_dictionary()
    SetUpTop()
    gamethread.cancelDelayed('RemoveIdleGuns')
    gamethread.delayedname(1,'RemoveIdleGuns',RemoveIdleGuns)
    
    mapName = es.ServerVar("eventscripts_currentmap")
    if mapName == 'bhop_baltimoron_beta_v2':
        for entity in es.createentityindexlist('hostage_entity'):
            LocLoc0 = es.getindexprop(entity,'CBaseEntity.m_vecOrigin').split(",")
            LocLocX = LocLoc0[0]
            LocLocY = LocLoc0[1]
            LocLocZ = LocLoc0[2]
            LocLoc1 = "%f,%f,%f" %(float(LocLocX),float(LocLocY),float(LocLocZ) + 60)
            if LocLocZ == '833.031250':
                es.setindexprop(entity,'CBaseEntity.m_vecOrigin',LocLoc1)

def TickListener_Enabled2(Value):
    if Value:
        return True
    return False
def round_end(ev):
    es_map_start({"mapname":str(currentMap)})
    save_cpdict()
def SetUpSlots():
    entities = list(es.createentityindexlist("info_player_terrorist")) + list(es.createentityindexlist("info_player_counterterrorist"))
    count = len(entities)
    while count < 64:
        for entity in entities:
            count += 1
            index = es.createentity(es.entitygetvalue(entity, "classname"))
            es.entitysetvalue(index, "origin", es.entitygetvalue(entity, "origin"))
            es.entitysetvalue(index, "angles", es.entitygetvalue(entity, "angles"))
            es.spawnentity(index)
def es_map_start(ev):
    #ResetStats()
    global cs_player_manager
    cs_player_manager = es.getentityindex("cs_player_manager")
    SetUpSlots()
    addMap(ev['mapname'])
    ''' Clear the lists '''
    del started[:]
    players.clear()
    ''' Save the database '''
    fileStream = open(dictPath, 'wb')
    cPickle.dump(mapDicts, fileStream)
    fileStream.close()
    fileStream_W = open(dictPath_W, 'wb')
    cPickle.dump(mapDicts_W, fileStream_W)
    fileStream_W.close()
    fileStream_SW = open(dictPath_SW, 'wb')
    cPickle.dump(mapDicts_SW, fileStream_SW)
    fileStream_SW.close()
    fileStream_54 = open(dictPath_54, 'wb')
    cPickle.dump(mapDicts_54, fileStream_54)
    fileStream_54.close()
    fileStream_W_54 = open(dictPath_W_54, 'wb')
    cPickle.dump(mapDicts_W_54, fileStream_W_54)
    fileStream_W_54.close()
    fileStream_SW_54 = open(dictPath_SW_54, 'wb')
    cPickle.dump(mapDicts_SW_54, fileStream_SW_54)
    fileStream_SW_54.close()
    fileStream_300 = open(dictPath_300, 'wb')
    cPickle.dump(mapDicts_300, fileStream_300)
    fileStream_300.close()
    fileStream_W_300 = open(dictPath_W_300, 'wb')
    cPickle.dump(mapDicts_W_300, fileStream_W_300)
    fileStream_W_300.close()
    fileStream_SW_300 = open(dictPath_SW_300, 'wb')
    cPickle.dump(mapDicts_SW_300, fileStream_SW_300)
    fileStream_SW_300.close()
    ''' Restart the timer if there isn't a timer already '''
    gamethread.cancelDelayed('climbtime_checkloop')
    gamethread.cancelDelayed('RemoveIdleGuns')
    gamethread.cancelDelayed('climbtimer_hudloop')
    gamethread.cancelDelayed('climbtimer_hudloop2')
    StopCode = 0
    if (ev['mapname']) in mapDicts:
        if "endpos" not in mapDicts[ev['mapname']]:
            StopCode = 1
        if "startpos" not in mapDicts[ev['mapname']]:
            StopCode = 1
        if StopCode == 0:
            gamethread.delayedname(0.1, 'climbtime_checkloop', checkLoop)
            hudLoop()
            hudLoop2()

def save_cpdict():
    cp_save = os.path.join( es.getAddonPath( "bananascript" ) , "saves.db" )
    cp_saves = open(cp_save, 'wb')
    cPickle.dump(checkpoints, cp_saves)
    cp_saves.close()

def save_dictionary():
    file_players = open(es.getAddonPath('bananascript') + '/infos.db', 'wb')
    cPickle.dump(infos, file_players)
    file_players.close()

def player_disconnect(ev):
    ''' If a player disconnects early, clear up the delay list. '''
    userid = int(ev['userid'])
    if userid in started:
        started.remove(userid)
    if userid in players:
        del players[userid]

def flashbang_detonate(ev):
    for flashedplayer in es.getUseridList():
        es.setplayerprop(flashedplayer, 'CCSPlayer.m_flFlashDuration', 0, 8)

def weapon_fire(ev):
    if ev['weapon'] == 'flashbang':
        es.delayed(1.45, 'es_xremove flashbang_projectile')
def wantsboost():
    if not int(es.ServerVar("enable_jump")): return
    Userid  = es.getcmduserid()
    SteamID = es.getplayersteamid(Userid)
    if not es.exists('userid',Userid): return
    if SteamID not in Push11FPS and SteamID not in Push00FPS: return
    if SteamID not in WantsBoostDict[0]: WantsBoostDict[0][SteamID] = 0
    if SteamID not in WantsBoostDict[1]: WantsBoostDict[1][SteamID] = 0
    if SteamID not in WantsBoostDict[2]: WantsBoostDict[2][SteamID] = 0
    WantsBoostMenu = popuplib.easymenu("WantsBoostMenu%s" %(Userid), None, wantsboostChoice)
    WantsBoostMenu.c_beginsep = "-"*35
    WantsBoostMenu.c_pagesep = "-"*35
    WantsBoostMenu.settitle("[Banana : Boost]\n%s\nCurrent Boost:\n%02d,%02d,%02d\n%s\nPage: " % ("-" * 35,WantsBoostDict[0][SteamID],WantsBoostDict[1][SteamID],WantsBoostDict[2][SteamID],"-" * 35))
    WantsBoostMenu.addoption("00|00|00","Off            - 00,00,00")
    WantsBoostMenu.addoption("30|02|01","2x Speed   - 30,02,01")
    WantsBoostMenu.addoption("50|04|01","5x Speed   - 50,04,01")
    #WantsBoostMenu.addoption("400|08|01","9x Speed   - 400,08,01")
    WantsBoostMenu.send(Userid)
def wantsboostChoice(userid,choice,popupname):
    ChoiceSplitted = choice.split("|")
    SteamID = es.getplayersteamid(userid)
    WantsBoostDict[0][SteamID] = int(ChoiceSplitted[0])
    WantsBoostDict[1][SteamID] = int(ChoiceSplitted[1])
    WantsBoostDict[2][SteamID] = int(ChoiceSplitted[2])
def player_jump(ev):
    ShallPush = 0
    userid = int(ev['userid'])
    if int(es.ServerVar("enable_jump")):
        useridSTR = str(userid)
        SteamID = ev['es_steamid']
        if SteamID in Push11FPS:
            ShallPush = 1
        if SteamID in Push00FPS:
            if useridSTR in fps_max_dict:
                WantedFPS = int(fps_max_dict[useridSTR])
                if WantedFPS >= FPS54_Starts and WantedFPS <= FPS54_Ends:
                    ShallPush = 0
        if ShallPush:
            if SteamID not in WantsBoostDict[0]: WantsBoostDict[0][SteamID] = 0
            if SteamID not in WantsBoostDict[1]: WantsBoostDict[1][SteamID] = 0
            if SteamID not in WantsBoostDict[2]: WantsBoostDict[2][SteamID] = 0
            es.server.queuecmd("playerset push %s %s %s %s" %(userid,WantsBoostDict[0][SteamID],WantsBoostDict[1][SteamID],WantsBoostDict[2][SteamID]))
    if userid not in players:
        return
    players[userid][1] += 1
def MapsFix():
    AllPlayersPlayerLibs = playerlib.getUseridList("#alive")
    mapName = es.ServerVar("eventscripts_currentmap")
    SpecialMapos = ['bhop_exodus','bhop_challenge','bhop_baltimoron_beta_v2']
    if mapName not in SpecialMapos:
        gamethread.delayedname(20,'MapsFix',MapsFix)
    else:
        gamethread.delayedname(0.4,'MapsFix',MapsFix)
    for userid in AllPlayersPlayerLibs:
        Location = es.getplayerlocation(userid)
        # BHOP CHALLENGE
        if mapName == 'bhop_challenge':
            if Location[0] > 1450.0 and Location[0] < 1850.0:
                if Location[1] > 650.0 and Location[1] < 1000.0:
                    if Location[2] > 0.0 and Location[2] < 100.0:
                        es.entitysetvalue(playerlib.getPlayer(userid).index, 'origin', ' '.join("-1498.1920166015625,8222.7841796875,2513.924560546875".split(',')))
                        return
        # BHOP BALTIMORON BETA V2
        elif mapName == 'bhop_baltimoron_beta_v2':
            if Location[0] > 3100.0 and Location[0] < 3208.0:
                if Location[1] > 1872.0 and Location[1] < 3951.0:
                    if Location[2] > 888.0 and Location[2] < 1357.9:
                        es.entitysetvalue(playerlib.getPlayer(userid).index, 'origin', ' '.join("8112.8203125,2866.783203125,896.03125".split(',')))
                        return
        # BHOP EXODUS
        elif mapName == 'bhop_exodus':
            # Exodus level 3 fix
            if Location[0] == -6368.0 and Location[1] == -4992.0:
                if Location[2] > 4045.0 and Location[2] < 4075.0:
                    es.entitysetvalue(playerlib.getPlayer(userid).index, 'origin', ' '.join("-7162.977051,-4985.606934,4104.093750".split(',')))
                    return
            # Exodus level 6 fix
            elif Location[0] > 1750.0 and Location[0] < 3750.0:
                if Location[1] > 7800.0 and Location[1] < 9800.0:
                    if Location[2] > 5000.0 and Location[2] < 6300.0:
                        es.entitysetvalue(playerlib.getPlayer(userid).index, 'origin', ' '.join("-10935.9033203125,6694.24462890625,2497.34423828125".split(',')))
                        return
            # Exodus level 10 fix'''
            elif Location[0] > -500.0 and Location[0] < -425.0:
                if Location[1] > 11450.0 and Location[1] < 11770.0:
                    if Location[2] > 5000.0 and Location[2] < 5100.0:
                        es.entitysetvalue(playerlib.getPlayer(userid).index, 'origin', ' '.join("-1280.95,11909.90,4800.10".split(',')))
                        return

def StartValueChecker():
    gamethread.delayedname(15,'StartValueChecker',StartValueChecker)
    for userid in playerlib.getUseridList("#human"):
        QueryClientVars(userid)

def dissolve(userid):
    waitTempo = waitTime + 0.05
    es.server.queuecmd('es_give %s env_entity_dissolver'% userid)
    es.server.queuecmd('es_xfire %s env_entity_dissolver AddOutput "target cs_ragdoll"'% userid)
    es.server.queuecmd('es_xfire %s env_entity_dissolver AddOutput "magnitude 1"'% userid)
    if dissolventMethod == 4:
        es.server.queuecmd('es_xfire %s env_entity_dissolver AddOutput "dissolvetype %s"' % (userid, random.randint(0, 3)))
    else:
        es.server.queuecmd('es_xfire %s env_entity_dissolver AddOutput "dissolvetype %s"' % (userid, dissolventMethod))
    es.server.queuecmd('es_xfire %s env_entity_dissolver Dissolve'% userid)
    gamethread.delayed(waitTempo, es.server.queuecmd, 'es_xremove env_entity_dissolver')

def ticklistener():
    for player in playerlib.getPlayerList("#all"):
        userid = int(player.userid)
        if not userid in deaths_list:
            continue
        es.setindexprop(es.getentityindex("cs_player_manager"), "CPlayerResource.m_iDeaths.%.3d" % player.attributes["index"], deaths_list[userid])

def player_death(ev):
    userid = int(ev['userid'])
    #deaths_list[userid] += 1
    playersteamid = es.getplayersteamid(userid)
    dissolve(userid)
    mapName = str(currentMap)
    SetPlayersKills(userid,infos[playersteamid][mapName]["kills"])
    if userid in started:
        started.remove(userid)
    if userid in players:
        del players[userid]
    if userid in scoutlist:
        scoutlist.remove(userid)
def myfilter(userid, args,PreventError=True):
    if args[0] == 'joinclass':
        gamethread.delayed(0.1,RespawnIfDead,userid)
    return True
def RespawnIfDead(userid):
    if playerlib.getPlayer(userid).isdead:
        es.setplayerprop(userid,'CBasePlayer.m_lifeState',512)
        es.setplayerprop(userid,'CCSPlayer.m_iPlayerState',0)
        es.server.queuecmd("es_xspawnplayer %s" % userid)
def player_activate(event_var):
    es.server.mp_disable_autokick(event_var["userid"])
def GiveNeededGuns(userid):
    if playerlib.getPlayer(userid).isdead: return
    es.server.queuecmd("es_xgive %s player_weaponstrip" %(userid))
    es.server.queuecmd("es_xfire %s player_weaponstrip strip" %(userid))
    es.server.queuecmd("es_xfire %s player_weaponstrip kill" %(userid))
    gamethread.delayed(0.05,GiveNeededGuns2,userid)
def GiveNeededGuns2(userid):
    es.server.queuecmd("es_xgive %s weapon_knife" %(userid))
    es.server.queuecmd("es_xgive %s weapon_usp" %(userid))
    es.server.queuecmd("es_xgive %s weapon_scout" %(userid))
def player_spawn(ev):
    global infos
    userid = int(ev['userid'])
    gamethread.delayed(0.1,GiveNeededGuns,userid)
    if not es.exists('userid',userid): return
    if currentMap == 'bhop_exodus': es.server.queuecmd("es_xfire %s env_soundscape kill" %(userid))
    if int(es.getplayerteam(userid)) not in [2,3]: return
    player = playerlib.getPlayer(userid)
    player.setModel("player/slow/banana_joe/slow.mdl")
    if userid in JumpDict["Status"]: del JumpDict["Status"][userid]
    if userid in JumpDict["LastJump"]: del JumpDict["LastJump"][userid]
    steamid1 = ev['es_steamid']
    if steamid1 != 'STEAM_ID_PENDING':
        if steamid1 not in infos:
            infos[steamid1] = {} 
        if str(currentMap) not in infos[steamid1]:
            infos[steamid1][str(currentMap)] = {}
        if userid in started:
            started.remove(userid)
            tell(userid, 'Reset Spawn', {})
        if "kills" not in infos[steamid1][str(currentMap)]:
            infos[steamid1][str(currentMap)]["kills"] = 2000
        if int(negScore(infos[steamid1][str(currentMap)]["kills"])) > -1999:
            SetPlayersKills(player.userid,negScore(infos[steamid1][str(currentMap)]["kills"])-1)
        else:
            SetPlayersKills(player.userid,-2000)
        (_pos, _len) = mk_sortDictIndex(str(currentMap), steamid1)
        SetDeaths(player.userid, _pos)
    player.set('health', '500')
    if not player.get('noblock'):
        player.set('noblock', '1')
        player.set('color', (255, 255, 255, 100))

def player_hurt(ev):
    if not es.exists('userid',ev['userid']): return
    player = playerlib.getPlayer(ev['userid'])
    player.set('health', '500')

def goSpec():
    userid = es.getcmduserid()
    if not es.exists('userid',userid): return
    player = playerlib.getPlayer(userid)
    if userid in started:
        started.remove(userid)
        tell(userid, 'Reset Spec', {})
    if userid in players:
        del players[userid]
    if player['team'] != 1:
        es.give(userid, 'player_weaponstrip')
        es.fire(userid, 'player_weaponstrip', 'strip')
        es.fire(userid, 'player_weaponstrip', 'kill')
        es.server.queuecmd("es_xchangeteam %s 1" % player)
        dissolve(userid)
def client_keypress(ev):
    pressedKey = ev["keyname"]
    if pressedKey not in ['forward','back','moveright','moveleft','left','right','duck','jump']: return
    userid = int(ev['userid'])
    NewStatus = int(ev['status'])
    if not es.exists('userid',userid): return
    useridP = playerlib.getPlayer(userid)
    if int(es.ServerVar("block_left")):
        if pressedKey in ['left','right'] and not NewStatus:
            es.tell(userid, 'Unfrozen for stopped using +left/+right!')
            useridP.freeze(0)
            useridP.setColor(255,255,255,100)
    if pressedKey == 'forward':
        JumpDict["Active"]["w"][userid] = NewStatus
        hudLoop2()
    elif pressedKey == 'moveleft':
        JumpDict["Active"]["a"][userid] = NewStatus
        hudLoop2()
    elif pressedKey == 'back':
        JumpDict["Active"]["s"][userid] = NewStatus
        hudLoop2()
    elif pressedKey == 'moveright':
        JumpDict["Active"]["d"][userid] = NewStatus
        hudLoop2()
    elif pressedKey == 'jump':
        JumpDict["Active"]["jump"][userid] = NewStatus
        hudLoop2()
    elif pressedKey == 'duck':
        JumpDict["Active"]["duck"][userid] = NewStatus
        hudLoop2()
        return
    if not NewStatus: return
    if int(es.ServerVar("block_left")):
        if pressedKey in ['left','right']:
            es.tell(userid, 'Frozen for using +left/+right!')
            useridP.freeze(1)
            useridP.setColor(0,0,255,255)
    if pressedKey in ['left','right','duck','jump']: return
    if playerlib.getPlayer(userid).onGround(): return
    if userid not in JumpDict["LastJump"]:
        JumpDict["LastJump"][userid] = pressedKey
        return
    if userid not in JumpDict["Status"]:
        JumpDict["Status"][userid] = "Haven't started yet!"
        return
    NewStatus = "None"
    #es.tell(userid,"1: %s" %(ev["keyname"]))                    #1: back        .
    #es.tell(userid,"2: %s" %(JumpDict["LastJump"][userid]))     #2: forward     .
    #es.tell(userid,"3: %s" %(JumpDict["Status"][userid]))       #3: W Only         .
    if ev["keyname"] == 'forward' and JumpDict["Status"][userid] != 'Sideways' and JumpDict["Status"][userid] != "Normal" and JumpDict["Status"][userid] != "None":
        NewStatus = "W Only"
    elif pressedKey == 'back' and JumpDict["Status"][userid] == 'W Only':
        NewStatus = "Sideways"
    elif JumpDict["LastJump"][userid] == 'back' or JumpDict["LastJump"][userid] == 'forward':
        if ev["keyname"] == 'forward' or ev["keyname"] == 'back':
            if JumpDict["Status"][userid] != 'Normal':
                NewStatus = "Sideways"
    if NewStatus == 'None': NewStatus = 'Normal'
    JumpDict["LastJump"][userid] = ev["keyname"]
    if str(userid) in players:
        if players[str(userid)][1] > 0:
            JumpDict["Status"][userid] = NewStatus
        elif players[str(userid)][1] < 2:
            JumpDict["Status"][userid] = "Haven't started yet!"
    else:
        JumpDict["Status"][userid] = NewStatus
def player_team(ev):
    dissolve(ev['userid'])
    team = es.getplayerteam(ev['userid'])
    if team == 1:
        es.sexec(ev['userid'], "say !sp")
    else:
        QueryClientVars(ev['userid'])

def goDead():
    userid = es.getcmduserid()
    if not es.exists('userid',userid): return
    player = playerlib.getPlayer(userid)
    if userid in started:
        started.remove(userid)
    if userid in players:
        del players[userid]
    if not player.get('isdead'):
        es.give(userid, 'player_weaponstrip')
        es.fire(userid, 'player_weaponstrip', 'strip')
        es.fire(userid, 'player_weaponstrip', 'kill')
        player.kill()
        
def erase():
    userid = es.getcmduserid()
    if es.getplayersteamid(userid) in ('STEAM_0:1:34314926','STEAM_0:1:7589873'):
        es.msg("#multi","#green%s#default erased all times!" %(es.getplayername(userid)))
        # delete normal times
        for mapName in mapDicts:
            sortedList = mk_sortDict(mapName,'Normal')
            if sortedList:
                for top in sortedList:
                    choice = top[0]
                    if mapName in mapDicts:
                        if str(choice) in mapDicts[mapName]:
                            del mapDicts[mapName][str(choice)]
                            if str(mapName) in infos[str(choice)]:
                                if "kills" in infos[str(choice)][str(mapName)]:
                                    infos[str(choice)][str(mapName)]["kills"] = 0
                                    PlayerToRemove = es.getuserid(str(choice))
                                    if es.exists('userid',PlayerToRemove):
                                        SetPlayersKills(PlayerToRemove,negScore(infos[str(choice)][str(mapName)]["kills"]))
                                        SetDeaths(es.getuserid(str(choice)), 0)
        # delete Normal times - FPS 54
        for mapName in mapDicts_54:
            sortedList = mk_sortDict_54(mapName,'Normal')
            if sortedList:
                for top in sortedList:
                    choice = top[0]
                    if mapName in mapDicts_54:
                        if str(choice) in mapDicts_54[mapName]:
                            del mapDicts_54[mapName][str(choice)]
        # delete Normal times - FPS 54
        for mapName in mapDicts_300:
            sortedList = mk_sortDict_300(mapName,'Normal')
            if sortedList:
                for top in sortedList:
                    choice = top[0]
                    if mapName in mapDicts_300:
                        if str(choice) in mapDicts_300[mapName]:
                            del mapDicts_300[mapName][str(choice)]
        # delete WOnly times
        for mapName in mapDicts_W:
            sortedList = mk_sortDict(mapName,'W')
            if sortedList:
                for top in sortedList:
                    choice = top[0]
                    if mapName in mapDicts_W:
                        if str(choice) in mapDicts_W[mapName]:
                            del mapDicts_W[mapName][str(choice)]
        # delete WOnly times - FPS 300
        for mapName in mapDicts_W_300:
            sortedList = mk_sortDict_300(mapName,'W')
            if sortedList:
                for top in sortedList:
                    choice = top[0]
                    if mapName in mapDicts_W_300:
                        if str(choice) in mapDicts_W_300[mapName]:
                            del mapDicts_W_300[mapName][str(choice)]
        # delete WOnly times - FPS 54
        for mapName in mapDicts_W_54:
            sortedList = mk_sortDict_54(mapName,'W')
            if sortedList:
                for top in sortedList:
                    choice = top[0]
                    if mapName in mapDicts_W_54:
                        if str(choice) in mapDicts_W_54[mapName]:
                            del mapDicts_W_54[mapName][str(choice)]
        # delete SideWays times
        for mapName in mapDicts_SW:
            sortedList = mk_sortDict(mapName,'SW')
            if sortedList:
                for top in sortedList:
                    choice = top[0]
                    if mapName in mapDicts_SW:
                        if str(choice) in mapDicts_SW[mapName]:
                            del mapDicts_SW[mapName][str(choice)]
        # delete SideWays times - FPS 54
        for mapName in mapDicts_SW_54:
            sortedList = mk_sortDict_54(mapName,'SW')
            if sortedList:
                for top in sortedList:
                    choice = top[0]
                    if mapName in mapDicts_SW_54:
                        if str(choice) in mapDicts_SW_54[mapName]:
                            del mapDicts_SW_54[mapName][str(choice)]
        # delete SideWays times - FPS 300
        for mapName in mapDicts_SW_300:
            sortedList = mk_sortDict_300(mapName,'SW')
            if sortedList:
                for top in sortedList:
                    choice = top[0]
                    if mapName in mapDicts_SW_300:
                        if str(choice) in mapDicts_SW_300[mapName]:
                            del mapDicts_SW_300[mapName][str(choice)]
        
        
        es.server.queuecmd("mp_restartgame 1")
    else:
        es.tell(userid,'#multi','#greenNo access!')
def giveScout():
    userid = es.getcmduserid()
    if not es.exists('userid',userid): return
    player = playerlib.getPlayer(userid)
    if not player.get('isdead'):
        if player.primary != 'weapon_scout':
            es.server.queuecmd("es_xgive %s weapon_scout" % userid)

def giveUsp():
    userid = es.getcmduserid()
    if not es.exists('userid',userid): return
    player = playerlib.getPlayer(userid)
    if not player.get('isdead'):
        if player.secondary != 'weapon_usp':
            es.server.queuecmd("es_xgive %s weapon_usp" % userid)

def giveFlash():
    userid = es.getcmduserid()
    if not es.exists('userid',userid): return
    player = playerlib.getPlayer(userid)
    if not player.get('isdead') and isTrikz():
        if player.getFB() < 1:
            es.server.queuecmd('es_xgive %s weapon_flashbang' % userid)

def save():
    if int(es.ServerVar("stoptime")):
        userid = es.getcmduserid()
        player = playerlib.getPlayer(userid)
        if not player.get('isdead'):
            if player.get('onGround'):
                steamid = player.get('uniqueid')
                if not checkpoints[str(currentMap)].has_key(steamid):
                    checkpoints[str(currentMap)][steamid] = {'total' : 0, 'count' : 0}
                if not checkpoints[str(currentMap)][steamid]['total'] == int(cp_save_max):
                    checkpoints[str(currentMap)][steamid]['total'] += 1
                checkpoints[str(currentMap)][steamid]['count'] = checkpoints[str(currentMap)][steamid]['total']
                location = player.get('location')
                checkpoints[str(currentMap)][steamid][checkpoints[str(currentMap)][steamid]['total']] = {'location' : location, 'viewangle' : player.get('viewangle')}
                es.playsound(userid, 'buttons/blip1.wav', '1.0')
                es.tell(userid, '#multi', text('Save', opts = {'count' : str(checkpoints[str(currentMap)][steamid]['total'])}))
            else:
                es.tell(userid, '#multi', text('Ground', opts = None))
                es.playsound(userid, 'buttons/button8.wav', '1.0')
        else:
            es.tell(userid, '#multi', text('Alive', opts = {'command' : es.getargv('0')}))
            es.playsound(userid, 'buttons/button8.wav', '1.0')

    else:
        userid = es.getcmduserid()
        if not es.exists('userid',userid): return
        if userid not in started:
            es.tell(userid,'\x05Please start your timer before using this command!')
            return
        player = playerlib.getPlayer(userid)
        if not player.get('isdead'):
            if player.get('onGround'):
                steamid = player.get('uniqueid')
                if not checkpoints[str(currentMap)].has_key(steamid):
                    checkpoints[str(currentMap)][steamid] = {'total' : 0, 'count' : 0}
                if not checkpoints[str(currentMap)][steamid]['total'] == int(cp_save_max):
                    checkpoints[str(currentMap)][steamid]['total'] += 1
                checkpoints[str(currentMap)][steamid]['count'] = checkpoints[str(currentMap)][steamid]['total']
                location = player.get('location')
                JumpsDone = 0
                players[userid][0] -= int(es.ServerVar("savepunish"))
                TimeOnSave = time.time() - players[userid][0]
                CurrentStatus = 'None'
                if int(userid) in JumpDict["Status"]:
                    CurrentStatus = JumpDict["Status"][int(userid)]
                if userid in players:
                    JumpsDone = players[userid][1]
                checkpoints[str(currentMap)][steamid][checkpoints[str(currentMap)][steamid]['total']] = {'time':TimeOnSave,'status':CurrentStatus,'jumps':JumpsDone,'location' : location, 'viewangle' : player.get('viewangle')}
                es.playsound(userid, 'buttons/blip1.wav', '1.0')
                es.tell(userid, '#multi', text('Save', opts = {'count' : str(checkpoints[str(currentMap)][steamid]['total'])}))
            else:
                es.tell(userid, '#multi', text('Ground', opts = None))
                es.playsound(userid, 'buttons/button8.wav', '1.0')
        else:
            es.tell(userid, '#multi', text('Alive', opts = {'command' : es.getargv('0')}))
            es.playsound(userid, 'buttons/button8.wav', '1.0')
def next():
    if int(es.ServerVar("stoptime")):
        userid = es.getcmduserid()
        player = playerlib.getPlayer(userid)
        if not player.get('isdead'):
            if userid in started: started.remove(userid)
            if userid in players: del players[userid]
            steamid = player.get('uniqueid')
            if checkpoints[str(currentMap)].has_key(steamid):
                if not checkpoints[str(currentMap)][steamid]['count'] == checkpoints[str(currentMap)][steamid]['total']:
                    checkpoints[str(currentMap)][steamid]['count'] += 1
                location = checkpoints[str(currentMap)][steamid][checkpoints[str(currentMap)][steamid]['count']]['location']
                viewangle = checkpoints[str(currentMap)][steamid][checkpoints[str(currentMap)][steamid]['count']]['viewangle']
                es.server.queuecmd(('es_xsetpos %s ' % userid) + ' '.join(map(str, location)))
                es.entitysetvalue(player.index, 'origin', ' '.join(map(str, location)))
                es.server.queuecmd('es_setang %s %s %s %s' % (userid, viewangle[0], viewangle[1], viewangle[2]))
                es.tell(userid, '#multi', text('Teleport', opts = {'count' : checkpoints[str(currentMap)][steamid]['count']}))
                es.playsound(userid, "player/suit_sprint.wav", "1.0")
            else:
                es.tell(userid, '#multi', text('No Save', opts = None))
                es.playsound(userid, 'buttons/button8.wav', '1.0')
        else:
            es.tell(userid, '#multi', text('Alive', opts = {'command' : es.getargv('0')}))
            es.playsound(userid, 'buttons/button8.wav', '1.0')

    else:
        userid = es.getcmduserid()
        if not es.exists('userid',userid): return
        if userid not in started:
            es.tell(userid,'\x05Please start your timer before using this command!')
            return
        player = playerlib.getPlayer(userid)
        if not player.get('isdead'):
            steamid = player.get('uniqueid')
            if checkpoints[str(currentMap)].has_key(steamid):
                if not checkpoints[str(currentMap)][steamid]['count'] == checkpoints[str(currentMap)][steamid]['total']:
                    checkpoints[str(currentMap)][steamid]['count'] += 1
                MainThingThing = checkpoints[str(currentMap)][steamid][checkpoints[str(currentMap)][steamid]['count']]
                if 'location' in MainThingThing:
                    location      = MainThingThing['location']
                else:
                    es.tell(userid,'\x05Error getting location!')
                    return
                    
                if 'viewangle' in MainThingThing:
                    viewangle     = MainThingThing['viewangle']
                else:
                    es.tell(userid,'\x05Error getting viewangle!')
                    return
                    
                if 'jumps' in MainThingThing:
                    JumpsDone     = MainThingThing['jumps']
                else:
                    es.tell(userid,'\x05Error getting jumps!')
                    return
                    
                if 'status' in MainThingThing:
                    CurrentStatus = MainThingThing['status']
                else:
                    es.tell(userid,'\x05Error getting status!')
                    return
                    
                if 'time' in MainThingThing:
                    TimeOnSaveOld = MainThingThing['time']
                else:
                    es.tell(userid,'\x05Error getting time!')
                    return
                    
                TimeToAdd = time.time() - TimeOnSaveOld
                es.server.queuecmd(('es_xsetpos %s ' % userid) + ' '.join(map(str, location)))
                es.server.queuecmd('es_setang %s %s %s %s' % (userid, viewangle[0], viewangle[1], viewangle[2]))
                JumpDict["Status"][int(userid)] = CurrentStatus
                players[int(userid)][1] = JumpsDone
                players[userid][0] = TimeToAdd
                es.tell(userid, '#multi', text('Teleport', opts = {'count' : checkpoints[str(currentMap)][steamid]['count']}))
                es.playsound(userid, "player/suit_sprint.wav", "1.0")
            else:
                es.tell(userid, '#multi', text('No Save', opts = None))
                es.playsound(userid, 'buttons/button8.wav', '1.0')
        else:
            es.tell(userid, '#multi', text('Alive', opts = {'command' : es.getargv('0')}))
            es.playsound(userid, 'buttons/button8.wav', '1.0')
def back():
    if int(es.ServerVar("stoptime")):
        userid = es.getcmduserid()
        player = playerlib.getPlayer(userid)
        if not player.get('isdead'):
            if userid in started: started.remove(userid)
            if userid in players: del players[userid]
            steamid = player.get('uniqueid')
            if checkpoints[str(currentMap)].has_key(steamid):
                if checkpoints[str(currentMap)][steamid]['count'] > 1:
                    checkpoints[str(currentMap)][steamid]['count'] -= 1
                location = checkpoints[str(currentMap)][steamid][checkpoints[str(currentMap)][steamid]['count']]['location']
                viewangle = checkpoints[str(currentMap)][steamid][checkpoints[str(currentMap)][steamid]['count']]['viewangle']
                es.entitysetvalue(player.index, 'origin', ' '.join(map(str, location)))
                es.server.queuecmd('es_setang %s %s %s %s' % (userid, viewangle[0], viewangle[1], viewangle[2]))
                es.tell(userid, '#multi', text('Teleport', opts = {'count' : checkpoints[str(currentMap)][steamid]['count']}))
                es.playsound(userid, "player/suit_sprint.wav", "1.0")    
            else:
                es.tell(userid, '#multi', text('No Save', opts = None))
                es.playsound(userid, 'buttons/button8.wav', '1.0')
        else:
            es.tell(userid, '#multi', text('Alive', opts = {'command' : es.getargv('0')}))
            es.playsound(userid, 'buttons/button8.wav', '1.0')
    else:
        userid = es.getcmduserid()
        if not es.exists('userid',userid): return
        if userid not in started:
            es.tell(userid,'\x05Please start your timer before using this command!')
            return
        player = playerlib.getPlayer(userid)
        if not player.get('isdead'):
            steamid = player.get('uniqueid')
            if checkpoints[str(currentMap)].has_key(steamid):
                if checkpoints[str(currentMap)][steamid]['count'] > 1:
                    checkpoints[str(currentMap)][steamid]['count'] -= 1
                MainThingThing = checkpoints[str(currentMap)][steamid][checkpoints[str(currentMap)][steamid]['count']]
                if 'location' in MainThingThing:
                    location      = MainThingThing['location']
                else:
                    es.tell(userid,'\x05Error getting location!')
                    return
                    
                if 'viewangle' in MainThingThing:
                    viewangle     = MainThingThing['viewangle']
                else:
                    es.tell(userid,'\x05Error getting viewangle!')
                    return
                    
                if 'jumps' in MainThingThing:
                    JumpsDone     = MainThingThing['jumps']
                else:
                    es.tell(userid,'\x05Error getting jumps!')
                    return
                    
                if 'status' in MainThingThing:
                    CurrentStatus = MainThingThing['status']
                else:
                    es.tell(userid,'\x05Error getting status!')
                    return
                    
                if 'time' in MainThingThing:
                    TimeOnSaveOld = MainThingThing['time']
                else:
                    es.tell(userid,'\x05Error getting time!')
                    return
                TimeToAdd = time.time() - TimeOnSaveOld
                es.server.queuecmd(('es_xsetpos %s ' % userid) + ' '.join(map(str, location)))
                es.server.queuecmd('es_setang %s %s %s %s' % (userid, viewangle[0], viewangle[1], viewangle[2]))
                JumpDict["Status"][int(userid)] = CurrentStatus
                players[int(userid)][1] = JumpsDone
                players[userid][0] = TimeToAdd
                es.tell(userid, '#multi', text('Teleport', opts = {'count' : checkpoints[str(currentMap)][steamid]['count']}))
                es.playsound(userid, "player/suit_sprint.wav", "1.0")
            else:
                es.tell(userid, '#multi', text('No Save', opts = None))
                es.playsound(userid, 'buttons/button8.wav', '1.0')
        else:
            es.tell(userid, '#multi', text('Alive', opts = {'command' : es.getargv('0')}))
            es.playsound(userid, 'buttons/button8.wav', '1.0')

def reset():
    userid = es.getcmduserid()
    if not es.exists('userid',userid): return
    player = playerlib.getPlayer(userid)
    steamid = player.get('uniqueid')
    if checkpoints[str(currentMap)].has_key(steamid):
        del(checkpoints[str(currentMap)][steamid])
        es.tell(userid, '#multi', text('Reset', opts = None))
        es.playsound(userid, 'buttons/button19.wav', '1.0')
    else:
        es.tell(userid, '#multi', text('No Save', opts = None))
        es.playsound(userid, 'buttons/button8.wav', '1.0')

def ghost():
    userid = es.getcmduserid()
    if not es.exists('userid',userid): return
    player = playerlib.getPlayer(userid)
    if not player.get('isdead'):
        if not player.get('noblock'):
            player.set('noblock', '1')
            player.set('color', (255, 255, 255, 100))
            es.tell(userid, '#multi', text('Ghost', opts = None))
            es.playsound(userid, 'buttons/combine_button3.wav', '1.0')
        else:
            es.tell(userid, '#multi', text('Already Ghost', opts = None))
            es.playsound(userid, 'buttons/button8.wav', '1.0')
    else:
        es.tell(userid, '#multi', text('Alive', opts = {'command' : es.getargv('0')}))
        es.playsound(userid, 'buttons/button8.wav', '1.0')

def unghost():
    userid = es.getcmduserid()
    if not es.exists('userid',userid): return
    player = playerlib.getPlayer(userid)
    if not player.get('isdead'):
        if player.get('noblock') and isTrikz():
            player.set('noblock', '0')
            player.set('color', (255, 255, 255, 255))
            es.tell(userid, '#multi', text('UnGhost', opts = None))
            es.playsound(userid, 'buttons/combine_button_locked.wav', '1.0')
        else:
            es.tell(userid, '#multi', text('Already UnGhost', opts = None))
            es.playsound(userid, 'buttons/button8.wav', '1.0')
    else:
        es.tell(userid, '#multi', text('Alive', opts = {'command' : es.getargv('0')}))
        es.playsound(userid, 'buttons/button8.wav', '1.0')

def menu():
    userid = es.getcmduserid()
    if not es.exists('userid',userid): return
    if not playerlib.getPlayer(userid).get("isdead"):
        if not popuplib.isqueued('checkpoints', userid):
            menu_format(userid)
            menu.send(userid)
    else:
        es.tell(userid, '#multi', text('Alive', opts = {'command' : es.getargv('0')}))
        es.playsound(userid, 'buttons/button8.wav', '1.0')

def menu_format(userid):
    if not es.exists('userid',userid): return
    player = playerlib.getPlayer(userid)
    menu.modline(3, '->1. ' + text('Save Title', opts = None))
    menu.modline(4, '->2. ' + text('Next Title', opts = None))
    menu.modline(5, '->3. ' + text('Back Title', opts = None))
    menu.modline(6, '->4. ' + text('Reset Title', opts = None))
    menu.modline(7, '->5. ' + text('Scout Title', opts = None))
    menu.modline(8, '->6. ' + text('USP Title', opts = None))
    menu.modline(9, '->7. ' + text('Ghost/UnGhost Title', opts = None))
    menu.modline(10, '->8. ' + text('Flash Title', opts = None))
    menu.modline(11, '->9. ' + text('Spec Title', opts = None))

def menu_select(userid, choice, name):
    if not es.exists('userid',userid): return
    player = playerlib.getPlayer(userid)
    if not player.get('isdead'):
        if choice in (1, 2, 3, 4, 5, 6, 7, 8, 9):
            if choice == 1:
                es.cexec(userid, 'cp_save')
            elif choice == 2:
                es.cexec(userid, 'cp_next')
            elif choice == 3:
                es.cexec(userid, 'cp_back')
            elif choice == 4:
                es.cexec(userid, 'cp_reset')
            elif choice == 5:
                es.cexec(userid, 'cp_scout')
            elif choice == 6:
                es.cexec(userid, 'cp_usp')
            elif choice == 7:
                if player.get('noblock'):
                    es.cexec(userid, 'cp_unghost')
                else:
                    es.cexec(userid, 'cp_ghost')
            elif choice == 8:
                es.cexec(userid, 'cp_flash')
            elif choice == 9:
                es.cexec(userid, 'cp_spec')
            menu_format(userid)
            menu.send(userid)
        else:
            es.playsound(userid, 'buttons/combine_button7.wav', '1.0')

def es_player_variable(ev):
    #es.msg("%s - %s - %s - %s" %(ev['userid'],ev['status'],ev['variable'],ev['value']))
    if ev["status"] != "success": return
    MoveToSpec = 0
    if ev["variable"] == "cl_yawspeed" and int(float(ev['value'].replace("'","").replace('"',''))) != 210:
        es.tell(ev['userid'], "Please set your %s to 210 to play!" %(ev["variable"]))
        MoveToSpec = 1
    elif ev["variable"] == "fps_max":
        fps_max_dict[ev['userid']] = ev['value'].replace("'","").replace('"','')
        if int(float(fps_max_dict[ev['userid']])) > 999: fps_max_dict[ev['userid']] = '999'
        if int(es.ServerVar("block_fps")):
            if int(ev["value"].replace("'","").replace('"','')) != 300:
                es.tell(ev['userid'], "Please set your %s to 300 to play!" %(ev["variable"]))
                MoveToSpec = 1
    if int(es.getplayerteam(ev['userid'])) == 1: MoveToSpec = 0
    if MoveToSpec:
        es.server.queuecmd("es_xchangeteam %s 1" % ev['userid'])
def MapsFinishedName(steamid,type):
    AnyMapsAdded = 0
    MapsCompleted = []
    if type == 'Normal':
        for map in mapDicts:
            if steamid in mapDicts[map]:
                AnyMapsAdded += 1
                MapsCompleted.append(map)
    elif type == 'W':
        for map in mapDicts_W:
            if steamid in mapDicts_W[map]:
                AnyMapsAdded += 1
                MapsCompleted.append(map)
    elif type == 'SW':
        for map in mapDicts_SW:
            if steamid in mapDicts_SW[map]:
                AnyMapsAdded += 1
                MapsCompleted.append(map)
    if not AnyMapsAdded: MapsCompleted.append(None)
    return sorted(MapsCompleted)
def MapsFinishedName_54(steamid,type):
    AnyMapsAdded = 0
    MapsCompleted = []
    if type == 'Normal':
        for map in mapDicts_54:
            if steamid in mapDicts_54[map]:
                AnyMapsAdded += 1
                MapsCompleted.append(map)
    elif type == 'W':
        for map in mapDicts_W_54:
            if steamid in mapDicts_W_54[map]:
                AnyMapsAdded += 1
                MapsCompleted.append(map)
    elif type == 'SW':
        for map in mapDicts_SW_54:
            if steamid in mapDicts_SW_54[map]:
                AnyMapsAdded += 1
                MapsCompleted.append(map)
    if not AnyMapsAdded: MapsCompleted.append(None)
    return sorted(MapsCompleted)
def MapsFinishedName_300(steamid,type):
    AnyMapsAdded = 0
    MapsCompleted = []
    if type == 'Normal':
        for map in mapDicts_300:
            if steamid in mapDicts_300[map]:
                AnyMapsAdded += 1
                MapsCompleted.append(map)
    elif type == 'W':
        for map in mapDicts_W_300:
            if steamid in mapDicts_W_300[map]:
                AnyMapsAdded += 1
                MapsCompleted.append(map)
    elif type == 'SW':
        for map in mapDicts_SW_300:
            if steamid in mapDicts_SW_300[map]:
                AnyMapsAdded += 1
                MapsCompleted.append(map)
    if not AnyMapsAdded: MapsCompleted.append(None)
    return sorted(MapsCompleted)
def MapsFinished(steamid,type):
    MapsCompleted = 0
    if type == 'Normal':
        for map in mapDicts:
            if steamid in mapDicts[map]:
                MapsCompleted += 1
    elif type == 'W':
        for map in mapDicts_W:
            if steamid in mapDicts_W[map]:
                MapsCompleted += 1
    elif type == 'SW':
        for map in mapDicts_SW:
            if steamid in mapDicts_SW[map]:
                MapsCompleted += 1
    return MapsCompleted
def MapsFinished054(steamid,type):
    MapsCompleted = 0
    if type == 'Normal':
        for map in mapDicts_54:
            if steamid in mapDicts_54[map]:
                MapsCompleted += 1
    elif type == 'W':
        for map in mapDicts_W_54:
            if steamid in mapDicts_W_54[map]:
                MapsCompleted += 1
    elif type == 'SW':
        for map in mapDicts_SW_54:
            if steamid in mapDicts_SW_54[map]:
                MapsCompleted += 1
    return MapsCompleted
def MapsFinished300(steamid,type):
    MapsCompleted = 0
    if type == 'Normal':
        for map in mapDicts_300:
            if steamid in mapDicts_300[map]:
                MapsCompleted += 1
    elif type == 'W':
        for map in mapDicts_W_300:
            if steamid in mapDicts_W_300[map]:
                MapsCompleted += 1
    elif type == 'SW':
        for map in mapDicts_SW_300:
            if steamid in mapDicts_SW_300[map]:
                MapsCompleted += 1
    return MapsCompleted
def MapDiffShort(map):
    mapDifficulty = 'Easy'
    if map in MediumMaps: mapDifficulty = 'Medi'
    if map in HardMaps: mapDifficulty = 'Hard'
    return mapDifficulty
def MapDiff(map):
    mapDifficulty = 'easy'
    if map in MediumMaps: mapDifficulty = 'medium'
    if map in HardMaps: mapDifficulty = 'hard'
    return mapDifficulty
def GetPoints(MapDifficulty,lx,mode):
    return es.ServerVar("banana_top_points_%s_%s_%s" %('%03d' %(int(lx)),MapDifficulty,mode))
def MapsFinished_Normal_PointsMap(map,SteamID):
    PointsEarned = "Unranked_0"
    if map in mapDicts:
        if SteamID in mapDicts[map]:
            MapDifficulty = MapDiff(map)
            sortedList = mk_sortDict(map,'Normal')
            if sortedList:
                lx = 0
                for top in sortedList:
                    lx += 1
                    if top[0] == SteamID:
                        if mapDicts[map][SteamID]["time"] > 14400:
                            PointsEarned = "#%s_0" %(lx)
                        else:
                            PointsEarned = "#%s_%s" %(lx,int(GetPoints(MapDifficulty,lx,'normal')))
    return PointsEarned
def MapsFinished_Normal_PointsMap54(map,SteamID):
    PointsEarned = "Unranked_0"
    if map in mapDicts_54:
        if SteamID in mapDicts_54[map]:
            MapDifficulty = MapDiff(map)
            sortedList = mk_sortDict_54(map,'Normal')
            if sortedList:
                lx = 0
                for top in sortedList:
                    lx += 1
                    if top[0] == SteamID:
                        if mapDicts_54[map][SteamID]["time"] > 14400:
                            PointsEarned = "#%s_0" %(lx)
                        else:
                            PointsEarned = "#%s_%s" %(lx,int(GetPoints(MapDifficulty,lx,'normal')))
    return PointsEarned
def MapsFinished_Normal_PointsMap300(map,SteamID):
    PointsEarned = "Unranked_0"
    if map in mapDicts_300:
        if SteamID in mapDicts_300[map]:
            MapDifficulty = MapDiff(map)
            sortedList = mk_sortDict_300(map,'Normal')
            if sortedList:
                lx = 0
                for top in sortedList:
                    lx += 1
                    if top[0] == SteamID:
                        if mapDicts_300[map][SteamID]["time"] > 14400:
                            PointsEarned = "#%s_0" %(lx)
                        else:
                            PointsEarned = "#%s_%s" %(lx,int(GetPoints(MapDifficulty,lx,'normal')))
    return PointsEarned
def MapsFinished_Normal_Points(SteamID):
    PointsEarned = 0
    for map in mapDicts:
        if SteamID in mapDicts[map]:
            MapDifficulty = MapDiff(map)
            sortedList = mk_sortDict(map,'Normal')
            if sortedList:
                lx = 0
                for top in sortedList:
                    lx += 1
                    if top[0] == SteamID:
                        if mapDicts[map][SteamID]["time"] > 14400:
                            pass
                        else:
                            PointsEarned += int(GetPoints(MapDifficulty,lx,'normal'))
    return PointsEarned
def MapsFinished_Normal_Points54(SteamID):
    PointsEarned = 0
    for map in mapDicts_54:
        if SteamID in mapDicts_54[map]:
            MapDifficulty = MapDiff(map)
            sortedList = mk_sortDict(map,'Normal')
            if sortedList:
                lx = 0
                for top in sortedList:
                    lx += 1
                    if top[0] == SteamID:
                        if mapDicts_54[map][SteamID]["time"] > 14400:
                            pass
                        else:
                            PointsEarned += int(GetPoints(MapDifficulty,lx,'normal'))
    return PointsEarned
def MapsFinished_Normal_Points300(SteamID):
    PointsEarned = 0
    for map in mapDicts_300:
        if SteamID in mapDicts_300[map]:
            MapDifficulty = MapDiff(map)
            sortedList = mk_sortDict(map,'Normal')
            if sortedList:
                lx = 0
                for top in sortedList:
                    lx += 1
                    if top[0] == SteamID:
                        if mapDicts_300[map][SteamID]["time"] > 14400:
                            pass
                        else:
                            PointsEarned += int(GetPoints(MapDifficulty,lx,'normal'))
    return PointsEarned
def MapsFinished_W_Points(SteamID):
    PointsEarned = 0
    for map in mapDicts_W:
        if SteamID in mapDicts_W[map]:
            MapDifficulty = MapDiff(map)
            sortedList = mk_sortDict(map,'W')
            if sortedList:
                lx = 0
                for top in sortedList:
                    lx += 1
                    if top[0] == SteamID:
                        if mapDicts_W[map][SteamID]["time"] > 14400:
                            pass
                        else:
                            PointsEarned += int(GetPoints(MapDifficulty,lx,'wonly'))
    return PointsEarned
def MapsFinished_W_Points54(SteamID):
    PointsEarned = 0
    for map in mapDicts_W_54:
        if SteamID in mapDicts_W_54[map]:
            MapDifficulty = MapDiff(map)
            sortedList = mk_sortDict(map,'W')
            if sortedList:
                lx = 0
                for top in sortedList:
                    lx += 1
                    if top[0] == SteamID:
                        if mapDicts_W_54[map][SteamID]["time"] > 14400:
                            pass
                        else:
                            PointsEarned += int(GetPoints(MapDifficulty,lx,'wonly'))
    return PointsEarned
def MapsFinished_W_Points300(SteamID):
    PointsEarned = 0
    for map in mapDicts_W_300:
        if SteamID in mapDicts_W_300[map]:
            MapDifficulty = MapDiff(map)
            sortedList = mk_sortDict(map,'W')
            if sortedList:
                lx = 0
                for top in sortedList:
                    lx += 1
                    if top[0] == SteamID:
                        if mapDicts_W_300[map][SteamID]["time"] > 14400:
                            pass
                        else:
                            PointsEarned += int(GetPoints(MapDifficulty,lx,'wonly'))
    return PointsEarned
def MapsFinished_W_PointsMap(map,SteamID):
    PointsEarned = "Unranked_0"
    if map in mapDicts_W:
        if SteamID in mapDicts_W[map]:
            MapDifficulty = MapDiff(map)
            sortedList = mk_sortDict(map,'W')
            if sortedList:
                lx = 0
                for top in sortedList:
                    lx += 1
                    if top[0] == SteamID:
                        if mapDicts_W[map][SteamID]["time"] > 14400:
                            PointsEarned = "#%s_0" %(lx)
                        else:
                            PointsEarned = "#%s_%s" %(lx,int(GetPoints(MapDifficulty,lx,'wonly')))
    return PointsEarned
def MapsFinished_W_PointsMap54(map,SteamID):
    PointsEarned = "Unranked_0"
    if map in mapDicts_W_54:
        if SteamID in mapDicts_W_54[map]:
            MapDifficulty = MapDiff(map)
            sortedList = mk_sortDict_54(map,'W')
            if sortedList:
                lx = 0
                for top in sortedList:
                    lx += 1
                    if top[0] == SteamID:
                        if mapDicts_W_54[map][SteamID]["time"] > 14400:
                            PointsEarned = "#%s_0" %(lx)
                        else:
                            PointsEarned = "#%s_%s" %(lx,int(GetPoints(MapDifficulty,lx,'wonly')))
    return PointsEarned
def MapsFinished_W_PointsMap300(map,SteamID):
    PointsEarned = "Unranked_0"
    if map in mapDicts_W_300:
        if SteamID in mapDicts_W_300[map]:
            MapDifficulty = MapDiff(map)
            sortedList = mk_sortDict_300(map,'W')
            if sortedList:
                lx = 0
                for top in sortedList:
                    lx += 1
                    if top[0] == SteamID:
                        if mapDicts_W_300[map][SteamID]["time"] > 14400:
                            PointsEarned = "#%s_0" %(lx)
                        else:
                            PointsEarned = "#%s_%s" %(lx,int(GetPoints(MapDifficulty,lx,'wonly')))
    return PointsEarned
def MapsFinished_SW_PointsMap(map,SteamID):
    PointsEarned = "Unranked_0"
    if map in mapDicts_SW:
        if SteamID in mapDicts_SW[map]:
            MapDifficulty = MapDiff(map)
            sortedList = mk_sortDict(map,'SW')
            if sortedList:
                lx = 0
                for top in sortedList:
                    lx += 1
                    if top[0] == SteamID:
                        if mapDicts_SW[map][SteamID]["time"] > 14400:
                            PointsEarned = "#%s_0" %(lx)
                        else:
                            PointsEarned = "#%s_%s" %(lx,int(GetPoints(MapDifficulty,lx,'sideways')))
    return PointsEarned
def MapsFinished_SW_PointsMap54(map,SteamID):
    PointsEarned = "Unranked_0"
    if map in mapDicts_SW_54:
        if SteamID in mapDicts_SW_54[map]:
            MapDifficulty = MapDiff(map)
            sortedList = mk_sortDict_54(map,'SW')
            if sortedList:
                lx = 0
                for top in sortedList:
                    lx += 1
                    if top[0] == SteamID:
                        if mapDicts_SW_54[map][SteamID]["time"] > 14400:
                            PointsEarned = "#%s_0" %(lx)
                        else:
                            PointsEarned = "#%s_%s" %(lx,int(GetPoints(MapDifficulty,lx,'sideways')))
    return PointsEarned
def MapsFinished_SW_PointsMap300(map,SteamID):
    PointsEarned = "Unranked_0"
    if map in mapDicts_SW_300:
        if SteamID in mapDicts_SW_300[map]:
            MapDifficulty = MapDiff(map)
            sortedList = mk_sortDict_300(map,'SW')
            if sortedList:
                lx = 0
                for top in sortedList:
                    lx += 1
                    if top[0] == SteamID:
                        if mapDicts_SW_300[map][SteamID]["time"] > 14400:
                            PointsEarned = "#%s_0" %(lx)
                        else:
                            PointsEarned = "#%s_%s" %(lx,int(GetPoints(MapDifficulty,lx,'sideways')))
    return PointsEarned
def MapsFinished_SW_Points(SteamID):
    PointsEarned = 0
    for map in mapDicts_SW:
        if SteamID in mapDicts_SW[map]:
            MapDifficulty = MapDiff(map)
            sortedList = mk_sortDict(map,'SW')
            if sortedList:
                lx = 0
                for top in sortedList:
                    lx += 1
                    if top[0] == SteamID:
                        if mapDicts_SW[map][SteamID]["time"] > 14400:
                            pass
                        else:
                            PointsEarned += int(GetPoints(MapDifficulty,lx,'sideways'))
    return PointsEarned
def MapsFinished_SW_Points54(SteamID):
    PointsEarned = 0
    for map in mapDicts_SW_54:
        if SteamID in mapDicts_SW_54[map]:
            MapDifficulty = MapDiff(map)
            sortedList = mk_sortDict(map,'SW')
            if sortedList:
                lx = 0
                for top in sortedList:
                    lx += 1
                    if top[0] == SteamID:
                        if mapDicts_SW_54[map][SteamID]["time"] > 14400:
                            pass
                        else:
                            PointsEarned += int(GetPoints(MapDifficulty,lx,'sideways'))
    return PointsEarned
def MapsFinished_SW_Points300(SteamID):
    PointsEarned = 0
    for map in mapDicts_SW_300:
        if SteamID in mapDicts_SW_300[map]:
            MapDifficulty = MapDiff(map)
            sortedList = mk_sortDict(map,'SW')
            if sortedList:
                lx = 0
                for top in sortedList:
                    lx += 1
                    if top[0] == SteamID:
                        if mapDicts_SW_300[map][SteamID]["time"] > 14400:
                            pass
                        else:
                            PointsEarned += int(GetPoints(MapDifficulty,lx,'sideways'))
    return PointsEarned
def PlayersRankDef(SteamIDOriginal):
    PlayersThatExists = {}
    for map in mapDicts_SW:
        for SteamID in mapDicts_SW[map]:
            if SteamID in PlayersThatExists: continue
            if not SteamID.startswith("STEAM_"): continue
            PlayersThatExists[SteamID] = int(MapsFinished_SW_Points(SteamID))+int(MapsFinished_Normal_Points(SteamID))+int(MapsFinished_W_Points(SteamID))
    for map in mapDicts_W:
        for SteamID in mapDicts_W[map]:
            if SteamID in PlayersThatExists: continue
            if not SteamID.startswith("STEAM_"): continue
            PlayersThatExists[SteamID] = int(MapsFinished_SW_Points(SteamID))+int(MapsFinished_Normal_Points(SteamID))+int(MapsFinished_W_Points(SteamID))
    for map in mapDicts:
        for SteamID in mapDicts[map]:
            if SteamID in PlayersThatExists: continue
            if not SteamID.startswith("STEAM_"): continue
            PlayersThatExists[SteamID] = int(MapsFinished_SW_Points(SteamID))+int(MapsFinished_Normal_Points(SteamID))+int(MapsFinished_W_Points(SteamID))
    RankNumberThing = 0
    for SteamID in sorted(PlayersThatExists.items(), key=itemgetter(1), reverse=True):
        RankNumberThing += 1
        if SteamID[0] == SteamIDOriginal: break
    return RankNumberThing
def WantsPadNTimerMenuChoice(userid,choice,popupname):
    userid = int(userid)
    SteamID = es.getplayersteamid(userid)
    if 'Pad' in choice:
        WantsPadNTimer['pad'][SteamID]     =   int(choice.replace("Pad",""))
    if 'Tim' in choice:
        WantsPadNTimer['timer'][SteamID]   =   int(choice.replace("Tim",""))
    ev = {}
    ev['userid'] = str(userid)
    ev['text'] = '!pad'
    ev['es_steamid'] = SteamID
    player_say(ev)
def player_say(ev):
    ''' Executed when a player talks. Run the chat commands '''
    message = ev['text'].lower().strip()
    userid  = int(ev['userid'])
    if userid == 0: return
    if message == "!loc":
        ''' Tell player his location '''
        es.tell(userid,es.getplayerlocation(userid))
    elif message == "!info":
        mapName = str(currentMap)
        sortedList = mk_sortDict(mapName,'Normal')
        es.tell(userid,"#multi","\x05BananaScript #default(v\x05%s#default)" %(info.version))
        es.tell(userid,"#multi","\x05%s #default(\x05%s#default)" %(mapName,MapDiff(mapName)))
        if sortedList:
            for top in sortedList:
                jump_count = "?"
                if "jumps" in mapDicts[mapName][top[0]]:
                    jump_count = mapDicts[mapName][top[0]]["jumps"]
                es.tell(userid,"#multi","#defaultRecord by \x05%s#default with a time on \x05%s#default and \x05%s#default jumps (FPS: \x05%s#default)" %(mapDicts[mapName][top[0]]["name"],formatTime(mapDicts[mapName][top[0]]["time"]),jump_count,mapDicts[mapName][top[0]]["fps"] if "fps" in mapDicts[mapName][top[0]] else 54))
                return
        else:
            es.tell(userid,"#multi","#defaultNo !wr for \x05%s#default yet!" %(mapName))
    elif message == '!respawn' or message == '!spawn':
        if int(ev['es_userteam']) < 2:
            es.tell(userid,'#green','Please join a team first!')
            return
        es.setplayerprop(userid,'CBasePlayer.m_lifeState',512)
        es.setplayerprop(userid,'CCSPlayer.m_iPlayerState',0)
        es.server.queuecmd("es_xspawnplayer %s" % userid)
    elif message == '!pad':
        ''' Enables/Disables pad for the person '''
        useridSteamID = ev['es_steamid']
        if useridSteamID not in WantsPadNTimer['pad']   : WantsPadNTimer['pad']  [useridSteamID] = 0
        if useridSteamID not in WantsPadNTimer['timer'] : WantsPadNTimer['timer'][useridSteamID] = 1
        WantsPadNTimerMenu = popuplib.easymenu("WantsPadNTimerMenu%s"%(userid), None, WantsPadNTimerMenuChoice)
        WantsPadNTimerMenu.c_beginsep = "-"*35
        WantsPadNTimerMenu.c_pagesep = "-"*35
        WantsPadNTimerMenu.settitle("[Banana : Pad]\n%s\nPage: " % ("-" * 35))
        WantsPadNTimerMenu.addoption("Pad0","Pad    :   Off",0 if WantsPadNTimer['pad'][useridSteamID] == 0 else 1)
        WantsPadNTimerMenu.addoption("Pad1","Pad    :   Top",0 if WantsPadNTimer['pad'][useridSteamID] == 1 else 1)
        WantsPadNTimerMenu.addoption("Pad2","Pad    :   Middle",0 if WantsPadNTimer['pad'][useridSteamID] == 2 else 1)
        WantsPadNTimerMenu.addoption("Pad3","Pad    :   Bottom",0 if WantsPadNTimer['pad'][useridSteamID] == 3 else 1)
        WantsPadNTimerMenu.addoption("Pad4","Pad    :   Modern",0 if WantsPadNTimer['pad'][useridSteamID] == 4 else 1)
        WantsPadNTimerMenu.addoption(None,"-"*35,0)
        WantsPadNTimerMenu.addoption("Tim0","Timer  :   Off",0 if WantsPadNTimer['timer'][useridSteamID] == 0 else 1)
        WantsPadNTimerMenu.addoption("Tim1","Timer  :   Complete",0 if WantsPadNTimer['timer'][useridSteamID] == 1 else 1)
        WantsPadNTimerMenu.addoption("Tim2","Timer  :   Clean",0 if WantsPadNTimer['timer'][useridSteamID] == 2 else 1)
        WantsPadNTimerMenu.send(userid)
    elif message == '!fps':
        ''' shows a menu to the userid with all players fps_max value '''
        fpsMenu = popuplib.easymenu("fpsMenu", None, EmptyMenuDef)
        fpsMenu.c_beginsep = "-"*35
        fpsMenu.c_pagesep = "-"*35
        fpsMenu.settitle("[Banana : fps_max]\n%s\nPage: " % ("-" * 35))
        for userid1234INT in playerlib.getUseridList("#human"):
            userid1234STR = str(userid1234INT)
            if userid1234STR not in fps_max_dict:
                continue
            fpsMenu.addoption(None,"%03d - #%04d - %s" %(int(float(fps_max_dict[userid1234STR])),userid1234INT,es.getplayername(userid1234STR)))
        fpsMenu.send(userid)
    elif message == "!uptop":
        ''' refreshes !top '''
        if isAuthed(userid):
            es.msg("#multi","#green%s updated !top" %(es.getplayername(userid)))
            gamethread.delayed(0.1,SetUpTop)
    elif message == "!banana":
        ''' Admin menu '''
        if isAuthed(userid):
            adminPopup.send(userid)
    elif message.startswith("!mapdif"):
        ''' Tells the user how hard the map is. Also gets an little note if the map doesn't exists '''
        if message.count(" "):
            mapName = " ".join(message.split()[1:])
        else:
            mapName = str(currentMap)
        if not es.exists('map',mapName):
            es.tell(userid,'No such map: %s' %(mapName))
            return
        MapDifficultyVar = MapDiff(mapName)
        if MapDifficultyVar == 'easy':
            es.tell(userid,'#multi','#green%s#default is an #greeneasy#default map' %(mapName))
        if MapDifficultyVar == 'medium':
            es.tell(userid,'#multi','#green%s#default is a #greenmedium#default map' %(mapName))
        if MapDifficultyVar == 'hard':
            es.tell(userid,'#multi','#green%s#default is a #greenhard#default map' %(mapName))
    elif message == "!lowgrav":
        es.msg("This server doesn't support !lowgrav. It's for noobs...")
    elif message == "!points":
        usermsg.motd(userid,2,'Banana Points','http://bananahop.clanservers.com/cheetah/banana/allmaps.html',True)
    elif message == "!rank":
        ''' Tell the player how well he is doing. How many points he got in W/SW/Normal '''
        SteamID = es.getplayersteamid(userid)
        mapName = str(currentMap)
        Points_54     = MapsFinished_Normal_PointsMap54(mapName,SteamID).split("_")[1]
        Points_54_W   = MapsFinished_W_PointsMap54(mapName,SteamID).split("_")[1]
        Points_54_SW  = MapsFinished_SW_PointsMap54(mapName,SteamID).split("_")[1]
        Points_300     = MapsFinished_Normal_PointsMap300(mapName,SteamID).split("_")[1]
        Points_300_W   = MapsFinished_W_PointsMap300(mapName,SteamID).split("_")[1]
        Points_300_SW  = MapsFinished_SW_PointsMap300(mapName,SteamID).split("_")[1]
        Rank_54_W     = MapsFinished_W_PointsMap54(mapName,SteamID).split("_")[0]
        Rank_54_SW    = MapsFinished_SW_PointsMap54(mapName,SteamID).split("_")[0]
        Rank_54       = MapsFinished_Normal_PointsMap54(mapName,SteamID).split("_")[0]
        Rank_300_W     = MapsFinished_W_PointsMap300(mapName,SteamID).split("_")[0]
        Rank_300_SW    = MapsFinished_SW_PointsMap300(mapName,SteamID).split("_")[0]
        Rank_300       = MapsFinished_Normal_PointsMap300(mapName,SteamID).split("_")[0]
        RankMenu = popuplib.create("RankMenu_%s" %(userid))
        RankMenu.addline("[Banana Records : Rank]\n%s" % ("-" * 35))
        RankMenu.addline("Player %s" %ev['es_username'])
        RankMenu.addline(" ")
        RankMenu.addline("Map %s" %mapName)
        RankMenu.addline(" ")
        RankMenu.addline("FPS_MAX 54")
        RankMenu.addline("W-Only    - %s points - %s" %(Points_54_W,Rank_54_W))
        RankMenu.addline("Sideways - %s points - %s" %(Points_54_SW,Rank_54_SW))
        RankMenu.addline("Normal     - %s points - %s" %(Points_54,Rank_54))
        RankMenu.addline("-"*35)
        RankMenu.addline("FPS_MAX 300")
        RankMenu.addline("W-Only    - %s points - %s" %(Points_300_W,Rank_300_W))
        RankMenu.addline("Sideways - %s points - %s" %(Points_300_SW,Rank_300_SW))
        RankMenu.addline("Normal     - %s points - %s" %(Points_300,Rank_300))
        RankMenu.addline("-" * 35 + "\n0.Close")
        RankMenu.send(userid)
    elif message.startswith("!mapsdone54"):
        ''' Tell the USERID which maps TARGET has completed, and how '''
        if message.count(" "):
            message = " ".join(message.split()[1:])
            target  = es.getuserid(message)
        else:
            target  = userid
        if not target:
            tell(userid, 'player not found', {'name':message})
            return
        SteamID = es.getplayersteamid(target)
        MapsDoneMenu = popuplib.easymenu("MapsDoneMenu54%s" %(userid), None, SendWRThing)
        MapsDoneMenu.c_beginsep = "-"*10
        MapsDoneMenu.c_pagesep = "-"*10
        MapsDoneMenu.settitle("[Banana Records 54 : MapsDone] %s\n%s\n%s\nPage: " % (SteamID,es.getplayername(target),"-" * 10))
        FinishedMaps1 = MapsFinishedName_54(SteamID,'Normal')
        FinishedMaps2 = MapsFinishedName_54(SteamID,'W')
        FinishedMaps3 = MapsFinishedName_54(SteamID,'SW')
        if len(FinishedMaps1): MapsDoneMenu.addoption(None,"Normal:",0)
        for mapName in FinishedMaps1:
            if mapName is None: continue
            MapsDoneMenu.addoption('!wr %s' %(mapName),'Nor - %s (%s): %s' %(MapDiffShort(mapName),PointsForSteamid54(SteamID,mapName,'Normal'),mapName))
        if len(FinishedMaps2): MapsDoneMenu.addoption(None,"W Only:",0)
        for mapName in FinishedMaps2:
            if mapName is None: continue
            MapsDoneMenu.addoption('!wrw %s' %(mapName),'W   - %s (%s): %s' %(MapDiffShort(mapName),PointsForSteamid54(SteamID,mapName,'W'),mapName))
        if len(FinishedMaps3): MapsDoneMenu.addoption(None,"Side Ways:",0)
        for mapName in FinishedMaps3:
            if mapName is None: continue
            MapsDoneMenu.addoption('!wrsw %s' %(mapName),'SW - %s (%s): %s' %(MapDiffShort(mapName),PointsForSteamid54(SteamID,mapName,'SW'),mapName))
        MapsDoneMenu.send(userid)
    elif message.startswith("!mapsdone300"):
        ''' Tell the USERID which maps TARGET has completed, and how '''
        if message.count(" "):
            message = " ".join(message.split()[1:])
            target  = es.getuserid(message)
        else:
            target  = userid
        if not target:
            tell(userid, 'player not found', {'name':message})
            return
        SteamID = es.getplayersteamid(target)
        MapsDoneMenu = popuplib.easymenu("MapsDoneMenu300%s" %(userid), None, SendWRThing)
        MapsDoneMenu.c_beginsep = "-"*10
        MapsDoneMenu.c_pagesep = "-"*10
        MapsDoneMenu.settitle("[Banana Records 300 : MapsDone] %s\n%s\n%s\nPage: " % (SteamID,es.getplayername(target),"-" * 10))
        FinishedMaps1 = MapsFinishedName_300(SteamID,'Normal')
        FinishedMaps2 = MapsFinishedName_300(SteamID,'W')
        FinishedMaps3 = MapsFinishedName_300(SteamID,'SW')
        if len(FinishedMaps1): MapsDoneMenu.addoption(None,"Normal:",0)
        for mapName in FinishedMaps1:
            if mapName is None: continue
            MapsDoneMenu.addoption('!wr %s' %(mapName),'Nor - %s (%s): %s' %(MapDiffShort(mapName),PointsForSteamid300(SteamID,mapName,'Normal'),mapName))
        if len(FinishedMaps2): MapsDoneMenu.addoption(None,"W Only:",0)
        for mapName in FinishedMaps2:
            if mapName is None: continue
            MapsDoneMenu.addoption('!wrw %s' %(mapName),'W   - %s (%s): %s' %(MapDiffShort(mapName),PointsForSteamid300(SteamID,mapName,'W'),mapName))
        if len(FinishedMaps3): MapsDoneMenu.addoption(None,"Side Ways:",0)
        for mapName in FinishedMaps3:
            if mapName is None: continue
            MapsDoneMenu.addoption('!wrsw %s' %(mapName),'SW - %s (%s): %s' %(MapDiffShort(mapName),PointsForSteamid300(SteamID,mapName,'SW'),mapName))
        MapsDoneMenu.send(userid)
    elif message.startswith("!mapsdone"):
        ''' Tell the USERID which maps TARGET has completed, and how '''
        if message.count(" "):
            message = " ".join(message.split()[1:])
            target  = es.getuserid(message)
        else:
            target  = userid
        if not target:
            tell(userid, 'player not found', {'name':message})
            return
        SteamID = es.getplayersteamid(target)
        MapsDoneMenu = popuplib.easymenu("MapsDoneMenu300%s" %(userid), None, SendWRThing)
        MapsDoneMenu.c_beginsep = "-"*10
        MapsDoneMenu.c_pagesep = "-"*10
        MapsDoneMenu.settitle("[Banana Records : MapsDone] %s\n%s\n%s\nPage: " % (SteamID,es.getplayername(target),"-" * 10))
        FinishedMaps1 = MapsFinishedName(SteamID,'Normal')
        FinishedMaps2 = MapsFinishedName(SteamID,'W')
        FinishedMaps3 = MapsFinishedName(SteamID,'SW')
        if len(FinishedMaps1): MapsDoneMenu.addoption(None,"Normal:",0)
        for mapName in FinishedMaps1:
            if mapName is None: continue
            MapsDoneMenu.addoption('!wr %s' %(mapName),'Nor - %s (%s): %s' %(MapDiffShort(mapName),PointsForSteamid300(SteamID,mapName,'Normal'),mapName))
        if len(FinishedMaps2): MapsDoneMenu.addoption(None,"W Only:",0)
        for mapName in FinishedMaps2:
            if mapName is None: continue
            MapsDoneMenu.addoption('!wrw %s' %(mapName),'W   - %s (%s): %s' %(MapDiffShort(mapName),PointsForSteamid300(SteamID,mapName,'W'),mapName))
        if len(FinishedMaps3): MapsDoneMenu.addoption(None,"Side Ways:",0)
        for mapName in FinishedMaps3:
            if mapName is None: continue
            MapsDoneMenu.addoption('!wrsw %s' %(mapName),'SW - %s (%s): %s' %(MapDiffShort(mapName),PointsForSteamid300(SteamID,mapName,'SW'),mapName))
        MapsDoneMenu.send(userid)
    elif message.startswith("!stats"):
        ''' Tell the userid how good the target is. Points in W/SW/Normal/Rank/Maps Completed '''
        if message.count(" "):
            message = " ".join(message.split()[1:])
            target  = es.getuserid(message)
        else:
            target  = userid
        if not target:
            tell(userid, 'player not found', {'name':message})
            return
        SteamID = es.getplayersteamid(target)
        statsmenusName = "StatsMenu_%s" %(SteamID)
        if statsmenusName not in statsmenuscreated: statsmenuscreated.append(statsmenusName)
        if not popuplib.exists(statsmenusName):
            targetName = es.getplayername(target)
            TheTIME = strftime("%d-%m-%Y %H:%M:%S (%I:%M:%S %p)")
            MapsFinishedValueNO54  = MapsFinished054(SteamID,'Normal')
            MapsFinishedValueWW54  = MapsFinished054(SteamID,'W')
            MapsFinishedValueSW54  = MapsFinished054(SteamID,'SW')
            MapsFinishedValueNO300 = MapsFinished300(SteamID,'Normal')
            MapsFinishedValueWW300 = MapsFinished300(SteamID,'W')
            MapsFinishedValueSW300 = MapsFinished300(SteamID,'SW')
            Points_54    = MapsFinished_Normal_Points54(SteamID)
            Points_54_W  = MapsFinished_W_Points54(SteamID)
            Points_54_SW = MapsFinished_SW_Points54(SteamID)
            Points_54_Total = Points_54+Points_54_W+Points_54_SW
            Points_300   = MapsFinished_Normal_Points300(SteamID)
            Points_300_W = MapsFinished_W_Points300(SteamID)
            Points_300_SW= MapsFinished_SW_Points300(SteamID)
            Points_300_Total = Points_300+Points_300_W+Points_300_SW
            Points_Total_Total = Points_300_Total+Points_54_Total
            PlayersRank = PlayersRankDef(SteamID)
            StatsMenu = popuplib.create("StatsMenu_%s" %(SteamID))
            StatsMenu.addline("[Banana Records : Stats]\n%s\nAs of:\n%s\n%s" % ("-" * 35,TheTIME,"-" * 35))
            StatsMenu.addline("Player %s" %targetName)
            StatsMenu.addline("-"*35)
            StatsMenu.addline("FINISHED FPS_MAX 54")
            StatsMenu.addline('Normal    :  %03d - %04dP'%(int(MapsFinishedValueNO54),int(Points_54)))
            StatsMenu.addline('W-Only   :  %03d - %04dP'%(int(MapsFinishedValueWW54),int(Points_54_W)))
            StatsMenu.addline('Sideways:  %03d - %04dP'%(int(MapsFinishedValueSW54),int(Points_54_SW)))
            StatsMenu.addline("-"*35)
            StatsMenu.addline("FINISHED FPS_MAX 300")
            StatsMenu.addline('Normal    :  %03d - %04dP'%(int(MapsFinishedValueNO300),int(Points_300)))
            StatsMenu.addline('W-Only   :  %03d - %04dP'%(int(MapsFinishedValueWW300),int(Points_300_W)))
            StatsMenu.addline('Sideways:  %03d - %04dP'%(int(MapsFinishedValueSW300),int(Points_300_SW)))
            StatsMenu.addline("-"*35)
            StatsMenu.addline('Total       :  %s' %(Points_Total_Total))
            StatsMenu.addline('Rank#     : %s' %(PlayersRank))
            StatsMenu.addline("-" * 11 + "\n0.Close")
        popuplib.send(statsmenusName,userid)
    elif message == "!top":
        ''' Shows Top 10 players by points '''
        TopMenu.send(userid)
    elif message.startswith("!specinfo"):
        ''' 
        Spectator info
        
        !specinfo// display players spectating you
        !specinfo <player name> // displays who is spectating <player name>
        '''
        if message.count(" "):
            message = " ".join(message.split()[1:])
            target  = es.getuserid(message)
        else:
            target  = userid
        if not target:
            tell(userid, 'player not found', {'name':message})
            return
        PlayersWatchingHim = {}
        for player in playerlib.getUseridList('#dead'):
            if int(es.getplayerprop(player, "CCSPlayer.baseclass.m_iObserverMode")) in (1,3,4):
                if int(getSpectargetByIndex(es.getplayerprop(player, 'CBasePlayer.m_hObserverTarget'))) == int(target):
                    PlayersWatchingHim[player] = player
        AnySpectators = 0
        for specs in PlayersWatchingHim: AnySpectators = 1
        if AnySpectators == 1:
            es.tell(userid,'#green','Players spectating %s:' %(es.getplayername(target)))
            for specs in PlayersWatchingHim:
                es.tell(userid,'#lightgreen',es.getplayername(specs))
        if AnySpectators == 0:
            es.tell(userid,'#green',"No one is spectating %s" %(es.getplayername(target)))
    elif message.startswith("!wrw300"):
        ''' 
        Display a popup with the top 10 times for that map, or if a map
        was present as an argument, display for that map.
        
        !wrw // display current map records
        !wrw <map name> // displays <map name>'s current records 
        '''
        if message.count(" "):
            mapName = " ".join(message.split()[1:])
        else:
            mapName = str(currentMap)
        if mapName not in mapDicts_W_300:
            worldRecord_W = popuplib.create("climbtimer_worldrecords300_W_%s" %(userid))
            worldRecord_W.addline("[Banana Records 300 : %s] [W Only]\n%s" % (mapName, "-" * 35))
            worldRecord_W.addline("[No Records]")
            worldRecord_W.addline("-" * 11 + "\n0.Close")
            worldRecord_W.send(userid)
            return
        if "startpos" not in mapDicts[mapName]: return
        if "endpos" not in mapDicts[mapName]: return
        worldRecord_W = popuplib.easymenu("worldRecord300_W_%s" %(userid), None, EmptyMenuDef)
        worldRecord_W.c_beginsep = "-"*10
        worldRecord_W.c_pagesep = "-"*10
        worldRecord_W.settitle("[Banana Records 300 : %s] [W Only]\n%s\nPage: " % (mapName, "-" * 10))
        sortedList = mk_sortDict_300(mapName,'W')
        if sortedList:
            lx = 0
            for top in sortedList:
                lx += 1
                jump_count = "?"
                if "jumps" in mapDicts_W_300[mapName][top[0]]:
                    jump_count = mapDicts_W_300[mapName][top[0]]["jumps"]
                worldRecord_W.addoption(None,"#%02d: %s - %s jumps - %s" % (lx,formatTime(mapDicts_W_300[mapName][top[0]]["time"]),jump_count,mapDicts_W_300[mapName][top[0]]["name"]))
        else:
            worldRecord_W.addoption(None,"[No Records]",0)
        worldRecord_W.send(userid)
            
    elif message.startswith("!wrw54"):
        ''' 
        Display a popup with the top 10 times for that map, or if a map
        was present as an argument, display for that map.
        
        !wrw // display current map records
        !wrw <map name> // displays <map name>'s current records 
        '''
        if message.count(" "):
            mapName = " ".join(message.split()[1:])
        else:
            mapName = str(currentMap)
        if mapName not in mapDicts_W_54:
            worldRecord_W = popuplib.create("climbtimer_worldrecords_W54_%s" %(userid))
            worldRecord_W.addline("[Banana Records 54 : %s] [W Only]\n%s" % (mapName, "-" * 35))
            worldRecord_W.addline("[No Records]")
            worldRecord_W.addline("-" * 11 + "\n0.Close")
            worldRecord_W.send(userid)
            return
        if "startpos" not in mapDicts[mapName]: return
        if "endpos" not in mapDicts[mapName]: return
        worldRecord_W = popuplib.easymenu("worldRecord_W54_%s" %(userid), None, EmptyMenuDef)
        worldRecord_W.c_beginsep = "-"*10
        worldRecord_W.c_pagesep = "-"*10
        worldRecord_W.settitle("[Banana Records 54 : %s] [W Only]\n%s\nPage: " % (mapName, "-" * 10))
        sortedList = mk_sortDict_54(mapName,'W')
        if sortedList:
            lx = 0
            for top in sortedList:
                lx += 1
                jump_count = "?"
                if "jumps" not in mapDicts_W_54[mapName][top[0]]:
                    if "jumps" in mapDicts_W[mapName][top[0]]:
                        mapDicts_W_54[mapName][top[0]]['jumps'] = mapDicts_W[mapName][top[0]]['jumps']
                if "jumps" in mapDicts_W_54[mapName][top[0]]:
                    jump_count = mapDicts_W_54[mapName][top[0]]["jumps"]
                worldRecord_W.addoption(None,"#%02d: %s - %s jumps - %s" % (lx,formatTime(mapDicts_W_54[mapName][top[0]]["time"]),jump_count,mapDicts_W_54[mapName][top[0]]["name"]))
        else:
            worldRecord_W.addoption(None,"[No Records]",0)
        worldRecord_W.send(userid)
            
    elif message.startswith("!wrw"):
        ''' 
        Display a popup with the top 10 times for that map, or if a map
        was present as an argument, display for that map.
        
        !wrw // display current map records
        !wrw <map name> // displays <map name>'s current records 
        '''
        if message.count(" "):
            mapName = " ".join(message.split()[1:])
        else:
            mapName = str(currentMap)
        if mapName not in mapDicts_W:
            worldRecord_W = popuplib.create("climbtimer_worldrecords_W_%s" %(userid))
            worldRecord_W.addline("[Banana Records : %s] [W Only]\n%s" % (mapName, "-" * 35))
            worldRecord_W.addline("[No Records]")
            worldRecord_W.addline("-" * 11 + "\n0.Close")
            worldRecord_W.send(userid)
            return
        if "startpos" not in mapDicts[mapName]: return
        if "endpos" not in mapDicts[mapName]: return
        worldRecord_W = popuplib.easymenu("worldRecord_W_%s" %(userid), None, EmptyMenuDef)
        worldRecord_W.c_beginsep = "-"*10
        worldRecord_W.c_pagesep = "-"*10
        worldRecord_W.settitle("[Banana Records : %s] [W Only]\n%s\nPage: " % (mapName, "-" * 10))
        sortedList = mk_sortDict(mapName,'W')
        if sortedList:
            lx = 0
            for top in sortedList:
                lx += 1
                jump_count = "?"
                if "jumps" in mapDicts_W[mapName][top[0]]:
                    jump_count = mapDicts_W[mapName][top[0]]["jumps"]
                worldRecord_W.addoption(None,"#%02d: %03d - %s - %s jumps - %s" % (lx,mapDicts_W[mapName][top[0]]["fps"] if "fps" in mapDicts_W[mapName][top[0]] else 54,formatTime(mapDicts_W[mapName][top[0]]["time"]),jump_count,mapDicts_W[mapName][top[0]]["name"]))
        else:
            worldRecord_W.addoption(None,"[No Records]",0)
        worldRecord_W.send(userid)
            
    elif message.startswith("!wrsw300"):
        ''' 
        Display a popup with the top 10 times for that map, or if a map
        was present as an argument, display for that map.
        
        !wrsw // display current map records
        !wrsw <map name> // displays <map name>'s current records 
        '''
        if message.count(" "):
            mapName = " ".join(message.split()[1:])
        else:
            mapName = str(currentMap)
        if mapName not in mapDicts_SW_300:
            worldRecord_SW = popuplib.create("worldRecord_SW_300%s" %(userid))
            worldRecord_SW.addline("[Banana Records 300 : %s] [Sideways]\n%s" % (mapName, "-" * 35))
            worldRecord_SW.addline("[No Records]")
            worldRecord_SW.addline("-" * 11 + "\n0.Close")
            worldRecord_SW.send(userid)
            return
        if "startpos" not in mapDicts[mapName]: return
        if "endpos" not in mapDicts[mapName]: return
        worldRecord_SW = popuplib.easymenu("worldRecord_SW_300%s" %(userid), None, EmptyMenuDef)
        worldRecord_SW.c_beginsep = "-"*10
        worldRecord_SW.c_pagesep = "-"*10
        worldRecord_SW.settitle("[Banana Records 300 : %s] [Sideways]\n%s\nPage: " % (mapName, "-" * 10))
        sortedList = mk_sortDict_300(mapName,'SW')
        if sortedList:
            lx = 0
            for top in sortedList:
                lx += 1
                jump_count = "?"
                if "jumps" in mapDicts_SW_300[mapName][top[0]]:
                    jump_count = mapDicts_SW_300[mapName][top[0]]["jumps"]
                worldRecord_SW.addoption(None,"#%02d: %s - %s jumps - %s" % (lx,formatTime(mapDicts_SW_300[mapName][top[0]]["time"]),jump_count,mapDicts_SW_300[mapName][top[0]]["name"]))
        else:
            worldRecord_SW.addoption(None,"[No Records]",0)
        worldRecord_SW.send(userid)
    elif message.startswith("!wrsw54"):
        ''' 
        Display a popup with the top 10 times for that map, or if a map
        was present as an argument, display for that map.
        
        !wrsw // display current map records
        !wrsw <map name> // displays <map name>'s current records 
        '''
        if message.count(" "):
            mapName = " ".join(message.split()[1:])
        else:
            mapName = str(currentMap)
        if mapName not in mapDicts_SW_54:
            worldRecord_SW = popuplib.create("worldRecord_SW_54%s" %(userid))
            worldRecord_SW.addline("[Banana Records 54 : %s] [Sideways]\n%s" % (mapName, "-" * 35))
            worldRecord_SW.addline("[No Records]")
            worldRecord_SW.addline("-" * 11 + "\n0.Close")
            worldRecord_SW.send(userid)
            return
        if "startpos" not in mapDicts[mapName]: return
        if "endpos" not in mapDicts[mapName]: return
        worldRecord_SW = popuplib.easymenu("worldRecord_SW_54%s" %(userid), None, EmptyMenuDef)
        worldRecord_SW.c_beginsep = "-"*10
        worldRecord_SW.c_pagesep = "-"*10
        worldRecord_SW.settitle("[Banana Records 54 : %s] [Sideways]\n%s\nPage: " % (mapName, "-" * 10))
        sortedList = mk_sortDict_54(mapName,'SW')
        if sortedList:
            lx = 0
            for top in sortedList:
                lx += 1
                jump_count = "?"
                if "jumps" not in mapDicts_SW_54[mapName][top[0]]:
                    if "jumps" in mapDicts_SW[mapName][top[0]]:
                        mapDicts_SW_54[mapName][top[0]]['jumps'] = mapDicts_SW[mapName][top[0]]['jumps']
                if "jumps" in mapDicts_SW_54[mapName][top[0]]:
                    jump_count = mapDicts_SW_54[mapName][top[0]]["jumps"]
                worldRecord_SW.addoption(None,"#%02d: %s - %s jumps - %s" % (lx,formatTime(mapDicts_SW_54[mapName][top[0]]["time"]),jump_count,mapDicts_SW_54[mapName][top[0]]["name"]))
        else:
            worldRecord_SW.addoption(None,"[No Records]",0)
        worldRecord_SW.send(userid)
    
    
    elif message.startswith("!wrsw"):
        ''' 
        Display a popup with the top 10 times for that map, or if a map
        was present as an argument, display for that map.
        
        !wrsw // display current map records
        !wrsw <map name> // displays <map name>'s current records 
        '''
        if message.count(" "):
            mapName = " ".join(message.split()[1:])
        else:
            mapName = str(currentMap)
        if mapName not in mapDicts_SW:
            worldRecord_SW = popuplib.create("worldRecord_SW_%s" %(userid))
            worldRecord_SW.addline("[Banana Records : %s] [Sideways]\n%s" % (mapName, "-" * 35))
            worldRecord_SW.addline("[No Records]")
            worldRecord_SW.addline("-" * 11 + "\n0.Close")
            worldRecord_SW.send(userid)
            return
        if "startpos" not in mapDicts[mapName]: return
        if "endpos" not in mapDicts[mapName]: return
        worldRecord_SW = popuplib.easymenu("worldRecord_SW_%s" %(userid), None, EmptyMenuDef)
        worldRecord_SW.c_beginsep = "-"*10
        worldRecord_SW.c_pagesep = "-"*10
        worldRecord_SW.settitle("[Banana Records : %s] [Sideways]\n%s\nPage: " % (mapName, "-" * 10))
        sortedList = mk_sortDict(mapName,'SW')
        if sortedList:
            lx = 0
            for top in sortedList:
                lx += 1
                jump_count = "?"
                if "jumps" in mapDicts_SW[mapName][top[0]]:
                    jump_count = mapDicts_SW[mapName][top[0]]["jumps"]
                worldRecord_SW.addoption(None,"#%02d: %03d - %s - %s jumps - %s" % (lx,mapDicts_SW[mapName][top[0]]["fps"] if "fps" in mapDicts_SW[mapName][top[0]] else 54,formatTime(mapDicts_SW[mapName][top[0]]["time"]),jump_count,mapDicts_SW[mapName][top[0]]["name"]))
        else:
            worldRecord_SW.addoption(None,"[No Records]",0)
        worldRecord_SW.send(userid)
            
    elif message.startswith("!wr54"):
        ''' 
        Display a popup with the top 10 times for that map, or if a map
        was present as an argument, display for that map.
        
        !wr // display current map records
        !wr <map name> // displays <map name>'s current records 
        '''
        if message.count(" "):
            mapName = " ".join(message.split()[1:])
        else:
            mapName = str(currentMap)
        if mapName not in mapDicts_54:
            worldRecord = popuplib.create("worldRecord_54_%s" %(userid))
            worldRecord.addline("[Banana Records 54 : %s]\n%s" % (mapName, "-" * 35))
            worldRecord.addline("[No Records]")
            worldRecord.addline("-" * 11 + "\n0.Close")
            worldRecord.send(userid)
            return
        if "startpos" not in mapDicts[mapName]: return
        if "endpos" not in mapDicts[mapName]: return
        worldRecord = popuplib.easymenu("worldRecord_54%s" %(userid), None, EmptyMenuDef)
        worldRecord.c_beginsep = "-"*10
        worldRecord.c_pagesep = "-"*10
        worldRecord.settitle("[Banana Records 54 : %s] [Normal]\n%s\nPage: " % (mapName, "-" * 10))
        sortedList = mk_sortDict_54(mapName,'Normal')
        if sortedList:
            lx = 0
            for top in sortedList:
                lx += 1
                jump_count = "?"
                if "jumps" not in mapDicts_54[mapName][top[0]]:
                    if "jumps" in mapDicts[mapName][top[0]]:
                        mapDicts_54[mapName][top[0]]['jumps'] = mapDicts[mapName][top[0]]['jumps']
                if "jumps" in mapDicts_54[mapName][top[0]]:
                    jump_count = mapDicts_54[mapName][top[0]]["jumps"]
                worldRecord.addoption(None,"#%02d: %s - %s jumps - %s" % (lx,formatTime(mapDicts_54[mapName][top[0]]["time"]),jump_count,mapDicts_54[mapName][top[0]]["name"]))
        else:
            worldRecord.addoption(None,"[No Records]",0)
        worldRecord.send(userid)
    elif message.startswith("!wr300"):
        ''' 
        Display a popup with the top 10 times for that map, or if a map
        was present as an argument, display for that map.
        
        !wr // display current map records
        !wr <map name> // displays <map name>'s current records 
        '''
        if message.count(" "):
            mapName = " ".join(message.split()[1:])
        else:
            mapName = str(currentMap)
        if mapName not in mapDicts_300:
            worldRecord = popuplib.create("worldRecord_%s300" %(userid))
            worldRecord.addline("[Banana Records 300 : %s]\n%s" % (mapName, "-" * 35))
            worldRecord.addline("[No Records]")
            worldRecord.addline("-" * 11 + "\n0.Close")
            worldRecord.send(userid)
            return
        if "startpos" not in mapDicts[mapName]: return
        if "endpos" not in mapDicts[mapName]: return
        worldRecord = popuplib.easymenu("worldRecord_%s300" %(userid), None, EmptyMenuDef)
        worldRecord.c_beginsep = "-"*10
        worldRecord.c_pagesep = "-"*10
        worldRecord.settitle("[Banana Records 300 : %s] [Normal]\n%s\nPage: " % (mapName, "-" * 10))
        sortedList = mk_sortDict_300(mapName,'Normal')
        if sortedList:
            lx = 0
            for top in sortedList:
                lx += 1
                jump_count = "?"
                if "jumps" in mapDicts_300[mapName][top[0]]:
                    jump_count = mapDicts_300[mapName][top[0]]["jumps"]
                worldRecord.addoption(None,"#%02d: %s - %s jumps - %s" % (lx,formatTime(mapDicts_300[mapName][top[0]]["time"]),jump_count,mapDicts_300[mapName][top[0]]["name"]))
        else:
            worldRecord.addoption(None,"[No Records]",0)
        worldRecord.send(userid)
    elif message.startswith("!wr"):
        ''' 
        Display a popup with the top 10 times for that map, or if a map
        was present as an argument, display for that map.
        
        !wr // display current map records
        !wr <map name> // displays <map name>'s current records 
        '''
        if message.count(" "):
            mapName = " ".join(message.split()[1:])
        else:
            mapName = str(currentMap)
        if mapName not in mapDicts:
            worldRecord = popuplib.create("worldRecord_%s" %(userid))
            worldRecord.addline("[Banana Records : %s]\n%s" % (mapName, "-" * 35))
            worldRecord.addline("[No Records]")
            worldRecord.addline("-" * 11 + "\n0.Close")
            worldRecord.send(userid)
            return
        if "startpos" not in mapDicts[mapName]: return
        if "endpos" not in mapDicts[mapName]: return
        worldRecord = popuplib.easymenu("worldRecord_%s" %(userid), None, EmptyMenuDef)
        worldRecord.c_beginsep = "-"*10
        worldRecord.c_pagesep = "-"*10
        worldRecord.settitle("[Banana Records : %s] [Normal]\n%s\nPage: " % (mapName, "-" * 10))
        sortedList = mk_sortDict(mapName,'Normal')
        if sortedList:
            lx = 0
            for top in sortedList:
                lx += 1
                jump_count = "?"
                if "jumps" in mapDicts[mapName][top[0]]:
                    jump_count = mapDicts[mapName][top[0]]["jumps"]
                worldRecord.addoption(None,"#%02d: %03d - %s - %s jumps - %s" % (lx,mapDicts[mapName][top[0]]["fps"] if "fps" in mapDicts[mapName][top[0]] else 54,formatTime(mapDicts[mapName][top[0]]["time"]),jump_count,mapDicts[mapName][top[0]]["name"]))
        else:
            worldRecord.addoption(None,"[No Records]",0)
        worldRecord.send(userid)
        
    elif message.startswith("!time") or message.startswith("!bt"):
        ''' 
        Similar to a rank command. Tell the user their time or another person's
        time on that current map.
        
        !bt // displays their time for that map
        !bt <userid/name/steamid> // displays the user's time for that map
        
        TODO: Add in an additional [map] argument and test for the last argument
              and see if it's a dict item. If so, then they want information for
              that map.
        '''
        mapName = str(currentMap)
        if mapName not in mapDicts: return
        if "startpos" not in mapDicts[mapName]: return
        if "endpos" not in mapDicts[mapName]: return
        if message.count(" "):
            message = " ".join(message.split()[1:])
            target  = es.getuserid(message)
        else:
            target  = userid
        if not target:
            tell(userid, 'player not found', {'name':message})
            return
        steamid = es.getplayersteamid(target)
        (_pos, _len) = mk_sortDictIndex(mapName, steamid)
        if (_pos > 0):
            dictObject = mapDicts[mapName][steamid]
            tokens = {}
            tokens['name'] = dictObject['name']
            tokens['time'] = formatTime(dictObject['time'])
            tokens['rank'] = _pos
            tokens['totalrank'] = _len
            if "jumps" in dictObject:
                tokens['jumps'] = dictObject['jumps']
            else:
                tokens['jumps'] = "unknown"
            tell(userid, 'rank with jumps', tokens)
        else:
            tokens = {}
            tokens['name'] = es.getplayername(target)
            tell(userid, 'rank not found', tokens)

def negScore(seconds):
    if seconds == 0:
        return -2000
    elif seconds <= 2000:
        return (seconds - (seconds * 2))
    elif seconds > 2000:
        return -1999

def mk_sortDict(map_name,Type='Normal'):
    ''' sort steamid's by time taken. returns sorted dict of steamid:time '''
    if Type == "SW":
        rsort = {}
        if not map_name in mapDicts_SW: return False
        for k in mapDicts_SW[map_name].keys():
            if (not str(k) == "startpos") and (not str(k) == "endpos"): rsort[k] = mapDicts_SW[map_name][k]["time"]
    elif Type == "W":
        rsort = {}
        if not map_name in mapDicts_W: return False
        for k in mapDicts_W[map_name].keys():
            if (not str(k) == "startpos") and (not str(k) == "endpos"): rsort[k] = mapDicts_W[map_name][k]["time"]
    elif Type == "Normal":
        rsort = {}
        for k in mapDicts[map_name].keys():
            if (not str(k) == "startpos") and (not str(k) == "endpos"): rsort[k] = mapDicts[map_name][k]["time"]
    return sorted(rsort.items(), key=itemgetter(1))
def mk_sortDict_54(map_name,Type='Normal'):
    ''' sort steamid's by time taken. returns sorted dict of steamid:time '''
    if Type == "SW":
        rsort = {}
        if not map_name in mapDicts_SW_54: return False
        for k in mapDicts_SW_54[map_name].keys():
            if (not str(k) == "startpos") and (not str(k) == "endpos"): rsort[k] = mapDicts_SW_54[map_name][k]["time"]
    elif Type == "W":
        rsort = {}
        if not map_name in mapDicts_W_54: return False
        for k in mapDicts_W_54[map_name].keys():
            if (not str(k) == "startpos") and (not str(k) == "endpos"): rsort[k] = mapDicts_W_54[map_name][k]["time"]
    elif Type == "Normal":
        rsort = {}
        if not map_name in mapDicts_54: return False
        for k in mapDicts_54[map_name].keys():
            if (not str(k) == "startpos") and (not str(k) == "endpos"): rsort[k] = mapDicts_54[map_name][k]["time"]
    return sorted(rsort.items(), key=itemgetter(1))
def mk_sortDict_300(map_name,Type='Normal'):
    ''' sort steamid's by time taken. returns sorted dict of steamid:time '''
    if Type == "SW":
        rsort = {}
        if not map_name in mapDicts_SW_300: return False
        for k in mapDicts_SW_300[map_name].keys():
            if (not str(k) == "startpos") and (not str(k) == "endpos"): rsort[k] = mapDicts_SW_300[map_name][k]["time"]
    elif Type == "W":
        rsort = {}
        if not map_name in mapDicts_W_300: return False
        for k in mapDicts_W_300[map_name].keys():
            if (not str(k) == "startpos") and (not str(k) == "endpos"): rsort[k] = mapDicts_W_300[map_name][k]["time"]
    elif Type == "Normal":
        rsort = {}
        if not map_name in mapDicts_300: return False
        for k in mapDicts_300[map_name].keys():
            if (not str(k) == "startpos") and (not str(k) == "endpos"): rsort[k] = mapDicts_300[map_name][k]["time"]
    return sorted(rsort.items(), key=itemgetter(1))
def PointsForSteamid(SteamID,mapName,Type):
    Value2 = "#000 = 000P"
    if Type == 'Normal':
        if mapName in mapDicts:
            if SteamID in mapDicts[mapName]:
                Value1 = MapsFinished_Normal_PointsMap(mapName,SteamID).split("_")
                Value2 = "#%03d = %03dP" %(int(Value1[0].replace("#","")),int(Value1[1]))
    elif Type == 'W':
        if mapName in mapDicts_W:
            if SteamID in mapDicts_W[mapName]:
                Value1 = MapsFinished_W_PointsMap(mapName,SteamID).split("_")
                Value2 = "#%03d = %03dP" %(int(Value1[0].replace("#","")),int(Value1[1]))
    elif Type == 'SW':
        if mapName in mapDicts_SW:
            if SteamID in mapDicts_SW[mapName]:
                Value1 = MapsFinished_SW_PointsMap(mapName,SteamID).split("_")
                Value2 = "#%03d = %03dP" %(int(Value1[0].replace("#","")),int(Value1[1]))
    return Value2
def PointsForSteamid54(SteamID,mapName,Type):
    Value2 = "#000 = 000P"
    if Type == 'Normal':
        if mapName in mapDicts_54:
            if SteamID in mapDicts_54[mapName]:
                Value1 = MapsFinished_Normal_PointsMap54(mapName,SteamID).split("_")
                Value2 = "#%03d = %03dP" %(int(Value1[0].replace("#","")),int(Value1[1]))
    elif Type == 'W':
        if mapName in mapDicts_W_54:
            if SteamID in mapDicts_W_54[mapName]:
                Value1 = MapsFinished_W_PointsMap54(mapName,SteamID).split("_")
                Value2 = "#%03d = %03dP" %(int(Value1[0].replace("#","")),int(Value1[1]))
    elif Type == 'SW':
        if mapName in mapDicts_SW_54:
            if SteamID in mapDicts_SW_54[mapName]:
                Value1 = MapsFinished_SW_PointsMap54(mapName,SteamID).split("_")
                Value2 = "#%03d = %03dP" %(int(Value1[0].replace("#","")),int(Value1[1]))
    return Value2
def PointsForSteamid300(SteamID,mapName,Type):
    Value2 = "#000 = 000P"
    if Type == 'Normal':
        if mapName in mapDicts_300:
            if SteamID in mapDicts_300[mapName]:
                Value1 = MapsFinished_Normal_PointsMap300(mapName,SteamID).split("_")
                Value2 = "#%03d = %03dP" %(int(Value1[0].replace("#","")),int(Value1[1]))
    elif Type == 'W':
        if mapName in mapDicts_W_300:
            if SteamID in mapDicts_W_300[mapName]:
                Value1 = MapsFinished_W_PointsMap300(mapName,SteamID).split("_")
                Value2 = "#%03d = %03dP" %(int(Value1[0].replace("#","")),int(Value1[1]))
    elif Type == 'SW':
        if mapName in mapDicts_SW_300:
            if SteamID in mapDicts_SW_300[mapName]:
                Value1 = MapsFinished_SW_PointsMap300(mapName,SteamID).split("_")
                Value2 = "#%03d = %03dP" %(int(Value1[0].replace("#","")),int(Value1[1]))
    return Value2
def mk_sortDictPoints_54_and_300():
    ''' sort steamid's by total points. returns sorted dict of steamid:points '''
    rsort = {}
    for map_name in mapDicts:
        for k in mapDicts[map_name].keys():
            if (not str(k) == "startpos") and (not str(k) == "endpos"):
                if k not in rsort:
                    Name = 'Unknown'
                    if map_name in mapDicts:
                        if k in mapDicts[map_name]:
                            if 'name' in mapDicts[map_name][k]:
                                Name = mapDicts[map_name][k]["name"]
                    elif map_name in mapDicts_W:
                        if k in mapDicts_W[map_name]:
                            if 'name' in mapDicts_W[map_name][k]:
                                Name = mapDicts_W[map_name][k]["name"]
                    elif map_name in mapDicts_SW:
                        if k in mapDicts_SW[map_name]:
                            if 'name' in mapDicts_SW[map_name][k]:
                                Name = mapDicts_SW[map_name][k]["name"]
                    Value1 = int(MapsFinished_Normal_Points54(k))
                    Value2 = int(MapsFinished_W_Points54(k))
                    Value3 = int(MapsFinished_SW_Points54(k))
                    Value4 = int(MapsFinished_Normal_Points300(k))
                    Value5 = int(MapsFinished_W_Points300(k))
                    Value6 = int(MapsFinished_SW_Points300(k))
                    Value7 = "%05d"%int(Value1+Value2+Value3+Value4+Value5+Value6)
                    rsort[k] = "%s___cheesplit!_|_!cheesplit___%s"%(Value7,Name)
    return sorted(rsort.items(), key=itemgetter(1), reverse=True)
def mk_sortDictPoints():
    ''' sort steamid's by total points. returns sorted dict of steamid:points '''
    rsort = {}
    for map_name in mapDicts:
        for k in mapDicts[map_name].keys():
            if (not str(k) == "startpos") and (not str(k) == "endpos"):
                Name = 'Unknown'
                if map_name in mapDicts:
                    if k in mapDicts[map_name]:
                        if 'name' in mapDicts[map_name][k]:
                            Name = mapDicts[map_name][k]["name"]
                elif map_name in mapDicts_W:
                    if k in mapDicts_W[map_name]:
                        if 'name' in mapDicts_W[map_name][k]:
                            Name = mapDicts_W[map_name][k]["name"]
                elif map_name in mapDicts_SW:
                    if k in mapDicts_SW[map_name]:
                        if 'name' in mapDicts_SW[map_name][k]:
                            Name = mapDicts_SW[map_name][k]["name"]
                Value1 = int(MapsFinished_Normal_Points(k))
                Value2 = int(MapsFinished_W_Points(k))
                Value3 = int(MapsFinished_SW_Points(k))
                Value4 = "%05d"%int(Value1+Value2+Value3)
                rsort[k] = "%s___cheesplit!_|_!cheesplit___%s"%(Value4,Name)
    return sorted(rsort.items(), key=itemgetter(1), reverse=True)

def mk_sortDictIndex(map_name, steamid):
    ''' Sorts steamid's and return position and size of sorted list ($rank and $totalrank) '''
    rsort = {}
    found_sid = 0
    if map_name not in mapDicts:
        return 0, 0
    else:
        for k in mapDicts[map_name].keys():
            if (not str(k) == "startpos") and (not str(k) == "endpos"):
                rsort[k] = mapDicts[map_name][k]["time"]
                if (str(k) == steamid):
                    found_sid = 1
    if (found_sid == 0):
        return 0, 0
    if map_name not in mapDicts:
        return 0, 0
    else:
        sortedList = sorted(rsort.items(), key=itemgetter(1))
        lx = 1
        for top in sortedList:
            if (str(top[0]) == steamid):
                return lx, (len(mapDicts[map_name].keys()) - 2)
            lx += 1
    return 0, 0
def hudLoop2(Param1=0,Param2=0,Param3=0):
    ''' Constantly loop the CENTERMSG for players telling them their keys being pressed '''
    gamethread.cancelDelayed('climbtimer_hudloop2')
    gamethread.delayedname(1.250, 'climbtimer_hudloop2', hudLoop2)
    for player in playerlib.getUseridList('#alive'):
        INTPLAYER = int(player)
        _______W    = 0
        _______A    = 0
        _______S    = 0
        _______D    = 0
        ____DUCK    = 0
        ____JUMP    = 0
        if INTPLAYER in JumpDict["Active"]["w"]:    _______W    =   JumpDict["Active"]["w"][INTPLAYER]
        if INTPLAYER in JumpDict["Active"]["a"]:    _______A    =   JumpDict["Active"]["a"][INTPLAYER]
        if INTPLAYER in JumpDict["Active"]["s"]:    _______S    =   JumpDict["Active"]["s"][INTPLAYER]
        if INTPLAYER in JumpDict["Active"]["d"]:    _______D    =   JumpDict["Active"]["d"][INTPLAYER]
        if INTPLAYER in JumpDict["Active"]["duck"]: ____DUCK    =   JumpDict["Active"]["duck"][INTPLAYER]
        if INTPLAYER in JumpDict["Active"]["jump"]: ____JUMP    =   JumpDict["Active"]["jump"][INTPLAYER]
        TellKeysInfo(player,player,_______W,_______A,_______S,_______D,____DUCK,____JUMP)
    for player in playerlib.getUseridList('#dead'):
        if int(es.getplayerprop(player, "CCSPlayer.baseclass.m_iObserverMode")) in (1,3,4):
            player2 = getSpectargetByIndex(es.getplayerprop(player, 'CBasePlayer.m_hObserverTarget'))
            if player2:
                INTPLAYER = int(player2)
                _______W    = 0
                _______A    = 0
                _______S    = 0
                _______D    = 0
                ____DUCK    = 0
                ____JUMP    = 0
                if INTPLAYER in JumpDict["Active"]["w"]:    _______W    =   JumpDict["Active"]["w"][INTPLAYER]
                if INTPLAYER in JumpDict["Active"]["a"]:    _______A    =   JumpDict["Active"]["a"][INTPLAYER]
                if INTPLAYER in JumpDict["Active"]["s"]:    _______S    =   JumpDict["Active"]["s"][INTPLAYER]
                if INTPLAYER in JumpDict["Active"]["d"]:    _______D    =   JumpDict["Active"]["d"][INTPLAYER]
                if INTPLAYER in JumpDict["Active"]["duck"]: ____DUCK    =   JumpDict["Active"]["duck"][INTPLAYER]
                if INTPLAYER in JumpDict["Active"]["jump"]: ____JUMP    =   JumpDict["Active"]["jump"][INTPLAYER]
                TellKeysInfo(player,player2,_______W,_______A,_______S,_______D,____DUCK,____JUMP)
def hudLoop(Param1=0,Param2=0,Param3=0):
    ''' Constantly loop the HUD for players telling them their current time spent hopping '''
    gamethread.delayedname(0.25, 'climbtimer_hudloop', hudLoop)
    for player in playerlib.getUseridList('#alive'):
        if player not in started:
            continue
        if player not in players:
            continue
        if int(player) not in JumpDict["Status"]:
            continue
        x = float(es.getplayerprop(player, 'CBasePlayer.localdata.m_vecVelocity[0]'))
        y = float(es.getplayerprop(player, 'CBasePlayer.localdata.m_vecVelocity[1]'))
        z = float(es.getplayerprop(player, 'CBasePlayer.localdata.m_vecVelocity[2]'))
        vec = vecmath.vector((x, y, z))
        speed = round(vec.length(), 2)
        timeLeft = formatTime(time.time() - players[player][0])
        if int(players[player][1]) < 1:
            JumpDict["Status"][int(player)] = "Haven't started yet!"
        if JumpDict["Status"][int(player)] == "Haven't started yet!" and int(players[player][1]) > 0:
            JumpDict["Status"][int(player)] = "None"
        if int(players[player][1]) == 1 and JumpDict["Status"][int(player)] == "None":
            JumpDict["Status"][int(player)] = "W Only"
        FPSWanted = 54
        if str(player) in fps_max_dict:
            FPSWanted = int(float(fps_max_dict[str(player)]))
        TellBhopInfo(player,player,speed,timeLeft,FPSWanted)
    for player in playerlib.getUseridList('#dead'):
        if int(es.getplayerprop(player, "CCSPlayer.baseclass.m_iObserverMode")) in (1,3,4):
            player2 = getSpectargetByIndex(es.getplayerprop(player, 'CBasePlayer.m_hObserverTarget'))
            if player2 not in started:
                continue
            if player2 not in players:
                continue
            if int(player2) not in JumpDict["Status"]:
                continue
            if int(player2) > 0:
                x = float(es.getplayerprop(player2, 'CBasePlayer.localdata.m_vecVelocity[0]'))
                y = float(es.getplayerprop(player2, 'CBasePlayer.localdata.m_vecVelocity[1]'))
                z = float(es.getplayerprop(player2, 'CBasePlayer.localdata.m_vecVelocity[2]'))
                vec = vecmath.vector((x, y, z))
                speed = round(vec.length(), 2)
                timeLeft = formatTime(time.time() - players[player2][0])
                FPSWanted = 54
                if str(player2) in fps_max_dict:
                    FPSWanted = int(float(fps_max_dict[str(player2)]))
                TellBhopInfo(player,player2,speed,timeLeft,FPSWanted)

def checkLoop(Param1=0,Param2=0,Param3=0):
    gamethread.delayedname(0.25, 'climbtime_checkloop', checkLoop)
    ''' Iterate through a list of all the players and check their location '''
    for player in es.getUseridList():
        if (player in started) and (int(es.getplayerteam(player)) > 1):
            lowerVertex, upperVertex = mapDicts[str(currentMap)]["endpos"]
            timeTaken = time.time() - players[player][0]
            if vecmath.isbetweenRect(es.getplayerlocation(player), lowerVertex, upperVertex):
                ''' Player has finished... '''
                ''' Add their time to the dictionary which will save '''
                if timeTaken > 4:
                    steamid   = es.getplayersteamid(player)
                    if int(player) not in JumpDict["Status"]: JumpDict["Status"][int(player)] = "Normal"
                    if JumpDict["Status"][int(player)] == "W Only": # This is for the W-Only people
                        if str(currentMap) not in mapDicts_W: mapDicts_W[str(currentMap)] = {}
                        if str(currentMap) not in mapDicts_W_54: mapDicts_W_54[str(currentMap)] = {}
                        if str(currentMap) not in mapDicts_W_300: mapDicts_W_300[str(currentMap)] = {}
                        tokens          = {}
                        tokens['name']  = es.getplayername(player)
                        tokens['time']  = formatTime(timeTaken)
                        tokens['end']   = "."
                        tokens['end']   = " with %s jumps." % players[player][1]
                        for tellplayer in es.getUseridList(): tell(tellplayer, "finish_W", tokens)
                        WantedFPS = 54
                        if str(player) in fps_max_dict:
                            WantedFPS = int(float(fps_max_dict[str(player)]))
                        if WantedFPS >= FPS54_Starts and WantedFPS <= FPS54_Ends:
                            WantedFPS = 54
                        if steamid not in mapDicts_W[str(currentMap)]:
                            mapDicts_W[str(currentMap)][steamid] = {'time':timeTaken, 'name':es.getplayername(player), 'jumps':players[player][1],'fps':WantedFPS}
                        else:
                            if mapDicts_W[str(currentMap)][steamid]['time'] > timeTaken:
                                mapDicts_W[str(currentMap)][steamid]['time']  = timeTaken
                                mapDicts_W[str(currentMap)][steamid]['jumps'] = players[player][1]
                                mapDicts_W[str(currentMap)][steamid]['fps'] = WantedFPS
                                es.tell(player,'New record [W Only]')
                        if steamid not in mapDicts_W_300[str(currentMap)]:
                            if WantedFPS == 300:
                                mapDicts_W_300[str(currentMap)][steamid] = {'time':timeTaken, 'name':es.getplayername(player), 'jumps':players[player][1],'fps':WantedFPS}
                        else:
                            if WantedFPS == 300:
                                if mapDicts_W_300[str(currentMap)][steamid]['time'] > timeTaken:
                                    mapDicts_W_300[str(currentMap)][steamid] = {'time':timeTaken, 'name':es.getplayername(player), 'jumps':players[player][1],'fps':WantedFPS}
                        if steamid not in mapDicts_W_54[str(currentMap)]:
                            if WantedFPS == 54:
                                mapDicts_W_54[str(currentMap)][steamid] = {'time':timeTaken, 'name':es.getplayername(player), 'jumps':players[player][1],'fps':WantedFPS}
                        else:
                            if WantedFPS == 54:
                                if mapDicts_W_54[str(currentMap)][steamid]['time'] > timeTaken:
                                    mapDicts_W_54[str(currentMap)][steamid] = {'time':timeTaken, 'name':es.getplayername(player), 'jumps':players[player][1],'fps':WantedFPS}

                    elif JumpDict["Status"][int(player)] == "Sideways": # This is the for SW (SideWays) people
                        if str(currentMap) not in mapDicts_SW: mapDicts_SW[str(currentMap)] = {}
                        if str(currentMap) not in mapDicts_SW_54: mapDicts_SW_54[str(currentMap)] = {}
                        if str(currentMap) not in mapDicts_SW_300: mapDicts_SW_300[str(currentMap)] = {}
                        tokens          = {}
                        tokens['name']  = es.getplayername(player)
                        tokens['time']  = formatTime(timeTaken)
                        tokens['end']   = "."
                        tokens['end']   = " with %s jumps." % players[player][1]
                        for tellplayer in es.getUseridList(): tell(tellplayer, "finish_SW", tokens)
                        WantedFPS = 54
                        if str(player) in fps_max_dict:
                            WantedFPS = int(float(fps_max_dict[str(player)]))
                        if WantedFPS >= FPS54_Starts and WantedFPS <= FPS54_Ends:
                            WantedFPS = 54
                        if steamid not in mapDicts_SW[str(currentMap)]:
                            mapDicts_SW[str(currentMap)][steamid] = {'time':timeTaken, 'name':es.getplayername(player), 'jumps':players[player][1],'fps':WantedFPS}
                        else:
                            if steamid not in mapDicts_SW[str(currentMap)]: mapDicts_SW[str(currentMap)][steamid] = {}
                            if mapDicts_SW[str(currentMap)][steamid]['time'] > timeTaken:
                                mapDicts_SW[str(currentMap)][steamid]['time']  = timeTaken
                                mapDicts_SW[str(currentMap)][steamid]['jumps'] = players[player][1]
                                mapDicts_SW[str(currentMap)][steamid]['fps'] = WantedFPS
                                es.tell(player,'New record [Sideways]')
                        if steamid not in mapDicts_SW_300[str(currentMap)]:
                            if WantedFPS == 300:
                                mapDicts_SW_300[str(currentMap)][steamid] = {'time':timeTaken, 'name':es.getplayername(player), 'jumps':players[player][1],'fps':WantedFPS}
                        else:
                            if WantedFPS == 300:
                                if mapDicts_SW_300[str(currentMap)][steamid]['time'] > timeTaken:
                                    mapDicts_SW_300[str(currentMap)][steamid] = {'time':timeTaken, 'name':es.getplayername(player), 'jumps':players[player][1],'fps':WantedFPS}
                        if steamid not in mapDicts_SW_54[str(currentMap)]:
                            if WantedFPS == 54:
                                mapDicts_SW_54[str(currentMap)][steamid] = {'time':timeTaken, 'name':es.getplayername(player), 'jumps':players[player][1],'fps':WantedFPS}
                        else:
                            if WantedFPS == 54:
                                if mapDicts_SW_54[str(currentMap)][steamid]['time'] > timeTaken:
                                    mapDicts_SW_54[str(currentMap)][steamid] = {'time':timeTaken, 'name':es.getplayername(player), 'jumps':players[player][1],'fps':WantedFPS}
                    else: # This is for the rest
                        if str(currentMap) not in mapDicts: mapDicts[str(currentMap)] = {}
                        if str(currentMap) not in mapDicts_54: mapDicts_54[str(currentMap)] = {}
                        if str(currentMap) not in mapDicts_300: mapDicts_300[str(currentMap)] = {}
                        tokens          = {}
                        tokens['name']  = es.getplayername(player)
                        tokens['time']  = formatTime(timeTaken)
                        tokens['end']   = "."
                        tokens['end']   = " with %s jumps." % players[player][1]
                        for tellplayer in es.getUseridList(): tell(tellplayer, "finish", tokens)
                        WantedFPS = 54
                        if str(player) in fps_max_dict:
                            WantedFPS = int(float(fps_max_dict[str(player)]))
                        if WantedFPS >= FPS54_Starts and WantedFPS <= FPS54_Ends:
                            WantedFPS = 54
                        if steamid not in mapDicts[str(currentMap)]:
                            SetPlayersKills(player,negScore(timeTaken))
                            infos[steamid][str(currentMap)]["kills"] = timeTaken
                            mapDicts[str(currentMap)][steamid] = {'time':timeTaken, 'name':es.getplayername(player), 'jumps':players[player][1],'fps':WantedFPS}
                        else:
                            if mapDicts[str(currentMap)][steamid]['time'] > timeTaken:
                                mapDicts[str(currentMap)][steamid]['time']  = timeTaken
                                SetPlayersKills(player,negScore(mapDicts[str(currentMap)][steamid]['time']))
                                infos[steamid][str(currentMap)]["kills"] = mapDicts[str(currentMap)][steamid]['time']
                                mapDicts[str(currentMap)][steamid]['jumps'] = players[player][1]
                                mapDicts[str(currentMap)][steamid]['fps'] = WantedFPS
                                es.tell(player,'New record [Normal]')
                        if steamid not in mapDicts_300[str(currentMap)]:
                            if WantedFPS == 300:
                                mapDicts_300[str(currentMap)][steamid] = {'time':timeTaken, 'name':es.getplayername(player), 'jumps':players[player][1],'fps':WantedFPS}
                        else:
                            if WantedFPS == 300:
                                if mapDicts_300[str(currentMap)][steamid]['time'] > timeTaken:
                                    mapDicts_300[str(currentMap)][steamid] = {'time':timeTaken, 'name':es.getplayername(player), 'jumps':players[player][1],'fps':WantedFPS}
                        if steamid not in mapDicts_54[str(currentMap)]:
                            if WantedFPS == 54:
                                mapDicts_54[str(currentMap)][steamid] = {'time':timeTaken, 'name':es.getplayername(player), 'jumps':players[player][1],'fps':WantedFPS}
                        else:
                            if WantedFPS == 54:
                                if mapDicts_54[str(currentMap)][steamid]['time'] > timeTaken:
                                    mapDicts_54[str(currentMap)][steamid] = {'time':timeTaken, 'name':es.getplayername(player), 'jumps':players[player][1],'fps':WantedFPS}
                                    
                                    
                    fileStream = open(dictPath, 'wb')
                    cPickle.dump(mapDicts, fileStream)
                    fileStream.close()
                    fileStream_W = open(dictPath_W, 'wb')
                    cPickle.dump(mapDicts_W, fileStream_W)
                    fileStream_W.close()
                    fileStream_SW = open(dictPath_SW, 'wb')
                    cPickle.dump(mapDicts_SW, fileStream_SW)
                    fileStream_SW.close()
                    fileStream_54 = open(dictPath_54, 'wb')
                    cPickle.dump(mapDicts_54, fileStream_54)
                    fileStream_54.close()
                    fileStream_W_54 = open(dictPath_W_54, 'wb')
                    cPickle.dump(mapDicts_W_54, fileStream_W_54)
                    fileStream_W_54.close()
                    fileStream_SW_54 = open(dictPath_SW_54, 'wb')
                    cPickle.dump(mapDicts_SW_54, fileStream_SW_54)
                    fileStream_SW_54.close()
                    fileStream_300 = open(dictPath_300, 'wb')
                    cPickle.dump(mapDicts_300, fileStream_300)
                    fileStream_300.close()
                    fileStream_W_300 = open(dictPath_W_300, 'wb')
                    cPickle.dump(mapDicts_W_300, fileStream_W_300)
                    fileStream_W_300.close()
                    fileStream_SW_300 = open(dictPath_SW_300, 'wb')
                    cPickle.dump(mapDicts_SW_300, fileStream_SW_300)
                    fileStream_SW_300.close()
                    ''' append his ID to the finished list '''
                    for tellplayer in es.getUseridList():
                        steamidl = es.getplayersteamid(tellplayer)
                        (_pos, _len) = mk_sortDictIndex(str(currentMap), steamidl)
                        SetDeaths(tellplayer, _pos)
                    started.remove(player)
                else:
                    started.remove(player)
            else:
                lowerVertex, upperVertex = mapDicts[str(currentMap)]["startpos"]
                if vecmath.isbetweenRect(es.getplayerlocation(player), lowerVertex, upperVertex):
                    players[player] = [time.time(), 0]
                    JumpDict["Status"][int(player)] = 'None'
        elif (int(es.getplayerteam(player)) > 1):
            if not es.exists('userid',player): return
            c_player = playerlib.getPlayer(player)
            if (c_player.attributes["isdead"] == 0):
                lowerVertex, upperVertex = mapDicts[str(currentMap)]["startpos"]
                if vecmath.isbetweenRect(es.getplayerlocation(player), lowerVertex, upperVertex):
                    ''' Player has started '''
                    tokens = {}
                    tokens['name'] = es.getplayername(player)
                    tell(player, "started", tokens)
                    started.append(player)
                    players[player] = [time.time(), 0]
                    JumpDict["Status"][int(player)] = 'None'

def tell(userid, message, options = {}, tellMessage = True):
    ''' Just a simple wrapper to send a multi language text or return it if tellMessage is False '''
    if not es.exists('userid',userid): return
    message = text(message, options, playerlib.getPlayer(userid).get("lang") )
    if tellMessage:
        es.tell(userid, '#multi', '#lightgreen[#defaultBanana #greenTimer#lightgreen]#default - #lightgreen%s' % message)
    else:
        return message

def formatTime(seconds):
    ''' Format the time in H:M:S when seconds is given. '''
    hours, minutes   = divmod(seconds, 3600)
    minutes, seconds = divmod(minutes, 60)
    hundreths = seconds*1000
    bla, hundreths = divmod(hundreths, 1000)
    return "%s:%02i:%02i.%03i" % (int(hours), minutes, seconds, hundreths)

def effectLoop(userid, start, red = 0, green = 255, blue = 0):
    ''' A method to loop the effects '''
    effectlib.drawBox(start, es.getplayerlocation(userid), red=red, green=green, blue=blue, seconds=0.1)
    gamethread.delayedname(0.1, 'climbtimer_effects', effectLoop, (userid, start, red, green, blue) )

def adminPopupMenuselect4(userid, choice, popupid):
    mapName = str(currentMap)
    global playerList
    if choice == 1:
        if mapName in mapDicts_SW:
            popuplib.close("climbtimer_admin", userid)
            playerList = popuplib.easymenu("climbtimer_playerlist_31", None, playerPopupMenuselectSideways)
            playerList.settitle("[Banana Timer DB SW: %s]\n%s" % (mapName, "-" * 30))
            sortedList = mk_sortDict(mapName,'SW')
            if sortedList:
                lx = 0
                for top in sortedList:
                    playerList.addoption('%s' % str(top[0]), "%s. %s - %s" % (lx + 1, mapDicts_SW[mapName][top[0]]["name"], formatTime(mapDicts_SW[mapName][top[0]]["time"])))
                    lx += 1
            else:
                playerList.setdescription("[No places recorded]")
            playerList.send(userid)
        else:
            tell(userid, 'no map records', {})
    elif choice == 2:
        if mapName in mapDicts_SW_54:
            popuplib.close("climbtimer_admin", userid)
            playerList = popuplib.easymenu("climbtimer_playerlist_32", None, playerPopupMenuselectSideways_54)
            playerList.settitle("[Banana Timer DB 54 SW: %s]\n%s" % (mapName, "-" * 30))
            sortedList = mk_sortDict_54(mapName,'SW')
            if sortedList:
                lx = 0
                for top in sortedList:
                    playerList.addoption('%s' % str(top[0]), "%s. %s - %s" % (lx + 1, mapDicts_SW_54[mapName][top[0]]["name"], formatTime(mapDicts_SW_54[mapName][top[0]]["time"])))
                    lx += 1
            else:
                playerList.setdescription("[No places recorded]")
            playerList.send(userid)
        else:
            tell(userid, 'no map records', {})
    elif choice == 3:
        if mapName in mapDicts_SW_300:
            popuplib.close("climbtimer_admin", userid)
            playerList = popuplib.easymenu("climbtimer_playerlist_33", None, playerPopupMenuselectSideways_300)
            playerList.settitle("[Banana Timer DB 300 SW: %s]\n%s" % (mapName, "-" * 30))
            sortedList = mk_sortDict_300(mapName,'SW')
            if sortedList:
                lx = 0
                for top in sortedList:
                    playerList.addoption('%s' % str(top[0]), "%s. %s - %s" % (lx + 1, mapDicts_SW_300[mapName][top[0]]["name"], formatTime(mapDicts_SW_300[mapName][top[0]]["time"])))
                    lx += 1
            else:
                playerList.setdescription("[No places recorded]")
            playerList.send(userid)
        else:
            tell(userid, 'no map records', {})
    elif choice == 8:
        adminPopup_3.send(userid)
def adminPopupMenuselect3(userid, choice, popupid):
    mapName = str(currentMap)
    global playerList
    if choice == 1:
        if mapName in mapDicts_W:
            popuplib.close("climbtimer_admin", userid)
            playerList = popuplib.easymenu("climbtimer_playerlist_21", None, playerPopupMenuselectWonly)
            playerList.settitle("[Banana Timer DB : %s]\n%s" % (mapName, "-" * 30))
            sortedList = mk_sortDict(mapName,'W')
            if sortedList:
                lx = 0
                for top in sortedList:
                    playerList.addoption('%s' % str(top[0]), "%s. %s - %s" % (lx + 1, mapDicts_W[mapName][top[0]]["name"], formatTime(mapDicts_W[mapName][top[0]]["time"])))
                    lx += 1
            else:
                playerList.setdescription("[No places recorded]")
            playerList.send(userid)
        else:
            tell(userid, 'no map records', {})
    elif choice == 2:
        if mapName in mapDicts_W_54:
            popuplib.close("climbtimer_admin", userid)
            playerList = popuplib.easymenu("climbtimer_playerlist_22", None, playerPopupMenuselectWonly_54)
            playerList.settitle("[Banana Timer DB 54 W Only : %s]\n%s" % (mapName, "-" * 30))
            sortedList = mk_sortDict_54(mapName,'W')
            if sortedList:
                lx = 0
                for top in sortedList:
                    playerList.addoption('%s' % str(top[0]), "%s. %s - %s" % (lx + 1, mapDicts_W_54[mapName][top[0]]["name"], formatTime(mapDicts_W_54[mapName][top[0]]["time"])))
                    lx += 1
            else:
                playerList.setdescription("[No places recorded]")
            playerList.send(userid)
        else:
            tell(userid, 'no map records', {})
    elif choice == 3:
        if mapName in mapDicts_W_300:
            popuplib.close("climbtimer_admin", userid)
            playerList = popuplib.easymenu("climbtimer_playerlist_23", None, playerPopupMenuselectWonly_300)
            playerList.settitle("[Banana Timer DB 300 W Only: %s]\n%s" % (mapName, "-" * 30))
            sortedList = mk_sortDict_300(mapName,'W')
            if sortedList:
                lx = 0
                for top in sortedList:
                    playerList.addoption('%s' % str(top[0]), "%s. %s - %s" % (lx + 1, mapDicts_W_300[mapName][top[0]]["name"], formatTime(mapDicts_W_300[mapName][top[0]]["time"])))
                    lx += 1
            else:
                playerList.setdescription("[No places recorded]")
            playerList.send(userid)
        else:
            tell(userid, 'no map records', {})
    elif choice == 8:
        adminPopup_2.send(userid)
    elif choice == 9:
        adminPopup_4.send(userid)
def adminPopupMenuselect2(userid, choice, popupid):
    mapName = str(currentMap)
    global playerList
    if choice == 1:
        if mapName in mapDicts:
            popuplib.close("climbtimer_admin", userid)
            playerList = popuplib.easymenu("climbtimer_playerlist_11", None, playerPopupMenuselectNormal)
            playerList.settitle("[Banana Timer DB : %s]\n%s" % (mapName, "-" * 30))
            sortedList = mk_sortDict(mapName,'Normal')
            if sortedList:
                lx = 0
                for top in sortedList:
                    playerList.addoption('%s' % str(top[0]), "%s. %s - %s" % (lx + 1, mapDicts[mapName][top[0]]["name"], formatTime(mapDicts[mapName][top[0]]["time"])))
                    lx += 1
            else:
                playerList.setdescription("[No places recorded]")
            playerList.send(userid)
        else:
            tell(userid, 'no map records', {})
    elif choice == 2:
        if mapName in mapDicts:
            popuplib.close("climbtimer_admin", userid)
            playerList = popuplib.easymenu("climbtimer_playerlist_12", None, playerPopupMenuselectNormal_54)
            playerList.settitle("[Banana Timer DB 54: %s]\n%s" % (mapName, "-" * 30))
            sortedList = mk_sortDict_54(mapName,'Normal')
            if sortedList:
                lx = 0
                for top in sortedList:
                    playerList.addoption('%s' % str(top[0]), "%s. %s - %s" % (lx + 1, mapDicts_54[mapName][top[0]]["name"], formatTime(mapDicts_54[mapName][top[0]]["time"])))
                    lx += 1
            else:
                playerList.setdescription("[No places recorded]")
            playerList.send(userid)
        else:
            tell(userid, 'no map records', {})
    elif choice == 3:
        if mapName in mapDicts:
            popuplib.close("climbtimer_admin", userid)
            playerList = popuplib.easymenu("climbtimer_playerlist_13", None, playerPopupMenuselectNormal_300)
            playerList.settitle("[Banana Timer DB 300: %s]\n%s" % (mapName, "-" * 30))
            sortedList = mk_sortDict_300(mapName,'Normal')
            if sortedList:
                lx = 0
                for top in sortedList:
                    playerList.addoption('%s' % str(top[0]), "%s. %s - %s" % (lx + 1, mapDicts_300[mapName][top[0]]["name"], formatTime(mapDicts_300[mapName][top[0]]["time"])))
                    lx += 1
            else:
                playerList.setdescription("[No places recorded]")
            playerList.send(userid)
        else:
            tell(userid, 'no map records', {})
    elif choice == 8:
        adminPopup.send(userid)
    elif choice == 9:
        adminPopup_3.send(userid)
def adminPopupMenuselect(userid, choice, popupid):
    '''
    Handles the menu select from the admin menu.
    
    Note: You have to staticly cast the getplayerlocation to a list so we can
          edit the items in it as getplayerlocation returns a tuple which can't
          be edited. 
    '''
    mapName = str(currentMap)
    global playerList
    if choice == 1:
        if mapName not in mapDicts:
            mapDicts[mapName] = {}
        if "startpos" not in mapDicts[mapName]:
            mapDicts[mapName]['startpos'] = [ (0,0,0), (0,0,0) ]
        if userid not in effects:
            effects.append(userid)
            tell(userid, 'added start one')
            start = list(es.getplayerlocation(userid))
            start[2] -= 5
            mapDicts[mapName]["startpos"][0] = start
            effectLoop(userid, start)
        else:
            effects.remove(userid)
            gamethread.cancelDelayed('climbtimer_effects')
            tell(userid, 'added start two')
            mapDicts[mapName]["startpos"][1] = list(es.getplayerlocation(userid))
            mapDicts[mapName]["startpos"][1][2] -= 5
            if "endpos" in mapDicts[mapName]:
                gamethread.delayedname(0.1, 'climbtime_checkloop', checkLoop)
                hudLoop()
        adminPopup.send(userid)
            
    elif choice == 2:
        if mapName not in mapDicts:
            mapDicts[mapName] = {}
        if "endpos" not in mapDicts[mapName]:
            mapDicts[mapName]['endpos'] = [ (0,0,0), (0,0,0) ]
        if userid not in effects:
            effects.append(userid)
            tell(userid, 'added end one')
            start = list(es.getplayerlocation(userid))
            start[2] -= 5
            mapDicts[mapName]["endpos"][0] = start
            effectLoop(userid, start, 255, 0)
        else:
            effects.remove(userid)
            gamethread.cancelDelayed('climbtimer_effects')
            tell(userid, 'added end two')
            mapDicts[mapName]["endpos"][1] = list(es.getplayerlocation(userid))
            mapDicts[mapName]["endpos"][1][2] -= 5
            if "startpos" in mapDicts[mapName]:
                gamethread.delayedname(0.1, 'climbtime_checkloop', checkLoop)
                hudLoop()
        adminPopup.send(userid)
            
    elif choice == 3:
        if mapName in mapDicts:
            del mapDicts[mapName]
            gamethread.cancelDelayed('climbtime_checkloop')
        tell(userid, 'delete')    
        
    elif choice == 4:
        SetUpTop()
        es.msg("#multi","#green%s updated !top" %(es.getplayername(userid)))
    elif choice == 5:
        ResetStats(userid)
    elif choice == 9:
        adminPopup_2.send(userid)
def playerPopupMenuselectNormal(userid, choice, popupid):
    mapName = str(currentMap)
    if mapDicts[mapName]:
        if mapDicts[mapName][str(choice)]:
            tokens = {}
            tokens['steamid'] = str(choice)
            tokens['name'] = mapDicts[mapName][str(choice)]["name"]
            del mapDicts[mapName][str(choice)]
            if "kills" in infos[str(choice)][str(currentMap)]:
                infos[str(choice)][str(currentMap)]["kills"] = 0
                SetPlayersKills(es.getuserid(str(choice)), negScore(infos[str(choice)][str(currentMap)]["kills"]))
            SetDeaths(es.getuserid(str(choice)), 0)
            if es.exists('userid',userid):
                tell(userid, 'remove player', tokens)
                adminPopupMenuselect2(userid,1,None)
        else:
            if "STEAM" in str(choice):
                if es.exists('userid',userid):
                    tell(userid, 'failed remove player', {})
                    adminPopupMenuselect2(userid,1,None)
    else:
        if es.exists('userid',userid):
            tell(userid, 'no map records', {})
def playerPopupMenuselectNormal_54(userid, choice, popupid):
    mapName = str(currentMap)
    if mapDicts_54[mapName]:
        if mapDicts_54[mapName][str(choice)]:
            tokens = {}
            tokens['steamid'] = str(choice)
            tokens['name'] = mapDicts_54[mapName][str(choice)]["name"]
            del mapDicts_54[mapName][str(choice)]
            if es.exists('userid',userid):
                tell(userid, 'remove player', tokens)
                adminPopupMenuselect2(userid,2,None)
        else:
            if "STEAM" in str(choice):
                if es.exists('userid',userid):
                    tell(userid, 'failed remove player', {})
                    adminPopupMenuselect2(userid,2,None)
    else:
        if es.exists('userid',userid):
            tell(userid, 'no map records', {})
def playerPopupMenuselectNormal_300(userid, choice, popupid):
    mapName = str(currentMap)
    if mapDicts_300[mapName]:
        if mapDicts_300[mapName][str(choice)]:
            tokens = {}
            tokens['steamid'] = str(choice)
            tokens['name'] = mapDicts_300[mapName][str(choice)]["name"]
            del mapDicts_300[mapName][str(choice)]
            if es.exists('userid',userid):
                tell(userid, 'remove player', tokens)
                adminPopupMenuselect2(userid,3,None)
        else:
            if "STEAM" in str(choice):
                if es.exists('userid',userid):
                    tell(userid, 'failed remove player', {})
                    adminPopupMenuselect2(userid,3,None)
    else:
        if es.exists('userid',userid):
            tell(userid, 'no map records', {})

def playerPopupMenuselectWonly(userid, choice, popupid):
    mapName = str(currentMap)
    if mapDicts_W[mapName]:
        if mapDicts_W[mapName][str(choice)]:
            tokens = {}
            tokens['steamid'] = str(choice)
            tokens['name'] = mapDicts_W[mapName][str(choice)]["name"]
            del mapDicts_W[mapName][str(choice)]
            if es.exists('userid',userid):
                tell(userid, 'remove player', tokens)
                adminPopupMenuselect3(userid,1,None)
        else:
            if "STEAM" in str(choice):
                if es.exists('userid',userid):
                    tell(userid, 'failed remove player', {})
                    adminPopupMenuselect3(userid,1,None)
    else:
        if es.exists('userid',userid):
            tell(userid, 'no map records', {})
def playerPopupMenuselectWonly_54(userid, choice, popupid):
    mapName = str(currentMap)
    if mapDicts_W_54[mapName]:
        if mapDicts_W_54[mapName][str(choice)]:
            tokens = {}
            tokens['steamid'] = str(choice)
            tokens['name'] = mapDicts_W_54[mapName][str(choice)]["name"]
            del mapDicts_W_54[mapName][str(choice)]
            if es.exists('userid',userid):
                tell(userid, 'remove player', tokens)
                adminPopupMenuselect3(userid,2,None)
        else:
            if "STEAM" in str(choice):
                if es.exists('userid',userid):
                    tell(userid, 'failed remove player', {})
                    adminPopupMenuselect3(userid,2,None)
    else:
        if es.exists('userid',userid):
            tell(userid, 'no map records', {})
def playerPopupMenuselectWonly_300(userid, choice, popupid):
    mapName = str(currentMap)
    if mapDicts_W_300[mapName]:
        if mapDicts_W_300[mapName][str(choice)]:
            tokens = {}
            tokens['steamid'] = str(choice)
            tokens['name'] = mapDicts_W_300[mapName][str(choice)]["name"]
            del mapDicts_W_300[mapName][str(choice)]
            if es.exists('userid',userid):
                tell(userid, 'remove player', tokens)
                adminPopupMenuselect3(userid,3,None)
        else:
            if "STEAM" in str(choice):
                if es.exists('userid',userid):
                    tell(userid, 'failed remove player', {})
                    adminPopupMenuselect3(userid,3,None)
    else:
        if es.exists('userid',userid):
            tell(userid, 'no map records', {})

def playerPopupMenuselectSideways(userid, choice, popupid):
    mapName = str(currentMap)
    if mapDicts_SW[mapName]:
        if mapDicts_SW[mapName][str(choice)]:
            tokens = {}
            tokens['steamid'] = str(choice)
            tokens['name'] = mapDicts_SW[mapName][str(choice)]["name"]
            del mapDicts_SW[mapName][str(choice)]
            if es.exists('userid',userid):
                tell(userid, 'remove player', tokens)
                adminPopupMenuselect4(userid,1,None)
        else:
            if "STEAM" in str(choice):
                tell(userid, 'failed remove player', {})
                adminPopupMenuselect4(userid,1,None)
    else:
        if es.exists('userid',userid):
            tell(userid, 'no map records', {})
def playerPopupMenuselectSideways_54(userid, choice, popupid):
    mapName = str(currentMap)
    if mapDicts_SW_54[mapName]:
        if mapDicts_SW_54[mapName][str(choice)]:
            tokens = {}
            tokens['steamid'] = str(choice)
            tokens['name'] = mapDicts_SW_54[mapName][str(choice)]["name"]
            del mapDicts_SW_54[mapName][str(choice)]
            SetDeaths(es.getuserid(str(choice)), 0)
            if es.exists('userid',userid):
                tell(userid, 'remove player', tokens)
                adminPopupMenuselect4(userid,2,None)
        else:
            if "STEAM" in str(choice):
                tell(userid, 'failed remove player', {})
                adminPopupMenuselect4(userid,2,None)
    else:
        if es.exists('userid',userid):
            tell(userid, 'no map records', {})
def playerPopupMenuselectSideways_300(userid, choice, popupid):
    mapName = str(currentMap)
    if mapDicts_SW_300[mapName]:
        if mapDicts_SW_300[mapName][str(choice)]:
            tokens = {}
            tokens['steamid'] = str(choice)
            tokens['name'] = mapDicts_SW_300[mapName][str(choice)]["name"]
            del mapDicts_SW_300[mapName][str(choice)]
            SetDeaths(es.getuserid(str(choice)), 0)
            if es.exists('userid',userid):
                tell(userid, 'remove player', tokens)
                adminPopupMenuselect4(userid,3,None)
        else:
            if "STEAM" in str(choice):
                tell(userid, 'failed remove player', {})
                adminPopupMenuselect4(userid,3,None)
    else:
        if es.exists('userid',userid):
            tell(userid, 'no map records', {})
def ResetStats(userid=0):
    global statsmenuscreated
    for statsmenusName in statsmenuscreated:
        if not popuplib.exists(statsmenusName):
            continue
        popuplib.delete(statsmenusName)
        if es.exists('userid',userid): es.tell(userid,'deleted %s' %(statsmenusName))
    statsmenuscreated = []
    if es.exists('userid',userid): es.msg("#multi","#green%s \x05reset #green!stats" %(es.getplayername(userid)))
def unload():
    ResetStats()
    es.msg("#multi","#darkgreenBanana Script #default(#greenv%s#default)#darkgreen has been #lightgreenunloaded#darkgreen!"%info.version)
    gamethread.cancelDelayed('MapsFix')
    gamethread.cancelDelayed('StartValueChecker')
    if TickListener_Enabled:
        es.addons.unregisterTickListener(ticklistener)
    es.addons.unregisterClientCommandFilter(myfilter)
    del started[:]
    players.clear()
    save_dictionary()
    
    fileStream = open(dictPath, 'wb')
    cPickle.dump(mapDicts, fileStream)
    fileStream.close()
    fileStream_W = open(dictPath_W, 'wb')
    cPickle.dump(mapDicts_W, fileStream_W)
    fileStream_W.close()
    fileStream_SW = open(dictPath_SW, 'wb')
    cPickle.dump(mapDicts_SW, fileStream_SW)
    fileStream_SW.close()
    fileStream_54 = open(dictPath_54, 'wb')
    cPickle.dump(mapDicts_54, fileStream_54)
    fileStream_54.close()
    fileStream_W_54 = open(dictPath_W_54, 'wb')
    cPickle.dump(mapDicts_W_54, fileStream_W_54)
    fileStream_W_54.close()
    fileStream_SW_54 = open(dictPath_SW_54, 'wb')
    cPickle.dump(mapDicts_SW_54, fileStream_SW_54)
    fileStream_SW_54.close()
    fileStream_300 = open(dictPath_300, 'wb')
    cPickle.dump(mapDicts_300, fileStream_300)
    fileStream_300.close()
    fileStream_W_300 = open(dictPath_W_300, 'wb')
    cPickle.dump(mapDicts_W_300, fileStream_W_300)
    fileStream_W_300.close()
    fileStream_SW_300 = open(dictPath_SW_300, 'wb')
    cPickle.dump(mapDicts_SW_300, fileStream_SW_300)
    fileStream_SW_300.close()
    
    gamethread.cancelDelayed('climbtime_checkloop')
    gamethread.cancelDelayed('climbtimer_hudloop')
    gamethread.cancelDelayed('climbtimer_hudloop2')
    if playerList:
        playerList.delete()

# SAY
    if es.exists('saycommand', '!save'):
        es.unregsaycmd('!save')
    if es.exists('saycommand', '!lazyshit'):
        es.unregsaycmd('!lazyshit')
    if es.exists('saycommand', '!next'):
        es.unregsaycmd('!next')
    if es.exists('saycommand', '!back'):
        es.unregsaycmd('!back')
    if es.exists('saycommand', '!reset'):
        es.unregsaycmd('!reset')
    if es.exists('saycommand', '!ghost'):
        es.unregsaycmd('!ghost')
    if es.exists('saycommand', '!unghost'):
        es.unregsaycmd('!unghost')
    if es.exists('saycommand', '!menu'):
        es.unregsaycmd('!menu')
    if es.exists('saycommand', '!scout'):
        es.unregsaycmd('!scout')
    if es.exists('saycommand', '!usp'):
        es.unregsaycmd('!usp')
    if es.exists('saycommand', '!flash'):
        es.unregsaycmd('!flash')
    if es.exists('saycommand', '!kill'):
        es.unregsaycmd('!kill')
    if es.exists('saycommand', '!spec'):
        es.unregsaycmd('!spec')
    if es.exists('saycommand', '!chee'):
        es.unregsaycmd('!chee')

# CLIENT
    if es.exists('clientcommand', '!lazyshit'):
        es.unregclientcmd('!lazyshit')
    if es.exists('clientcommand', 'cp_save'):
        es.unregclientcmd('cp_save')
    if es.exists('clientcommand', 'cp_next'):
        es.unregclientcmd('cp_next')
    if es.exists('clientcommand', 'cp_back'):
        es.unregclientcmd('cp_back')
    if es.exists('clientcommand', 'cp_reset'):
        es.unregclientcmd('cp_reset')
    if es.exists('clientcommand', 'cp_ghost'):
        es.unregclientcmd('cp_ghost')
    if es.exists('clientcommand', 'cp_unghost'):
        es.unregclientcmd('cp_unghost')
    if es.exists('clientcommand', 'cp_menu'):
        es.unregclientcmd('cp_menu')
    if es.exists('clientcommand', 'cp_scout'):
        es.unregclientcmd('cp_scout')
    if es.exists('clientcommand', 'cp_usp'):
        es.unregclientcmd('cp_usp')
    if es.exists('clientcommand', 'cp_flash'):
        es.unregclientcmd('cp_flash')
    if es.exists('clientcommand', 'cp_kill'):
        es.unregclientcmd('cp_kill')
    if es.exists('clientcommand', 'cp_spec'):
        es.unregclientcmd('cp_spec')

def SetDeaths(userid,N):
    deaths_list[userid] = N

def TellBhopInfo(To,From,speed,timeLeft,FPSReal):
    To = int(To)
    ToSteamID = es.getplayersteamid(To)
    OldThing = JumpDict["Status"][int(From)]
    if int(players[From][1]) < 2:
        JumpDict["Status"][int(From)] = "Haven't started yet!"
    
    if FPSReal >= FPS54_Starts and FPSReal <= FPS54_Ends:
        FPSRound = 54
    else:
        FPSRound = 300
        
    if ToSteamID not in WantsPadNTimer['timer']: WantsPadNTimer['timer'][ToSteamID] = 1
    elif WantsPadNTimer['timer'][ToSteamID] == 1:
        usermsg.hudhint(To,tell(From, 'timer with jump counter complete', {'FPSReal':FPSReal,'FPSRound':FPSRound,'mode':JumpDict["Status"][int(From)],'name':es.getplayername(From).replace('"','').replace("'",""),'time':timeLeft, 'jumps':players[From][1], 'speed': speed}, False))
    elif WantsPadNTimer['timer'][ToSteamID] == 2:
        usermsg.hudhint(To,tell(From, 'timer with jump counter clean', {'FPSReal':FPSReal,'FPSRound':FPSRound,'mode':JumpDict["Status"][int(From)],'time':timeLeft}, False))
    JumpDict["Status"][int(From)] = OldThing
def TellKeysInfo(To,From,_______W,_______A,_______S,_______D,____DUCK,____JUMP):
    To = int(To)
    ToSteamID = es.getplayersteamid(To)
    if ToSteamID not in WantsPadNTimer['pad']: WantsPadNTimer['pad'][ToSteamID] = 0
    elif WantsPadNTimer['pad'][ToSteamID] == 1:
        Sentence1 = " "*2
        Sentence2 = " "*5
        Sentence3 = " "*2
        Sentence4 = " "*2
        Sentence5 = " "*5
        Sentence6 = " "*2
        if _______W: Sentence1 = 'W'
        if ____DUCK: Sentence2 = '▼'
        if _______A: Sentence3 = 'A'
        if _______D: Sentence4 = 'D'
        if ____JUMP: Sentence5 = '▲ '
        if _______S: Sentence6 = 'S'
        usermsg.centermsg(To,tell(From, 'toppanel', {'W':Sentence1,'DUCKS':Sentence2,'A':Sentence3,'D':Sentence4,'JUMPS':Sentence5,'S':Sentence6}, False))
    elif WantsPadNTimer['pad'][ToSteamID] == 2:
        Sentence1 = " "*2
        Sentence2 = " "*5
        Sentence3 = " "*2
        Sentence4 = " "*2
        Sentence5 = " "*5
        Sentence6 = " "*2
        if _______W: Sentence1 = 'W'
        if ____DUCK: Sentence2 = '▼'
        if _______A: Sentence3 = 'A'
        if _______D: Sentence4 = 'D'
        if ____JUMP: Sentence5 = '▲ '
        if _______S: Sentence6 = 'S'
        usermsg.centermsg(To,tell(From, 'middlepanel', {'W':Sentence1,'DUCKS':Sentence2,'A':Sentence3,'D':Sentence4,'JUMPS':Sentence5,'S':Sentence6}, False))
    elif WantsPadNTimer['pad'][ToSteamID] == 3:
        Sentence1 = " "*2
        Sentence2 = " "*5
        Sentence3 = " "*2
        Sentence4 = " "*2
        Sentence5 = " "*5
        Sentence6 = " "*2
        if _______W: Sentence1 = 'W'
        if ____DUCK: Sentence2 = '▼'
        if _______A: Sentence3 = 'A'
        if _______D: Sentence4 = 'D'
        if ____JUMP: Sentence5 = '▲ '
        if _______S: Sentence6 = 'S'
        usermsg.centermsg(To,tell(From, 'bottompanel', {'W':Sentence1,'DUCKS':Sentence2,'A':Sentence3,'D':Sentence4,'JUMPS':Sentence5,'S':Sentence6}, False))
    elif WantsPadNTimer['pad'][ToSteamID] == 4:
        Sentence1 = " "*3   # W
        Sentence2 = " "*6   # DUCK
        Sentence3 = " "*2   # A
        Sentence4 = " "*2   # D
        Sentence5 = " "*6   # jumps
        Sentence6 = " "*2   # S
        if _______W: Sentence1 = 'W'
        if ____DUCK: Sentence2 = 'DUK'
        if _______A: Sentence3 = 'A'
        if _______D: Sentence4 = 'D'
        if ____JUMP: Sentence5 = 'JMP'
        if _______S: Sentence6 = 'S'
        usermsg.centermsg(To,tell(From, 'modernpanel', {'W':Sentence1,'DUCKS':Sentence2,'A':Sentence3,'D':Sentence4,'JUMPS':Sentence5,'S':Sentence6}, False))
def getSpectargetByIndex(index):
    ''' Loops through alive targets to compare the given index and the handle of the looped player '''
    for userid in filter(lambda temp: not es.getplayerprop(temp, "CCSPlayer.baseclass.pl.deadflag"), es.getUseridList()):
        if es.getplayerhandle(userid) == index: return userid
def SetPlayersKills(userid,score):
    es.server.queuecmd("score set %s %s" %(userid,score))
    #es.setplayerprop(userid, 'CBasePlayer.m_iScore',int(score))