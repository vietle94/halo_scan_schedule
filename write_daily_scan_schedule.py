"""Generate the daily scan schedule"""

from __future__ import annotations

from pathlib import Path
from collections.abc import Sequence

SCHEDULE_LINES = [
    "VAD_scan_1deg\t1\tS\t6", # Number of integration, Scan type (Step-stare or CSM), focus (6 is 2000 m, not needed for XR but need to be included)
    "VAD_scan_5deg\t3\tS\t6", # So should change first number (integration per beam) if needed
    "VAD_scan_70deg\t3\tS\t6",
]
SCHEDULE_OFFSETS_SECONDS = [10, 160, 320] # 10s from 15-minute interval, 160s from 15-minute interval, 320s from 15-minute interval (for each scan, need to space out so the scan can finish)

SECONDS_PER_DAY = 24 * 60 * 60
INTERVAL_SECONDS = 15 * 60
NUM_INTERVALS = SECONDS_PER_DAY // INTERVAL_SECONDS

def hhmmss_from_seconds(total_seconds: int) -> str:
    """Format seconds since midnight as HHMMSS with wrap-around at 24h."""
    seconds = total_seconds % SECONDS_PER_DAY
    hours, rem = divmod(seconds, 3600)
    minutes, secs = divmod(rem, 60)
    return f"{hours:02d}{minutes:02d}{secs:02d}"


def write_schedule(
    file_path: str | Path,
    lines: Sequence[str],
    offsets_seconds: Sequence[int],
) -> None:
    """Write one schedule file using fixed offsets for each 15-minute interval."""
    if len(lines) != len(offsets_seconds):
        raise ValueError("lines and offsets_seconds must contain the same number of items")

    entries = (
        f"{hhmmss_from_seconds(i * INTERVAL_SECONDS + offset)}\t{line}"
        for i in range(NUM_INTERVALS)
        for line, offset in zip(lines, offsets_seconds)
    )
    with Path(file_path).open("w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(entries))


if __name__ == "__main__":
    write_schedule(
            "scan_schedule.dss", # change name if needed
            SCHEDULE_LINES,
            SCHEDULE_OFFSETS_SECONDS,
        )
