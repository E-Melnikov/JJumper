import webbrowser
try:
    from Tkinter import *
    import urllib2, json
    instance = 'python2'
except:
    from tkinter import *
    import urllib.request
    instance = 'python3'
from platform import system as platform
from os import system
import json
from threading import Thread

############### APP CONFIGURATION #########################
# Put here list of your current projects
projects = ['CHAT', 'WSM', 'EE', 'ADI']

# Project that will bw open if letters index is not specified
default_project = 'EE'

buttons_font = 'Verdana 12'
buttons_font_status = 'Verdana 11'
input_font = 'Verdana 18'

# Values: True or False
destroy_app_in_the_end = True # True or False

###########################################################

app_version = "2.0"


def send_bi_python_3(arg):
    token_value = arg
    BI_URL = 'https://evgeniyme.wixsite.com/assistan-bi/_functions/bi/jjumper/{}/{}'.format(app_version, token_value)
    urllib.request.urlopen(BI_URL)


def send_bi_python_2(arg):
    token_value = arg
    BI_URL = 'https://evgeniyme.wixsite.com/assistan-bi/_functions/bi/jjumper/{}/{}'.format(app_version, token_value)
    req = urllib2.Request(BI_URL)
    urllib2.urlopen(req)

try:
    from uuid import getnode as get_mac
    mac = get_mac()
    print(mac)
    token_value = '{}'.format(mac)
    if instance == 'python2':
        thread = Thread(target=send_bi_python_2, args=(token_value,))
        thread.start()
    elif instance == 'python3':
        thread = Thread(target=send_bi_python_3, args=(token_value,))
        thread.start()
except:
    pass

current_jira_project = None

tasks = {
    '1': 'Bug',
    '3': 'Task',
    '2': 'New Feature',
    '4': 'Improvement',
}


if len(tasks) >= len(projects):
    columnspan_value = len(tasks)
else:
    columnspan_value = len(projects)

# if platform() == 'Darwin':
#     chrome_path = chrome_path_macos
# elif platform() == 'Windows':
#     chrome_path = chrome_path_windows


def on_key_release(event):
    ctrl = (event.state & 0x4) != 0
    if event.keycode == 88 and ctrl and event.keysym.lower() != "x":
        event.widget.event_generate("<<Cut>>")
    if event.keycode == 86 and ctrl and event.keysym.lower() != "v":
        event.widget.event_generate("<<Paste>>")
    if event.keycode == 67 and ctrl and event.keysym.lower() != "c":
        event.widget.event_generate("<<Copy>>")


if len(projects) == 1:
    width_value = 15
else:
    width_value = 13

root = Tk()
root.title("JJumper " + app_version)
entry_text = StringVar()


def key(event):
    print("pressed", repr(event.char))
    print('help')


def auto_uppercase(*arg):
    current_entry = entry_text.get()
    print('UPDATE', current_entry)

    if (current_entry
        and current_entry[-1].isdigit()
        and not '-' in current_entry
        and len(current_entry) > 1
        and not current_entry[-2].isdigit()):
        new_line = []
        for letter in current_entry:
            if not letter.isdigit():
                entry_text.set(current_entry.upper())
            if letter.isdigit() and not current_entry[-1] == '-':
                new_line.append('-')
                new_line.append(letter)
                entry.insert(len(entry_text.get()) - 1, '-')
        entry_text.set(entry_text.get().upper())
    else:
        entry_text.set(current_entry.upper())


def func(event):
    print(entry.get())
    open_jira(entry.get())


root.bind('<Return>', func)
root.bind_all("<Key>", on_key_release, "+")
frame = Frame(root)
root.resizable(0,0)
frame.grid()


