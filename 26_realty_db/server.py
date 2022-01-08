from flask import render_template, request, url_for
from sqlalchemy import and_
from init import app, Advertisement
import math
import datetime


def get_num_of_pages():
    adverts_num = Advertisement.query.count()
    return math.ceil(adverts_num / app.config['ADVERTS_PER_PAGE'])


def get_filters(params):
    filters = []
    if params['oblast_district']:
        filters.append(Advertisement.oblast_district == params['oblast_district'])
    if params['min_price']:
        filters.append(Advertisement.price >= params['min_price'])
    if params['max_price']:
        filters.append(Advertisement.price <= params['max_price'])
    if params['new_building']:
        new_build_year = datetime.datetime.now().year - app.config['NEW_BUILD_AGE_LIMIT']
        filters.append(Advertisement.construction_year >= new_build_year)
    return filters


def get_url_for(params_dict, page_num):
    return url_for('ads_list', **{**params_dict, 'page': page_num})


def get_pages_num(adverts_num):
    return math.ceil(adverts_num / app.config['ADVERTS_PER_PAGE'])


def get_page_links(params_dict, pages_num):
    if pages_num < 2:
        return None
    return [get_url_for(params_dict, page_num) for page_num in range(1, pages_num + 1)]


@app.route('/')
def ads_list():
    params_list = [
        'oblast_district',
        'min_price',
        'max_price',
        'new_building'
    ]
    params_dict = {param: request.args.get(param) for param in params_list}
    active_page = request.args.get('page', 1, type=int)
    query = Advertisement.query.filter(and_(*get_filters(params_dict)))
    pagination = query.paginate(active_page, app.config['ADVERTS_PER_PAGE'], False)
    prev_page = get_url_for(params_dict, active_page - 1)
    next_page = get_url_for(params_dict, active_page + 1)
    return render_template(
        'ads_list.html',
        ads=pagination.items,
        params=params_dict,
        pages={
            'active_page': active_page,
            'links': get_page_links(params_dict, get_pages_num(query.count())),
            'prev_page': prev_page if pagination.has_prev else None,
            'next_page': next_page if pagination.has_next else None
        }
    )


if __name__ == "__main__":
    app.run()
