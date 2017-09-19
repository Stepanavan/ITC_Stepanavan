#include <stdio.h>

int main (void)
{
    int a=26;
   
    while (a>23 || a<(-1))
    {
        printf("a = ");
        scanf("%d", &a);

    };
    char text[a];
    for (int i=1;i< a;++i){
        for (int j=0;j < a;++j)
        {
           text[j]=' ';
        }
        text[a-1]= '\0';
        for (int j = (a-i); j < a; ++j)
        {
            text[j] = '#';
        }
        printf("%s",text);
        printf("%c",'\n');
    }
    return 0;
}