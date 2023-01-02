#include <iostream>
#include "string"
#include "stdlib.h"

using namespace std;

int main(int argc, char* argv[]) {
	
	int n = atoi(argv[1]);
	cout << n << " is type " << typeid(n).name() << endl;
	return 0;
}
