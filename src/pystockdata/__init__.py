#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" pystockdata

 Copyright 2019 Christoph Dieck

 Use of this source code is governed by a GNU General Public License v3 or later that can be
 found in the LICENSE file.
"""
import os

import yaml


class PyStockData:

    def __init__(self):
        self.__stocks = None
        yaml_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data', 'stocks.yaml')
        with open(yaml_path) as stocks:
            self.__stocks = yaml.safe_load(stocks)

    def get_all_indices(self):
        """
        Returns all available indices
        :return: list of index names
        """
        return self.__get_sub_items('indices')

    def get_all_industries(self):
        """
        Returns all available industries
        :return: list of industries
        """
        return self.__get_sub_items('industries')

    def get_all_countries(self):
        """
        Returns all available countries
        :return: list of country names
        """
        return list(set([stock['country'] for stock in self.__stocks['companies']]))

    def get_stocks_by_index(self, index):
        """
        Returns a list with stocks who belongs to given index.
        :param index: name of index
        :return: list of stocks
        """
        return self.__get_items('indices', index)

    def get_stocks_by_industry(self, industry):
        """
        Returns a list with stocks who belongs to given index.
        :param industry: name of index
        :return: list of stocks
        """
        return self.__get_items('industries', industry)

    def get_stocks_by_country(self, country):
        """
        Returns a list with stocks who belongs to given country.
        :param country: name of country
        :return: list of stocks
        """
        return [stock for stock in self.__stocks['companies'] if stock['country'].lower() == country.lower()]

    def __get_items(self, key, search):
        stocks = []
        if self.__stocks:
            stocks = [stock for stock in self.__stocks['companies']
                      for my_item in stock[key] if search.lower() == my_item.lower()]
        return stocks

    def __get_sub_items(self, key):
        sub_items = []
        if self.__stocks:
            sub_items = list(set([item for stock in self.__stocks['companies'] for item in stock[key]]))
        return sub_items
