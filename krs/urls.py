# krs/urls.py
from django.urls import path
from .views import (
    HomePageView,
    AboutPageView,
    AufgabenPageView,
    ZehnerraumPageView,
    ZwanzigerraumPageView,
    HunderterraumPageView,
    TausenderraumPageView,
    Kleines1x1PageView,
    Groszes1x1PageView,
    Plus_im_10erPageView,
    Plus_im_10er_checkPageView,
)


urlpatterns = [
    path('zwanzigerraum/', ZwanzigerraumPageView.as_view(), name='zwanzigerraum'),  # noqa
    path('zehnerraum/', ZehnerraumPageView.as_view(), name='zehnerraum'),  # noqa
    path('tausenderraum/', TausenderraumPageView.as_view(), name='tausenderraum'),  # noqa
    path('plus_im_10er/', Plus_im_10erPageView.as_view(), name='plus_im_10er'),  # noqa
    path('plus_im_10er_check/', Plus_im_10er_checkPageView.as_view(), name='plus_im_10er_check'),  # noqa
    path('kleines1x1/', Kleines1x1PageView.as_view(), name='kleines1x1'),  # noqa
    path('hunderterraum/', HunderterraumPageView.as_view(), name='hunderterraum'),  # noqa
    path('großes1x1/', Groszes1x1PageView.as_view(), name='großes1x1'),  # noqa
    path('aufgaben/', AufgabenPageView.as_view(), name='aufgaben'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('', HomePageView.as_view(), name='home'),
]
