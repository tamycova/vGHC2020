import csv
from datetime import datetime
from json import load
from collections import defaultdict


def join_event_speaker(events, speakers):
    for event in events:
        events[event]['speakers_info'] = defaultdict(list)
        for speaker in events[event]["speakerIds"]:
            speaker_id = str(speaker)
            events[event]['speakers_info']['speakers_name'].append(
                speakers[speaker_id]['lastName'] + speakers[speaker_id]['firstName'])
            events[event]['speakers_info']['speakers_company'].append(
                speakers[speaker_id]['company'])
            events[event]['speakers_info']['speakers_title'].append(
                speakers[speaker_id]['title'])
            events[event]['speakers_info']['speakers_biography'].append(
                speakers[speaker_id]['biography'])
        events[event]['n_speakers'] = len(events[event]["speakerIds"])


def group_by_days(events):
    output = defaultdict(list)
    for event in events.values():
        start = event['date']['start_date']
        end = event['date']['end_date']
        if start != end:
            output['multiday'].append(event)
        else:
            output[start].append(event)
    return output


def output_csv(day, sessions):
    output = []
    sessions.sort(key=lambda x: datetime.strptime(
        x['date']["start_ET"], '%I:%M %p'))
    for x in sessions:
        base = []
        if day == 'multiday':
            base = [x["date"]["start_date"], x["date"]["end_date"]]
        base.extend([x["date"]["start_ET"], x["date"]["end_ET"], x['n_speakers'], x['name'], x['description'], x['type'], x['categories'], x['speakers_info']['speakers_name'], x['speakers_info']['speakers_company'], x['speakers_info']['speakers_title'], x['speakers_info']['speakers_biography']])
        output.append(base)
    with open("./csv/{}.csv".format(day), "w") as f:
        writer = csv.writer(f)
        writer.writerows(output)


EVENTS_PATH = "./raw_data/events.json"
SPEAKERS_PATH = "./raw_data/speakers.json"
DAYS = []

with open(EVENTS_PATH, "r") as f:
    events = load(f)
with open(SPEAKERS_PATH, "r") as f:
    speakers = load(f)

join_event_speaker(events, speakers)
grouped = group_by_days(events)

for day, sessions in grouped.items():
    day = day.replace("/", '-')
    output_csv(day, sessions)
