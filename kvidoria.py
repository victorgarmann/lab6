from pathlib import Path


def get_word_count(path):
    d = dict()
   
    content_string = Path(path).read_text(encoding='utf-8')
    content_string = content_string.lower()
    content_string = cleaned_text(content_string)
    liste = content_string.split(" ")
    
    
    res = []
    for i in liste:
        if i not in res:
            res.append(i)
    
    
    
    for word in res:
        antall = 0
        for i in liste:
            if word == i:
                antall += 1
        d[word] = antall
    return d


def cleaned_text(text):
    mongo = []
    vanlig = [" ",'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', "\n"]
    for char in list(text):
        if char in vanlig:
            mongo.append(char)
    mongo = ''.join(map(str, mongo))
    return mongo
                
def pop_most_common_word(word_count):
    oppslag = word_count
    count = 0
    most = None
    for i in oppslag:
        if oppslag[i] > count:
            count = oppslag[i]
            most = i
    for i in oppslag:
        if oppslag[i] == oppslag[most]:
            if i < most:
                most = i
    oppslag.pop(most)
    return most

def n_common_words(word_count,n):
    common_words = []
    most = None
    for ganger in range(n):
        most = pop_most_common_word(word_count)
        common_words.append(str(most))
    return common_words
            
def common_words(path, n):
    list = get_word_count(path)
    ny = n_common_words(list,n)
    
    return ny
    
    
    
    
    
    

def test_common_words():
    print('Tester common_words... ', end='')
    # Test 1
    expected = ['pusur', 'var']
    actual = common_words('pusur.txt', 2)
    assert actual == expected

    # Test 2
    expected = ['pusur', 'var', 'en', 'katt', 'det', 'het', 'snill', 'som']
    actual = common_words('pusur.txt', 8)
    assert actual == expected

    print('OK')

if __name__ == '__main__':
    
    test_common_words()