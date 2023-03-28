def flatten_dict(dictionary):
    flattened = {}
    for key in dictionary:
        if isinstance(dictionary[key], dict):
            for inner_key, inner_value in dictionary[key].items():
                flattened.update({key + '.' + inner_key: inner_value})
            else: 
                flattened.update({key: dictionary[key]})
            return flattened
    return()

def unflatten_dict(dictionary):
    unflatten = {}
    for key in dictionary.keys():
        if '.' in key:
            split_key = key.split('.')
            outer_key = split_key[0]
            for inner_key in split_key[1:]:
            unflatten.update({outer_key: {dictionary[key]}})