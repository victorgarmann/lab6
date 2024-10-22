from pathlib import Path

def best_alignment(genome,pattern):
    length_p = 0
    length_g = 0
    overlap = 0
    splittet_p = list(pattern)
    splittet_g = list(genome)
    length_p = len(splittet_p)
    length_g = len(splittet_g)
    forrigeverdi = 0
    best_pos = 0
    diff = length_g - length_p
    for i in range(diff + 1):
        overlap = 0
        for pos in range(length_p):
            if splittet_p[pos] == splittet_g[pos + i]:
                overlap += 1
        if overlap > forrigeverdi:
            forrigeverdi = overlap
            best_pos = i
    return best_pos

def best_alignment_to_file(path,pattern):
    vei = Path(path)
    try:
        with vei.open("r", encoding = "utf-8") as fil:
            content= fil.read()
            list = best_alignment(content, pattern)
            return list
        
    except Exception as e:
        print(f"ERROR {e}")

def test_best_alignment():
    print('Testing best_alignment...', end='')
    genome = 'AAACACCCCCGGGGGTGTTTTTTTTTTTTTTTTTTTTTTTTTTTT'
    pattern =  'ACACCCCCGGGGATGT'
    assert 2 == best_alignment(genome, pattern)

    genome = 'AAAAAAAAAAAAAAAAACACCCCCGGGGGTGTTTTTTTTTTTTTT'
    pattern =                      'CCGGGGATGT'
    assert 22 == best_alignment(genome, pattern)

    genome = 'TTTAAG'
    pattern =  'AAGT'
    assert 2 == best_alignment(genome, pattern)
    print(' OK')
    
def test_best_alignment_to_file():
    print('Testing best_alignment_to_file...', end='')
    path = 'human_genome_excerpt.txt'
    assert 30864 == best_alignment_to_file(path, 'AAACAAAGAA')
    assert 2097 == best_alignment_to_file(path, 'GAGTGGGATGAGCCATTGTTCATCT')
    assert 0 == best_alignment_to_file(path, 'TAACCC' * 18)
    assert 49913 == best_alignment_to_file(path, 'CATTTCAGTAGTAATAGGAATCTCCAC')
    print(' OK')

if __name__ == '__main__':
    test_best_alignment()
    test_best_alignment_to_file()
            
            
                
        
    