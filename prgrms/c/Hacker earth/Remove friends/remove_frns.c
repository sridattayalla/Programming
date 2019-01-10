#include<stdio.h>
#include<stdlib.h>

struct Node{
	int val;
	struct Node *next;
	struct Node *prev;
};

void insert_last();
void display();
void remove_frns();
struct Node *first = 0;
struct Node *last = 0;
int size, rem;

void main(){
	int count = 0;
	//getting count
	scanf("%d", &count);
	for(int i = 0; i<count; i++){
		scanf("%d", &size);
		scanf("%d", &rem);
		//getting array
		first = 0;
		for(int j = 0; j< size; j++){
			int temp;
			scanf("%d", &temp);
			insert_last(temp);
		}
		remove_frns(first);
		display();
	}
}

void insert_last(int data){
	struct Node *new;
	new = (struct Node *) malloc(sizeof(struct Node));
	new->val = data;
	new->next = 0;
	new->prev = 0;
	if(first == 0){
		first = new;
		last = new;
	}
	else{
		struct Node *temp;
		temp = first;
		while(temp->next != 0){
			temp = temp->next;
		}
		new->prev = temp;
		temp->next = new;
		last = new;
	}
}

void remove_frns(struct Node *p){
	if(rem > 0){
		struct Node *temp_prev = p->prev;
		struct Node *temp_curr = p;
		struct Node *temp_nxt = p->next;
		if(temp_curr == first){
			if(temp_curr-> val < temp_nxt-> val){
				first = temp_nxt;
				first->prev = 0;
				rem--;
				remove_frns(first);
			}
			else{
				remove_frns(first->next);
			}
		}
		else if(temp_curr == last){
			temp_prev->next = 0;
			rem--;
			remove_frns(temp_prev);
		}
		else{
			if(temp_curr-> val < temp_nxt-> val){
				temp_prev->next = temp_curr->next;
				temp_nxt->prev = temp_curr->prev;
				rem--;
				remove_frns(temp_prev);
			}
			else{
				remove_frns(temp_nxt);
			}
		}
		
	}
}

void display(){
	struct Node *temp;
		temp = first;
		while(temp->next != 0){
			printf("%d ", temp->val);
			temp = temp->next;
		}
		printf("%d\n", temp->val);
}
