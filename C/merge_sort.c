#include<stdio.h>

void merge(int A[], int start, int mid, int end){
	//store the starting position of both parts in temporary variables.
	int p = start, q = mid + 1;
	
	int Arr[end - start + 1], k = 0;
	
	for (int i = start; i <= end ; i++){
		if(p > mid){
			Arr[ k++ ] = A[ q++ ];
		}
		
		else if(q > end){
			Arr[k++] = A[p++];
		}
		
		else if( A[p] < A[q] ){
		Arr[k++] = A[ p++ ];
		}
		
		else{
		Arr[k++] = A[ q++];
		}
	}
	
	for(int p =0; p<k ; p++){
		A[start ++ ] = Arr[p];
	}
	
}

void merge_sort(int A[], int start, int end){
	if(start < end){
		int mid = (start + end) / 2;
		
		merge_sort( A, start, mid);
		
		merge_sort(A, mid + 1, end);
		
		merge(A, start, mid, end);
	}
}

void main(){
	int A[7] = {10, 4, 2, 3, 6, 11, 1};
	merge_sort(A, 0, 6);
	
	for (int i =0; i<= 6; i++){
		printf("%d ", A[i]);
	}
}
