#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
int main()
{
	int j=0,casevalue = 0;
	scanf("%d", &casevalue);
	for (j = 0; j < casevalue; j++) {
		int i = 0, value = 0, a, score[101] = {0,},max=0,maxvalue=0;
		scanf("%d", &a);
		for (i = 0; i < 1000; i++) {
			scanf("%d", &value);
			score[value] = score[value] + 1;
		}
		for (i = 0; i < 101; i++) {
			if (max < score[i]) {
				max = score[i];
				maxvalue = i;
			}
			else if (max == score[i]) {
				if (maxvalue < i)
					maxvalue = i;
			}
		}
		printf("#%d %d\n", j+1,maxvalue);
	}
}
