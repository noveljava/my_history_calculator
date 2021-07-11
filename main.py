from datetime import datetime, timedelta


def diff_month(start_date: datetime, end_date: datetime) -> (int, int, int):
    diff: timedelta = end_date - start_date
    days = diff.days
    year = int(days / 365)
    days %= 365

    month = int(days / 30)
    days %= 30
    return year, month, days


if __name__ == '__main__':
    start_info = [(2009, 5), (2013, 10), (2015, 4), (2018, 8)]
    end_info = [(2011, 1), (2014, 6), (2018, 6), (2021, 2)]

    sum_year, sum_month = 0, 0
    for i in range(len(start_info)):
        year, month, days = \
            diff_month(
                datetime(year=start_info[i][0], month=start_info[i][1], day=1),
                datetime(year=end_info[i][0], month=end_info[i][1], day=1)
            )

        print(year, month)
        sum_year += year
        sum_month += month


    sum_year += int(sum_month / 12)
    sum_month %= 12
    print(sum_year, sum_month)
