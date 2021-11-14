def delete_keys(keys, dictionary):
    remaining = {}
    for key in dictionary:
        if key not in keys:
            remaining[key] = dictionary[key]

    return remaining


dict = {'firstName': 'Mohamed', 'lastName':'Farag', 'birthYear': 1990, 'nationality': 'Egyptian'}

print(delete_keys(['lastName','birthYear'], dict))