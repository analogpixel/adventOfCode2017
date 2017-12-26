#include <iostream>
using namespace std;
 
int main () {
	long long int a=0;
	long long int b=0;
	long long int c=0;
	long long int d=0;
	long long int e=0;
	long long int f=0;
	long long int g=0;
	long long int h=0;

	b = 93;
	c = b;

	b = b * 100;
	b = b + 100000;
	c = b;
	c = c + 17000;

	l23:
		f = 1;
		d = 2;
		l13:
			e = 2;
			l8:
				g = d;
				g = g * e;
				g = g - b;
				if (g ==0) { f=0; }
				e = e + 1;
				g = e;
				g = g - b;
				if (g !=0 ) { goto l8; }
			d = d + 1;
			g = d;
			g = g - b;
			if (g !=0) { goto l13; }
		if (f ==0) { h = h + 1;}
		g = b;
		g = g -c;
		if (g ==0) {cout << "H:" << h; return 0;}
		b = b + 17;
		goto l23;
}