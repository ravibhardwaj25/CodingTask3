#include <stdio.h>
#include <stdlib.h>
#include <string.h>
  
/* A function that prints given number in words */
void numbers_to_words(char* n)
{
    int len = strlen(
        n); // Get number of digits in given number
  
    /* Base cases */
    if (len == 0) {
        //fprintf(stderr, "empty string\n");
        printf("No number entered");
        return;
    }
    if (len > 4) {
        //fprintf(stderr,"Length more than 4 is not supported\n");
        printf("Length more than 4 is not supported by this program");
        return;
    }
  
    /* The first string is not used, it is to make
        array indexing simple */
    char* one_digits[]
        = { "zero", "one", "two", "three", "four",
            "five", "six", "seven", "eight", "nine" };
  
    /* The first string is not used, it is to make
        array indexing simple */
    char* two_digits[]
        = { "", "ten", "eleven", "twelve",
            "thirteen", "fourteen", "fifteen", "sixteen",
            "seventeen", "eighteen", "nineteen" };
  
    /* The first two string are not used, they are to make
        array indexing simple*/
    char* tens_multiple[] = { "",       "",        "twenty",
                              "thirty", "forty",   "fifty",
                              "sixty",  "seventy", "eighty",
                              "ninety" };
  
    char* tens_power[] = { "hundred", "thousand" };
  
    /* Used for debugging purpose only */
    printf("\n%s = ", n);
  
    /* For single digit number */
    if (len == 1) {
        printf("%s\n", one_digits[*n - '0']);
        return;
    }
  
    /* Iterate while num is not '\0' */
    while (*n != '\0') {
        
        /* Code path for first 2 digits */
        if (len >= 3) {

            if (*n - '0' != 0) {
                printf("%s ", one_digits[*n - '0']);
                printf("%s ",tens_power[len - 3]); // here len can be 3 or 4
            }
            --len;
        }
  
        /* Code path for last 2 digits */
        else {
            /* Need to explicitly handle 10-19. Sum of the
            two digits is used as index of "two_digits"
            array of strings */
            if (*n == '1') {
                int sum = *n - '0' + *(n + 1) - '0';
                printf("%s\n", two_digits[sum]);
                return;
            }
  
            /* Need to explicitly handle 20 */
            else if (*n == '2' && *(n + 1) == '0') {
                printf("twenty");
                return;
            }
            else if((*n >= '2' && *n <= '9') && (*(n+1) >= '1' && *(n+1) <= '9') ){
                int j = *n - '0';
                printf("%s-", j ? tens_multiple[j] : "");
                ++n;
                if (*n != '0')
                    printf("%s ",one_digits[*n - '0']);
            }
            /* Rest of the two digit numbers i.e., 21 to 99
             */
            else {
                int i = *n - '0';
                printf("%s ", i ? tens_multiple[i] : "");
                ++n;
                if (*n != '0')
                    printf("%s ",one_digits[*n - '0']);
            }
        }
        ++n;
    }
}
  
/* Driver program to test above function */
int main(void)
{
    numbers_to_words("0");
    numbers_to_words("5");
    numbers_to_words("8");
    numbers_to_words("10");
    numbers_to_words("21");
    numbers_to_words("77");
    numbers_to_words("100");
    numbers_to_words("303");
    numbers_to_words("555");
    numbers_to_words("2000");
    numbers_to_words("3466");
    numbers_to_words("2400");
    return 0;
}