def main(nums):
    nums = sorted(nums)
    return nums


for _ in range(int(input())):
    numbers = input().split()
    print(main(numbers))