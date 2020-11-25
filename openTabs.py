import json, webbrowser

with open('pastTabs.json') as json_file:
    data = json.load(json_file)
    for p in data['pastTabs']:
        webbrowser.open(p)