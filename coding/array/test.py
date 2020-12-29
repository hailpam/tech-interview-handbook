
def product_array(nums):
    prefix = [1 for i in range(len(nums))]
    i = 1
    while i < len(nums):
        prefix[i] = prefix[i-1]*nums[i-1]
        i += 1

    postfix = [1 for i in range(len(nums))]
    i = len(nums) - 2
    while i >= 0:
        postfix[i] = postfix[i+1]*nums[i+1]
        i -= 1
    
    prods = []
    for i, _ in enumerate(nums):
        prods.append(prefix[i]*postfix[i])
    
    return prods

def product_array_recursive(nums, n, left=1, idx=0):
    if idx == n:
        return 1
    curr = nums[idx]
    right = product_array_recursive(nums, n, left*nums[idx], idx+1)
    nums[idx] = left * right
    
    return curr * right

def main():
    nums = [1, 2, 3, 4]
    print(product_array(nums))
    
    product_array_recursive(nums, len(nums))
    print(nums)

if __name__ == '__main__':
    main()
