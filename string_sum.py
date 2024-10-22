from pathlib import Path

def get_stringsum(s):
    sum = 0
    
    splittet = s.split(" ")
    for tall in splittet:
        try:
            sum += int(tall)
        except:
            continue    
            
    return sum

    
def get_line_with_highest_stringsum(s):
    lines = s.splitlines()
    i = 0
    t = 0
    r = None
    
    for index, line in enumerate(lines):
        
        string_sum = get_stringsum(line)
        if string_sum > t:
            r = line
            t = string_sum
            i = index + 1
            
            
            
        
    return (i,t,r)
    
    
def test_get_stringsum():
    print('Testing get_stringsum... ', end='')
    assert 6 == get_stringsum('4 2')
    assert 9 == get_stringsum('5 -1 3 +2')
    assert 11 == get_stringsum('5 - 1 3 + 2')
    assert 42 == get_stringsum('42')
    assert 42 == get_stringsum('forty-one 42 førtitre')
    assert 42 == get_stringsum('foo2 42 2qux 3x1')
    assert 0 == get_stringsum('')
    assert 0 == get_stringsum('foo bar qux')
    assert 0 == get_stringsum('-9- 3+2')
    print('OK')

def test_get_line_with_highest_stringsum():
    print('Testing get_line_with_highest_stringsum... ', end='')

    arg = '4 2\n3 3\n6 6 6 6 12 6\n'
    assert (3, 42, '6 6 6 6 12 6') == get_line_with_highest_stringsum(arg)

    arg = '4 99 -98\nfoo 42 qux\nfoo bar quz\n'
    assert (2, 42, 'foo 42 qux') == get_line_with_highest_stringsum(arg)

    arg = '4 2\n3 3\n'
    assert (1, 6, '4 2') == get_line_with_highest_stringsum(arg)

    print('OK')
    
def main():
    filnavn = input("Hvilken fil? ")
    vei = Path(filnavn)
    
    try:
        with vei.open("r", encoding = "utf-8") as fil:
            content= fil.read()
        index,sum,linje = get_line_with_highest_stringsum(content)
        
        print(f"Høyeste strengsum er {sum}, funnet først på linje {index}: {linje}")
        
        
    except Exception as e:
        print(f"ERROR {e}")
    

if __name__ == '__main__':
    test_get_stringsum()
    test_get_line_with_highest_stringsum()
    main()
    