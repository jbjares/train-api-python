from testcontainers.core.generic import GenericContainer
from pht.station import StationClient
import requests
import time

# Environment variables that need to be set for the test container
# "PHT_DATA_STORAGE_FILENAME"
# "PHT_DATA_STORAGE_NAME"
PORT = 5000
STATION_NAME = "station"
station_container_name = "lukaszimmermann/pht-test-data-storage-service:latest"
station_container = GenericContainer(station_container_name)\
    .with_exposed_ports(PORT)\
    .with_env('PHT_DATA_STORAGE_FILENAME', 'processed.cleveland.data')\
    .with_env("PHT_DATA_STORAGE_NAME", STATION_NAME)


def test_station_client_1():
    with station_container as station:
        time.sleep(2)
        host = station.get_container_host_ip()
        port = station.get_exposed_port(PORT)
        client = StationClient(host + ':' + port)
        assert client.request_name() == STATION_NAME
