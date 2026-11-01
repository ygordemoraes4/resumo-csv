from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime

from summary.csv_reader import read_rows

RESOURCES_COLUMN = "Recursos empenhados"
CREATED_COLUMN = "Data/hora de criação"
CURRENT_STATUS_COLUMN = "Data/hora da situação atual"
LOCATION_COLUMN = "Local do fato"
RESOURCE_SEPARATOR = "/"
DATETIME_FORMAT = "%d/%m/%Y %H:%M"


@dataclass(frozen=True)
class Trip:
    departure: str
    arrival: str
    address: str


def split_resources(value: str) -> list[str]:
    parts = (part.strip() for part in value.split(RESOURCE_SEPARATOR))
    return list(dict.fromkeys(part for part in parts if part))


def departure_time(trip: Trip) -> datetime:
    return datetime.strptime(trip.departure, DATETIME_FORMAT)


def group_by_vehicle(content: bytes) -> dict[str, list[Trip]]:
    trips: dict[str, list[Trip]] = defaultdict(list)
    for row in read_rows(content):
        trip = Trip(
            departure=row[CREATED_COLUMN],
            arrival=row[CURRENT_STATUS_COLUMN],
            address=row[LOCATION_COLUMN],
        )
        for vehicle in split_resources(row[RESOURCES_COLUMN]):
            trips[vehicle].append(trip)
    return {
        vehicle: sorted(vehicle_trips, key=departure_time)
        for vehicle, vehicle_trips in sorted(trips.items())
    }
