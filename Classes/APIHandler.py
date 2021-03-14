from typing import Dict
from Classes.Account import Account
import requests


class APIHandler:
    def __init__(self, isPaper: bool = True) -> None:
        self.__account__ = Account(isPaper)
        self.__endpoints__ = ("account", 'account/configurations', 'account/activities', 'account/portfolio/history', 'orders', 'positions',
                              'assets', 'watchlists', 'calendar', 'clock')
        self.__session__ = requests.session()
        self.__headers__ = {'APCA-API-KEY-ID': self.__account__.GetId(),
                            'APCA-API-SECRET-KEY': self.__account__.GetSecret()}

    def __MakeGetRequest__(self, endPoint: str) -> Dict:
        response = self.__session__.get(
            f'{self.__account__.GetURL()}{endPoint}', headers=self.__headers__)
        return response.json()

    def GetAccountInformation(self) -> Dict:
        return self.__MakeGetRequest__(self.__endpoints__[0])

    def GetAccountConfigurationsInformation(self) -> Dict:
        return self.__MakeGetRequest__(self.__endpoints__[1])

    def GetAccountActivitiesInformation(self) -> Dict:
        return self.__MakeGetRequest__(self.__endpoints__[2])

    def GetAccountPortfolioHistoryInformation(self) -> Dict:
        return self.__MakeGetRequest__(self.__endpoints__[3])

    def GetOrdersInformation(self) -> Dict:
        return self.__MakeGetRequest__(self.__endpoints__[4])

    def GetPositionsInformation(self) -> Dict:
        return self.__MakeGetRequest__(self.__endpoints__[5])

    def GetAssetsInformation(self) -> Dict:
        return self.__MakeGetRequest__(self.__endpoints__[6])

    def GetWatchlistsInformation(self) -> Dict:
        return self.__MakeGetRequest__(self.__endpoints__[7])

    def GetCalendarInformation(self) -> Dict:
        return self.__MakeGetRequest__(self.__endpoints__[8])

    def GetClockInformation(self) -> Dict:
        return self.__MakeGetRequest__(self.__endpoints__[9])
