#include<stdio.h>

int s[22],curr_size=0;
int ins_num;
int num_entered;

void insert();
void delete();
void display_num();
void exit_here();

void main(){
	printf("select a num to do following \n1)insert\n2)delete\n3)display\n ");
	/* get input*/
	scanf("%d",&num_entered);
	switch(num_entered){
		case 1:
			printf("enter a num to insert: ");
			scanf("%d",&ins_num);
			insert(ins_num);
			break;
		case 2:
			delete();
			break;
		case 3:
			display_num();
			break;
		case 4:
			exit_here();
			break;
		default:
			printf("opps! it's not in options");
			main();
	}
}

void insert(int ins_num){
	if(curr_size==22){
		printf("its'nt possible to add");
	}
	else{
		s[curr_size]=ins_num;
		curr_size++;
		printf("now it is:\n");
		for(int i=0;i<curr_size;i++){
			printf("%d\n",s[i]);
		}
	}
	
	main();
}

void delete(){
	if(curr_size==0){
		printf("Deletion not possible \n");
	}
	else{
		s[curr_size-1]=s[curr_size];
		curr_size--;
		printf("now it is:\n");
		for(int i=0;i<curr_size;i++){
			printf("%d\n",s[i]);
		}
	}
	main();
}

void display_num(){
	for(int i=0;i<curr_size;i++){
		printf("%d \n",s[i]);
	}
	main();
}

void exit_here(){
	printf("thank u...");
}