import argparse
import json
from init import Advertisement, db


def get_cmdline_args():
    parser = argparse.ArgumentParser(description='Script for advert upload')
    parser.add_argument('json_filename', metavar='json_filename', type=str,
                        help='JSON filename')
    return parser.parse_args()


def load_data(filepath):
    try:
        with open(filepath, encoding='utf-8') as json_file_obj:
            return json.load(json_file_obj)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        return None


def exists_advert(advert):
    return Advertisement.query.filter(Advertisement.id == advert['id']).count()


def update_advert(advert):
    return Advertisement.query.filter(
        Advertisement.id == advert['id']
    ).update(advert)


def insert_advert(advert):
    db.session.add(Advertisement().from_dict(advert))


if __name__ == '__main__':
    args = get_cmdline_args()
    loaded_adverts = load_data(args.json_filename)
    if loaded_adverts is None:
        exit('Input file not found or not a JSON')
    archived_adverts_num = Advertisement.query.update({'active': False})
    print("Advertisements in base (old): {}".format(archived_adverts_num))
    print("Advertisements loaded: {}".format(len(loaded_adverts)))
    inserted_adverts_num = 0
    for loaded_advert in loaded_adverts:
        loaded_advert['active'] = True
        if exists_advert(loaded_advert):
            update_advert(loaded_advert)
            archived_adverts_num -= 1
        else:
            insert_advert(loaded_advert)
            inserted_adverts_num += 1
    db.session.commit()
    print("Advertisements archived: {}".format(archived_adverts_num))
    print("Advertisements added: {}".format(inserted_adverts_num))
