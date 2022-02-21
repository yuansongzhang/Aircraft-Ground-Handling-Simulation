# -*- coding: utf-8 -*-
from description import Flight, GatePosition
from aircraft import Aircraft
from vehicle import Vehicle

import pandas as pd


def generate_instances(filename):
    df = pd.read_csv(filename)

    gate_position_dict = {}
    aircraft_list = []

    virtual_gate_position = GatePosition('Virtual', 0, 'virtual')
    for gate_position_id in df['gate_position'].unique():
        gate_position = GatePosition('PD', 0, str(gate_position_id))
        gate_position_dict[str(gate_position_id)] = gate_position

    for row_id, row in df.iterrows():
        if row['flight_type'] == 'A':
            flight = Flight(category=0,  # Arrival
                            scheduled_departure_time=None,
                            scheduled_arrival_time=row['scheduled_timestamp'],
                            origin=virtual_gate_position,
                            destination=gate_position_dict[str(row['gate_position'])],
                            )
        else:
            flight = Flight(category=1,  # Departure
                            scheduled_departure_time=row['scheduled_timestamp'],
                            scheduled_arrival_time=None,
                            origin=gate_position_dict[str(row['gate_position'])],
                            destination=virtual_gate_position,
                            )
        aircraft = Aircraft(aircraft_id=row['flight_id'], flight=flight, arrival_delay=row['delay_time'])
        aircraft_list.append(aircraft)

    vehicle_list = []
    depot_gate_position = GatePosition('PD', 0, 'depot')
    for i in range(10):
        veh = Vehicle(depot_gate_position, i)
        vehicle_list.append(veh)

    return gate_position_dict, aircraft_list, vehicle_list
