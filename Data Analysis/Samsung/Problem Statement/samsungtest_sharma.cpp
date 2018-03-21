#include <bits/stdc++.h>
#include <dirent.h>

using namespace std;

map<string, vector<string> > concepts;
map<string, vector<string> > placeholder;
map<string, pair<set<string>, set<string> > > grammar;

map<string, int> counters;

void print_set(set<string> chu_chain) {
	set<string>::iterator dil_karein;
	for(dil_karein = chu_chain.begin(); dil_karein != chu_chain.end(); ++dil_karein) {
		cout << *dil_karein << " ";
	}
	cout << endl;
}

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
		strcpy(file, ("PlaceHolder/" + filenames[i]).c_str());
		stream.open(file);
		char temp[250];
		vector <string> v;
		while(stream) {
			stream.getline(temp, 250);
			if (stream) {
				v.push_back(temp);
				if(temp == string("bengaluru")) v.push_back("bangalore");
			}
		}
		stream.close();
		if (filenames[i] == "contact_name.txt") {
			stream.open(file);
			string s;
			while(stream >> s) {
				v.push_back(s);
			}
			stream.close();
		}
		filenames[i] = filenames[i].substr(0, filenames[i].length() - 4);
		filenames[i] = '<' + filenames[i] + '>';
		if(filenames[i] == "<places>") placeholder.insert(make_pair("<place>", v));
		placeholder.insert(make_pair(filenames[i], v));
	}
	//Remember to minimize/remove this hard-coding
	vector<string> v_s = {"a.m.", " am ", "p.m.", " pm "};
	placeholder.insert(make_pair("<dateTime>", v_s));
	v_s.clear();
	v_s = {"monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "today", "tomorrow"};
	placeholder.insert(make_pair("<day>", v_s));
	v_s.clear();
	v_s = {"january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"};
	placeholder.insert(make_pair("<date>", v_s));
	v_s.clear();
}

