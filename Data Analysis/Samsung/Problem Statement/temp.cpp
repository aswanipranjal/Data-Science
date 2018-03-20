#include <bits/stdc++.h>
#include <dirent.h>
using namespace std;
int main() {
	DIR *dir;
	cout << "===";
	struct dirent *ent;
	if ((dir = opendir ("Concept")) != NULL) {
	  /* print all the files and directories within directory */
	  while ((ent = readdir (dir)) != NULL) {
	    printf ("%s\n", ent->d_name);
	  }	
	  closedir (dir);
	} else {
	  /* could not open directory */
	  perror ("");
	  return EXIT_FAILURE;
	}
}