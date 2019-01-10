#include <stdio.h>

void main(){
	int arr[] = {55, 2, 5, 4, 3, 1};
	int x, y;
	for(int i = 0; i<6; i++){
		for(int j = 0; j < 6 - 1 - i; j++){
			if( arr[j] > arr[j + 1]){
				x = arr[j];
				y = arr[j + 1];
				arr[j] = y;
				arr[j + 1] = x;
			}
		} 
	}
	for(int i = 0; i< 6; i++){
		printf("%d ", arr[i]);
	}
}