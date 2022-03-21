#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

class Translation(object):
    
    START_TEXT = """<b>ഹേയ് {} 😛 

വെറുതെ start കുത്തി കളിക്കരുത്. സിനിമയുടെ ലിങ്ക് ആണ് വേണ്ടതെങ്കിൽ <a href='https://t.me/+F6wJqZhDRTkxOTA1'>ഈ ഗ്രൂപ്പിൽ</a> സിനിമയുടെ പേര് ടൈപ്പ് ചെയ്യ്, അപ്പോൽ ഞാൻ ലിങ്ക് തരാം എന്നിട്ട് ഇവിടെ വന്ന് start കൊടുക്കണം😜
ഇനി ഇനേക്കൊണ്ട് വീണ്ടും വീണ്ടും പറയിപ്പിക്കരുത്. 🤷‍♂</b>

<i>താഴെ കാണുന്ന രണ്ട് ചാനലുകളിലും ജോയിൻ ചെയ്യാൻ മറക്കരുതേ...🦧</i>"""    
    
    HELP_TEXT = """
<b>സിനിമയുടെ ലിങ്ക് ആണ് വേണ്ടതെങ്കിൽ <a href='https://t.me/Pushpa_Minnal_murali_2021'>ഈ ഗ്രൂപ്പിൽ</a> സിനിമയുടെ പേര് ടൈപ്പ് ചെയ്യ്, അപ്പോൽ ഞാൻ ലിങ്ക് തരാം എന്നിട്ട് ഇവിടെ വന്ന് start കൊടുക്കണം😜
ഇനി ഇനേക്കൊണ്ട് വീണ്ടും വീണ്ടും പറയിപ്പിക്കരുത്. 🤷‍♂</b>
"""
    
    ABOUT_TEXT = """<b>You know, I'm always different🙄🙄</b>
"""

    MOVIES = """https://t.me/+4R49xhZWINphMjdl"""

    SERIES = """https://t.me/joinchat/WQNEfDIqGDpkYzcx"""

    GROUP = """https://t.me/+F6wJqZhDRTkxOTA1"""

    SHARE = """https://t.me/share/url?url=%E0%B4%AA%E0%B5%81%E0%B4%A4%E0%B4%BF%E0%B4%AF%20%E0%B4%B8%E0%B4%BF%E0%B4%A8%E0%B4%BF%E0%B4%AE%E0%B4%95%E0%B5%BE%20%E0%B4%9F%E0%B5%86%E0%B4%B2%E0%B4%97%E0%B5%8D%E0%B4%B0%E0%B4%BE%E0%B4%82%20%E0%B4%87%E0%B4%B1%E0%B4%99%E0%B5%8D%E0%B4%99%E0%B5%81%E0%B4%AE%E0%B5%8D%E0%B4%AA%E0%B5%8B%E0%B5%BE%20%E0%B4%A4%E0%B4%A8%E0%B5%8D%E0%B4%A8%E0%B5%86%20%E0%B4%A8%E0%B5%8B%E0%B4%9F%E0%B5%8D%E0%B4%9F%E0%B4%BF%E0%B4%AB%E0%B4%BF%E0%B4%95%E0%B5%8D%E0%B4%95%E0%B5%87%E0%B4%B7%E0%B5%BB%20%E0%B4%B2%E0%B4%AD%E0%B4%BF%E0%B4%95%E0%B5%8D%E0%B4%95%E0%B5%81%E0%B4%B5%E0%B4%BE%E0%B5%BB%20%E0%B4%A4%E0%B4%BE%E0%B4%B4%E0%B5%86%20%E0%B4%95%E0%B4%BE%E0%B4%A3%E0%B5%81%E0%B4%A8%E0%B5%8D%E0%B4%A8%20%E0%B4%9A%E0%B4%BE%E0%B4%A8%E0%B4%B2%E0%B4%BF%E0%B5%BD%20%E0%B4%9C%E0%B5%8B%E0%B4%AF%E0%B4%BF%E0%B5%BB%20%E0%B4%9A%E0%B5%86%E0%B4%AF%E0%B5%8D%E0%B4%AF%E0%B5%81%E0%B4%95%20%F0%9F%A5%B3%0A%E2%9C%85%20https%3A%2F%2Ft.me%2F%2B4R49xhZWINphMjdl%0A%0A%E0%B4%B8%E0%B4%BF%E0%B4%A8%E0%B4%BF%E0%B4%AE%20%E0%B4%8F%E0%B4%A4%E0%B5%81%E0%B4%AE%E0%B4%BE%E0%B4%AF%E0%B4%BF%E0%B4%95%E0%B5%8D%E0%B4%95%E0%B5%8B%E0%B4%9F%E0%B5%8D%E0%B4%9F%E0%B5%86%F0%9F%A4%B7%E2%80%8D%E2%99%82.%20%E0%B4%AA%E0%B5%87%E0%B4%B0%E0%B5%8D%20%E0%B4%85%E0%B4%9F%E0%B4%BF%E0%B4%9A%E0%B5%8D%E0%B4%9A%E0%B4%BE%E0%B5%BD%20%E0%B4%85%E0%B4%AA%E0%B5%8D%E0%B4%AA%E0%B5%8B%E0%B5%BE%E0%B4%A4%E0%B4%A8%E0%B5%8D%E0%B4%A8%E0%B5%86%20%E0%B4%B2%E0%B4%BF%E0%B4%99%E0%B5%8D%E0%B4%95%E0%B5%8D%20%E0%B4%B2%E0%B4%AD%E0%B4%BF%E0%B4%95%E0%B5%8D%E0%B4%95%E0%B5%81%E0%B4%A8%E0%B5%8D%E0%B4%A8%20Group%F0%9F%98%8D%F0%9F%98%8D%0A%E2%9C%85%20https%3A%2F%2Ft.me%2F%2BF6wJqZhDRTkxOTA1"""

    IID = """-1001630133749"""
    START_LOG = """🟢 <b>Mallu Movies Bot 
 
Name    : {mention} 
User Id : </b><pre>{id}</pre> 
<b>Username: {username}</b>"""
    FILE_LOG = """🗂 <b>Mallu Movies Bot 
 
Name    : {mention} 
User Id : </b><pre>{id}</pre> 
<b>Username: {username}</b>"""
