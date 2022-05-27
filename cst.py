import re

def __read_lines(filepath: str) -> 'list[str]':
    lines = []
    with open(filepath) as f:
        lines = f.readlines()
    return lines

def __split_line(line: str) -> 'list[str]':
    # Split line, respecting quotes:
    values: 'list[str]' = re.findall(r'(?:[^\s,"]|"(?:\\.|[^"])*")+', line)
    # Remove quotes:
    values = [value.replace('"', '') for value in values]
    return values

def __get_column_titles(line: str) -> 'list[str]':
    pass

def read(filepath: str) -> list:
    lines: 'list[str]' = __read_lines(filepath)
    if len(lines) < 2:
        print(f'[ERROR] {str} does not contain a full header.')
    
    names: 'list[str]' = [] # List of column titles.
    types: 'list[str]' = [] # List of column types.
    data: 'list[dict]' = []         # Index represents data row (without header) and values are
                            # dictionaries who's keys are column titles.
    
    names = __split_line(lines[0])
    types = __split_line(lines[1])
    for idx_line in range(2, len(lines)):
        line: str = lines[idx_line]
        values: 'list[str]' = __split_line(line)
        line_data: dict = {}
        for idx_value in range(len(values)):
            value_name: str = names[idx_value]
            value_type: str = types[idx_value]
            value: str = values[idx_value]
            if value_type == 'bool':
                if value == 'true':
                    line_data[value_name] = True
                elif value == 'false':
                    line_data[value_name] = False
                else:
                    print(f'[ERROR] Unknown bool value `{value}`!')
                    pass
            elif value_type == 'int':
                line_data[value_name] = int(value)
            elif value_type == 'string':
                line_data[value_name] = str(value)
            elif value_type == 'float':
                line_data[value_name] = float(value)
            else:
                # TODO: Throw error.
                print(f'[ERROR] Unknown type `{value_type}`!')
        data.append(line_data)
    return data