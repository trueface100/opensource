#include <iostream>
#include<map>
#include<vector>
#include<algorithm>

using namespace std;
map<int, int> m;

void array_to_map(int* input, int len_input) {
	for (int i = 0; i < len_input; i++) {
		if (m.find(input[i]) == m.end()) {
			m.insert({ input[i],1 });
		}
		else {
			m[input[i]] += 1;
		}
	}
}
bool cmp(const pair<int, int>& a, const pair<int, int>& b) {
	if (a.second == b.second) return a.first < b.first;
	return a.second < b.second;
}


int main() {
	int size;
	cin >> size;

	int N;
	cin >> N;

	int* input = new int[size];
	for (int idx = 0; idx < size; idx++) {
		cin >> input[idx];
	}
	int vec_size;
	array_to_map(input, size);

	vector<pair<int, int>> vec(m.begin(), m.end());
	sort(vec.begin(), vec.end(), cmp);
	vec_size = vec.size();
	//reverse(vec.begin(), vec.end());
	cout << vec_size << endl;
	cout << vec[vec_size - 1].first << " " << vec[vec_size - N].first << endl;
	delete[] input;
	return 0;
	
}