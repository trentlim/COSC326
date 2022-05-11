#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

// Needs comments or README

struct S {
    char *firstName;
    char *lastName;
    int phone;
    char *emailAddress;
};

static int i, j;
static int count;

// Sorts structs by first name in ascending order.
void sfn(struct S** ss){
    for(i = 0; i < count; i++){
        for (j = i; j < count; j++){
            if (ss[i]->firstName > ss[j]->firstName){ 
                struct S *s = ss[j]; // here you needed to tempararily put ss[j] somewhere
                ss[j] = ss[i];
                ss[i] = s;
            }
        }
    }
}

// Finds instance of first name in all structs.
// Returns the index in ss of the struct holding data 
// that matches the inputted String.
// returns -1 if no matches were found
int ffn(struct S** ss, char* s){
    i = -1;
    while(++i < count){
        if(strcmp(ss[i]->firstName, s) == 0){
            return i;
        }
    }
    return -1;
}

void sln(struct S** ss){
    for(i = 0; i < count; i++){
        for (j = i; j < count; j++){
            if (ss[i]->lastName > ss[j]->lastName){
                struct S *s = ss[j];
                ss[j] = ss[i];
                ss[i] = s;
            }
        }
    }
}

int fln(struct S** ss, char* s){
    i = -1;
    while(++i < count){
        if(strcmp(ss[i]->lastName, s) == 0){
            return i;
        }
    }
    return -1;
}

void sem(struct S** ss){
    for(i = 0; i < count; i++) {
        for (j = i; j < count; j++) {
            if (ss[i]->emailAddress > ss[j]->emailAddress) {
                struct S *s = ss[j];
                ss[j] = ss[i];
                ss[i] = s;
            }
        }
    }
}

int fem(struct S** ss, char* s){
    i = -1;
    while(++i < count){
        if(strcmp(ss[i]->emailAddress, s) == 0){
            return i;
        }
    }
    return -1;
}

void sph(struct S** ss){
    for(i=0; i++ < count; i++) {
        for (j=i; j < count; j++) {
            if (ss[i]->phone > ss[j]->phone) {
                struct S *s = ss[i];
                ss[i] = ss[j];
                ss[j] = s;
            }
        }
    }
}

int fph(struct S** ss, int s){
    i = -1;
    while(++i < count){
        if(ss[i]->phone == s){
            return i;
        }
    }
    return -1;
}

int main(int argc, char ** argv) {
    count = 0;
    char buffer[10];

    // Space for a struct that points to structs is allocated.
    struct S** ss = (struct S**) malloc(100 * sizeof(struct S*));
    // A general struct is initialised, ready to be allocated data in the while loop,
    // if space is allocated here, old data will be overwritten,
    // everytime new data is added
    struct S* s; 

    FILE *f = fopen(argv[1], "r");

    // Loop iterates through the file and allocates space for a struct
    // and the Strings that go into this struct.
    // It then inputs data from the file to a struct and points the ss array
    // at an index equal to count to this struct.
    // New space is allocated for each object and element each iteration,
    // and count is incremented by 1 each time.
    while(!feof(f) && count < 100){ // memory leakage
        
        s = malloc(sizeof(*s));

        s->firstName = (char*) malloc(80 * sizeof(s->firstName[0]));
        s->lastName = (char*) malloc(80 * sizeof(s->firstName[0]));
        s->emailAddress = (char*) malloc(80 * sizeof(s->firstName[0]));

        fscanf(f, "%s %s %d %s", s->firstName, s->lastName, &s->phone, s->emailAddress); // no need for & on the Strings

        ss[count] = s;
        count += 1;

    }

    // Loop takes in user input, calls sort functions and find functions
    // based on these inputs and outputs the matching information
    int command = 10;
    // outside the while loop so that new memory isn't created everytime without freeing up the old val
    char* val = malloc(100*sizeof(val[0])); // memory leakage
    while(1) {

        // gets an input from the user of max size 10
        // converts it to an int and passes it to command
        printf("Enter a number: (0=exit program, 1=email, 2=first name, 3=last name, 4=phone number)\n");
        fgets(buffer, 10, stdin);
        command = atoi(buffer);
        if(command == 0){
            break;
        }

        // does the same but val keeps the input instead of passing it along
        printf("Enter a string to find:\n");
        fgets(val, 100, stdin);

        // removes next line value from val
        val[strcspn(val, "\n")] = 0;
        int location = -1;

        switch(command){
            case 1:
                printf("looking for email %s\n", val);
                sem(ss);
                location = fem(ss, val);
                break;
            case 2:
                printf("looking for firstname %s\n", val);
                sfn(ss);
                location = ffn(ss, val);
                break;
            case 3:
                printf("looking for lastname %s\n", val);
                sln(ss);
                location = fln(ss, val);
                break;
            case 4:
                printf("looking for phone %s\n", val);
                sph(ss);
                location = fph(ss, atoi(val));
            default:
                break;
        }
        // location equals -1 if nothing happened or the find functions
        // couldn't find a match, equals the index of the matching struct
        // in the sorted ss array if a match was found
        if (location >= 0) {
            printf("\nFirst name: %s\n", ss[location]->firstName);
            printf("Last name: %s\n", ss[location]->lastName);
            printf("Phone: %d\n", ss[location]->phone);
            printf("Email: %s\n", ss[location]->emailAddress);
        } else {
            printf("Didn't find anything matching %s!\n", val);
        }

    }
}
