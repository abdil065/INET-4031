#include <stdio.h>

int main() {
    char *listOfUsers[] = {"User1", "User2", "User3"};
    int i;

    printf("Printing users from C program:\n");
    for (i = 0; i < 3; i++) {
        printf("%s\n", listOfUsers[i]);
    }

    return 0;
}
