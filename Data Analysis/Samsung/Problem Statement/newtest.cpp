#include <bits/stdc++.h>
using namespace std;

int main() {
	string pattern = "Aba";
	string target = "AbBa";
	transform(pattern.begin(), pattern.end(), pattern.begin(), ::tolower);
	transform(target.begin(), target.end(), target.begin(), ::tolower);
	cout << target << " " << pattern;
	return 0;
 }