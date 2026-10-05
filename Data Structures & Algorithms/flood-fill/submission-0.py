class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        orig = image[sr][sc]
        if orig == color:
            return image

        validRows = len(image) - 1
        validColumns = len(image[0]) - 1

        # Since we are returning the same array we can modify that directly.
        def dfs(sr, sc, vr, vc):
            if sr > vr or sr < 0:
                return
            if sc > vc or sc < 0:
                return
            
            if image[sr][sc] != orig:
                return

            image[sr][sc] = color

            dfs(sr+1, sc, validRows, validColumns)
            dfs(sr-1, sc, validRows, validColumns)
            dfs(sr, sc+1, validRows, validColumns)
            dfs(sr, sc-1, validRows, validColumns)

        dfs(sr,sc, validRows, validColumns)
        return image
