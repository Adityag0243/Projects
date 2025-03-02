
# pip install bitarray 
from bitarray import bitarray

# pip install mmh3  --> for murmur hash function
import mmh3

# for random ip address generation
import random

from input_taker import * 
from ip_generator import *


# bloom filter class
class BloomFilter:
    def __init__(self, size, no_of_hash, multiplier):
        self.size = size
        self.multiplier = multiplier
        self.filter = bitarray(self.size * multiplier)  
        self.filter.setall(0) 
        self.no_of_hash = no_of_hash
        self.seeds = [i * 31 + 7 for i in range(no_of_hash)] # prime no helps to take a good seed value for better distribution


    def add(self, ip):
        for i in range(0,self.no_of_hash):
            hash_value = mmh3.hash(ip, seed=self.seeds[i]) & 0x7FFFFFFF  # Ensures positive hash values
            self.filter[hash_value % (self.size * self.multiplier)] = True



    def exists(self, ip):
        for i in range(self.no_of_hash):
            hash_value = mmh3.hash(ip, seed=self.seeds[i]) & 0x7FFFFFFF 
            if not self.filter[hash_value % (self.size * self.multiplier)]:
                return False
        return True




if __name__ == "__main__":

    #input taking 
    sz, no_of_hash, multiplier = inputTaking()

    # Generate a file named "ip_addresses.txt" with sz no of random IPs
    generate_ip_file("ip_addresses.txt", sz)

    print()
    print(f"Value Entered >>>\nSize of array : {sz} \nNumber of hash functions: {no_of_hash}\nMultiplier: {multiplier}")
    print()

    filter_bloom1 = BloomFilter(sz, no_of_hash, multiplier)

    # Reading IP addresses from file "ip_addresses.txt"
    ip_addresses = read_ip_file("ip_addresses.txt")

    # adding first half of the IP addresses in the bloom filter then check for all 
    trained_cnt = 0
    for ip in ip_addresses[:len(ip_addresses) // 2]:  
        filter_bloom1.add(ip)
        trained_cnt += 1

    
    cnt_true = 0 # will count no of true bloom filter is saying 
    for ip in ip_addresses:
        if filter_bloom1.exists(ip) == True:
            cnt_true += 1
    
    false_positive = 0
    if len(ip_addresses) != trained_cnt:
        false_positive = (cnt_true - trained_cnt) / (len(ip_addresses) - trained_cnt)

    print(f"False positive rate: {false_positive:.2%}") 

