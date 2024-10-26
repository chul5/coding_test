#include <iostream>
using namespace std;

int main() {
    int T;
    cin >> T;

    int count0[41] = {1, 0};
    int count1[41] = {0, 1};  

    for (int i = 2; i <= 40; i++) {
        count0[i] = count0[i - 1] + count0[i - 2];
        count1[i] = count1[i - 1] + count1[i - 2];
    }

    while (T--) {
        int N;
        cin >> N;
        cout << count0[N] << " " << count1[N] << endl;
    }

    return 0;
}