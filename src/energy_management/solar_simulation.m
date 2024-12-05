% Solar Energy Simulation
battery_capacity = 5000; % mAh
solar_efficiency = 0.85;
load = 800; % Power demand in Watts

if load > battery_capacity * solar_efficiency
    disp('Warning: Insufficient energy!');
else
    disp(['Energy allocated: ', num2str(load), ' Watts.']);
end
