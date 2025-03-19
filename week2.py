# from collections import Counter

# words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']

# print(dict(Counter(words)))


# def countWords(words):

#     myDict = {}
#     for word in words:
#         if word in myDict:
#             myDict[word] += 1
#         else:
#             myDict[word] = 1
#     return myDict
# print(countWords(words))

# def find_duplicate_chests(chests):
#     mySet = set()
#     mylist = []
#     for num in chests:
#         if num in mySet:
#             mylist.append(num)
#         else:
#             mySet.add(num)
#     return mylist
# chests1 = [4, 3, 2, 7, 8, 2, 3, 1]
# chests2 = [1, 1, 2]
# chests3 = [1]

# print(find_duplicate_chests(chests1))
# print(find_duplicate_chests(chests2))
# print(find_duplicate_chests(chests3))

# def is_balanced(code):
#     strList = list(code)
#     #print(strList)
#     myDict = {}
#     myFreq = {}


#     for letter in strList:
#         if letter in myDict:
#             myDict[letter] += 1
#         else:
#             myDict[letter] = 1

#     minLetter = min(myDict.values())

#     expected = minLetter * len(myDict)
#     #print(myDict)
#     #print(len(myDict))
#     #print(expected)
#     if expected == (len(strList) - 1):
#         return True
#     else:
#         return False

# code1 = "arghh"
# code2 = "haha"

# print(is_balanced(code1)) 
# print(is_balanced(code2)) 

####            Week 2, Session 2           ####  

from collections import Counter

# def find_balanced_subsequence(art_pieces):
#     freq = Counter(art_pieces)

#     max_length = 0

#     for key in freq:
#         if key + 1 in freq:
#             max_length = max(max_length, freq[key] + freq[key + 1])
#     return max_length

# art_pieces1 = [1,3,2,2,5,2,3,7]
# art_pieces2 = [1,2,3,4]
# art_pieces3 = [1,1,1,1]

# print(find_balanced_subsequence(art_pieces1))
# print(find_balanced_subsequence(art_pieces2))
# print(find_balanced_subsequence(art_pieces3))

# def is_authentic_collection(art_pieces):
#     myset = set(art_pieces)
#     counter = Counter(art_pieces)
#     return len(myset) == counter.most_common(1)[0][0]

# collection1 = [1, 1, 3, 2]
# collection2 = [1, 3, 3, 2]
# collection3 = [1, 2]

# print(is_authentic_collection(collection1))
# print(is_authentic_collection(collection2))
# print(is_authentic_collection(collection3))     


# def organize_exhibition(collection):
#     counter = Counter(collection)
#     #print(counter)
#     maxval = max(counter.values())
#     #print(maxval)
#     my2d = []
#     for val in range(maxval+1):
#         if val+1 in counter.values():
#             my2d.append([key for key in counter if val+1 <= counter[key]])
#     return my2d

# collection1 = ["O'Keefe", "Kahlo", "Picasso", "O'Keefe", "Warhol", 
#               "Kahlo", "O'Keefe"]
# collection2 = ["Kusama", "Monet", "Ofili", "Banksy"]

# print(organize_exhibition(collection1))
# print(organize_exhibition(collection2))

import re
# def intersect(nums1, nums2):
#     # Write your code here
#     if not nums1 and not nums2:
#         return
#     string1 = "".join(map(str,nums1))
#     string2 = "".join(map(str,nums2))
#     print (string1)
#     print(string2)
#     minLen = min(len(string1), len(string2))
#     if minLen == len(string1):
#         string1 = string1
#     if minLen == len(string2):
#         tempstring = string1
#         string1 = string2
#         string2 = tempstring
#     intersectionlist = []

#     for i in range(minLen):
#         for j in range(1,minLen+1):
#             print(string1[i:j])
#             print(string2)
#             if re.search(string1[i:j], string2) and string1[i:j] != '':
#                 print(string1[i:j])
#                 intersectionlist.append(string1[i:j])

#     maxlen = max(intersectionlist, key=len)
#     matchlist = [int(i) for i in maxlen]
#     return matchlist

# nums1 = [1,2,3,4]
# nums2 = [5,2,3,4]

# print(intersect(nums1, nums2))

# lst = [5, 4, 3, 2, 1]

# def get_min(lst):   
#     minimum = float('inf')
#     for num in lst:
#         if num < minimum:
#             minimum = num

#     return minimum

# print(get_min(lst))

# cereals = ['cheerios', 'fruity pebbles', 'cocoa puffs']
# for count, cereal in enumerate(cereals, start=1):
#   print(count, cereal)

# Prints:
# 1 cheerios
# 2 fruity pebbles
# 3 cocoa puffs

# names = ['Alice', 'Bob', 'Charlie']
# ages = [25, 30, 35]
# zipped = list(zip(names, ages))
# print(zipped) # Prints [('Alice', 25), ('Bob', 30), ('Charlie', 35)]

# myDict = {}

# for i in range(len(zipped)):
#     myDict[zipped[i][0]] = zipped[i][1]
# print(myDict)

# # Example 2: Zipping Lists of Different Lengths
# names = ['Alice', 'Bob', 'Charlie', 'David']
# ages = [25, 30, 35]
# zipped = zip(names, ages)
# print(list(zipped)) # Prints [('Alice', 25), ('Bob', 30), ('Charlie', 35)]

#!/bin/python3

import math
import os
import random
import re
import sys
import ast



# Enter your code here. Read input from STDIN. Print output to STDOUT
#
# Complete the 'roman_to_int' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

