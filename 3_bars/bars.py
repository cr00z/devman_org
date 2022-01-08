import json
import math
import argparse
import functools


def load_data(filepath):
    try:
        with open(filepath, encoding='utf-8') as json_file_object:
            return json.load(json_file_object)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return None


def get_bar_seats_count(bar):
    return bar['properties']['Attributes']['SeatsCount']


def get_bar_name(bar):
    return bar['properties']['Attributes']['Name']


def get_biggest_bar(bars_list):
    return max(bars_list, key=get_bar_seats_count)


def get_smallest_bar(bars_list):
    return min(bars_list, key=get_bar_seats_count)


def get_distance(latitude, longitude, bar):
    bar_coord = bar['geometry']['coordinates']
    longitude_delta = bar_coord[0] - longitude
    latitude_delta = bar_coord[1] - latitude
    return math.hypot(longitude_delta, latitude_delta)


def get_closest_bar(bars_list, latitude, longitude):
    calc_distance = functools.partial(get_distance, latitude, longitude)
    return min(bars_list, key=calc_distance)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Simple Moscow bars search')
    parser.add_argument('json_filename', metavar='json_filename', type=str,
                        help='JSON database filename')
    args = parser.parse_args()

    moscow_bars = load_data(args.json_filename)
    if moscow_bars is None:
        exit('Input file not found or not a JSON')
    moscow_bars = moscow_bars['features']

    print('Biggest bar: {}'.format(get_bar_name(get_biggest_bar(moscow_bars))))
    print('Smallest bar: {}'.format(get_bar_name(get_smallest_bar(moscow_bars))))
    try:
        # NB! in Russia we use latitude first
        user_latitude = float(input('Input your latitude: '))
        user_longitude = float(input('Input your longitude: '))
    except ValueError:
        exit('Coordinates must be digital')
    closest_bar = get_closest_bar(moscow_bars, user_latitude, user_longitude)
    print('Closest bar: {}'.format(get_bar_name(closest_bar)))
