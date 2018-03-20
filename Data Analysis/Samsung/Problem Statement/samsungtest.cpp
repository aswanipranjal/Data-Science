#include <bits/stdc++.h>
#include <dirent.h>

using namespace std;

map<string, vector<string> > concepts;
map<string, vector<string> > placeholder;

void print_vec(vector<string> a) {
	for (size_t i = 0; i < a.size(); ++i) {
		cout << a[i] << endl;
	}
	cout << endl;
}

void make_placeholder() {
	vector<string> filenames;
	DIR *dir;
	struct dirent *ent;
	if ((dir = opendir ("PlaceHolder")) != NULL) {
	  	while ((ent = readdir (dir)) != NULL) {
	    	filenames.push_back(ent->d_name);
	  	}	
	  	closedir (dir);
	} else {
	  	perror ("");
	  	return;
	}

	vector<string>::iterator it_v;
	for (it_v = filenames.begin(); it_v != filenames.end(); ++it_v) {
		if (*it_v == "PlaceHolderDetail.txt") {
			filenames.erase(it_v);
			break;
		}
	}
	for (size_t i = 2; i < filenames.size(); ++i) {
		ifstream stream;
		char * file = new char[("PlaceHolder/" + filenames[i]).length() + 1];
		std::strcpy(file, ("PlaceHolder/" + filenames[i]).c_str());
		stream.open(file);
		char temp[250];
		vector <string> v;
		while(stream) {
			stream.getline(temp, 250);
			if (stream) v.push_back(temp);
		}
		stream.close();
		filenames[i] = filenames[i].substr(0, filenames[i].length() - 4);
		filenames[i] = '{' + filenames[i] + '}';
		placeholder.insert(make_pair(filenames[i], v));
	}
}

void make_concept() {
	vector<string> filenames;
	DIR *dir;
	struct dirent *ent;
	if ((dir = opendir ("Concept")) != NULL) {
	  	while ((ent = readdir (dir)) != NULL) {
	    	filenames.push_back(ent->d_name);
	  	}	
	  	closedir (dir);
	} else {
	  	perror ("");
	  	return;
	}

	for (size_t i = 2; i < filenames.size(); ++i) {
		ifstream stream;
		char * file = new char[("Concept/" + filenames[i]).length() + 1];
		std::strcpy(file, ("Concept/" + filenames[i]).c_str());
		stream.open(file);
		char temp[250];
		vector <string> v;
		while(stream) {
			stream.getline(temp, 250);
			if (stream) v.push_back(temp);
		}
		stream.close();
		filenames[i] = filenames[i].substr(0, filenames[i].length() - 4);
		filenames[i] = '{' + filenames[i] + '}';
		concepts.insert(make_pair(filenames[i], v));
	}
}

int main() {
	make_concept();
	make_placeholder();
	map<string, vector<string> >::iterator it;
	for (it = placeholder.begin(); it != placeholder.end(); ++it) {
		cout << it->first << " ";
		print_vec(it->second);
	}
}