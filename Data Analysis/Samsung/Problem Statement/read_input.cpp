#include <bits/stdc++.h>

using namespace std;

void operate(string input) {
	cout << "Ye dekho input: " << input << endl;

}

int main(int argc, char const *argv[])
{
	ifstream infile("Testing/input.txt");
	ofstream outfile("Testing/output.txt")
	string linebuffer;

	while (infile && getline(infile, linebuffer)) {
		if (linebuffer.length() == 0) continue;
		string temp = linebuffer.substr(0, 5);
		transform(temp.begin(), temp.end(), temp.begin(), ::tolower);
		// cout << "Lower hua?" << temp << endl;
		if (temp == "case #" || temp == "case#") {
			// cout << "MoBhai Don Dekhe Porn";
			continue;
		}
		else {
			operate(linebuffer);
		}
	}
}