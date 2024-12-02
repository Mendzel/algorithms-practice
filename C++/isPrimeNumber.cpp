#include <iostream>
#include <cmath>

bool is_number_primal(unsigned int);

int main()
{
    using namespace std;
    cout << "Podaj dodatnią liczbę całkowitą: ";
    unsigned int number;
    cin >> number;
    bool is_primal = is_number_primal(number);

    if (is_primal)
    {
        cout << endl
             << "Podana liczba jest liczbą pierwszą." << endl;
    }
    else
    {
        cout << endl
             << "Podana liczba nie jest liczbą pierwszą." << endl;
    }

    return 0;
}

bool is_number_primal(unsigned int num)
{
    if (num < 2)
    {
        return false;
    }

    int i = 2;
    do
    {
        if (num % i == 0 && num != i)
        {
            return false;
        }
        i++;
    } while (i <= sqrt(num));

    return true;
}