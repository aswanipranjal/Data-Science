#include <bits/stdc++.h>

using namespace std;

int main(int argc, char const *argv[])
{
	ifstream file(argv[1]);
	string linebuffer;

	while (file && getline(file, linebuffer)) {
		if (linebuffer.length() == 0) continue;
		cout << "line";
	}
}