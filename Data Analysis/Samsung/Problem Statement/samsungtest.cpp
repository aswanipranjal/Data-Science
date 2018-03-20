#include <bits/stdc++.h>
#include <dirent.h>

using namespace std;

map<string, vector<string> > concepts;


void make_concept() {
	vector<string> filenames;
	DIR *dir;
	struct dirent *ent;
	if ((dir = opendir ("Concept")) != NULL) {
	  	/* print all the files and directories within directory */
	  	while ((ent = readdir (dir)) != NULL) {
		    // printf ("%s\n", ent->d_name);
	    	filenames.push_back(ent->d_name);
	  	}	
	  	closedir (dir);
	} else {
	  	/* could not open directory */
	  	perror ("");
	  	return;
	}

	for (size_t i = 2; i < filenames.size(); ++i) {
		ifstream mo_stream;
		char * file = new char[filenames[i].length() + 1];
		std::strcpy(file, filenames[i].c_str());
		mo_stream.open(file);
		string temp;
		vector<string> v;
		while (mo_stream >> temp) {
			v.push_back(temp);
		}
		filenames[i] = filenames[i].substr(0, filenames[i].length() - 4);
		filenames[i] = '{' + filenames[i] + '}';
		// cout << filenames[i] << endl;
		concepts.insert(make_pair(filenames[i], v));
	}
}

int main() {
	make_concept();
	map<string, vector<string> >::iterator it;
	for (it = concepts.begin(); it != concepts.end(); ++it) {
		
	}
}