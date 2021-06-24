# krs/urls.py
from django.urls import path
from .views import (
    HomePageView,
    AboutPageView,
    AufgabenPageView,
    TenSpacePageView,
    ZwanzigerraumPageView,
    HunderterraumPageView,
    TausenderraumPageView,
    Kleines1x1PageView,
    Groszes1x1PageView,
    Plus_in_10spacePageView,
    Minus_in_10spacePageView,
    Plus_in_10space_checkPageView,
    Minus_in_10space_checkPageView,
)


urlpatterns = [
    path('zwanzigerraum/', ZwanzigerraumPageView.as_view(), name='zwanzigerraum'),  # noqa
    path('ten_space/', TenSpacePageView.as_view(), name='ten_space'),  # noqa
    path('tausenderraum/', TausenderraumPageView.as_view(), name='tausenderraum'),  # noqa
    path('plus_in_10space/', Plus_in_10spacePageView.as_view(), name='plus_in_10space'),  # noqa
    path('minus_in_10space/', Minus_in_10spacePageView.as_view(), name='minus_in_10space'),  # noqa
    path('plus_in_10space_check/', Plus_in_10space_checkPageView.as_view(), name='plus_in_10space_check'),  # noqa
    path('minus_in_10space_check/', Minus_in_10space_checkPageView.as_view(), name='minus_in_10space_check'),  # noqa
    path('kleines1x1/', Kleines1x1PageView.as_view(), name='kleines1x1'),  # noqa
    path('hunderterraum/', HunderterraumPageView.as_view(), name='hunderterraum'),  # noqa
    path('großes1x1/', Groszes1x1PageView.as_view(), name='großes1x1'),  # noqa
    path('aufgaben/', AufgabenPageView.as_view(), name='aufgaben'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home'),
]
