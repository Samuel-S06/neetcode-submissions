class Solution:

    def encode(self, strs: List[str]) -> str:
        complete = ""
        for s in strs:
            length = len(s) #int
            complete = complete + str(length) + "#" + s
        return complete


    def decode(self, s: str) -> List[str]:
        li = []
        i = 0
        start_index = 0
        final_index = 0

        while i < len(s):
            num_str = ""
            while s[i] != "#":
                num_str += s[i]
                i += 1

            i += 1
            num_int = int(num_str)

            start_index = i
            final_index = start_index + num_int

            li.append(s[start_index : final_index])
            i = final_index

        return li

