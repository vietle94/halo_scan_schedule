# Halo scan schedule

Scripts for creating daily scan definition files and a 24-hour scan schedule.


## Create a daily scan file

Edit the configuration at the top of [`write_daily_scan_file.py`](./write_daily_scan_file.py):

```python
elevation_angle = 5
azimuth_step = 15
```

Then run:

```bash
python write_daily_scan_file.py
```

This creates `VAD_scan_{elevation_angle}deg.txt`, containing one azimuth/elevation position per
line. The filename is based on `elevation_angle`; change the value and run the
script again to create another scan definition.

## Create the daily schedule

Configure the scan entries and their offsets in
[`write_daily_scan_schedule.py`](./write_daily_scan_schedule.py):

```python
SCHEDULE_LINES = [
    "VAD_scan_1deg\t1\tS\t6",
    "VAD_scan_5deg\t3\tS\t6",
    "VAD_scan_70deg\t3\tS\t6",
]
SCHEDULE_OFFSETS_SECONDS = [10, 160, 320]
```

The entries are scheduled at the configured offsets after every 15-minute
interval. The default configuration creates 288 entries (96 intervals × 3
scans) in `scan_schedule.dss`.

Run:

```bash
python write_daily_scan_schedule.py
```

Each schedule line has this format:

```text
HHMMSS<TAB>scan-file<TAB>integration<TAB>scan-type<TAB>focus
```

The generated file uses Unix line endings and does not include a trailing
newline.

## Install on the lidar

1. Copy the generated daily scan `.txt` files to:
   `Scan parameters/Daily_Scan_Files`
2. Copy the generated `.dss` schedule file to:
   `Scan parameters`
3. Confirm that every scan filename in `SCHEDULE_LINES` matches a file in
   `Daily_Scan_Files`.
4. Confirm that the offsets leave enough time for each scan to finish and do
   not interfere with the background measurement.
