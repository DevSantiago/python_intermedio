def run():
    my_list = [1, 'hello', True, 4.5]
    my_dict = {"firstname": "Facundo", "lastname": "Garcia"}

    super_list = [
        {"firstname": "Facundo", "lastname": "Garcia"},
        {"firstname": "Miguel", "lastname": "Torres"},
        {"firstname": "Santiago", "lastname": "Martinez"},
        {"firstname": "Daniel", "lastname": "Martinez"},
        {"firstname": "Esther", "lastname": "Pineda"}
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.1, 4.5, 6.43]
    }

    for key, value in super_dict.items():
        print(key, "-", value)
    
    for list_item in super_list:
        print(list_item)


if __name__ == "__main__":
    run()