#include <iostream>

bool binarySearch(int[], int, int, int, int);

int main()
{
    using namespace std;
    int nums[] = {1, 2, 5, 8, 9, 11, 32, 55, 100};
    int answer;
    cout << "Podaj wartość której szukamy w tablicy: ";
    cin >> answer;

    int leftIndex = 0;
    int rightIndex = (sizeof(nums) / sizeof(nums[0])) - 1;
    int middleIndex = (leftIndex + rightIndex) / 2;

    bool isAnswerInArray = binarySearch(nums, leftIndex, middleIndex, rightIndex, answer);

    if (isAnswerInArray)
    {
        cout << "Podana wartość znajduje się w tablicy";
    }
    else
    {
        cout << "Podana wartość nie znajduje się w tablicy";
    }

    return 0;
}

bool binarySearch(int array[], int start, int middle, int end, int answer)
{
    while (start < end)
    {
        if (array[middle] == answer)
        {
            return true;
        }
        else if (array[middle] < answer)
        {
            start = middle + 1;
            middle = (start + end) / 2;
        }
        else
        {
            end = middle - 1;
            middle = (start + end) / 2;
        }
    }

    return false;
}