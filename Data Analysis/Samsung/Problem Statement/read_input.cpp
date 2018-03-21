#include <bits/stdc++.h>

using namespace std;

void operate() {

}

int main(int argc, char const *argv[])
{
	ifstream file("Testing/input.cpp");
	string linebuffer;

	while (file && getline(file, linebuffer)) {
		if (linebuffer.length() == 0) continue;
		cout << linebuffer;
	}
}