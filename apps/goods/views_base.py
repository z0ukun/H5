# coding=utf-8
__author__ = 'bobby'

from goods.models import Goods
from django.views.generic.base import View


# from django.views.generic import ListView


# class GoodsListView(View):
#     def get(selfself, request):
#         """
#         通过django的view实现商品列表页
#         :param request:
#         :return:
#         """
#
#         json_list = []
#         goods = Goods.objects.all()[:10]
#         for good in goods:
#             json_dict = {}
