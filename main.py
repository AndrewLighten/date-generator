import datetime
import sys
from typing import List


def main(when: datetime.date = datetime.date.today()) -> None:
    """
    This is the main function.
    """

    # Format this as the filename for the output
    filename = when.strftime('./%Y-Calendar.md')

    # Find the first day of the year
    current_date = datetime.date(when.year, 1, 1)
    start_year = when.year
    lines: List[str] = []

    # Visit each day until we find ourselves in the next year
    while current_date.year == start_year:
        if current_date.day == 1:
            lines.append(f"\n## {current_date.strftime('%B')}\n\n")
        if current_date.weekday() == 0:
            lines.append(f"\n")
        lines.append(f"[[{current_date.strftime('%Y-%m-%d-%a')}]]\n")
        current_date = current_date + datetime.timedelta(days=1)

    # Open the file for writing
    with open(filename, 'w') as f:
        f.writelines(lines)


# --------------------------------------------------

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(when=datetime.date.fromisoformat(sys.argv[1]))
    else:
        main()
