import asyncio

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from decimal import *
from kivy.config import Config
from client_lib import AtmClient


getcontext().prec = 23
Config.set('input', 'mouse', 'mouse,multitouch_on_demand')  # disable the right click red dot

host = "localhost"
port = 50051
grpcClient = None


def popupError(String):
    app = App.get_running_app()
    popuperror = Popup(title='Error', content=Label(text=String), size_hint=(None, None),
                       size=(app.root.width / 2, app.root.height / 2))
    popuperror.open()


class AuthPage(Screen):
    def __init__(self, **kwargs):
        super(AuthPage, self).__init__(**kwargs)

    def auth(self, name, pin):
        global grpcClient
        try:
            if pin == "" or name == "":
                popupError("Please fill in all fields")
            elif not pin.isdigit():
                popupError("Pin must be a number")
            else:
                grpcClient = AtmClient(str(name), int(pin), host, port)
                grpcClient.connect()
                authResponce = grpcClient.authenticate()
                if authResponce == "Authenticated":
                    self.manager.current = 'choose'
                    self.manager.get_screen('choose').updateBalance()
                else:
                    popupError(authResponce)

        except Exception as e:
            print(e)
            popupError("Server is offline")


class ChoosePage(Screen):
    def updateBalance(self):
        try:
            balance = grpcClient.getBalance()
            if balance == "Error with request":
                popupError("Error with request")
            else:
                money = round(balance, 2)
                self.ids.balance.text = str(money)
        except Exception as e:
            print(e)
            popupError("Server is offline")

    def withdraw(self):
        # change to withdraw page and pass authcode
        self.manager.current = 'withdraw'

    def deposit(self):
        self.manager.current = 'deposit'


class WithdrawPage(Screen):
    def withdraw(self, value):
        try:
            if value == "":
                popupError("Please fill in the value field")
            else:
                value = Decimal(value)
                withdrawResponce = grpcClient.withdraw(value)
                if withdrawResponce!="Withdrawn":
                    popupError(withdrawResponce)
                else:
                    self.manager.current = 'choose'
                    self.manager.get_screen('choose').updateBalance()
        except Exception as e:
            print(e)
            popupError("Server is offline")

    def back(self):
        self.manager.current = 'choose'
        self.manager.get_screen('choose').updateBalance()


class DepositPage(Screen):
    def deposit(self, value):
        try:
            if value == "":
                popupError("Please fill in the value field")
            else:
                depositResponce = grpcClient.deposit(Decimal(value))
                if depositResponce!="Deposited":
                    popupError(depositResponce)
                else:
                    self.manager.current = 'choose'
                    self.manager.get_screen('choose').updateBalance()
        except Exception as e:
            print(e)
            popupError("Server is offline")

    def back(self):
        self.manager.current = 'choose'
        self.manager.get_screen('choose').updateBalance()


class AtmApp(App):
    def build(self):
        sm = ScreenManager()
        screen1 = AuthPage()
        screen2 = ChoosePage()
        screen3 = WithdrawPage()
        screen4 = DepositPage()
        sm.add_widget(screen1)
        sm.add_widget(screen2)
        sm.add_widget(screen3)
        sm.add_widget(screen4)
        return sm


if __name__ == '__main__':

    # get server ip from terminal argument
    import sys

    if len(sys.argv) > 1:
        host = sys.argv[1]
    if len(sys.argv) > 2:
        port = sys.argv[2]

    AtmApp().run()
