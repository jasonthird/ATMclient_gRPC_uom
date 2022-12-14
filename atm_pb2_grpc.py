# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import atm_pb2 as atm__pb2


class AtmStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Authenticate = channel.unary_unary(
            '/Atm/Authenticate',
            request_serializer=atm__pb2.AuthenticateRequest.SerializeToString,
            response_deserializer=atm__pb2.AuthenticateResponse.FromString,
        )
        self.Withdraw = channel.unary_unary(
            '/Atm/Withdraw',
            request_serializer=atm__pb2.WithdrawRequest.SerializeToString,
            response_deserializer=atm__pb2.WithdrawReply.FromString,
        )
        self.Deposit = channel.unary_unary(
            '/Atm/Deposit',
            request_serializer=atm__pb2.DepositRequest.SerializeToString,
            response_deserializer=atm__pb2.DepositReply.FromString,
        )
        self.Balance = channel.unary_unary(
            '/Atm/Balance',
            request_serializer=atm__pb2.BalanceRequest.SerializeToString,
            response_deserializer=atm__pb2.BalanceReply.FromString,
        )


class AtmServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Authenticate(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Withdraw(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Deposit(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Balance(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AtmServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'Authenticate': grpc.unary_unary_rpc_method_handler(
            servicer.Authenticate,
            request_deserializer=atm__pb2.AuthenticateRequest.FromString,
            response_serializer=atm__pb2.AuthenticateResponse.SerializeToString,
        ),
        'Withdraw': grpc.unary_unary_rpc_method_handler(
            servicer.Withdraw,
            request_deserializer=atm__pb2.WithdrawRequest.FromString,
            response_serializer=atm__pb2.WithdrawReply.SerializeToString,
        ),
        'Deposit': grpc.unary_unary_rpc_method_handler(
            servicer.Deposit,
            request_deserializer=atm__pb2.DepositRequest.FromString,
            response_serializer=atm__pb2.DepositReply.SerializeToString,
        ),
        'Balance': grpc.unary_unary_rpc_method_handler(
            servicer.Balance,
            request_deserializer=atm__pb2.BalanceRequest.FromString,
            response_serializer=atm__pb2.BalanceReply.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'Atm', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class Atm(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Authenticate(request,
                     target,
                     options=(),
                     channel_credentials=None,
                     call_credentials=None,
                     insecure=False,
                     compression=None,
                     wait_for_ready=None,
                     timeout=None,
                     metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Atm/Authenticate',
                                             atm__pb2.AuthenticateRequest.SerializeToString,
                                             atm__pb2.AuthenticateResponse.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Withdraw(request,
                 target,
                 options=(),
                 channel_credentials=None,
                 call_credentials=None,
                 insecure=False,
                 compression=None,
                 wait_for_ready=None,
                 timeout=None,
                 metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Atm/Withdraw',
                                             atm__pb2.WithdrawRequest.SerializeToString,
                                             atm__pb2.WithdrawReply.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Deposit(request,
                target,
                options=(),
                channel_credentials=None,
                call_credentials=None,
                insecure=False,
                compression=None,
                wait_for_ready=None,
                timeout=None,
                metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Atm/Deposit',
                                             atm__pb2.DepositRequest.SerializeToString,
                                             atm__pb2.DepositReply.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Balance(request,
                target,
                options=(),
                channel_credentials=None,
                call_credentials=None,
                insecure=False,
                compression=None,
                wait_for_ready=None,
                timeout=None,
                metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Atm/Balance',
                                             atm__pb2.BalanceRequest.SerializeToString,
                                             atm__pb2.BalanceReply.FromString,
                                             options, channel_credentials,
                                             insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
