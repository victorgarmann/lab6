from pathlib import Path

def filter_wordlist(path, search_string):
    filtered_words = []
    
    
    content_string = Path(path).read_text(encoding='utf-8')
    splittet = content_string.splitlines()
    
    for line in splittet:
        if search_string in line:
            filtered_words.append(line)
    
    
    
    return filtered_words

def test_filter_wordlist():
    print('Tester filter_wordlist... ', end='')

    # Test 1
    expected = ['database', 'baser']
    actual = filter_wordlist('sample.txt', 'base')
    assert expected == actual

    # Test 2
    expected = [
      'småstad', 'småstaden', 'småstas', 'småstasen', 'småstat', 'småstaten',
      'småstatene', 'småstater',
    ]
    actual = filter_wordlist('nsf2022.txt', 'småsta')
    assert expected == actual

    # Test 3
    expected = [
      'stjerneskudd', 'stjerneskudda', 'stjerneskuddene', 'stjerneskuddet', 
    ]
    actual = filter_wordlist('nsf2022.txt', 'stjerneskudd')
    assert expected == actual

    print('OK')
    
if __name__ == '__main__':
    test_filter_wordlist()
