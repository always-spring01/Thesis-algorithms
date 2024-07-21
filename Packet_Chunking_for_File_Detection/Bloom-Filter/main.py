'''
Bloom-Filter with Python3

Author: CHB. Kookmin Univ
Date: 20240721
Associated Thesis: Packet Chunking for File Detaction
'''

# Import Modules
import math
import mmh3
from bitarray import bitarray

# Bloom-filter Class
class BloomFilter(object):
    # 생성자
    def __init__(self, item_cnt, fp_prob) -> None:

        '''
        item_cnt : Bloom filter에 저장될 item의 개수
        fp_prob : False Positive 문제가 발생될 확률
        '''
        
        self.fp_prob = fp_prob
        self.size = self.get_size(item_cnt, fp_prob)
        self.hash_count = self.get_hash_cnt(self.size, item_cnt)
        self.bit_array = bitarray(self.size)

    # Bloom filter 추가
    def add(self, item):
        digests = []
        for i in range(self.hash_count):
            digest = mmh3.hash(item, i) % self.size
            digests.append(digest)

            self.bit_array[digest] = True
    
    # Bloom filter에 속하는지 검증
    def check(self, item):
        for i in range(self.hash_count):
            digest = mmh3.hash(item, i) % self.size
            if self.bit_array[digest] == False:
                return False
        return True
    
    def get_size(self, n, p):
        m = -(n * math.log(p)) / (math.log(2) ** 2)
        return int(m)

    def get_hash_cnt(self, m, n):
        k = (m/n) * math.log(2)
        return int(k)
    
# main
if __name__ == "__main__":
    bloomfilter = BloomFilter(20, 0.05)
    print(bloomfilter.get_size)

    word_present = ['나는', '행복하다', '인생이', '강아지', '고양이', '국민대학교']
    word_absent = ['민수', '철수', '행복하다', '국민', '국민대학교']

    for word in word_present:
        bloomfilter.add(word)

    for word in word_absent:
        if bloomfilter.check(word):
            if word in word_present:
                print(f"{word}는 제공된 단어입니다.")
            else:
                print(f"{word}는 FP 문제입니다")
        else:
            print(f"{word}는 제공되지 않은 단어입니다.")