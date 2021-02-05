import random

def list_sort(sample_num):
    n = len(sample_num)
    for i in range(n):
        sorted = True
        for j in range(n - i - 1):
            if sample_num[j] > sample_num[j + 1]:
                sample_num[j], sample_num[j + 1] = sample_num[j + 1], sample_num[j]
                sorted = False
        if sorted:
            break
    print(sample_num)
    return sample_num


def main():
    sample_num = random.sample(range(0,100), 10)
    print(sample_num)
    list_sort(sample_num)


if __name__ == "__main__":
	main()
