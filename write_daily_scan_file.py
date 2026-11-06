"""Generate the daily scan file"""

elevation_angle = 5
azimuth_step = 15

with open(f"VAD_scan_{elevation_angle}deg.txt", "w") as file:
    rows = (
        f"{azimuth:03d}.000{elevation_angle:03d}.000"
        for azimuth in range(0, 360, azimuth_step)
    )
    file.write("\r\n".join(rows))

print(f"VAD_scan_{elevation_angle}deg.txt file created successfully!")