# def roman_to_int(s):
#     if not s:
#         return 0
#     roman_nums = {
#         'I': 1,
#         'V' : 5,
#         'X' : 10,
#         'L' : 50,
#         'C' : 100,
#         'D' : 500,
#         'M' : 1000,
#     }

#     RomeToInt = 0

#     for i in range(len(s)):
#         if i < (len(s)-1) and roman_nums[s[i]] < roman_nums[s[i+1]]:
#             RomeToInt -= roman_nums[s[i]]
#         else:
#             RomeToInt += roman_nums[s[i]]            

        
#     return RomeToInt

# def array_rank_transform(arr):
#     unsorted = [num for num in arr]
#     arr.sort()
#     #print(arr)
#     ranked = {} 
#     rank = 1
#     for num in arr:
#         if num not in ranked:
#             ranked[num] = rank
#             rank += 1

#     #print(ranked)
#     listrank = []
#     #print(unsorted)
#     for num in unsorted:
#         if num in ranked:
#             listrank.append(ranked[num])
#     return listrank


# arr = [1,2,8,9,5]

# print(array_rank_transform(arr))

# # #print(roman_to_int('XIV'))
# def length_of_longest_substring(s):
#     s_list = list(s)
#     #print(s_list)
#     myset = set(s_list)
#     print(myset)
#     for i in range(len(s))

# Example 1:
# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# Example 2:
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.

# Example 3:
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
# length_of_longest_substring('Honey')


# def valid_mtn_arr(arr):
#     # Write your code here
#     if not arr:
#         return False
    
#     if len(arr) < 3:
#         return False
#     indx = 0
#     length = len(arr)
    
#     while indx + 1 < length and arr[indx] < arr[indx + 1]:
#         indx += 1
    
#     if indx == 0 or indx == length:
#         return False
#     #print(arr[indx])
    
#     while indx + 1 < length and arr[indx] > arr[indx + 1]:
#         #print(arr[indx])
#         indx += 1
#     #print(indx) 
#     if arr[indx - 1] <= arr[indx]:
#         return False
#     if indx == length - 1:
#         return True
#     else:
#         return False
        

# print(valid_mtn_arr([1,2,3,4,5,4,3,2,1]))


# def decode_string(s):
#     # Write your code here
#     multiplier = []
#     letter = []
#     brackets = []
#     tempstring = ''
#     decoded = ''
#     for char in s:
#         if char == '[':
#             brackets.append(char)
#         if char == "]":
#             if brackets == []:
#                 return False
#             else:
#                 brackets.pop()
#                 multiple = multiplier.pop(0)
#                 print(multiple)
#                 print(letter)
#                 print(decoded)
#                 while letter:
#                     tempstring += letter.pop(0)
#                 print(tempstring)
#                 decoded += int(multiple) * tempstring
#                 print(decoded)
#                 tempstring = ''
#                 multiple = ''
#         if char.isdigit():
#             multiplier.append(char)
#         if char.isalpha():
#             letter.append(char)
#     while len(letter) >0:
#         decoded += letter.pop(0)
#     return decoded
# #Example 1:
# s = "3[a]2[bc]"
# print(decode_string(s))
# #Output: "aaabcbc"

# #Example 2:
# s = "3[a2[c]]"
# #Output: "accaccacc"

# #Example 3:
# s = "2[abc]3[cd]ef"
# #Output: "abcabccdcdcdef"

class Villager:
    def __init__(self, name, species, personality, catchphrase):
        self.name = name
        self.species = species
        self.personality = personality
        self.catchphrase = catchphrase
        self.furniture = []
    def add_item(self, item_name):
        valid = ["acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu", "cacao tree"]
        if item_name in valid:
            self.furniture.append(item_name)
def of_personality_type(townies, personality_type):
    return [villager.name for villager in townies if villager.personality == personality_type]

# isabelle = Villager("Isabelle", "Dog", "Normal", "what's up?")
# bob = Villager("Bob", "Cat", "Lazy", "pthhhpth")
# stitches = Villager("Stitches", "Cub", "Lazy", "stuffin'")

# print(of_personality_type([isabelle, bob, stitches], "Lazy"))
# print(of_personality_type([isabelle, bob, stitches], "Cranky"))

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# class LinkedList: 
#     def __init__(self, head):
#         self.head = head

# def print_linked_list(head):
#         current = head
#         while current:
#             print(current.value, end=" -> " if current.next else "\n")
#             current = current.next

# kk_slider = Node("K.K. Slider")
# harriet = Node("Harriet")
# saharah = Node("Saharah")
# isabelle = Node("Isabelle")

# kk_slider.next = harriet
# harriet.next = saharah
# saharah.next = isabelle 

# print_linked_list(kk_slider)

# class LinkedList:
#     def __init__(self, head):
#         self.head = head

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next
# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.value, end=" -> " if current.next else "\n")
#         current = current.next

class Node:
    def __init__(self, fish_name, next=None):
        self.fish_name = fish_name
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.fish_name, end=" -> " if current.next else "\n")
        current = current.next

def catch_fish(head):
    if head is None:
        print("Aw! Better luck next time!")
    else:
        fish = head.fish_name   
        print(f"I caught a {fish}!")
        return head.next


fish_list = Node("Carp", Node("Dace", Node("Cherry Salmon")))
empty_list = None

print_linked_list(fish_list)
print_linked_list(catch_fish(fish_list))
print(catch_fish(empty_list))