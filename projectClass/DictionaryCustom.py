import numpy as np


class DictionaryCustom():

    @staticmethod
    def sort_by_keys(dict) -> dict:
        keys = list(dict.keys())
        keys.sort()

        return {key: dict[key] for key in keys}

    @staticmethod
    def sort_by_values(dict, order='asc') -> dict:
        keys = list(dict.keys())
        values = list(dict.values())

        sorted_value_index = np.argsort(values)
        if order == 'desc':
            sorted_value_index = np.flip(sorted_value_index, axis=0)
        return {keys[i]: values[i] for i in sorted_value_index}

    @staticmethod
    def get_ids_keys_dict(dict, data) -> list:
        """
        Renvoie les id où data est présent dans les clés du dict
        :param dict:
        :return: list
        """
        # for key in dict:
        #     print(key)

        my_list = []

        for id_key, key in enumerate(dict):
            if type(key) is tuple:
                if data in key:
                    my_list.append(id_key)
            elif data == key:
                my_list.append(id_key)

        return my_list

