#include <stdio.h>
#include <errno.h>
#include <limits.h>
#include <stdlib.h>

int main(void) {
    int seq_count = 10;
    int seed_count = 4;
    int seeds[4] = {
        123456789,
        987654321,
        123456789,
        0,
    };
    int many = 10000;

    printf("import pytest\n\nfrom pyrand48 import pyrand48\n\n");
    printf("RAND48_MANY = %d\n\n", many);

    printf("RAND48_SEEDS = [\n");
    for (int i = 0; i < seed_count; i++) {
        printf("    %d,\n", seeds[i]);
    }
    printf("]\n\n");

    printf("DRAND48_EXPECTATIONS = [\n");
    for (int i = 0; i < seed_count; i++) {
        int seed = seeds[i];
        printf("    (\n        %d,\n        [\n", seed);
        srand48(seed);
        for (int j = 0; j < seq_count; j++) {
            printf("            %0.15lf,\n", drand48());
        }
        printf("        ],\n    ),\n");
    }
    printf("]\n\n");

    printf("LRAND48_EXPECTATIONS = [\n");
    for (int i = 0; i < seed_count; i++) {
        int seed = seeds[i];
        printf("    (\n        %d,\n        [\n", seed);
        srand48(seed);
        for (int j = 0; j < seq_count; j++) {
            printf("            %lu,\n", lrand48());
        }
        printf("        ],\n    ),\n");
    }
    printf("]\n\n");

    printf("MRAND48_EXPECTATIONS = [\n");
    for (int i = 0; i < seed_count; i++) {
        int seed = seeds[i];
        printf("    (\n        %d,\n        [\n", seed);
        srand48(seed);
        for (int j = 0; j < seq_count; j++) {
            printf("            %ld,\n", mrand48());
        }
        printf("        ],\n    ),\n");
    }
    printf("]\n\n");

    printf("\n");
    printf("@pytest.mark.parametrize(\"seed,expected\", DRAND48_EXPECTATIONS)\n");
    printf("def test_drand48(seed, expected):\n");
    printf("    prng = pyrand48.Rand48(seed)\n");
    printf("    for n in range(%d):\n", seq_count);
    printf("        assert prng.drand48() == pytest.approx(expected[n])\n");
    printf("\n");

    printf("\n");
    printf("@pytest.mark.parametrize(\"seed\", RAND48_SEEDS)\n");
    printf("def test_drand48_bounds(seed):\n");
    printf("    prng = pyrand48.Rand48(seed)\n");
    printf("    for i in range(RAND48_MANY):\n");
    printf("        value = prng.drand48()\n");
    printf("        assert (value >= 0) and (value < 1)\n");
    printf("\n");

    printf("\n");
    printf("@pytest.mark.parametrize(\"seed,expected\", LRAND48_EXPECTATIONS)\n");
    printf("def test_lrand48(seed, expected):\n");
    printf("    prng = pyrand48.Rand48(seed)\n");
    printf("    for n in range(%d):\n", seq_count);
    printf("        assert prng.lrand48() == expected[n]\n");
    printf("\n");

    printf("\n");
    printf("@pytest.mark.parametrize(\"seed\", RAND48_SEEDS)\n");
    printf("def test_lrand48_bounds(seed):\n");
    printf("    prng = pyrand48.Rand48(seed)\n");
    printf("    for i in range(RAND48_MANY):\n");
    printf("        value = prng.lrand48()\n");
    printf("        assert (value >= 0) and (value < (1 << 31))\n");
    printf("\n");

    printf("\n");
    printf("@pytest.mark.parametrize(\"seed,expected\", MRAND48_EXPECTATIONS)\n");
    printf("def test_mrand48(seed, expected):\n");
    printf("    prng = pyrand48.Rand48(seed)\n");
    printf("    for n in range(%d):\n", seq_count);
    printf("        assert prng.mrand48() == expected[n]\n");
    printf("\n");

    printf("\n");
    printf("@pytest.mark.parametrize(\"seed\", RAND48_SEEDS)\n");
    printf("def test_mrand48_bounds(seed):\n");
    printf("    prng = pyrand48.Rand48(seed)\n");
    printf("    for i in range(RAND48_MANY):\n");
    printf("        value = prng.mrand48()\n");
    printf("        assert (value >= -(1 << 31)) and (value < (1 << 31))\n");
    printf("\n");

    printf("\n");
    printf("@pytest.mark.parametrize(\"seed\", RAND48_SEEDS)\n");
    printf("def test_random_element_selection(seed):\n");
    printf("    prng = pyrand48.Rand48(seed)\n");
    printf("    d6 = [1, 2, 3, 4, 5, 6]\n");
    printf("    for i in range(RAND48_MANY):\n");
    printf("        d6_index = int(prng.drand48() * len(d6))\n");
    printf("        assert (d6_index >= 0) and (d6_index < 6)\n");

    printf("\n");

    printf("\n");
    printf("# See also\n");
    printf("# https://www.nntp.perl.org/group/perl.perl5.porters/2012/11/msg196019.html\n");
    printf("# https://github.com/Perl/perl5/blob/82c49390396382408fdafe8b813efdc28eb1ccdc/t/op/rand.t#L136-L140\n");
    printf("def test_perl_conformance():\n");
    printf("    prng = pyrand48.Rand48(1)\n");
    printf("    assert int(prng.drand48() * 1000) == 41\n");
    printf("    assert int(prng.drand48() * 1000) == 454\n");

    return 0;
}
