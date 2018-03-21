#include <bits/stdc++.h>
using namespace std;

int KMP(string X, string Y)
{
	int m = X.length();
	int n = Y.length();
 
	if (n == 0)
	{
		cout << "Pattern occurs with shift 0";
		return 0;
	}
	if (m < n)
	{
		cout << "Pattern not found";
		return -1;
	}
 
	int next[n + 1];
 
	for (int i = 0; i < n + 1; i++)
		next[i] = 0;
 
	for (int i = 1; i < n; i++)
	{
		int j = next[i + 1];
		while (j > 0 && Y[j] != Y[i])
			j = next[j];
		if (j > 0 || Y[j] == Y[i])
			next[i + 1] = j + 1;
	}
 
	for (int i = 0, j = 0; i < m; i++)
	{
		if (X[i] == Y[j])
		{
			if (++j == n) {
				return i - j + 1;
			}
		} else if (j > 0) {
			j = next[j];
			i--;
		}
	}
}

int main() {
	string name = "ABCDABCD";
	string key = "egufgeb";
	cout << KMP(name, key) << endl;
	string key2 = "DAB";
	cout << KMP(name, key2) << endl;
}