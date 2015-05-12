#!/usr/bin/env python
# coding=utf-8

import pdb

class SimHash:

    def __init__(self, tokens = '', hashbits = 128):
        #pdb.set_trace()
        self.hashbits = hashbits
        self.hash = self.simhash(tokens)

    def __str__(self):
        return str(self.hash)

    def simhash(self, tokens):
        v = [0] * self.hashbits
        for t in [self.string_hash(x) for x in tokens]:
            for i in xrange(self.hashbits):
                bitmask = 1 << i
                if t & bitmask:
                    v[i] += 1
                else:
                    v[i] -= 1
        fin = 0
        for i in xrange(self.hashbits):
            if v[i] >= 0:
                fin += 1 << i
        return fin

    def hamming_distance(self, other):
        x = (self.hash ^ other.hash ) & ((2 ** self.hashbits) - 1)
        cnt = 0
        while x:
            cnt += 1
            x &= x - 1
        return cnt

    def similarity(self, other):
        a = float(self.hash)
        b = float(other.hash)
        if a > b:
            return b / a
        else:
            return a / b
    
    def string_hash(self, source):
        if source == '':
            return 0
        else:
            x = ord(source[0]) << 7
            m = 1000003
            mask = 2 ** self.hashbits - 1
            for c in source:
                x = ((x * m) ^ ord(c)) & mask
            x ^= len(source)
            if x == -1:
                x = -2
  #          print x
            return x

if __name__ == '__main__':
    s = 'This is a test string for testing'
    hash1 = SimHash(s.split())

    s = 'This is a test string for testing too'
    hash2 = SimHash(s.split())
            
    s = 'asdasd'
    hash3 = SimHash(s.split())

    print hash1.hamming_distance(hash2), hash1.similarity(hash2)
    print hash1.hamming_distance(hash3), hash1.similarity(hash3)