def new_jira_task(issue_type):
    entry_text_value = entry.get()

    if entry_text_value:
        pid = get_pid(entry_text_value)
    else:
        pid = get_pid(default_project)
    if not pid:
        pid = 'PROJECT_ID_NOT_FOUND'
        entry_text.set('Project key "{}" not fond'.format(entry_text_value))
    else:
        pid = pid[0]
    URL = 'https://jira.wixpress.com/CreateIssueDetails!init.jspa?pid={pid}&issuetype={issue_type}&summary='. \
        format(issue_type=issue_type, pid=pid)
    webbrowser.open_new_tab(URL)
    if destroy_app_in_the_end:
        root.destroy()


def open_jira(value, project_name_=default_project):
    global current_jira_project
    base_URL = "https://jira.wixpress.com/browse/"
    print('value is ', repr(value), repr(project_name_))

    if value.isdigit():
        URL = base_URL + "{}-".format(project_name_) + value

    elif not value and project_name_:
        init_tasks_status()
        current_jira_project = project_name_
        entry_text.set(current_jira_project)
        return True

    elif not '-' in value and not current_jira_project:
        init_tasks_status()
        current_jira_project = entry.get()
        entry_text.set(current_jira_project)
        return True

    elif current_jira_project and not '-' in value:
        entry_text.set(project_name_)
        current_jira_project = entry_text.get()
        return True

    else:
        URL = base_URL + value

    webbrowser.open_new_tab(URL)
    if destroy_app_in_the_end:
        root.destroy()


def retrieve_input(project_name):
    entry_value = entry.get()
    open_jira(entry.get(), project_name)


