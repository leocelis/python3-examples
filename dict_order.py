from collections import OrderedDict

some_dict = {'ad_id': '123',
             'device_type': 'iphone',
             'campaign_name': 'awesome campaign',
             'currency': 'USD',
             'advertiser': 'leocelis',
             'postback_id': '1234566',
             'pixel_time': 1481081775000,
             'publisher': 'facebook',
             'campaign_id': '12345',
             'attribution_time': 1461729600000,
             'ad_name': 'awesome ad',
             'mmp': 'leocelis',
             'session_time': 1460494800000,
             'revenue': 125,
             'event': 'conversion'}

order_by = ['event', 'revenue', 'session_time', 'mmp', 'ad_name',
            'attribution_time', 'campaign_id', 'publisher', 'pixel_time',
            'postback_id', 'advertiser', 'currency', 'campaign_name',
            'device_type', 'ad_id']

order_by_dict = {k: v for v, k in enumerate(order_by)}

ordered_dict = OrderedDict(
    sorted(some_dict.items(), key=lambda i: order_by_dict.get(i[0])))

print("")
print("Unordered dict: {u}".format(u=some_dict))
print("")
print("Order by: {o}".format(o=order_by))
print("")
print("Ordered dict: {d}".format(d=ordered_dict))
print("")

data_blob = "-------".join(
    [":".join([key, str(val)]) for key, val in ordered_dict.items()])

print("Data blob: {d}".format(d=data_blob))
