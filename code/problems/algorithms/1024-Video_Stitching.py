# -*- coding: utf-8 -*-
class Solution:

    #1. 按照开始时间排序
    def videoStitching(self, clips, T: int) -> int:
        size = 101
        slimClips=[None] * (size)
        slimClipsReplica = [None] * (size)
        for i in range(len(clips)):
            e = clips[i]
            start=e[0]
            end=e[1]
            if slimClips[start] == None:
                slimClips[start] = e
            else:
                if slimClips[start][1]-slimClips[start][0] < e[1] - e[0]:
                    slimClips[start] = e
            if slimClipsReplica[end] == None:
                slimClipsReplica[end] = e
            else:
                if slimClipsReplica[end][1]-slimClipsReplica[end][0] < e[1] - e[0]:
                    slimClipsReplica[end] = e

        intersect = [v for v in slimClips if v in slimClipsReplica and v is not None]

        index = 0
        currentClip=intersect[index]
        newSlimClips = [None] * len(intersect)
        for i in range(len(intersect)):
            e = intersect[i]
            if i == index:
                newSlimClips[index] = e
                currentClip = e
                continue

            if e[0] >= currentClip[0] and e[0] <= currentClip[1]:
                if newSlimClips[index + 1] == None:
                    newSlimClips[index + 1] = e
                elif e[1] >  newSlimClips[index + 1][1]:
                    newSlimClips[index + 1] = e
            else:
                index += 1
                currentClip=newSlimClips[index]
                if currentClip is None:
                    break
                newSlimClips[index + 1] = e

        newSlimClips = [v for v in newSlimClips if v is not None]

        # print("intersect:",intersect)
        print("newSlimClips:", newSlimClips)

        result = -1
        if newSlimClips[0][0] != 0 or newSlimClips[len(newSlimClips)-1][1] < T:
            result = -1
        else:
            for i in range(len(newSlimClips)):
                e = newSlimClips[i]
                if e[1] >= T:
                    result = i + 1
                    break
        return result



# clips = [[0,1],[6,8],[0,2],[5,6],[0,4],[0,3],[6,7],[1,3],[4,7],[1,4],[2,5],[2,6],[3,4],[4,5],[5,7],[6,9]]
# T = 9
# result=Solution().videoStitching(clips, T)
# print(result)
#
# clips = [[0,2],[4,6],[8,10],[1,9],[1,5],[5,9]]
# T = 10
# result=Solution().videoStitching(clips, T)
# print(result)
#
# clips = [[0,1],[1,2]]
# T = 5
# result=Solution().videoStitching(clips, T)
# print(result)
#
# clips =  [[0,4],[2,8]]
# T = 5
# result=Solution().videoStitching(clips, T)
# print(result)

# clips =[[5,7],[1,8],[0,0],[2,3],[4,5],[0,6],[5,10],[7,10]]
# T=5
# result=Solution().videoStitching(clips, T)
# print(result)

# clips =[[8,10],[17,39],[18,19],[8,16],[13,35],[33,39],[11,19],[18,35]]
# T=20
# result=Solution().videoStitching(clips, T)
# print(result)

# clips=[[0,5],[1,6],[2,7],[3,8],[4,9],[5,10],[6,11],[7,12],[8,13],[9,14],[10,15],[11,16],[12,17],[13,18],[14,19],[15,20],[16,21],[17,22],[18,23],[19,24],[20,25],[21,26],[22,27],[23,28],[24,29],[25,30],[26,31],[27,32],[28,33],[29,34],[30,35],[31,36],[32,37],[33,38],[34,39],[35,40],[36,41],[37,42],[38,43],[39,44],[40,45],[41,46],[42,47],[43,48],[44,49],[45,50],[46,51],[47,52],[48,53],[49,54]]
# T=50
# result=Solution().videoStitching(clips, T)
# print(result)

clips=[[11,28],[35,40],[28,38],[0,10],[37,39],[40,40],[18,34],[32,38],[14,36],[33,36]]
T=8
result=Solution().videoStitching(clips, T)
print(result)
