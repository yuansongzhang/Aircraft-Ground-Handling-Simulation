# -*- coding: utf-8 -*-
import os
import json
import datetime
import pandas as pd

OUTPUT_PATH = "output"


def get_current_time():
    return datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')


def export_log(events_info_list, trips_info_list, aircraft_info_list, current_time=None):
    current_time = get_current_time() if current_time is None else current_time
    path = os.path.join(OUTPUT_PATH, current_time)
    if not os.path.exists(path):
        os.makedirs(path)
    filename = os.path.join(path, f"events.json")
    with open(filename, 'w') as f:
        json.dump(events_info_list, f)
    print(filename)
    filename = os.path.join(path, f"trips.json")
    with open(filename, 'w') as f:
        json.dump(trips_info_list, f)
    print(filename)
    filename = os.path.join(path, f"flights.json")
    with open(filename, 'w') as f:
        json.dump(aircraft_info_list, f)
    print(filename)
    export_csv_log(events_info_list, trips_info_list, aircraft_info_list, current_time)


def export_csv_log(events_info_list, trips_info_list, aircraft_info_list, current_time=None):
    current_time = get_current_time() if current_time is None else current_time
    path = os.path.join(OUTPUT_PATH, current_time)
    if not os.path.exists(path):
        os.makedirs(path)

    event_df_dict = {}
    for item in events_info_list:
        if item['event_name'] not in event_df_dict:
            event_df_dict[item['event_name']] = [item]
        else:
            event_df_dict[item['event_name']].append(item)
    for event_name in event_df_dict.keys():
        event_df = pd.DataFrame(event_df_dict[event_name])
        filename = os.path.join(path, f"{event_name}.csv")
        event_df.to_csv(filename, index=False)
    df = pd.DataFrame(trips_info_list)
    filename = os.path.join(path, 'VehicleTrips.csv')
    df.to_csv(filename, index=False)
    df = pd.DataFrame(aircraft_info_list)
    filename = os.path.join(path, 'Flights.csv')
    df.to_csv(filename, index=False)


if __name__ == '__main__':
    print(get_current_time())
