import pandas as pd


def pd_by_dates_range(df, csdate, cedate, vsdate, vedate):
    """
    Filter DataFrame by date range.
    End date is inclusive.

    :param self:
    :param df:
    :param csdate:
    :param cedate:
    :param vsdate:
    :param vedate:
    :return:
    """
    # convert string dates to dates dates
    df[csdate] = pd.to_datetime(df[csdate])
    df[cedate] = pd.to_datetime(df[cedate])

    # filter by date range
    df = df[(vsdate >= df[csdate]) & (vsdate <= df[cedate])]
    df = df[(vedate >= df[csdate]) & (vedate <= df[cedate])]

    return df


df_sample = {'clicks': [100, 200, 300],
             'impressions': [100000, 200000, 300000],
             'start_date': ['2018-02-03', '2018-02-04', '2018-02-05'],
             'end_date': ['2018-02-04', '2018-02-05', '2018-02-06']}
df = pd.DataFrame(df_sample, columns=['start_date', 'end_date', 'clicks', 'impressions'])

df = pd_by_dates_range(df=df,
                       csdate='start_date', cedate='end_date',
                       vsdate='2018-02-03', vedate='2018-02-04')

print(df)
