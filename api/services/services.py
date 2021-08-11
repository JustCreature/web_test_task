from ..models import Site
import requests
from django_filters import rest_framework as filters


def get_status(url) -> bool:
    """
    Checks the status of given site
    :param url: url to check
    :return: Bool status
    """
    try:
        res_status_code = requests.get(url).status_code
    except requests.exceptions.SSLError:
        res_status_code = 400

    return res_status_code == 200

def update_statuses():
    """
    Updates statuses for each web site in the database
    """
    sites = Site.objects.all()

    for site in sites:
        try:
            res_status_code = requests.get(site.url).status_code
        except requests.exceptions.SSLError:
            res_status_code = 400

        print(res_status_code)

        if res_status_code == 200:
            site.status = True
        else:
            site.status = False

        site.save()

class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass

class SiteFilter(filters.FilterSet):
    """
    Filter and its settings
    """
    name = CharFilterInFilter(field_name='name', lookup_expr='in')
    status = filters.BooleanFilter()

    class Meta:
        model = Site
        fields = ['name', 'status']
