from concurrent import futures
import grpc
import communication_pb2
import communication_pb2_grpc

class CommandService(communication_pb2_grpc.CommandServicer):
    def SendCommand(self, request, context):
        print(f"Received: {request.command}")
        return communication_pb2.Response(status="ACK")

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
communication_pb2_grpc.add_CommandServicer_to_server(CommandService(), server)
server.add_insecure_port('[::]:50051')
server.start()
server.wait_for_termination()