void make_grammar() {
	//Remember to incorporate support for grammars containing <number> placeholers.
	vector<string> filenames;
	DIR *dir;
	struct dirent *ent;
	if ((dir = opendir ("Grammar")) != NULL) {
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
		char * file = new char[("Grammar/" + filenames[i]).length() + 1];
		strcpy(file, ("Grammar/" + filenames[i]).c_str());
		stream.open(file);
		char temp[250];
		set <string> v_c, v_p;
		
			string s;
			while(stream >> s) {
				if(s.at(0) == '{') {
					string toput;
					for(int i = 0; i < s.length(); ++i) {
						toput.push_back(s.at(i));
						if(s.at(i) == '}') {
							v_c.insert(toput);
							toput.clear();
						}
					}
				}
				else if(s.at(0) == '<') {
					string toput;
					for(int i = 0; i < s.length(); ++i) {
						toput.push_back(s.at(i));
						if(s.at(i) == '>') {
							if(toput == "<time>") toput = "<dateTime>";
							v_p.insert(toput);
							toput.clear();
						}
					}
				}
			}
			stream.close();
		// }
		filenames[i] = filenames[i].substr(0, filenames[i].length() - 4);
		// filenames[i] = '<' + filenames[i] + '>';
		grammar.insert(make_pair(filenames[i], make_pair(v_c, v_p)));
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

void preKMP(string pattern, int f[]) {
    int m = pattern.length(), k;
    f[0] = -1;
    for (int i = 1; i < m; i++)
    {
        k = f[i - 1];
        while (k >= 0)
        {
            if (pattern[k] == pattern[i - 1])
                break;
            else
                k = f[k];
        }
        f[i] = k + 1;
    }
}
 
bool KMP(string pattern, string target) {
	transform(pattern.begin(), pattern.end(), pattern.begin(), ::tolower);
	transform(target.begin(), target.end(), target.begin(), ::tolower);
    int m = pattern.length();
    int n = target.length();
    int f[m];     
    preKMP(pattern, f);     
    int i = 0;
    int k = 0;        
    while (i < n)
    {
        if (k == -1)
        {
            i++;
            k = 0;
        }
        else if (target[i] == pattern[k])
        {
            i++;
            k++;
            if (k == m)
                return 1;
        }
        else
            k = f[k];
    }
    return 0;
}

bool is_concept_present(vector<string> v, string s) {
	bool flag = false; 
	vector<string>::iterator it1;
	for(it1 = v.begin(); it1 != v.end(); ++it1) {
		// cout << *it1 << endl;
		flag = KMP(*it1, s);
		if(flag) break;
	}
	return flag;
}

vector<string> concepts_that_are_present(string s) {
	map<string, vector<string> >::iterator it;
	vector<string> res;
	for(it = concepts.begin(); it != concepts.end(); ++it) {
		// cout << it->first << endl;
		if(is_concept_present(it->second, s)){ 
					// cout << "I am going in\n";
					// cout << it->first << endl;
					if(it->first == "{search_concept}") {
						res.push_back("{search}");
					}

					res.push_back(it->first);
				}
	}

	// cout << res.size();
	return res;
}

bool is_placeholder_present(vector<string> v, string s) {
	bool flag = false; 
	vector<string>::iterator it1;
	for(it1 = v.begin(); it1 != v.end(); ++it1) {
		flag = KMP(*it1, s);
		if(flag) break;
	}

	return flag;
}

vector<string> placeholders_that_are_present(string s) {
	map<string, vector<string> >::iterator it;
	vector<string> res;
	for(it = placeholder.begin(); it != placeholder.end(); ++it) {
		if(is_placeholder_present(it->second, s)) {
			// cout << "I am going in again\n";
			// if(it->first == "<places>") {
			// 			res.push_back("<place>");
			// 		}
			res.push_back(it->first);
		}
	}

	// cout << res.size();
	return res;
}

void make_counters() {
	map<string, pair<set<string>, set<string> > >::iterator it;
	for(it = grammar.begin(); it != grammar.end();  ++it) {
		counters.insert(make_pair(it->first, 0));
	}
}

void find_grammar_scores_concept(vector<string> v) {
	map<string, pair<set<string>, set<string> > >::iterator it;
	for(size_t i = 0; i < v.size(); ++i) {
		for(it = grammar.begin(); it != grammar.end(); ++it) {
			set<string>::iterator it_s;
			it_s = it->second.first.find(v[i]);
			if(it_s != it->second.first.end()) {
				counters[it->first] = counters[it->first] + 1;
			}	
		}
	}
}

void find_grammar_scores_placeholder(vector<string> v) {
	map<string, pair<set<string>, set<string> > >::iterator it;
	for(size_t i = 0; i < v.size(); ++i) {
		for(it = grammar.begin(); it != grammar.end(); ++it) {
			set<string>::iterator it_s;
			it_s = it->second.second.find(v[i]);
			if(it_s != it->second.second.end()) {
				counters[it->first] = counters[it->first] + 1;
			}	
		}
	}
}

string command() {
	int max = 4 + 3 - 8;
	map<string, int>::iterator it;
	string s;
	for(it = counters.begin(); it != counters.end(); ++it) {
		if(max < it->second) {
			s = it->first;
			max = it->second;
		}
	}

	return s;
}

int main() {
	make_concept();
	make_placeholder();
	make_grammar();
	make_counters();
	string input_str = "Can you please set an alarm at 3 pm tomorrow  ";
	vector<string> v_c, v_p;
	v_c = concepts_that_are_present(input_str);
	v_p = placeholders_that_are_present(input_str);
	find_grammar_scores_concept(v_c);
	find_grammar_scores_placeholder(v_p);

	// print_vec(v_c);
	// print_vec(v_p);

	cout << command() << endl;

	// map<string, pair<set<string>, set<string> > >::iterator it;
	// for (it = grammar.begin(); it != grammar.end(); ++it) {
	// 	cout << it->first << " \nc\n--\n";
	// 	print_set(it->second.first);
	// 	cout << "p\n--\n";
	// 	print_set(it->second.second);
	// }

	// map<string, vector<string> >::iterator it;
	// for (it = placeholder.begin(); it != placeholder.end(); ++it) {
	// 	cout << it->first;
	// 	print_vec(it->second);
	// 	// cout << "p\n--\n";
	// 	// print_set(it->second.second);
	// }

	map<string, int>::iterator it;
	string s;
	for(it = counters.begin(); it != counters.end(); ++it) {
		cout << it->first << "\t" << it->second <<  endl;
	}
	

	return 0;
}
