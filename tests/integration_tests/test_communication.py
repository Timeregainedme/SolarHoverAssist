import unittest
from src.communication.mqtt_handler import on_connect, on_message
from src.communication.grpc_manager import CommandService

class TestCommunication(unittest.TestCase):
    def test_mqtt_connection(self):
        client_mock = type('MockClient', (), {"subscribe": lambda x: None})
        on_connect(client_mock, None, None, 0)
        print("MQTT connection test passed.")

    def test_grpc_service(self):
        service = CommandService()
        response = service.SendCommand(request=type('MockRequest', (), {"command": "TEST"}), context=None)
        self.assertEqual(response.status, "ACK")
        print("gRPC service test passed.")

if __name__ == "__main__":
    unittest.main()
