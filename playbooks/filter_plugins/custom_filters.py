# -- coding: utf-8 --

from ansible import errors

def convert_to_megabyte(num):
    table = {'K': 1 / 1024.0, 'M': 1, 'G': 1024, 'T': 1024 * 1024}
    ret = num

    if num[-1] in table.keys():
        ret = float(num[0:-1]) * table[num[-1]]

    return ret

class FilterModule(object):
    def filters(self):
        return {
            'convert_to_megabyte': convert_to_megabyte,
            'zip_for_loop': lambda a, b: [[i] for i in zip(a, b)] # with_items がネストされたリストを 1 階層フラットにしてしまうのに対応
        }
