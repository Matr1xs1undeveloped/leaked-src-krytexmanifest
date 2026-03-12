# Source Generated with Decompyle++
# File: main.pyc (Python 3.10)

import os
import sys
import json
import time
import secrets
import logging
import requests
import threading
import re
import webview
import webbrowser
from flask import Flask, Response, request, session, redirect, url_for, stream_with_context, send_file

def resource_path(relative_path):
    ''' Get absolute path to resource, works for dev and for PyInstaller '''
    pass
# WARNING: Decompyle incomplete


class WindowApi:
    
    def close_app(self):
        '''Closes the application'''
        webview.windows[0].destroy()

    
    def minimize_app(self):
        '''Minimizes the application'''
        webview.windows[0].minimize()

    
    def select_folder(self):
        '''Opens folder selection dialog'''
        result = webview.windows[0].create_file_dialog(webview.FOLDER_DIALOG)
        if result and len(result) > 0:
            return result[0]


app = Flask(__name__)
app.secret_key = 'krytex_v66_premium_full_desktop_final_ultimate_v16_multi_list'
DISCORD_CLIENT_ID = '1463985409838157949'
DISCORD_CLIENT_SECRET = 'pBt4i6XRqLiN4HXn6nhoq3RfV4vqOaO5'
DISCORD_REDIRECT_URI = 'http://127.0.0.1:5000/callback'
DISCORD_BOT_TOKEN = 'MTQ2Mzk4NTQwOTgzODE1Nzk0OQ.GjejX4.bDKFE6f2GZi_Wz5xLsyL0y5o5g3BXEy7hyPRcM'
DISCORD_LOG_CHANNEL_ID = '1463974807048556687'
DISCORD_GUILD_ID = '1463963344628351151'
DISCORD_INVITE_LINK = 'https://discord.gg/BjRJ7k6Zjs'
RYUU_API_KEY = 'RYUUMANIFEST8acau9'
RYUU_LUA_ENDPOINT = 'https://generator.ryuu.lol/resellerlua/__APPID__?auth_code=' + RYUU_API_KEY
CATALOG_PATH = resource_path('catalog.json')
CAT_IMAGE = resource_path('cat.png')
CATALOG_DATA = { }
DEFAULT_STEAM_PATH = 'C:\\Program Files (x86)\\Steam\\config\\stplug-in'
DISCORD_CACHE = { }
LAST_CACHE_UPDATE = 0
logging.basicConfig(logging.INFO, **('level',))
POPULAR_GAMES_LIST = [][{
    'id': '730',
    'title': 'Counter-Strike 2' }][{
    'id': '570',
    'title': 'Dota 2' }][{
    'id': '578080',
    'title': 'PUBG: BATTLEGROUNDS' }][{
    'id': '1172470',
    'title': 'Apex Legends' }][{
    'id': '1938090',
    'title': 'Call of Duty: Modern Warfare III' }][{
    'id': '359550',
    'title': "Tom Clancy's Rainbow Six Siege" }][{
    'id': '440',
    'title': 'Team Fortress 2' }][{
    'id': '2073850',
    'title': 'THE FINALS' }][{
    'id': '553850',
    'title': 'HELLDIVERS 2' }][{
    'id': '230410',
    'title': 'Warframe' }][{
    'id': '236390',
    'title': 'War Thunder' }][{
    'id': '1238840',
    'title': 'Battlefield 2042' }][{
    'id': '1238810',
    'title': 'Battlefield V' }][{
    'id': '1238860',
    'title': 'Battlefield 4' }][{
    'id': '1238820',
    'title': 'Battlefield 1' }][{
    'id': '222880',
    'title': 'Insurgency' }][{
    'id': '581320',
    'title': 'Insurgency: Sandstorm' }][{
    'id': '1085660',
    'title': 'Destiny 2' }][{
    'id': '252490',
    'title': 'Rust' }][{
    'id': '221100',
    'title': 'DayZ' }][{
    'id': '393380',
    'title': 'Squad' }][{
    'id': '686810',
    'title': 'Hell Let Loose' }][{
    'id': '1144200',
    'title': 'Ready or Not' }][{
    'id': '594650',
    'title': 'Hunt: Showdown 1896' }][{
    'id': '206420',
    'title': 'Saints Row IV' }][{
    'id': '550',
    'title': 'Left 4 Dead 2' }][{
    'id': '220',
    'title': 'Half-Life 2' }][{
    'id': '546560',
    'title': 'Half-Life: Alyx' }][{
    'id': '4000',
    'title': "Garry's Mod" }][{
    'id': '271590',
    'title': 'Grand Theft Auto V' }][{
    'id': '1174180',
    'title': 'Red Dead Redemption 2' }][{
    'id': '1091500',
    'title': 'Cyberpunk 2077' }][{
    'id': '1245620',
    'title': 'Elden Ring' }][{
    'id': '292030',
    'title': 'The Witcher 3: Wild Hunt' }][{
    'id': '489830',
    'title': 'The Elder Scrolls V: Skyrim Special Edition' }][{
    'id': '377160',
    'title': 'Fallout 4' }][{
    'id': '22380',
    'title': 'Fallout: New Vegas' }][{
    'id': '1151640',
    'title': 'Horizon Zero Dawn' }][{
    'id': '2420110',
    'title': 'Horizon Forbidden West' }][{
    'id': '1593500',
    'title': 'God of War' }][{
    'id': '1928980',
    'title': 'God of War Ragnarök' }][{
    'id': '1888930',
    'title': 'The Last of Us Part I' }][{
    'id': '1172380',
    'title': 'STAR WARS Jedi: Fallen Order' }][{
    'id': '1774580',
    'title': 'STAR WARS Jedi: Survivor' }][{
    'id': '990080',
    'title': 'Hogwarts Legacy' }][{
    'id': '582010',
    'title': 'Monster Hunter: World' }][{
    'id': '1446780',
    'title': 'Monster Hunter Rise' }][{
    'id': '601150',
    'title': 'Devil May Cry 5' }][{
    'id': '335300',
    'title': 'Dark Souls II' }][{
    'id': '374320',
    'title': 'Dark Souls III' }][{
    'id': '814380',
    'title': 'Sekiro: Shadows Die Twice' }][{
    'id': '1817070',
    'title': 'Marvel’s Spider-Man Remastered' }][{
    'id': '1817190',
    'title': 'Marvel’s Spider-Man: Miles Morales' }][{
    'id': '2344520',
    'title': 'Diablo IV' }][{
    'id': '2050650',
    'title': 'Resident Evil 4' }][{
    'id': '883710',
    'title': 'Resident Evil 2' }][{
    'id': '952060',
    'title': 'Resident Evil 3' }][{
    'id': '1196590',
    'title': 'Resident Evil Village' }][{
    'id': '418370',
    'title': 'Resident Evil 7 Biohazard' }][{
    'id': '1086940',
    'title': "Baldur's Gate 3" }][{
    'id': '1623730',
    'title': 'Palworld' }][{
    'id': '346110',
    'title': 'ARK: Survival Evolved' }][{
    'id': '2430930',
    'title': 'ARK: Survival Ascended' }][{
    'id': '105600',
    'title': 'Terraria' }][{
    'id': '252490',
    'title': 'Rust' }][{
    'id': '304930',
    'title': 'Unturned' }][{
    'id': '251570',
    'title': '7 Days to Die' }][{
    'id': '322330',
    'title': "Don't Starve Together" }][{
    'id': '892970',
    'title': 'Valheim' }][{
    'id': '1326470',
    'title': 'Sons Of The Forest' }][{
    'id': '242760',
    'title': 'The Forest' }][{
    'id': '1604030',
    'title': 'V Rising' }][{
    'id': '387990',
    'title': 'Scrap Mechanic' }][{
    'id': '313120',
    'title': 'Stranded Deep' }][{
    'id': '264710',
    'title': 'Subnautica' }][{
    'id': '275850',
    'title': "No Man's Sky" }][{
    'id': '294100',
    'title': 'RimWorld' }][{
    'id': '427520',
    'title': 'Factorio' }][{
    'id': '526870',
    'title': 'Satisfactory' }][{
    'id': '1366540',
    'title': 'Dyson Sphere Program' }][{
    'id': '1551360',
    'title': 'Forza Horizon 5' }][{
    'id': '1293830',
    'title': 'Forza Horizon 4' }][{
    'id': '227300',
    'title': 'Euro Truck Simulator 2' }][{
    'id': '270880',
    'title': 'American Truck Simulator' }][{
    'id': '2670630',
    'title': 'Supermarket Simulator' }][{
    'id': '1248130',
    'title': 'Farming Simulator 22' }][{
    'id': '2398830',
    'title': 'Farming Simulator 25' }][{
    'id': '805550',
    'title': 'Assetto Corsa Competizione' }][{
    'id': '244210',
    'title': 'Assetto Corsa' }][{
    'id': '1190000',
    'title': 'CarX Drift Racing Online' }][{
    'id': '284160',
    'title': 'BeamNG.drive' }][{
    'id': '1222670',
    'title': 'The Sims 4' }][{
    'id': '255710',
    'title': 'Cities: Skylines' }][{
    'id': '949230',
    'title': 'Cities: Skylines II' }][{
    'id': '1353230',
    'title': 'Planet Zoo' }][{
    'id': '493340',
    'title': 'Planet Coaster' }][{
    'id': '648350',
    'title': 'Jurassic World Evolution' }][{
    'id': '1244460',
    'title': 'Jurassic World Evolution 2' }][{
    'id': '281990',
    'title': 'Stellaris' }][{
    'id': '394360',
    'title': 'Hearts of Iron IV' }][{
    'id': '289070',
    'title': "Sid Meier's Civilization VI" }][{
    'id': '236850',
    'title': 'Europa Universalis IV' }][{
    'id': '1158310',
    'title': 'Crusader Kings III' }][{
    'id': '1142710',
    'title': 'Total War: WARHAMMER III' }][{
    'id': '594570',
    'title': 'Total War: WARHAMMER II' }][{
    'id': '200510',
    'title': 'XCOM: Enemy Unknown' }][{
    'id': '268500',
    'title': 'XCOM 2' }][{
    'id': '960090',
    'title': 'Bloons TD 6' }][{
    'id': '250900',
    'title': 'The Binding of Isaac: Rebirth' }][{
    'id': '1145360',
    'title': 'Hades' }][{
    'id': '646570',
    'title': 'Slay the Spire' }][{
    'id': '1794680',
    'title': 'Vampire Survivors' }][{
    'id': '262060',
    'title': 'Darkest Dungeon' }][{
    'id': '1942280',
    'title': 'Brotato' }][{
    'id': '632360',
    'title': 'Risk of Rain 2' }][{
    'id': '504230',
    'title': 'Celeste' }][{
    'id': '367520',
    'title': 'Hollow Knight' }][{
    'id': '268910',
    'title': 'Cuphead' }][{
    'id': '413150',
    'title': 'Stardew Valley' }][{
    'id': '945360',
    'title': 'Among Us' }][{
    'id': '1097150',
    'title': 'Fall Guys' }][{
    'id': '261180',
    'title': 'Lethal Company' }][{
    'id': '2861690',
    'title': 'Content Warning' }][{
    'id': '438100',
    'title': 'VRChat' }][{
    'id': '291550',
    'title': 'Brawlhalla' }][{
    'id': '2195250',
    'title': 'EA SPORTS FC 24' }][{
    'id': '2338770',
    'title': 'TEKKEN 8' }][{
    'id': '1778820',
    'title': 'TEKKEN 7' }][{
    'id': '1364780',
    'title': 'Street Fighter 6' }][{
    'id': '1971870',
    'title': 'Mortal Kombat 1' }][{
    'id': '252950',
    'title': 'Rocket League' }][{
    'id': '1203220',
    'title': 'NARAKA: BLADEPOINT' }][{
    'id': '381210',
    'title': 'Dead by Daylight' }][{
    'id': '431960',
    'title': 'Wallpaper Engine' }][{
    'id': '228980',
    'title': 'Steamworks Common Redistributables' }][{
    'id': '1840',
    'title': 'Source Filmmaker' }][{
    'id': '739630',
    'title': 'Phasmophobia' }][{
    'id': '108600',
    'title': 'Project Zomboid' }][{
    'id': '602960',
    'title': 'Barotrauma' }][{
    'id': '2321470',
    'title': 'Deep Rock Galactic: Survivor' }][{
    'id': '548430',
    'title': 'Deep Rock Galactic' }][{
    'id': '107410',
    'title': 'Arma 3' }][{
    'id': '2519060',
    'title': 'Enshrouded' }][{
    'id': '1361210',
    'title': 'Warhammer 40,000: Darktide' }][{
    'id': '552500',
    'title': 'Warhammer: Vermintide 2' }][{
    'id': '1092790',
    'title': 'Inscryption' }][{
    'id': '322170',
    'title': 'Geometry Dash' }][{
    'id': '203160',
    'title': 'Tomb Raider' }][{
    'id': '391220',
    'title': 'Rise of the Tomb Raider' }][{
    'id': '750920',
    'title': 'Shadow of the Tomb Raider' }][{
    'id': '2054970',
    'title': "Dragon's Dogma 2" }][{
    'id': '368370',
    'title': 'Her Story' }][{
    'id': '319630',
    'title': 'Life is Strange' }][{
    'id': '1627720',
    'title': 'Lies of P' }][{
    'id': '1229490',
    'title': 'ULTRAKILL' }][{
    'id': '218620',
    'title': 'PAYDAY 2' }][{
    'id': '1272080',
    'title': 'PAYDAY 3' }][{
    'id': '431730',
    'title': 'The Walking Dead' }][{
    'id': '261030',
    'title': 'The Walking Dead: Season Two' }][{
    'id': '204360',
    'title': 'Castle Crashers' }][{
    'id': '1046930',
    'title': 'Dota Underlords' }][{
    'id': '582660',
    'title': 'Black Desert' }][{
    'id': '306130',
    'title': 'The Elder Scrolls Online' }][{
    'id': '444200',
    'title': 'World of Tanks Blitz' }][{
    'id': '1599340',
    'title': 'Lost Ark' }][{
    'id': '2420510',
    'title': 'HoloCure' }][{
    'id': '286690',
    'title': 'Metro 2033 Redux' }][{
    'id': '287390',
    'title': 'Metro: Last Light Redux' }][{
    'id': '412020',
    'title': 'Metro Exodus' }][{
    'id': '333930',
    'title': 'Dirty Bomb' }][{
    'id': '222480',
    'title': 'Resident Evil Revelations' }][{
    'id': '287290',
    'title': 'Resident Evil Revelations 2' }][{
    'id': '209650',
    'title': 'Call of Duty: Advanced Warfare' }][{
    'id': '202970',
    'title': 'Call of Duty: Black Ops II' }][{
    'id': '311210',
    'title': 'Call of Duty: Black Ops III' }][{
    'id': '240',
    'title': 'Counter-Strike: Source' }][{
    'id': '10',
    'title': 'Counter-Strike' }][{
    'id': '400',
    'title': 'Portal' }][{
    'id': '620',
    'title': 'Portal 2' }][{
    'id': '12210',
    'title': 'Grand Theft Auto IV' }][{
    'id': '12120',
    'title': 'Grand Theft Auto: San Andreas' }][{
    'id': '1510',
    'title': 'Uplink' }][{
    'id': '220200',
    'title': 'Kerbal Space Program' }][{
    'id': '248820',
    'title': 'Risk of Rain' }][{
    'id': '221380',
    'title': 'Age of Empires II (2013)' }][{
    'id': '813780',
    'title': 'Age of Empires II: Definitive Edition' }][{
    'id': '1017900',
    'title': 'Age of Empires: Definitive Edition' }][{
    'id': '1466860',
    'title': 'Age of Empires IV' }][{
    'id': '39210',
    'title': 'FINAL FANTASY XIV Online' }][{
    'id': '1533420',
    'title': 'Monkey Island' }][{
    'id': '1659040',
    'title': 'Return to Monkey Island' }][{
    'id': '323190',
    'title': 'Frostpunk' }][{
    'id': '1363080',
    'title': 'Manor Lords' }][{
    'id': '1811990',
    'title': 'Helldivers' }][{
    'id': '356190',
    'title': 'Middle-earth: Shadow of War' }][{
    'id': '241930',
    'title': 'Middle-earth: Shadow of Mordor' }][{
    'id': '219990',
    'title': 'Grim Dawn' }][{
    'id': '200710',
    'title': 'Torchlight II' }][{
    'id': '238960',
    'title': 'Path of Exile' }][{
    'id': '1139900',
    'title': 'Ghostrunner' }][{
    'id': '1229490',
    'title': 'Ultrakill' }][{
    'id': '42700',
    'title': 'Call of Duty: Black Ops' }][{
    'id': '10180',
    'title': 'Call of Duty: Modern Warfare 2' }][{
    'id': '7940',
    'title': 'Call of Duty 4: Modern Warfare' }][{
    'id': '340',
    'title': 'Half-Life 2: Lost Coast' }][{
    'id': '380',
    'title': 'Half-Life 2: Episode One' }][{
    'id': '420',
    'title': 'Half-Life 2: Episode Two' }][{
    'id': '401920',
    'title': 'Warhammer 40,000: Eternal Crusade' }][{
    'id': '364360',
    'title': 'Total War: WARHAMMER' }][{
    'id': '214950',
    'title': 'Total War: ROME II - Emperor Edition' }][{
    'id': '71210',
    'title': 'Sonic Adventure 2' }][{
    'id': '71340',
    'title': 'Sonic Generations' }][{
    'id': '584400',
    'title': 'Sonic Mania' }][{
    'id': '1237320',
    'title': 'Sonic Frontiers' }][{
    'id': '208650',
    'title': 'Batman: Arkham Knight' }][{
    'id': '209000',
    'title': 'Batman: Arkham Origins' }][{
    'id': '200260',
    'title': 'Batman: Arkham City' }][{
    'id': '35140',
    'title': 'Batman: Arkham Asylum' }][{
    'id': '265590',
    'title': 'The Dark Pictures Anthology: Man of Medan' }][{
    'id': '1194630',
    'title': 'The Dark Pictures Anthology: Little Hope' }][{
    'id': '1281590',
    'title': 'The Dark Pictures Anthology: House of Ashes' }][{
    'id': '1567020',
    'title': 'The Dark Pictures Anthology: The Devil in Me' }][{
    'id': '1290000',
    'title': 'The Quarry' }][{
    'id': '212680',
    'title': 'FTL: Faster Than Light' }][{
    'id': '246620',
    'title': 'Plague Inc: Evolved' }][{
    'id': '606150',
    'title': 'Moonlighter' }][{
    'id': '501300',
    'title': 'What Remains of Edith Finch' }][{
    'id': '417290',
    'title': 'Mortal Kombat XL' }][{
    'id': '307780',
    'title': 'Mortal Kombat X' }][{
    'id': '976310',
    'title': 'Mortal Kombat 11' }][{
    'id': '4574',
    'title': 'Medal of Honor' }][{
    'id': '47790',
    'title': 'Medal of Honor: Airborne' }][{
    'id': '202170',
    'title': 'Sleeping Dogs: Definitive Edition' }][{
    'id': '429660',
    'title': 'Tales of Berseria' }][{
    'id': '740130',
    'title': 'Tales of Arise' }][{
    'id': '379720',
    'title': 'DOOM' }][{
    'id': '782330',
    'title': 'DOOM Eternal' }][{
    'id': '2280',
    'title': 'Ultimate Doom' }][{
    'id': '208200',
    'title': 'Doom 3' }][{
    'id': '1172620',
    'title': 'Sea of Thieves' }][{
    'id': '1172640',
    'title': 'Grounded' }][{
    'id': '1172370',
    'title': 'Halo: The Master Chief Collection' }][{
    'id': '1240440',
    'title': 'Halo Infinite' }][{
    'id': '950',
    'title': 'Spyro' }]

def load_catalog():
    global CATALOG_DATA
    pass
# WARNING: Decompyle incomplete


def fetch_steam_metadata(appid):
    
    try:
        url = f'''https://store.steampowered.com/api/appdetails?appids={appid}'''
        r = requests.get(url, 1.5, **('timeout',))
        data = r.json()
        if data or str(appid) in data or data[str(appid)]['success']:
            game_data = da