"""Generate Hyde daily scan schedule files.

Python translation of write_hyde_daily_scan_schedule.m.
"""

from __future__ import annotations

SECONDS_PER_DAY = 24 * 60 * 60
INTERVAL_SECONDS = 15 * 60
NUM_INTERVALS = 24 * 60 // 15  # 96 intervals: 00:00 through 23:45


def hhmmss_from_seconds(total_seconds: int) -> str:
    """Format seconds since midnight as HHMMSS with wrap-around at 24h."""
    seconds = total_seconds % SECONDS_PER_DAY
    hours, rem = divmod(seconds, 3600)
    minutes, secs = divmod(rem, 60)
    return f"{hours:02d}{minutes:02d}{secs:02d}"


def write_schedule(file_path: str, lines: list[str], offsets_seconds: list[int]) -> None:
    """Write one schedule file using fixed offsets for each line per 15-min interval."""
    with open(file_path, "w", encoding="utf-8", newline="\n") as f:
        for i in range(NUM_INTERVALS):
            base = i * INTERVAL_SECONDS
            for line, offset in zip(lines, offsets_seconds):
                hh = hhmmss_from_seconds(base + offset)
                f.write(f"{hh}\t{line}\n")


def main() -> None:
    # First schedule block from MATLAB script.
    lines_1 = [
        "hyde_VAD_scan_1deg_2\t1\tS\t6",
        "hyde_VAD_scan_5deg\t1\tS\t6",
        "VAD_scan_30deg\t3\tS\t6",
        "VAD_scan_70deg\t3\tS\t6",
    ]
    offsets_1 = [10, 60, 90, 160]
    write_schedule("hyde_shedule_1.dss", lines_1, offsets_1)

    # Second schedule block from MATLAB script.
    lines_2 = [
        "hyde_VAD_scan_1deg_2\t3\tS\t6",
        "hyde_VAD_scan_5deg\t3\tS\t6",
        "VAD_scan_30deg\t3\tS\t6",
        "VAD_scan_70deg\t3\tS\t6",
    ]
    offsets_2 = [10, 160, 240 * 60, 310]
    write_schedule("hyde_shedule_2.dss", lines_2, offsets_2)


if __name__ == "__main__":
    main()
