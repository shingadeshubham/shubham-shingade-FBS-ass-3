my_dict = {'a': 1, 'b': 2, 'c': 3}
key_to_remove = 'b'

if key_to_remove in my_dict:
    del my_dict[key_to_remove]

print("Dictionary after removal:", my_dict)
