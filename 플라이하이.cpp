#include <iostream>
#include <vector>
using namespace std;
int dx[] = { -1, 0,1,0 };
int dy[] = { 0, 1,0,-1 };
int n, siz, maxim = 0;
vector<vector<int>> search(int x, int y, vector<vector<int>> map, vector<vector<int>> result) {
	int candi = 0, exist = 0, mymaxi = 0;
	for (int l = 0; l < 4; l++) {
		int dj = x + dx[l], dk = y + dy[l];
		if (dj >= 0 && dk >= 0 && dj < siz && dk < siz && map[dj][dk]>map[x][y]) {
			if (result[dj][dk] != 0 && result[dj][dk] != -1) {    //������ ���� ģ�����
				candi = result[dj][dk] + 1;
				if (candi > mymaxi)
					mymaxi = candi;
				exist++;
			}
			else if (result[dj][dk] == -1) {      //�ڱ⺸�� ū�ִ��ִµ� �갡 �����ָ�
				candi = 2;
				if (candi > mymaxi)
					mymaxi = candi;
				exist++;
			}
			else if (result[dj][dk] == 0) {                   //���� ������ְ� �ƴ϶��
				result = search(dj, dk, map, result);   //�¸� ��������
				if (result[dj][dk] != 0 && result[dj][dk] != -1) {
					candi = result[dj][dk] + 1;
					if (candi > mymaxi)
						mymaxi = candi;
					exist++;
				}
				else if (result[dj][dk] == -1) {
					candi = 2;
					if (candi > mymaxi)
						mymaxi = candi;
					exist++;
				}
			}
		}
	}   //4���� ��
	if (exist == 0) {           //�� ���� ������
		result[x][y] = -1;
		return result;
	}
	else {                        //�� ���̶� �� ���� �ִٸ� 
		result[x][y] = mymaxi;
		if (maxim < mymaxi)
			maxim = mymaxi;
	}
	return result;
}
int main() {
	cin >> n;
	for (int i = 0; i < n; i++) {
		maxim = 0;
		siz = 0;
		scanf("%d", &siz);
		vector<vector<int>> map(siz, vector<int>(siz, 0));
		vector<vector<int>> result(siz, vector<int>(siz, 0));
		for (int j = 0; j < siz; j++) {
			for (int k = 0; k < siz; k++)
				scanf("%d", &map[j][k]);
		}
		for (int j = 0; j < siz; j++) {
			for (int k = 0; k < siz; k++) {
				if (result[j][k] == 0)
					result = search(j, k, map, result);
			}
		}
		printf("#%d %d\n", i + 1, maxim);
	}
	return 0;
}