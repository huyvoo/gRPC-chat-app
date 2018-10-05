# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import message_pb2 as message__pb2


class ChatServerStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.ReceiveMsg = channel.unary_stream(
        '/ChatServer/ReceiveMsg',
        request_serializer=message__pb2.Message.SerializeToString,
        response_deserializer=message__pb2.Message.FromString,
        )
    self.SendNote = channel.unary_unary(
        '/ChatServer/SendNote',
        request_serializer=message__pb2.Message.SerializeToString,
        response_deserializer=message__pb2.Empty.FromString,
        )


class ChatServerServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def ReceiveMsg(self, request, context):
    """This bi-directional stream makes it possible to send and receive Notes between 2 persons
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SendNote(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ChatServerServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'ReceiveMsg': grpc.unary_stream_rpc_method_handler(
          servicer.ReceiveMsg,
          request_deserializer=message__pb2.Message.FromString,
          response_serializer=message__pb2.Message.SerializeToString,
      ),
      'SendNote': grpc.unary_unary_rpc_method_handler(
          servicer.SendNote,
          request_deserializer=message__pb2.Message.FromString,
          response_serializer=message__pb2.Empty.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'ChatServer', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
