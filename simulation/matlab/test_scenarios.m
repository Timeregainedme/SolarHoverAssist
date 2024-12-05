% Test Scenarios for UAV Performance
clear; clc;

% Parameters
load_weights = [0, 1, 2, 3, 4]; % in kilograms
flight_times = [25, 22, 18, 15, 10]; % in minutes

% Plot performance
figure;
plot(load_weights, flight_times, '-o', 'LineWidth', 2, 'MarkerSize', 8);
xlabel('Load Weight (kg)');
ylabel('Flight Time (minutes)');
title('UAV Flight Time vs. Load Weight');
grid on;

% Display scenario analysis
for i = 1:length(load_weights)
    fprintf('Load: %d kg -> Flight Time: %d minutes\n', load_weights(i), flight_times(i));
end
