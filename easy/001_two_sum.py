"""
LeetCode Problem 1: Two Sum (Easy)

Problem Statement:
Given an array of integers `nums` and an integer `target`, return the indices of the 
two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use 
the same element twice.

You can return the answer in any order.

Example 1:
-----------
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
-----------
Input: nums = [3, 2, 4], target = 6
Output: [1, 2]

Example 3:
-----------
Input: nums = [3, 3], target = 6
Output: [0, 1]

Constraints:
------------
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists.

Follow-up:
----------
Can you solve it in O(n) time complexity?
"""


"""
What is the Brute Force Solution?
---------------------------------
(Deneme Yanılma Yöntemi)
Brute-force yöntemi, bütün ihtimalleri tek tek deneme anlamına gelir.

📌 Örnek: Diyelim ki arkadaşının çantasının şifresini unuttun ama biliyorsun ki şifre 00 ile 99 arasında bir sayı.

👉 Ne yaparsın? Sırayla tüm sayıları denersin!

00 → Açılmadı ❌
01 → Açılmadı ❌
02 → Açılmadı ❌
...
42 → 🎉 Açıldı! ✅
Bu yöntem her zaman işe yarar çünkü bütün olasılıkları deneriz. Ama bazen çok zaman alabilir!

What is the HashMap Solution?
-----------------------------
(Sihirli Not Defteri)
Şimdi HashMap’i anlamak için bir sihirli not defterin olduğunu düşün.

📌 Örnek: Diyelim ki sınıftaki herkesin en sevdiği dondurma çeşidini hatırlamak istiyorsun.

Normalde tek tek herkese sorarak hatırlaman gerekir:

❓ "Ahmet'in en sevdiği dondurma neydi?"
❓ "Ayşe çikolata mı seviyordu?"

Ama eğer bir not defterine yazarsan:

Kişi	En Sevdiği Dondurma
--------------------------------
Ahmet	Çikolata
Ayşe	Vanilya
Mehmet	Çilek

👉 Artık direkt not defterine bakarak bulabilirsin!
"Ayşe'nin en sevdiği dondurma nedir?" sorusunun cevabını hemen bulursun!

Bu sistem programlamada HashMap olarak adlandırılır. Bir şeyi hızlıca bulmak için kullanılır!

"""

"""
Brute Force Solution:
--------------------
Time Complexity: O(n^2)
Space Complexity: O(1)
"""

from typing import List

def two_sum_brute_force(nums: List[int], target: int) -> List[int]:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


print(f'Brute Force Solution: {two_sum_brute_force([2, 7, 11, 15], 9)}')
print(f'Brute Force Solution: {two_sum_brute_force([3, 2, 4], 6)}')
print(f'Brute Force Solution: {two_sum_brute_force([3, 3], 6)}')


"""
HashMap Solution:
-----------------
Time Complexity: O(n)
Space Complexity: O(n)

"""

def two_sum_hashmap(nums: List[int], target: int) -> List[int]:
    num_map = {} 
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i


print(f'hashMap Solution: {two_sum_hashmap([2, 7, 11, 15], 26)}')
print(f'hashMap Solution: {two_sum_hashmap([3, 2, 4], 7)}')
print(f'hashMap Solution: {two_sum_hashmap([3, 3], 6)}')


