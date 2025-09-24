class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1_list = version1.split('.')
        version2_list = version2.split('.')
        both_revisions = min(len(version1_list), len(version2_list))
        for index in range(both_revisions):
            version1_num = int(version1_list[index])
            version2_num = int(version2_list[index])
            if version1_num < version2_num:
                return -1
            if version1_num > version2_num:
                return 1

        if len(version1_list) == len(version2_list):
            return 0

        longer_version = 1 if len(version1_list) > len(version2_list) else 2
        longer_version_list = version1_list if longer_version == 1 else version2_list
        version_difference = abs(len(version1_list) - len(version2_list))

        for num in range(version_difference):
            version_num = int(longer_version_list[-num - 1])
            if version_num != 0:
                return 1 if longer_version == 1 else -1

        return 0

