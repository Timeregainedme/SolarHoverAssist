% Energy Efficiency Analysis for UAV
clear; clc;

% Parameters
battery_capacity = 5000; % mAh
voltage = 11.1; % Volts
power_consumption = 150; % Watts
flight_time = 20; % Minutes

% Energy calculations
energy_used = (power_consumption * flight_time) / 60; % in Watt-hours
remaining_capacity = battery_capacity * voltage / 1000 - energy_used;

% Plot
figure;
x = [1, 2];
y = [battery_capacity * voltage / 1000, remaining_capacity];
bar(x, y, 'FaceColor', 'b');
set(gca, 'XTickLabel', {'Initial Capacity', 'Remaining Capacity'});
ylabel('Energy (Watt-hours)');
title('Energy Efficiency Analysis');
