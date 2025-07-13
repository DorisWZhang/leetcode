class Solution:
    def applySubstitutions(self, replacements: List[List[str]], text: str) -> str:

        replacements_dict = {}
        for i in replacements:
            replacements_dict[i[0]] = i[1]
        

        def apply(i, s):
            result = ""
        
            while i < len(s):
                if s[i] == '%': # fetch replacement
                    i+=1
                    placeholder = "" 
                    while s[i] != '%':
                        placeholder += s[i]
                        i += 1
                    i +=1 # skip ending %
                    # retrieve replacement
                    replacement = replacements_dict[placeholder]
                    if '%' in replacement: # if requires more cleanup
                        # cleaned up replacement
                        replacement = apply(0,replacement)
                    result += replacement
                    
                else:
                    result += s[i]
                    i +=1
                apply(i, s)
            return result
        return apply(0, text)
            