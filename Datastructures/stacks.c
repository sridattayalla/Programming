#include <stdio.h>

int stack[10], curr_pos = 0;
void add();
void delete();
void display();
void exit();

void main(){
	printf("select a num to do following \n1)insert\n2)delete\n3)display\n ");
	/* get input*/
	int num_entered;
	int num_to_insert;
	scanf("%d", &num_entered);
	switch(num_entered){
		case 1:
			printf("enter a num to insert: \n");
			scanf("%d", &num_to_insert);
			add(num_to_insert);
			break;
		case 2:
			delete();
			break;
		case 3:
			display();
			break;
		default:
			printf("It's not in options\n");
			break;
	}

}

void add(int num){
	if(curr_pos < 10){
		stack[curr_pos] = num;
		curr_pos++;
		display();
	}
	else{
		printf("size exceeded\n");
		display();
	}
	main();
}

void delete(){
	if(curr_pos>0){
		stack[curr_pos - 1] = stack[curr_pos];
		curr_pos--;
		display;
	}
	else{
		printf("unable to delete\n");
		display();
	}
	main();
}

void display(){
	if(curr_pos == 0){
		printf("stact is empty\n");
	}
	for(int i=0; i<=curr_pos-1; i++){
		printf("%d ", stack[i]);
	}
	printf("\n");
	main();
}