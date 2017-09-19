#include <stdio.h>

int mutq(){
    int x=26;
	printf("a = ");
    scanf("%d", &x);
    while (x>23 || x<(-1))
    {
        printf("a = ");
        scanf("%d", &x);
    }
    return x;
}

void burg (int a){
    char x = ' ';
    char y = '#';
	 
	 for (int i = 2;i < a;++i){
	 	
	 					 
	    for (int j = 0;j < (a-i-1);++j){
	    	printf("%c",x);
	 	}


	    for (int k = (a-i);k<a;++k){
	 	    printf("%c",y);
	 	}

        printf("%c",x);

        for (int k = (a-i);k<a;++k){
	 	    printf("%c",y);
	 	}

        printf("\n");
	 }
}

int main(){
    int k;
    k = mutq();
    burg(k);	 

    return 0;
}
