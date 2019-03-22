#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int main()
{
	int j=0,casevalue = 0;
	scanf("%d", &casevalue);
	for (j = 0; j < casevalue; j++) {
		int i = 0, value = 0, result = 0;
		for (i = 0; i < 10; i++) {
			scanf("%d", &value);
			if (value % 2 == 1)
				result = result + value;
		}
		printf("#%d %d\n", j+1,result);
	}
}
