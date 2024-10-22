from pathlib import Path


def shopping_list_to_dict(shopping_list):
    d = dict()  
    splittet = shopping_list.splitlines()
    for line in splittet:
        if line == None:
            return None
        line = line.strip()
        parts = line.split(" ")
        if len(parts) == 2:
            if parts[0] != "":
                num = int(parts[0])
                food_name = parts[1].strip()
                d[food_name] = num
        
    return d

def shopping_list_file_to_dict(path):
    vei = Path(path)
    try:
        with vei.open("r", encoding = "utf-8") as fil:
            content= fil.read()
            list = shopping_list_to_dict(content)
            return list
        
    except Exception as e:
        print(f"ERROR {e}")
    
    
    
    
    
    
def test_shopping_list_file_to_dict():
    print('Tester shopping_list_file_to_dict... ', end='')
    expected = {
        'brød': 2,
        'pizza': 3,
        'poteter': 10,
        'kaffe': 1,
        'ost': 1,
        'epler': 13,
    }
    actual = shopping_list_file_to_dict('handleliste.txt')
    assert expected == actual
    print('OK')

    
if __name__ == '__main__':
    test_shopping_list_file_to_dict()
    
    

    