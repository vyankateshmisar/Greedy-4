"""
Problem : 1

Time Complexity : 

Approach 1 - O(nlogn)
Approach 2 - O(m*n) 

Space Complexity : O(1)

Did this code successfully run on Leetcode : Yes
Any problem you faced while coding this : No

"""

# Minimum Path Form String formation

# Approach - 1

import bisect
class Solution(object):
    def shortestWay(self, source, target):
        """
        :type source: str
        :type target: str
        :rtype: int
        """
        if not source:
            return -1
        sl=len(source)
        tl=len(target)
        count=1
        hmap={}
        for i in range(sl):
            if source[i] not in hmap:
                hmap[source[i]]=[]
            hmap[source[i]].append(i)
        sp=0
        tp=0
        while tp<tl:
            tChar=target[tp]
            if tChar not in hmap:
                return -1
            li=hmap[tChar]
            k = bisect.bisect_left(li, sp)
            # when no such index found
            if k==len(li):
                # reset the source pointer
                sp=0
                # increase the counter
                count+=1
            else:
                sp=li[k]
                sp+=1
                tp+=1
        return count


# Approach - 2

class Solution(object):
    def shortestWay(self, source, target):
        """
        :type source: str
        :type target: str
        :rtype: int
        """
        if not source:
            return -1
        sl=len(source)
        tl=len(target)
        count=1
        hset=set()
        for i in range(sl):
            hset.add(source[i])
        sp=0
        tp=0
        while tp<tl:
            if sp==sl:
                sp=0
                count+=1
            # sChar=source[sp]
            tChar=target[tp]
            if tChar not in hset:
                return -1
            if source[sp]==tChar:

                tp+=1
            sp+=1
        return count