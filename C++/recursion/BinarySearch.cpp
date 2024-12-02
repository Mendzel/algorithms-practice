#include <iostream>

bool binarySearch(int[], int, int, int);

int main()
{
    using namespace std;
    int nums[] = {1, 2, 5, 8, 9, 11, 32, 55, 100};
    int answer;
    cout << "Podaj wartość której szukamy w tablicy: ";
    cin >> answer;

    int leftIndex = 0;
    int rightIndex = (sizeof(nums) / sizeof(nums[0])) - 1;

    bool isAnswerInArray = binarySearch(nums, leftIndex, rightIndex, answer);

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

bool binarySearch(int array[], int start, int end, int answer)
{
    if (start > end)
        return false;

    int middle = (start + end) / 2;

    if (array[middle] == answer)
        return true;

    if (array[middle] < answer)
    {
        return binarySearch(array, middle + 1, end, answer);
    }
    else
    {
        return binarySearch(array, start, middle - 1, answer);
    }
}