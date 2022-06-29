#include <iostream>
#include <vector>

using namespace std;

void printResult(vector<int> a) {
    while (!a.empty()) {
        cout << a.back() << ",";
        a.pop_back();
    }
    cout << endl;
}

int findSolution(int nu, int m, int sum) {
    static int y = 0;
    static vector<int> result;
    for (int i = m; i > 0; i--) {
        sum += i;
        result.push_back(i);
        if (sum == nu) {
            y++;
            cout << "way" << y << ":";
            printResult(result);
        } else if (sum < nu) {
            findSolution(nu, i, sum);

        }
        sum -= i;
        result.pop_back();

    }
    return y;
}

void findway(int nu, int de) {
    int way = findSolution(nu, de, 0);
    cout << "total way:" <<way;
}


int main() {
    findway(6, 3);
    return 0;

}