def get_pid(project_name):
    pids = [{'key': 'PHOT', 'pid': 15500}, {'key': 'WMO', 'pid': 13500}, {'key': 'IPTF', 'pid': 14512},
     {'key': 'ACM', 'pid': 16404}, {'key': 'ACQOPS', 'pid': 14905}, {'key': 'ABS', 'pid': 12903},
     {'key': 'ADI', 'pid': 18501}, {'key': 'AQS', 'pid': 16900}, {'key': 'ALI', 'pid': 18902},
     {'key': 'ANATOLTEST', 'pid': 20009}, {'key': 'AN', 'pid': 14000}, {'key': 'AM', 'pid': 19914},
     {'key': 'ATW', 'pid': 14600}, {'key': 'AB', 'pid': 20616}, {'key': 'APLT', 'pid': 16023},
     {'key': 'ASS', 'pid': 18102}, {'key': 'ASST', 'pid': 18500}, {'key': 'APPSAUT', 'pid': 10600},
     {'key': 'APT', 'pid': 17108}, {'key': 'AFG', 'pid': 16503}, {'key': 'AFG2', 'pid': 18100},
     {'key': 'GTA', 'pid': 16401}, {'key': 'ACID', 'pid': 16607}, {'key': 'AUTODEV', 'pid': 10400},
     {'key': 'AUTOINF', 'pid': 14301}, {'key': 'AT', 'pid': 14522}, {'key': 'CRMA', 'pid': 20610},
     {'key': 'AWSM', 'pid': 14915}, {'key': 'BAGT', 'pid': 16608}, {'key': 'BAV', 'pid': 19006},
     {'key': 'BEP', 'pid': 14804}, {'key': 'BEA', 'pid': 12200}, {'key': 'BKNG', 'pid': 15601},
     {'key': 'BAGINF', 'pid': 16406}, {'key': 'BIAS', 'pid': 14415}, {'key': 'BATB', 'pid': 13108},
     {'key': 'WBB', 'pid': 13400}, {'key': 'BCT', 'pid': 14101}, {'key': 'BIF', 'pid': 19004},
     {'key': 'BIM', 'pid': 18003}, {'key': 'BIRM', 'pid': 14402}, {'key': 'BISCH', 'pid': 16408},
     {'key': 'BSA', 'pid': 14504}, {'key': 'BPS', 'pid': 13001}, {'key': 'BILAUTO', 'pid': 11005},
     {'key': 'SBS', 'pid': 16707}, {'key': 'BOLT', 'pid': 18400}, {'key': 'BONG', 'pid': 14703},
     {'key': 'BUF', 'pid': 19003}, {'key': 'BOOK', 'pid': 16403}, {'key': 'BOOKS', 'pid': 13008},
     {'key': 'BST', 'pid': 14913}, {'key': 'BS', 'pid': 16103}, {'key': 'BTM', 'pid': 12702},
     {'key': 'CTE', 'pid': 14617}, {'key': 'ARR', 'pid': 14607}, {'key': 'CHAL', 'pid': 20619},
     {'key': 'CHAT', 'pid': 17200}, {'key': 'CI', 'pid': 12004}, {'key': 'CIT', 'pid': 13109},
     {'key': 'CLC', 'pid': 13301}, {'key': 'APE', 'pid': 12902}, {'key': 'CINF', 'pid': 13201},
     {'key': 'CT', 'pid': 13002}, {'key': 'CLOUD', 'pid': 14505}, {'key': 'CO', 'pid': 12901},
     {'key': 'COOP', 'pid': 13700}, {'key': 'COL', 'pid': 19913}, {'key': 'COMTASK', 'pid': 14416},
     {'key': 'CMP', 'pid': 20201}, {'key': 'COMP', 'pid': 13000}, {'key': 'CNCT', 'pid': 12203},
     {'key': 'CE', 'pid': 11500}, {'key': 'CON', 'pid': 14516}, {'key': 'CSF', 'pid': 17107},
     {'key': 'COR3CI', 'pid': 16007}, {'key': 'CRVD', 'pid': 20006}, {'key': 'CDT', 'pid': 20002},
     {'key': 'CRZY', 'pid': 16022}, {'key': 'COM', 'pid': 14908}, {'key': 'CRMM', 'pid': 14910},
     {'key': 'CRMQA', 'pid': 20618}, {'key': 'SM', 'pid': 14909}, {'key': 'CSTR', 'pid': 17110},
     {'key': 'AST', 'pid': 14515}, {'key': 'CSTPA', 'pid': 20103}, {'key': 'CSB', 'pid': 14914},
     {'key': 'CWTST1', 'pid': 15800}, {'key': 'CWTSTKNBN', 'pid': 15802}, {'key': 'CWTSTSCRUM', 'pid': 15801},
     {'key': 'CWTSTX', 'pid': 14802}, {'key': 'CXBA', 'pid': 14601}, {'key': 'CPR', 'pid': 18305},
     {'key': 'CYREBROTST', 'pid': 20100}, {'key': 'DOP', 'pid': 18703}, {'key': 'DAE', 'pid': 17505},
     {'key': 'SMS', 'pid': 14704}, {'key': 'DAN', 'pid': 19915}, {'key': 'DC', 'pid': 12900},
     {'key': 'DICT', 'pid': 20300}, {'key': 'DSP', 'pid': 16711}, {'key': 'DSC', 'pid': 16500},
     {'key': 'DS', 'pid': 19400}, {'key': 'DB', 'pid': 12600}, {'key': 'DBS', 'pid': 16802},
     {'key': 'DEM', 'pid': 18001}, {'key': 'DEMO', 'pid': 10000}, {'key': 'CHF', 'pid': 12401},
     {'key': 'DEPM', 'pid': 14509}, {'key': 'DSM', 'pid': 20615}, {'key': 'DTNMY', 'pid': 16407},
     {'key': 'DEV', 'pid': 19904}, {'key': 'DIF', 'pid': 19909}, {'key': 'TRCR', 'pid': 17702},
     {'key': 'DM', 'pid': 19902}, {'key': 'DSS', 'pid': 15503}, {'key': 'GZ', 'pid': 20102},
     {'key': 'DSTUA', 'pid': 15700}, {'key': 'ECOMAUT', 'pid': 10602}, {'key': 'ESM', 'pid': 13403},
     {'key': 'EAP', 'pid': 20802}, {'key': 'EBR', 'pid': 13005}, {'key': 'EA', 'pid': 16107},
     {'key': 'ECL', 'pid': 20004}, {'key': 'EFT', 'pid': 11702}, {'key': 'EK', 'pid': 20104},
     {'key': 'EMP', 'pid': 19010}, {'key': 'EDRLS', 'pid': 20200}, {'key': 'EP', 'pid': 20301},
     {'key': 'EDIX', 'pid': 19903}, {'key': 'ELIWOW', 'pid': 17507}, {'key': 'BMA', 'pid': 16002},
     {'key': 'FM', 'pid': 13105}, {'key': 'FF', 'pid': 17301}, {'key': 'NGG', 'pid': 14507},
     {'key': 'FEDINF', 'pid': 16702}, {'key': 'FDC', 'pid': 12703}, {'key': 'FLASH', 'pid': 20501},
     {'key': 'FSM', 'pid': 16506}, {'key': 'FRM', 'pid': 14901}, {'key': 'INF', 'pid': 14614},
     {'key': 'GDPR', 'pid': 17302}, {'key': 'GFDB', 'pid': 14615}, {'key': 'GITHUB', 'pid': 16400},
     {'key': 'GROUP', 'pid': 18200}, {'key': 'BN', 'pid': 12501}, {'key': 'HAL', 'pid': 15300},
     {'key': 'HAPI', 'pid': 14003}, {'key': 'HRDB', 'pid': 19202}, {'key': 'HCS', 'pid': 13600},
     {'key': 'HEA', 'pid': 10704}, {'key': 'WOH', 'pid': 10100}, {'key': 'HSR', 'pid': 10001},
     {'key': 'HTMLSRVR', 'pid': 10700}, {'key': 'HDC', 'pid': 14801}, {'key': 'ICU', 'pid': 14800},
     {'key': 'IDENT', 'pid': 17003}, {'key': 'IM', 'pid': 20012}, {'key': 'INC', 'pid': 16507},
     {'key': 'INST', 'pid': 14904}, {'key': 'IPP', 'pid': 13503}, {'key': 'ISI', 'pid': 20612},
     {'key': 'SYSDEV', 'pid': 12500}, {'key': 'INV', 'pid': 14911}, {'key': 'IWIX', 'pid': 14618},
     {'key': 'GTOJ', 'pid': 10301}, {'key': 'JIR', 'pid': 14403}, {'key': 'JSAUTO', 'pid': 14409},
     {'key': 'KB', 'pid': 14514}, {'key': 'LGL', 'pid': 19912}, {'key': 'LIF', 'pid': 12003},
     {'key': 'LIFNG', 'pid': 14525}, {'key': 'TRNS', 'pid': 12700}, {'key': 'MT', 'pid': 19101},
     {'key': 'MKT', 'pid': 14517}, {'key': 'MKTBI', 'pid': 14616}, {'key': 'MD', 'pid': 16710},
     {'key': 'MRND', 'pid': 15201}, {'key': 'MAR', 'pid': 16402}, {'key': 'MST', 'pid': 19801},
     {'key': 'MCS', 'pid': 16712}, {'key': 'MCLOUD', 'pid': 12101}, {'key': 'MDN', 'pid': 20014},
     {'key': 'MH', 'pid': 19600}, {'key': 'MMGR', 'pid': 16700}, {'key': 'MP', 'pid': 18900},
     {'key': 'MDST', 'pid': 17601}, {'key': 'MBA', 'pid': 19011}, {'key': 'MA', 'pid': 19800},
     {'key': 'MS', 'pid': 10701}, {'key': 'MFBUFWTW', 'pid': 19200}, {'key': 'MOB', 'pid': 11200},
     {'key': 'WMG', 'pid': 16013}, {'key': 'MVM', 'pid': 20605}, {'key': 'MONEY', 'pid': 19201},
     {'key': 'RECON', 'pid': 18000}, {'key': 'MON', 'pid': 12503}, {'key': 'ML', 'pid': 16600},
     {'key': 'CRM', 'pid': 14526}, {'key': 'NE', 'pid': 16004}, {'key': 'NED', 'pid': 17102},
     {'key': 'NWB', 'pid': 16804}, {'key': 'WCD2', 'pid': 18702}, {'key': 'NODEINF', 'pid': 14603},
     {'key': 'NRD', 'pid': 20801}, {'key': 'NTT', 'pid': 20106}, {'key': 'OB', 'pid': 13501},
     {'key': 'WOAGR', 'pid': 20624}, {'key': 'WOAINFRA', 'pid': 17803}, {'key': 'WOAMRE', 'pid': 20623},
     {'key': 'WOARNN', 'pid': 20621}, {'key': 'WOAPFM', 'pid': 20611}, {'key': 'WOAUILIB', 'pid': 20622},
     {'key': 'OAV', 'pid': 18203}, {'key': 'MAM', 'pid': 20601}, {'key': 'OP', 'pid': 18101},
     {'key': 'OSL', 'pid': 16300}, {'key': 'OCCP', 'pid': 19005}, {'key': 'OPSHR', 'pid': 18304},
     {'key': 'OPSUA', 'pid': 20607}, {'key': 'OR', 'pid': 16000}, {'key': 'OTT', 'pid': 18701},
     {'key': 'OUT', 'pid': 19301}, {'key': 'PPL', 'pid': 17600}, {'key': 'PAY', 'pid': 20013},
     {'key': 'PCI', 'pid': 16713}, {'key': 'EX', 'pid': 12300}, {'key': 'PII', 'pid': 20604},
     {'key': 'POD', 'pid': 17501}, {'key': 'POST', 'pid': 19901}, {'key': 'PREM', 'pid': 16803},
     {'key': 'BIL', 'pid': 10900}, {'key': 'PSI', 'pid': 16808}, {'key': 'PG', 'pid': 14702},
     {'key': 'PIA', 'pid': 19907}, {'key': 'PROD', 'pid': 14907}, {'key': 'POT', 'pid': 15900},
     {'key': 'PP', 'pid': 16024}, {'key': 'ITP', 'pid': 15001}, {'key': 'PD', 'pid': 19701},
     {'key': 'PMC', 'pid': 16701}, {'key': 'PUS', 'pid': 15202}, {'key': 'QAH', 'pid': 18306},
     {'key': 'QUARK', 'pid': 18303}, {'key': 'QUIX', 'pid': 14605}, {'key': 'QUIXS', 'pid': 16200},
     {'key': 'RT', 'pid': 20400}, {'key': 'RGP', 'pid': 12100}, {'key': 'REJ', 'pid': 16901},
     {'key': 'ITRO', 'pid': 15501}, {'key': 'IS', 'pid': 16800}, {'key': 'RST', 'pid': 14400},
     {'key': 'RE', 'pid': 14906}, {'key': 'RICH', 'pid': 20902}, {'key': 'RF', 'pid': 16801},
     {'key': 'ROAD', 'pid': 19900}, {'key': 'RR', 'pid': 15000}, {'key': 'SKPA', 'pid': 18002},
     {'key': 'SKPB', 'pid': 18700}, {'key': 'SKPC', 'pid': 19908}, {'key': 'SKPD', 'pid': 20011},
     {'key': 'SAS', 'pid': 14523}, {'key': 'CLNT', 'pid': 13701}, {'key': 'SE', 'pid': 14406},
     {'key': 'SEA', 'pid': 14501}, {'key': 'SCA2', 'pid': 16510}, {'key': 'SCHED', 'pid': 13402},
     {'key': 'SDK', 'pid': 14414}, {'key': 'SER', 'pid': 19503}, {'key': 'SECDEV', 'pid': 20904},
     {'key': 'WIXSEC', 'pid': 16604}, {'key': 'SSM', 'pid': 16021}, {'key': 'SF', 'pid': 13003},
     {'key': 'SGB', 'pid': 11700}, {'key': 'SFBT', 'pid': 14508}, {'key': 'SFTT', 'pid': 13104},
     {'key': 'SHTOUT', 'pid': 13006}, {'key': 'SMA', 'pid': 11300}, {'key': 'STC', 'pid': 10800},
     {'key': 'SKUN', 'pid': 19000}, {'key': 'SCRM', 'pid': 14700}, {'key': 'ST', 'pid': 12400},
     {'key': 'STT', 'pid': 17701}, {'key': 'SG', 'pid': 16206}, {'key': 'STYL', 'pid': 19906},
     {'key': 'SUPQA', 'pid': 13200}, {'key': 'OMG', 'pid': 12502}, {'key': 'SNP', 'pid': 20901},
     {'key': 'HOSH', 'pid': 16409}, {'key': 'STGT', 'pid': 19501}, {'key': 'STP', 'pid': 20101},
     {'key': 'STMX', 'pid': 20903}, {'key': 'SYSIT', 'pid': 16026}, {'key': 'TM', 'pid': 13004},
     {'key': 'TMPLT', 'pid': 13106}, {'key': 'TEST', 'pid': 12002}, {'key': 'TBP', 'pid': 17304},
     {'key': 'TO', 'pid': 19905}, {'key': 'TB', 'pid': 20617}, {'key': 'TFQA', 'pid': 16504},
     {'key': 'TODO', 'pid': 20003}, {'key': 'TAQT', 'pid': 10302}, {'key': 'TSC', 'pid': 12504},
     {'key': 'TPAAUT', 'pid': 10401}, {'key': 'USOPS', 'pid': 16806}, {'key': 'SFCRM', 'pid': 13300},
     {'key': 'AF', 'pid': 17800}, {'key': 'USEO', 'pid': 12204}, {'key': 'USITE', 'pid': 16011},
     {'key': 'UEX', 'pid': 11100}, {'key': 'VPC', 'pid': 20620}, {'key': 'VI', 'pid': 17502},
     {'key': 'VP', 'pid': 16705}, {'key': 'PLAT', 'pid': 20000}, {'key': 'LAYOUT', 'pid': 20614},
     {'key': 'VSRV', 'pid': 18600}, {'key': 'VOM', 'pid': 17002}, {'key': 'VN', 'pid': 20500},
     {'key': 'VIS', 'pid': 17506}, {'key': 'VMAF', 'pid': 17900}, {'key': 'VOD', 'pid': 16102},
     {'key': 'W33D', 'pid': 18704}, {'key': 'WA11Y', 'pid': 19100}, {'key': 'WA', 'pid': 13302},
     {'key': 'WAMKT', 'pid': 20900}, {'key': 'WAM', 'pid': 17602}, {'key': 'WAA', 'pid': 20613},
     {'key': 'AR', 'pid': 16207}, {'key': 'AUDIO', 'pid': 20302}, {'key': 'WBHP', 'pid': 12800},
     {'key': 'WBT', 'pid': 12505}, {'key': 'WBTD', 'pid': 12205}, {'key': 'WBA', 'pid': 14612},
     {'key': 'WCC', 'pid': 14002}, {'key': 'WCSH', 'pid': 14518}, {'key': 'WCN', 'pid': 16010},
     {'key': 'WCCM', 'pid': 14912}, {'key': 'WCDS', 'pid': 14705}, {'key': 'WCSTS', 'pid': 17504},
     {'key': 'WCS', 'pid': 14620}, {'key': 'WCT', 'pid': 17111}, {'key': 'WCR', 'pid': 20700},
     {'key': 'DLR', 'pid': 14613}, {'key': 'WEED', 'pid': 16105}, {'key': 'ES', 'pid': 16003},
     {'key': 'EVNTS', 'pid': 14608}, {'key': 'WE', 'pid': 17400}, {'key': 'WHTL', 'pid': 13007},
     {'key': 'WHD', 'pid': 13114}, {'key': 'WKBM', 'pid': 15101}, {'key': 'WLB', 'pid': 17001},
     {'key': 'WLT', 'pid': 16708}, {'key': 'MUS', 'pid': 16205}, {'key': 'WMSC', 'pid': 14619},
     {'key': 'WOA', 'pid': 14707}, {'key': 'WP', 'pid': 19008}, {'key': 'WP2', 'pid': 18204},
     {'key': 'WPA', 'pid': 14701}, {'key': 'WQ', 'pid': 16601}, {'key': 'REST', 'pid': 14401},
     {'key': 'WS', 'pid': 17802}, {'key': 'WSS', 'pid': 16703}, {'key': 'WSCS', 'pid': 18302},
     {'key': 'WIT', 'pid': 14524}, {'key': 'WTS', 'pid': 14521}, {'key': 'WUO', 'pid': 16511},
     {'key': 'WUIP', 'pid': 19504}, {'key': 'WV', 'pid': 15401}, {'key': 'WVM', 'pid': 16203},
     {'key': 'WIXVOICE', 'pid': 14404}, {'key': 'WEB', 'pid': 14610}, {'key': 'WIXAPPS', 'pid': 10500},
     {'key': 'BLOG', 'pid': 11900}, {'key': 'WCD', 'pid': 14611}, {'key': 'USERS', 'pid': 10901},
     {'key': 'WLR', 'pid': 11400}, {'key': 'PROM', 'pid': 15400}, {'key': 'WAD', 'pid': 20105},
     {'key': 'WIXB', 'pid': 16016}, {'key': 'WD', 'pid': 16807}, {'key': 'WIXER', 'pid': 14602},
     {'key': 'WIXLABS', 'pid': 11800}, {'key': 'LABSASAL', 'pid': 17704}, {'key': 'LABSCO', 'pid': 17705},
     {'key': 'WIXMP', 'pid': 16204}, {'key': 'WOS', 'pid': 14530}, {'key': 'WOS2', 'pid': 16106},
     {'key': 'WOS3', 'pid': 16509}, {'key': 'WPCS', 'pid': 17401}, {'key': 'WPL', 'pid': 14606},
     {'key': 'EE', 'pid': 13404}, {'key': 'WSM', 'pid': 16501}, {'key': 'SLT', 'pid': 18300},
     {'key': 'CRMWF', 'pid': 20010}, {'key': 'ZWA', 'pid': 20008}]
    return [project['pid'] for project in pids if project['key'] == project_name]
    pass


def init_tasks_status():
    index = 0
    for key in tasks:
        Button(root, text=tasks[key], font=buttons_font_status, width=width_value, height=2, padx=1, pady=1, bg='#404040',
               activebackground="yellow", borderwidth=2, overrelief="solid",
               fg="#b3b300", command=lambda task_id=key:
            new_jira_task(task_id)).grid(row=2, column=index, sticky='ew')
        index += 1
        print(index)



entry = Entry(root, width=14, font=input_font, textvariable=entry_text)
entry.focus_set()
entry.grid(row=0, column=0, sticky='ew', columnspan=columnspan_value)

index = 0
for project_name in projects:
    print(project_name)

    Button(root, text=project_name, font=buttons_font, width=width_value, height=1, padx=1, pady=1, bg='#404040',
           activebackground="yellow", borderwidth=2, overrelief="solid",
           fg="#b3b300", command=lambda current_project=project_name:
        retrieve_input(current_project)).grid(row=1, column=index, sticky='ew')
    index += 1

root.call('wm', 'attributes', '.', '-topmost', '1')

entry_text.trace("w", auto_uppercase)

if platform() == 'Darwin':
    system('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "Python" to true' ''')

root.mainloop()
