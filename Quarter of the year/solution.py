def quarter_of(month):
    monthsByQuarter = {
        1: [3, 1, 2],
        2: [6, 4, 5],
        3: [9, 7, 8],
        4: [12, 10, 11]
      }

    for season in monthsByQuarter:
        if month in monthsByQuarter[season]:
            return season