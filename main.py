import datetime
from typing import List

if __name__ == '__main__':

    # Find the current date
    today = datetime.date.today()

    # Format this as the filename for the output
    filename = today.strftime('./%Y-Calendar.md')

    # Find the first day of the year
    current_date = datetime.date(today.year, 1, 1)
    start_year = today.year
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
