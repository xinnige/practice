
class Solution(object):
    def _overlapped(self, p1, p2, q1, q2):
        # p1, p2 always starts left/lower than q1, q2
        if p2 < q1:
            return 0
        if q2 < p2:
            return q2-q1
        return p2-q1

    def overlapped(self, p1, p2, q1, q2 ):
        if p1 < q1:
            # p1, p2 starts left/lower than q1, q2
            return self._overlapped(p1, p2, q1, q2)
        else:
            # p1, p2 starts righter/top than q1, q2
            return self._overlapped(q1, q2, p1, p2)

    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        width = self.overlapped(A, C, E, G)
        height = self.overlapped(B, D, F, H)
        area1 = (C-A) * (D-B)
        area2 = (G-E) * (H-F)
        return area1 + area2 - width * height
        
        

sol=Solution()
(A, B) = (1, 1)
(C, D) = (1, 1)
(E, F) = (0, 0)
(G, H) = (2, 2)
sol.computeArea(A, B, C, D, E, F, G, H)

