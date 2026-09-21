class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # counting method
        res = len(students) # number of students
        count = Counter(students) # counter of 1 and 0s

        for s in sandwiches:
            if count[s] > 0:
                res -= 1 # remove stuydent
                count[s] -= 1 # remove sandwich count
            else:
                break # we're out of the sandwiches
        return res # this is odd, what if later in sandwiches still a sandwich that matches? Does a break make more sense than continue?