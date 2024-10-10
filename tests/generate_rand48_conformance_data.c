#include <stdio.h>
#include <errno.h>
#include <limits.h>
#include <stdlib.h>

int main(void) {
    printf("{");

    /* How long to run a generator for extended tests? */
    int extended_sequence_length = 10000;
    printf("\"extended_sequence_length\":%d,", extended_sequence_length);

    /* How long to run a generator for short tests? */
    int sequence_length = 10;
    printf("\"sequence_length\":%d,", sequence_length);

    /* What seeds do we want to test? */
    int seed_count = 4;
    int seeds[4] = {
        123456789,
        987654321,
        123456789,
        0,
    };
    printf("\"seeds\":[");
    for (int i = 0; i < seed_count; i++) {
        printf("%d", seeds[i]);
        if (i + 1 < seed_count) {
            printf(",");
        }
    }
    printf("],");

    /* Conformance data for drand48 */
    printf("\"drand48_expectations\":[");
    for (int i = 0; i < seed_count; i++) {
        int seed = seeds[i];
        printf("{\"seed\":%d,\"sequence\":[", seed);
        srand48(seed);
        for (int j = 0; j < sequence_length; j++) {
            printf("%0.15lf", drand48());
            if (j + 1 < sequence_length) {
                printf(",");
            }
        }
        printf("]}");
        if (i + 1 < seed_count) {
            printf(",");
        }
    }
    printf("],");

    /* Conformance data for lrand48 */
    printf("\"lrand48_expectations\":[");
    for (int i = 0; i < seed_count; i++) {
        int seed = seeds[i];
        printf("{\"seed\":%d,\"sequence\":[", seed);
        srand48(seed);
        for (int j = 0; j < sequence_length; j++) {
            printf("%lu", lrand48());
            if (j + 1 < sequence_length) {
                printf(",");
            }
        }
        printf("]}");
        if (i + 1 < seed_count) {
            printf(",");
        }
    }
    printf("],");

    /* Conformance data for mrand48 */
    printf("\"mrand48_expectations\":[");
    for (int i = 0; i < seed_count; i++) {
        int seed = seeds[i];
        printf("{\"seed\":%d,\"sequence\":[", seed);
        srand48(seed);
        for (int j = 0; j < sequence_length; j++) {
            printf("%ld", mrand48());
            if (j + 1 < sequence_length) {
                printf(",");
            }
        }
        printf("]}");
        if (i + 1 < seed_count) {
            printf(",");
        }
    }
    printf("]");

    printf("}\n");
    return 0;
}
