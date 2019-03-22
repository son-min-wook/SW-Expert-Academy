#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>
int min(int,int,int,int);
int main()
{
	int i = 0;
	for (i = 0; i < 10; i++) {
		int casevalue = 0,j=0,count=0;
		scanf("%d", &casevalue);
		int* testcase = (int*)malloc(sizeof(int)*casevalue);
		for (j = 0; j < casevalue; j++) 
			scanf("%d", &testcase[j]);
		for (j = 2; j < casevalue - 2; j++) {
			if (testcase[j] - testcase[j - 2] > 0 && testcase[j] - testcase[j - 1] > 0 && testcase[j] - testcase[j + 1] > 0 && testcase[j] - testcase[j + 2] > 0) {
				count = count + min(testcase[j] - testcase[j - 2], testcase[j] - testcase[j - 1], testcase[j] - testcase[j + 1], testcase[j] - testcase[j + 2]);
			}
		}
		printf("#%d %d\n", i+1, count);
		count = 0;
	}
}
int min(int a, int b, int c, int d) {
	int mi = 300;
	if (mi > a)
		mi = a;
	if (mi > b)
		mi = b;
	if (mi > c)
		mi = c;
	if (mi > d)
		mi = d;
	return mi;
}