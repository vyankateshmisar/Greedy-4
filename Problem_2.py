"""
Problem : 2

Time Complexity : O(n)

Space Complexity : 
Approach 1 - O(1)
Approach 2 - O(n)

Did this code successfully run on Leetcode : Yes
Any problem you faced while coding this : No

"""

# Equal Row From Minimum Domino Rotations 

# Approach - 1

class Solution(object):
    def minDominoRotations(self, tops, bottoms):
        """
        :type tops: List[int]
        :type bottoms: List[int]
        :rtype: int
        """
        result=self.check(tops,bottoms,tops[0])
        if result!=-1:
            return result
        return self.check(tops,bottoms,bottoms[0])
    
    def check(self,tops,bottoms,target):
        aRot=0
        bRot=0
        for i in range(len(tops)):
            t=tops[i]
            b=bottoms[i]
            if t!=target and b!=target:
                return -1
            if t!=target:
                aRot+=1
            if b!=target:
                bRot+=1
        return min(aRot,bRot)
    

# Approach - 2

class Solution(object):
    def minDominoRotations(self, tops, bottoms):
        """
        :type tops: List[int]
        :type bottoms: List[int]
        :rtype: int
        """
        hmap={}
        target=-1
        maxx=0
        for i in range(len(tops)):
            t=tops[i]
            if t not in hmap:
                hmap[t]=0
            hmap[t]+=1
            maxx=max(maxx,hmap[t])
            b=bottoms[i]
            if b not in hmap:
                hmap[b]=0
            hmap[b]+=1
            maxx=max(maxx,hmap[b])
        for num in hmap.keys():
            if hmap[num]==maxx:
                target=num
        aRot=0
        bRot=0
        for i in range(len(tops)):
            if tops[i]!=target and bottoms[i]!=target:
                return -1
            if tops[i]!=target:
                aRot+=1
            if bottoms[i]!=target:
                bRot+=1
        return min(aRot,bRot)