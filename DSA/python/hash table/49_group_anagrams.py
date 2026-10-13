class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        group = dict()

        for i in range(len(strs)):
            ordered = "".join(sorted(strs[i]))

            if not group.get(ordered):
                group[ordered] = list()

            group[ordered].append(strs[i])

        return [groups for groups in group.values()]