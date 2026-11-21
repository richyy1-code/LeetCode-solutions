class Solution:
    def isValid(self, s: str) -> bool:
        bracks = {')':'(', ']':'[', '}': '{'}
        brack_list = []
        for brack in s:
            if brack in bracks and brack_list:
                if bracks[brack] == brack_list[-1]:
                    brack_list.pop()
                else:
                    return False
            else:
                brack_list.append(brack)
        return True if len(brack_list) == 0 else False











        # bracks_list = []
        # bracks_dict = {')':'(', ']':'[', '}':'{'}

        # for brack in s:
        #     if bracks_list and brack in bracks_dict:
        #         if bracks_dict[brack] == bracks_list[0]:
        #             bracks_list.pop(0)
        #         else:
        #             return False
        #     else:
        #         bracks_list.insert(0,brack)
        # return True if not bracks_list else False
        