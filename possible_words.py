from pathlib import Path

def possible_words_from_file(path, letters):
    riktig = []
    liste_ord = list(letters)
    content_string = Path(path).read_text(encoding='utf-8')
    ord_dict = content_string.splitlines()
    
    for ord in ord_dict:
        liste_ord = list(letters)
        bokstav = list(ord)
        for let in bokstav:
            if let in liste_ord:
                liste_ord.remove(let)
            else:
                break
            
        else:
            riktig.append(ord)
        
    return riktig
            
    
    
    
def test_possible_words_from_file():
    print('Tester possible_words_from_file... ', end='')
    assert(['du', 'dun', 'hu', 'hud', 'hun', 'hund', 'nu', 'uh']
            == possible_words_from_file('nsf2022.txt', 'hund'))

    # Ekstra test for varianten hvor det er wildcard i bokstavene
    # assert(['a', 'cd', 'cv', 'e', 'i', 'pc', 'wc', 'æ', 'å']
    #         == possible_words_from_file('nsf2022.txt', 'c*'))
    print('OK')

if __name__ == '__main__':
    test_possible_words_from_file()
