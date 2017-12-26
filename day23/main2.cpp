#include <iostream>
using namespace std;

// https://github.com/sim642/adventofcode/blob/master/src/main/resources/eu/sim642/adventofcode2017/day23/day23_4.txt

int main () {
	long long int a=0;
	long long int b=0;
	long long int c=0;
	long long int d=0;
	long long int e=0;
	long long int f=0;
	long long int g=0;
	long long int h=0;

	b = 93 * 100 + 100000; //109,300
	c = b + 17000; //  126,300

	b = 109300;
	c = 126300+17;
	h = 0;

	do {
		f = 1;
		d = 2;

		do {
			e = 2;

			do {
				if (d*e == b) { f=0; break;}
				e++;
			} while ( e != b ) ;

			d = d + 1;
			if (f==0) break;
		} while (d != b);

		if (f ==0)   { h = h + 1; cout << h << "," << b << "\n";}
		if (b != c)  {b = b + 17;}

	} while (b!=c);

	cout << "H:" << h;
}
