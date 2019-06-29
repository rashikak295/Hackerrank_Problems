import collections
import numpy as np
import collections
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        courses = collections.defaultdict(set)
        for p in prerequisites:
            courses[p[0]].add(p[1])
        
        complete = set()
        for n in range(numCourses):
            if n not in courses.keys():
                complete.add(n)
                
        flag = True
        while flag == True:
            flag = False
            for c in courses.keys():
                if len(courses[c]) != 0:
                    temp = []
                    for each in courses[c]:
                        if each in complete:
                            temp.append(each)
                            flag = True
                    if temp != []:
                        for t in temp:
                            courses[c].remove(t)
                else:
                    del courses[c]
                    complete.add(c)
                    flag = True
        
        if len(complete) == numCourses:
            return True
        return False