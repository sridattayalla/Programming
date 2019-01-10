#include <stdio.h>

void main(){
	int arr[] = {55, 4, 2, 17, 1, 3};
	for(int i =0; i<6; i++){
		int minimum = i;
		for (int j = i; j < 6; j++){
			if(arr[minimum] > arr[j]){
				minimum = j;
			}
		}
		int x = arr[i];
		int y = arr[minimum];
		
		arr[i] = y;
		arr[minimum] = x;
	}
	
	for(int i = 0; i<6; i++){
		printf("%d ", arr[i]);
	}
}