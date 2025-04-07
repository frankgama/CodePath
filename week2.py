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

# ####            Week 2, Session 2           ####  

# from collections import Counter

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

# import re
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

# !/bin/python3

# import math
# import os
# import random
# import re
# import sys
# import ast



# Enter your code here. Read input from STDIN. Print output to STDOUT

# Complete the 'roman_to_int' function below.

# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.


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

# class Villager:
#     def __init__(self, name, species, personality, catchphrase):
#         self.name = name
#         self.species = species
#         self.personality = personality
#         self.catchphrase = catchphrase
#         self.furniture = []
#     def add_item(self, item_name):
#         valid = ["acoustic guitar", "ironwood kitchenette", "rattan armchair", "kotatsu", "cacao tree"]
#         if item_name in valid:
#             self.furniture.append(item_name)
# def of_personality_type(townies, personality_type):
#     return [villager.name for villager in townies if villager.personality == personality_type]

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

# class Node:
#     def __init__(self, fish_name, next=None):
#         self.fish_name = fish_name
#         self.next = next

# # For testing
# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.fish_name, end=" -> " if current.next else "\n")
#         current = current.next

# def catch_fish(head):
#     if head is None:
#         print("Aw! Better luck next time!")
#     else:
#         fish = head.fish_name   
#         print(f"I caught a {fish}!")
#         return head.next


# fish_list = Node("Carp", Node("Dace", Node("Cherry Salmon")))
# empty_list = None

# print_linked_list(fish_list)
# print_linked_list(catch_fish(fish_list))
# print(catch_fish(empty_list))

# class ListNode(object):
#     def __init__(self, val =0, next=None):
#         self.val = val
#         self.next = next
# class Solution(object):
#     def reverseList(self, head):
#         self.head = head
        
#         curr = self.head
#         prev = None
#         while curr:
#             temp_node = curr.next
#             curr.next = prev
#             prev = curr
#             curr = temp_node
#         self.head = prev
#         return self.head
# # Helper function to print the list
# def print_list(head):
#     curr = head
#     while curr:
#         print(curr.val, end=" -> ")
#         curr = curr.next
#     print("None")

# # Create linked list: 1 -> 2 -> 3 -> 4 -> None
# head = ListNode(1)
# head.next = ListNode(2)
# head.next.next = ListNode(3)
# head.next.next.next = ListNode(4)

# print("Original list:")
# print_list(head)

# # Reverse the linked list
# sol = Solution()
# reversed_head = sol.reverseList(head)

# print("Reversed list:")
# print_list(reversed_head)

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# # For testing
# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.value, end=" -> " if current.next else "\n")
#         current = current.next

# def find_max(head):
#     # if empty list, return 0
#     if not head:
#         return None
    
#     #initialize a max val, initialize curr node
#     maxval= float('-inf')
#     curr = head

#     #iterate through list, keeping track of max val
#     while curr:
#         if curr.value >= maxval:
#             maxval = curr.value
#         curr = curr.next   
#     #return maxval  
#     return maxval


# head1 = Node(5, Node(6, Node(7, Node(8))))

# # Linked List: 5 -> 6 -> 7 -> 8
# print(find_max(head1))

# head2 = Node(5, Node(8, Node(6, Node(7))))

# # Linked List: 5 -> 8 -> 6 -> 7
# print(find_max(head2))

# def delete_dupes(head):
#     #initialize dummy node 
#     dummy = Node(0)
#     dummy.next = head
#     #initialize the pointers
#     curr = head
#     prev = dummy 
#     #iterate through the linked list
#     while curr: 
#         #check if the current node has duplicates
#         if curr.next and curr.value == curr.next.value: 
#             #skip the nodes with that value
#             duplicate_val = curr.value
#             while curr and curr.value == duplicate_val: 
#                 curr = curr.next
#             #update your pointers
#             prev.next = curr
#         else: 
#             prev = curr
#             curr = curr.next
    
#     return dummy.next
#     #return the list


# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# def has_cycle(head):
#     #if empty list
#     if head is None:
#         return False
#     if head.next is None:
#         return False

#     #initiate fast and slow pointers
#     fast = head
#     slow = head.next

#     #iterate through linked list with fast and slow
#     while fast:
#         #if fast and slow are equal, return true
#         if fast == slow:
#             return True
#         else:
#             fast = fast.next.next
#             slow = slow.next
#      #if you reach the end, return false
#     return False

# peach = Node("Peach", Node("Luigi", Node("Mario", Node("Toad"))))

# print(has_cycle(peach))


# class Player:
#     def __init__(self, character, kart):
#         self.character = character
#         self.kart = kart
#         self.items = []

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# # For testing
# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.value, end=" -> " if current.next else "\n")
#         current = current.next

# def arr_to_ll(arr):
#     #check if there is an array, if not return None
#     if arr is None:
#         return None
#     head = None
#     curr = None
#     prev = None

