
#include <stdio.h>


int main() {
	int num;
	scanf("%d", &num);
	int a, b;


	for (int i=0; i < num; i++) {
		scanf("%d %d", &a, &b);
		printf("Case #%d: %d\n", i + 1, a + b);
	}

	return 0;
}
