#include <bits/stdc++.h>

using namespace std;

string operate(string input) {
	return input;
}

int main(int argc, char const *argv[])
{
	ifstream infile("Testing/input.txt");
	ofstream outfile("Testing/output.txt", ios::out);
	string linebuffer;

	while (infile && getline(infile, linebuffer)) {
		if (linebuffer.length() == 0) continue;
		string temp5 = linebuffer.substr(0, 5);
		string temp6 = linebuffer.substr(0, 6);
		transform(temp5.begin(), temp5.end(), temp5.begin(), ::tolower);
		transform(temp6.begin(), temp6.end(), temp6.begin(), ::tolower);
		if (temp6 == "case #" || temp5 == "case#") {
			outfile << linebuffer;
		}
		else {
			outfile << operate(linebuffer);
		}
	}
}