#     #iterate through array by index
#     for i in range(len(arr)):
    
#     #if first index, create head node
#         if i == 0:
#             head = Node(arr[i].character)
#             prev = head
#         else:
#             #otherwise, create node
#             curr = Node(arr[i].character)
            
#             #link previous to curr
#             prev.next = curr
#             #set curr to prev
#             prev = curr


#     return head
   

# mario = Player("Mario", "Mushmellow")
# luigi = Player("Luigi", "Standard LG")
# peach = Player("Peach", "Bumble V")

# print_linked_list(arr_to_ll([mario, luigi, peach]))
# print_linked_list(arr_to_ll([peach]))

# class Node:
#     def __init__(self, value=None, next=None):
#         self.value = value
#         self.next = next

# # For testing
# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.value, end=" -> " if current.next else "\n")
#         current = current.next

# # Function with a bug!
# def remove_by_value(head, val):
#     if not head:
#         return None
#     if head.value == val:
#         return head.next  

#     current = head
#     while current.next:
#         if current.next.value == val:
#             current = current.next.next  
#             return head  
#         current = current.next

#     return head

# head = Node("Daisy", Node("Mario", Node("Waluigi", Node("Baby Peach"))))

# print_linked_list(remove_by_value(head, "Waluigi"))

# def count_layers(sandwich):
#     # if no list, return 0
#     if sandwich is None:
#         return 0
#     #if we have a list of length 1, return 1
#     if len(sandwich) == 1:
#         return 1
#     #we have a list greater than length 1, so we return the value plus the recursive value
#     return 1 + count_layers(sandwich[1])


# sandwich1 = ["bread", ["lettuce", ["tomato", ["bread"]]]]

# sandwich2 = ["bread", ["cheese", ["ham", ["mustard", ["bread"]]]]]

# print(count_layers(sandwich1))
# print(count_layers(sandwich2))

# def reverse_orders(orders):
#     # if the string is empty, return empty string
#     if orders is None:
#         return ""

#     order = orders.split()

#     # print(order)

#     if len(order) == 1:
#         return order[-1]

#     neworders = " ".join(order[0:-1])
#     # print(neworders)
#     return order[-1] + " " + reverse_orders(neworders)

    

# print(reverse_orders("Bagel Sandwich Coffee"))

# def can_split_coffee(coffee, n):
#     if len(coffee) == 1:
#         if coffee[0] % n == 0:
#             return True
#         return False
#     else:
#         return can_split_coffee(coffee[1:], n)

# print(can_split_coffee([4, 4, 8], 2))
# print(can_split_coffee([5, 10, 15], 4))

# class Node:
#     def __init__(self, value, next=None):
#         self.value = value
#         self.next = next

# # For testing
# def print_linked_list(head):
#     current = head
#     while current:
#         print(current.value, end=" -> " if current.next else "\n")
#         current = current.next

# def merge_orders(sandwich_a, sandwich_b)
#     pass

#### Hackerank####

# def reverse_between(head, left, right):
#     #check there is a valid head
#     if head is None:
#         return
#     #create temp head
#     curr = head
#     prev = None
#     #iterate through the list until you find the left node
#     while curr:
#         #make this the new head
#         if curr.val == left:
#             head = curr
#             #if there is a next node, update curr
#             if curr.next:
#                 prev = curr
#                 curr = curr.next
#             else:
#                 #otherwise we reached the end of the list, return head   
#                 return head
#         #if curr node is less than or equal to right as is the next one, keep updating
#         elif curr.val <= right:
#             if curr.next:
#                 prev = curr
#                 curr = curr.next
#         #if curr node is less than or equal to right, but next is greater
#         elif curr.val > right:
#             prev.next = None
#             return head
#             #set curr.next to none, finishing the list
        
# def find_affordable_ticket(prices, budget):
#     if prices is None:
#         return -1   
#     left = 0
#     right = len(prices) - 1
#     midpoint = len(prices)//2
    

#     while left < right:
#         # print(left)
#         # print(right)
#         # print(midpoint)
#         if prices[midpoint] < budget:
            
#             left = midpoint + 1
#             midpoint = (left + right)//2
#             # print(prices[left])
#         elif prices[midpoint] > budget:
            
#             right = midpoint - 1
#             midpoint = left + right // 2
#             # print(prices[right])
    
#     return left
        
# print(find_affordable_ticket([50, 75, 100, 150], 90))

def find_affordable_ticket(prices, budget):
    if prices is None:
        return -1
    left = 0
    right = len(prices) - 1
    #base case, left > right, return
    if left > right:
        return right

    #compute midpoint
    midpoint = left + right // 2

    #compare midpoint price with budet
    if prices[midpoint] > budget:
        find_affordable_ticket(prices[:midpoint], budget)
    
    find_affordable_ticket(prices[midpoint:], budget)
        
print(find_affordable_ticket([50, 75, 100, 150], 90))