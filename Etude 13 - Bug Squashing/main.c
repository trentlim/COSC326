#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

struct S{
    char *firstName;
    char* lastName;
    int phone;
    char* emailAddress;
};

static int i;
static int count;

// Find by first name
// Returns the index of the first name
// Returns -1 if not found
int find_first_name(struct S** ss, char* s){
    i = -1;
    while(++i < count){
        if(strcmp(ss[i]->firstName, s) == 0){
            return i;
        }
    }
    return -1;
}

// Find by last name
// Returns the index of the last name
// Returns -1 if not found
int find_last_name(struct S** ss, char* s){
    i = -1;
    while(++i < count){
        if(strcmp(ss[i]->lastName, s) == 0){
            return i;
        }
    }
    return -1;
}

// Find by email address
// Returns the index of the email address
// Returns -1 if not found
int find_email(struct S** ss, char* s){
    i = -1;
    while(++i < count){
        if(strcmp(ss[i]->emailAddress, s) == 0){
            return i;
        }
    }
    return -1;
}

// Find by phone number
// Returns the index of the phone number
// Returns -1 if not found
int find_phone(struct S** ss, int s){
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

    // Array of people
    struct S** ss = (struct S**) malloc(100*sizeof(struct S**));
    
    // Allocate memory for each person
    struct S* s = malloc(sizeof(*s));

    FILE *f = fopen(argv[1], "r");

    // Read in each line of the file into a new struct and store in the array
    if(f != NULL){
        while (!feof(f)) {
            s = malloc(sizeof(*s));

            s->firstName = (char*) malloc(80 * sizeof(s->firstName[0]));
            s->lastName = (char*) malloc(80 * sizeof(s->firstName[0]));
            s->emailAddress = (char*) malloc(80 * sizeof(s->firstName[0]));

            fscanf(f, "%s %s %d %s", s->firstName, s->lastName, &s->phone, s->emailAddress); // no need for & on the Strings

            ss[count] = s;
            count += 1;
        }
        fclose(f);
    } else {
        printf("File not found\n");
        return EXIT_FAILURE;
    }

    int command = 10; // which variable the user wants to search by
    char* val = (char*)malloc(90*sizeof(char)); // the user's query


    while(command != 0){
        printf("Enter a Number: [1] First Name, [2] Last Name, [3] Phone Number, [4] Email Address, [0] Exit\n");
        scanf("%d", &command);

        if (command == 0){
            printf("Exiting Program");
            return EXIT_SUCCESS;
        }

        printf("Enter your query:\n");
        scanf("%s", val);

        int index = -1;

        // Get the index of the person in the array based on the command
		switch(command){
			case 1:
			    printf("Looking for first name: %s\n", val);
                index = find_first_name(ss, val);
                break;
			case 2:
			    printf("Looking for last name: %s\n", val);
                index = find_last_name(ss, val);
                break;
			case 3:
                printf("Looking for phone number: %s\n", val);
                index = find_phone(ss, atoi(val));
			case 4:
			    printf("Looking for email: %s\n", val);
                index = find_email(ss, val);
			default:
                break;
		}

        // Print out the person's information if they are found
        if(index != -1){
            printf("Found: %s %s %d %s\n", ss[index]->firstName, ss[index]->lastName, ss[index]->phone, ss[index]->emailAddress);
        } else {
            printf("Not Found\n");
        }
		
	}
}