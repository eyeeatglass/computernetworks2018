//cameron betz
#include <iostream>
#include <fstream>
using namespace std;

int main(int argc, char *argv[]){

    ifstream source("from.ogv", ios::binary);
    ofstream destination("to.ogv", ios::binary);

    destination << source.rdbuf();
    return 0;
}