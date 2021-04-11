https://leetcode.com/problems/find-duplicate-file-in-system


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_map = dict()
        
        for path in paths:
            info_list = path.split(" ")
            directory_path = info_list[0]
            files = info_list[1:]
            
            for file in files:
                file = file.split("(")
                file_name = file[0]
                content = file[1]
                
                directory_path_file_name = directory_path + "/" + file_name
                
                if content not in content_map:
                    content_map[content] = [directory_path_file_name]
                    
                else: # content is in content_map
                    content_map[content].append(directory_path_file_name)
                
    
        return [content_map[key] for key in content_map if len(content_map[key]) >= 2]

