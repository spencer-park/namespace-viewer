def create_namespace_viewer(data:dict):
    for k, v in data.items():
        print(k, v, type(v))


def create_table(func):
    def decorator(data):
        head = "<table>"

        if isinstance(data, int):
            



def convert_int(data):
    ...


def convert_str(data):
    ...


def convert_list(data):
    ...


def convert_dict(data):
    ...


def convert_class(data):
    ...


if __name__=="__main__":
    # data = globals()
    a = 3
    b = "str"
    c = [1,2,3]
    d = {"name": "Spencer"}
    create_namespace_viewer(globals())