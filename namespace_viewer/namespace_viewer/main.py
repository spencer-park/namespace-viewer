def create_namespace_viewer(data:dict, css=None):
    # default css
    if not css:
        css = """
            table {margin-bottom: 10px; border: 1px solid #333;}
            thead, tfoot {background-color: #4aa8d8; color: #fff;}
            th, td {padding: 3px; border: 1px solid #333;}
            """

    # start html code        
    html = f"""<!DOCTYPE html><html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
            <!-- css -->
            <style>
                {css}
            </style>
        </head>
        <body>  
    """
    
    # split data type
    viewer_data = {}
    for k, v in data.items():
        print(k, v, type(v))

        # primitive_type
        if isinstance(v, (int, str, bool)):
            type_name = f'{type(v)}'[1:-1]

            if not viewer_data.get(type_name):
                viewer_data[type_name] = []        
            viewer_data[type_name].append((k, v))

    # create table
    for t, v in viewer_data.items():
        print(t)
        html += convert_primitive_type(t, v)


    # end html code
    html += f"""
        </body></html>  
    """

    # make viewer.html
    create_html(html)


def create_html(html, filepath = './', filename='viewer.html'):
    with open(filepath+filename, 'w') as fp:
        fp.write(html)


def create_table(func):
    def decorator(type_name, data):
        html = "<table>"
        html += func(type_name, data)
        html += "</table>"
        return html
    return decorator    
    

@create_table
def convert_primitive_type(type_name, data:list):
    html = f'''
    <thead>
        <th colspan="2">{type_name}</th>
    </thead>
        <tbody>
    '''
    for v in data:
        html += '<tr>'
        html += f'<td>{v[0]}</td>'
        html += f'<td>{v[1]}</td>'
        html += '<tr>'
    html += '</tbody>'
    return html



@create_table
def convert_list(data):
    ...


@create_table
def convert_dict(data):
    ...


@create_table
def convert_class(data):
    ...


if __name__=="__main__":
    sample_int = {'a': 3, 'b': 5}
    sample_A = {
        'a': 3, 'b': 5,
        'name': 'spencer', 'school': '프로그래머스',
        'res1': True, 'res2': False
    }

    create_namespace_viewer(sample_A)