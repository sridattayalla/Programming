#include<stdio.h>

int num_streets, streets[100], num_buildings[100],reward[100], building_ht[100][10000];
void print_taken();

void main(){
scanf("%d",&num_streets);

/*saving number of buildings ,reward and heights*/
for(int i=0;i<num_streets;i++){
	
	/*bbuilding count*/
	int temp_buldings;
	scanf("%d",&temp_buldings);
	num_buildings[i]=temp_buldings;
	
	/*reward*/
	int temp_reward;
	scanf("%d",&temp_reward);
	reward[i]=temp_reward;
	
	/*building heights*/
	for(int j=0;j<temp_buldings;j++){
		int temp_ht;
		scanf("%d",&temp_ht);
		building_ht[i][j]=temp_ht;
	}
 }
 print_taken();
}

void print_taken(){
	printf("%d\n",num_streets);
	for(int i=0;i<num_streets;i++){
	/*buidings*/
	printf("%d\t",num_buildings[i]);
	
	/*reward*/
	printf("%d\n",reward[i]);	
	
	/*building heights*/
	for(int j=0;j<temp_buldings;j++){
		printf("%d\t",building_ht[i][j]);
	}
	printf("\n");
 }
	
}
