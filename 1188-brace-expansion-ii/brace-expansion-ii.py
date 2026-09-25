class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        # Stack maintains pairs of (group_union_set, current_product_set)
        # union_set accumulates results separated by commas ','
        # product_set accumulates results combined by concatenation
        stack = []
        union_set = set()
        product_set = {""}

        for char in expression:
            if char.isalpha():
                # Concatenate current letter with existing combinations in product_set
                product_set = {s + char for s in product_set}
            elif char == '{':
                # Push current scope state to stack and reset for the new nested group
                stack.append((union_set, product_set))
                union_set = set()
                product_set = {""}
            elif char == ',':
                # A comma finishes a product expression within the current group
                union_set.update(product_set)
                product_set = {""}
            elif char == '}':
                # Complete the current inner union set
                union_set.update(product_set)
                
                # Pop previous scope state
                prev_union_set, prev_product_set = stack.pop()
                
                # Multiply the previous product set with the newly evaluated inner set
                product_set = {s1 + s2 for s1 in prev_product_set for s2 in union_set}
                union_set = prev_union_set

        # Final merge for remaining items in product_set
        union_set.update(product_set)
        
        # Return unique words in lexicographical sorted order
        return sorted(list(union_set))