#include <stdio.h>
#include <stdlib.h>


struct Node{
	int data;
	struct Node *next;
};
void insert_first();
void print_list();
void insert_last();
struct Node *first = 0;
void main(){
	//insert_first();
	insert_last();
	print_list();
}

void insert_first(){
	int i = 0;
	printf("enter a value to add: ");
	scanf("%d", &i);
	struct Node *temp;
	temp = (struct Node *) malloc(sizeof(struct Node));
	temp -> data = i;
	if(first == 0){
		first = temp;
		first -> next = 0;
	}
	else{
		temp -> next = first;
		first = temp;
	}
}

void insert_last(){
	int i = 0;
	printf("enter a value to insert: ");
	scanf("%d", &i);
	struct Node *new;
	new = (struct Node *) malloc(sizeof(struct Node));
	new->data = i;
	
	if(first == 0){
			first = new;
			first -> next = 0;
	}
	else{
		struct Node *temp = first; 
		while(temp -> next != 0){
			temp = temp -> next;
		}
		temp -> next = new;
	}
}

void print_list(){
	struct Node *temp = first;
	while (temp -> next != 0){
		printf("%d\n", temp -> data);
		temp = temp -> next;
	}
	printf("%d\n", temp -> data);
	main();
}