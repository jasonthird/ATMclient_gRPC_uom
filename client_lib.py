from decimal import Decimal, getcontext

import grpc

import atm_pb2
import atm_pb2_grpc

getcontext().prec = 23


class BadRequest(Exception):
    def __init__(self, message):
        self.message = message

        super().__init__(self.message)

    def __str__(self):
        return self.message


class AtmClient:
    def __init__(self, username, pin, host, port):
        self.username = str(username)
        self.pin = int(pin)
        self.AuthCode = None
        self.host = host
        self.port = port
        self.channel = None
        self.stub = None

    def connect(self):
        self.channel = grpc.insecure_channel(f"{self.host}:{self.port}")
        self.stub = atm_pb2_grpc.AtmStub(self.channel)

    def authenticate(self):
        try:
            response = self.stub.Authenticate(atm_pb2.AuthenticateRequest(username=self.username, pin=self.pin))
            if response.success:
                self.AuthCode = response.AuthCode
                return "Authenticated"
            else:
                return response.error
        except Exception as e:
            print(e)
            return "Error with request"

        self.AuthCode = str(response.AuthCode)

    def getBalance(self) -> Decimal:
        try:
            response = self.stub.Balance(atm_pb2.BalanceRequest(AuthCode=self.AuthCode))
            if response.success:
                return Decimal((Decimal(response.units) / Decimal(response.denomination)))
            else:
                return response.error
        except Exception as e:
            return "Error with request"

    def withdraw(self, amount: Decimal):
        try:
            amount = Decimal(amount)
            amount: tuple[int, int] = amount.as_integer_ratio()
            response = self.stub.Withdraw(
                atm_pb2.WithdrawRequest(AuthCode=self.AuthCode, units=(amount[0]), denomination=amount[1]))
            if not response.success:
                return response.error
            else:
                return "Withdrawn"
        except Exception as e:
            return "Error with request"

    def deposit(self, amount: Decimal):
        try:
            amount = Decimal(amount)
            amount: tuple[int, int] = amount.as_integer_ratio()
            response = self.stub.Deposit(
                atm_pb2.DepositRequest(AuthCode=self.AuthCode, units=(amount[0]), denomination=amount[1]))
            if not response.success:
                return response.error
            else:
                return "Deposited"
        except Exception as e:
            return "Error with request"

    def close(self):
        self.channel.close()
