# Definition for a point
class Point:
    def __init__(self, a=0, b=0):
         self.x = a
         self.y = b

class Solution:
    # @param points, a list of Points
    # @return an integer
    def maxPoints(self, points):
        kdict = {}
        if len(points)<=2:
            return len(points)

        coincides = {}
        unifypoints = []
        for point in points:              
            key = "%.4f,%.4f"%(point.x,point.y)
            if key not in coincides:
                coincides[key] = 1
                unifypoints.append(point)
            else:        
                coincides[key] += 1

#        print coincides
        if len(unifypoints) <= 2:
            return len(points)
        for i in range(len(unifypoints)):
            for j in range(i+1,len(unifypoints)):
                p1 = unifypoints[i]
                p2 = unifypoints[j]                
                if p1.x == p2.x:
                    kkey = "vertical"+str(p1.x)
                else:
                    k = float(p1.y-p2.y)/float(p1.x-p2.x)
                    b = p1.y - k*p1.x
                    kkey = "%.4f,%.4f"%(k,b)
 
                p1_r = coincides["%.4f,%.4f"%(p1.x,p1.y)] 
                p2_r = coincides["%.4f,%.4f"%(p2.x,p2.y)] 
                if kkey in kdict:
                    kdict[kkey][p1]=p1_r
                    kdict[kkey][p2]=p2_r
                else:
                    kdict[kkey] = {p1:p1_r,p2:p2_r}
        maxvalue = -1
        for key,value in kdict.items():
            maxpoints = 0
            for point,weight in value.items():
                maxpoints += weight
            maxvalue = max(maxvalue,maxpoints)
        return maxvalue


sol = Solution()
points = [Point(1,1),Point(2,2),Point(3,3), Point(7,10),Point(5,1),Point(4,4),Point(5,5)]
print sol.maxPoints(points)
points = [Point(-240,-657),Point(-27,-188),Point(-616,-247),Point(-264,-311),Point(-352,-393),Point(-270,-748),Point(3,4),Point(-308,-87),Point(150,526),Point(0,-13),Point(-7,-40),Point(-3,-10),Point(-531,-892),Point(-88,-147),Point(4,-3),Point(-873,-555),Point(-582,-360),Point(-539,-207),Point(-118,-206),Point(970,680),Point(-231,-47),Point(352,263),Point(510,143),Point(295,480),Point(-590,-990),Point(-236,-402),Point(308,233),Point(-60,-111),Point(462,313),Point(-270,-748),Point(-352,-393),Point(-35,-148),Point(-7,-40),Point(440,345),Point(388,290),Point(270,890),Point(10,-7),Point(60,253),Point(-531,-892),Point(388,290),Point(-388,-230),Point(340,85),Point(0,-13),Point(770,473),Point(0,73),Point(873,615),Point(-42,-175),Point(-6,-8),Point(49,176),Point(308,222),Point(170,27),Point(-485,-295),Point(170,27),Point(510,143),Point(-18,-156),Point(-63,-316),Point(-28,-121),Point(396,304),Point(472,774),Point(-14,-67),Point(-5,7),Point(-485,-295),Point(118,186),Point(-154,-7),Point(-7,-40),Point(-97,-35),Point(4,-9),Point(-18,-156),Point(0,-31),Point(-9,-124),Point(-300,-839),Point(-308,-352),Point(-425,-176),Point(-194,-100),Point(873,615),Point(413,676),Point(-90,-202),Point(220,140),Point(77,113),Point(-236,-402),Point(-9,-124),Point(63,230),Point(-255,-118),Point(472,774),Point(-56,-229),Point(90,228),Point(3,-8),Point(81,196),Point(970,680),Point(485,355),Point(-354,-598),Point(-385,-127),Point(-2,7),Point(531,872),Point(-680,-263),Point(-21,-94),Point(-118,-206),Point(616,393),Point(291,225),Point(-240,-657),Point(-5,-4),Point(1,-2),Point(485,355),Point(231,193),Point(-88,-147),Point(-291,-165),Point(-176,-229),Point(154,153),Point(-970,-620),Point(-77,33),Point(-60,-111),Point(30,162),Point(-18,-156),Point(425,114),Point(-177,-304),Point(-21,-94),Point(-10,9),Point(-352,-393),Point(154,153),Point(-220,-270),Point(44,-24),Point(-291,-165),Point(0,-31),Point(240,799),Point(-5,-9),Point(-70,-283),Point(-176,-229),Point(3,8),Point(-679,-425),Point(-385,-127),Point(396,304),Point(-308,-352),Point(-595,-234),Point(42,149),Point(-220,-270),Point(385,273),Point(-308,-87),Point(-54,-284),Point(680,201),Point(-154,-7),Point(-440,-475),Point(-531,-892),Point(-42,-175),Point(770,473),Point(118,186),Point(-385,-127),Point(154,153),Point(56,203),Point(-616,-247)]
print sol.maxPoints(points)
print sol.maxPoints([Point(1,1),Point(2,1),Point(3,1),Point(0,0)])
print sol.maxPoints([Point(1,1)])
print sol.maxPoints([])
print sol.maxPoints([Point(1,1),Point(1,1),Point(1,1)])
print sol.maxPoints([Point(1,1),Point(0,0),Point(0,0)])
print sol.maxPoints([Point(1,1),Point(0,0),Point(3,1),Point(4,2)])
