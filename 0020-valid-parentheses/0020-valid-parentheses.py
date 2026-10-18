class Solution:
    def isValid(self, s: str) -> bool:
        brack_dict = {"(":1, ")":1, "{":2, "}":2, "[":3, "]":3}
        bracks_list = []
        for brack in s:
            if brack == "(" or brack == "{" or brack == "[":
                bracks_list.insert(0,brack)
            else:
                if len(bracks_list) > 0:
                    if brack_dict[brack] == brack_dict[bracks_list[0]]:
                        bracks_list.remove(bracks_list[0])
                    else:
                        return False
                else:
                    return False
        if not bracks_list:
            return True
        else:
            return False

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
        