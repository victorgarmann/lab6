from pathlib import Path


def get_impact(line):
    parts = line.split(";")
    
    try:
        return float(parts[2])
        
    except Exception as e:
        return None
    
def filter_earthquakes(earthquake_csv_string, threshold):
    splittet = earthquake_csv_string.splitlines()
    nyliste = [splittet[0]]
    delimiter_space = "\n"
    string = delimiter_space.join(nyliste)
    for line in splittet:
        value = get_impact(line)
        if value == None:
            continue
        if value <= threshold:
            continue
        if value > threshold:
            nyliste.append(line)
            string = delimiter_space.join(nyliste)
    return string 

def filter_earthquakes_file(source_filename, target_filename, threshold):
    
    content_string = Path(source_filename).read_text(encoding='utf-8')
    
    
    
    content_string_a = filter_earthquakes(content_string,threshold)
    with open(target_filename, 'w', encoding='utf-8') as file:
        file.writelines(content_string_a)
    
    
    
def test_filter_earthquakes_file():
    print('Tester filter_earthquakes_file... ', end='')

    def read_file(path):
        with open(path, 'rt', encoding='utf-8') as f:
            return f.read()

    filter_earthquakes_file('earthquakes_simple.csv',
                            'earthquakes_above_7.csv', 7.0)
    expected_value = (
        'id;location;impact;time\n'
        'us100068jg;Northern Mariana Islands;7.7;2016-07-29 17:18:26\n'
        'us10006d5h;New Caledonia;7.2;2016-08-11 21:26:35\n'
        'us10006exl;South Georgia Island region;7.4;2016-08-19 03:32:22\n'
    )
    actual_value = read_file('earthquakes_above_7.csv')
    assert expected_value.strip() == actual_value.strip()
    print('OK')
          
        

if __name__ == '__main__':
    
    test_filter_earthquakes_file()
