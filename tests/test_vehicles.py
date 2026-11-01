from pathlib import Path

import pytest

from summary.vehicles import Trip, group_by_vehicle, split_resources

SAMPLE = Path(__file__).parent / "fixtures" / "vehicles_sample.csv"


def test_vehicles_are_in_alphabetical_order():
    grouped = group_by_vehicle(SAMPLE.read_bytes())
    assert list(grouped) == ["AAA0001", "BBB0002"]


def test_trip_takes_departure_arrival_and_address_from_their_columns():
    grouped = group_by_vehicle(SAMPLE.read_bytes())
    assert grouped["AAA0001"][1] == Trip(
        departure="01/01/2026 08:00",
        arrival="03/01/2026 09:00",
        address="RUA TESTE UM, Nº 1 - BAIRRO TESTE",
    )


def test_call_with_two_resources_appears_for_both():
    grouped = group_by_vehicle(SAMPLE.read_bytes())
    shared = "RUA TESTE DOIS, Nº 2 - BAIRRO TESTE"
    assert shared in [trip.address for trip in grouped["AAA0001"]]
    assert shared in [trip.address for trip in grouped["BBB0002"]]


def test_call_without_resource_is_ignored():
    grouped = group_by_vehicle(SAMPLE.read_bytes())
    addresses = [trip.address for trips in grouped.values() for trip in trips]
    assert not any("TRES" in address for address in addresses)


def test_vehicles_of_other_units_are_not_listed():
    grouped = group_by_vehicle(SAMPLE.read_bytes())
    addresses = [trip.address for trips in grouped.values() for trip in trips]
    assert "CCC0003" not in grouped
    assert not any("OUTRA UNIDADE" in address for address in addresses)


def test_unit_filter_ignores_letter_case():
    grouped = group_by_vehicle(SAMPLE.read_bytes())
    assert "RUA TESTE QUATRO, Nº 4 - BAIRRO TESTE" in [
        trip.address for trip in grouped["BBB0002"]
    ]


def test_trips_are_sorted_by_departure_time():
    grouped = group_by_vehicle(SAMPLE.read_bytes())
    assert [trip.departure for trip in grouped["AAA0001"]] == [
        "01/01/2026 06:30",
        "01/01/2026 08:00",
    ]


def test_missing_column_raises_key_error():
    with pytest.raises(KeyError):
        group_by_vehicle("Natureza\r\nP00001 - TESTE\r\n".encode("cp1252"))


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        ("", []),
        ("UR1", ["UR1"]),
        ("UR1 / BM2", ["UR1", "BM2"]),
        ("UR1 / UR1", ["UR1"]),
        (" UR1 /  / BM2 ", ["UR1", "BM2"]),
    ],
)
def test_split_resources(value, expected):
    assert split_resources(value) == expected
