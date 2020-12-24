class Solution(object):
    def floodFill(self, image, sr, sc, newColor, seen = {}):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        if tuple([sr,sc]) in seen:
          return image
        seen[tuple([sr,sc])] = True
        neighbors = self.get_neighbors(image,sr,sc,image[sr][sc])
        image[sr][sc] = newColor
        
        for neighbor in neighbors:
            self.floodFill(image,neighbor[0],neighbor[1],newColor,seen)
            
        return image
    
    def get_neighbors(self,image,r,c,color):
        neighbors = []
        directions = [[0,-1],[-1,0],[0,1],[1,0]]
        
        for direc in directions:
            new_pos = [r+direc[0],c+direc[1]]
            
            if new_pos[0] < 0 or new_pos[0] >= len(image):
                continue
            if new_pos[1] < 0 or new_pos[1] >= len(image[0]):
                continue 
            else:
                if image[new_pos[0]][new_pos[1]] == color:
                    neighbors.append(new_pos)
                    
        return neighbors

solution = Solution()
print(solution.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))