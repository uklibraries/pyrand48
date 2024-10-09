import pytest

from pyrand48 import pyrand48

RAND48_MANY = 10000

RAND48_SEEDS = [
    123456789,
    987654321,
    123456789,
    0,
]

DRAND48_EXPECTATIONS = [
    (
        123456789,
        [
            0.052468466878967,
            0.025444216651039,
            0.099272008557943,
            0.436130078366610,
            0.327740170655563,
            0.821202297447584,
            0.560493185321629,
            0.018157128751305,
            0.872757585477675,
            0.652495601506189,
        ],
    ),
    (
        987654321,
        [
            0.061172260278003,
            0.295554048006551,
            0.765584541988698,
            0.585471265806468,
            0.474469888618007,
            0.012732449671589,
            0.097144680234432,
            0.158903430722681,
            0.754069653098131,
            0.594905980223075,
        ],
    ),
    (
        123456789,
        [
            0.052468466878967,
            0.025444216651039,
            0.099272008557943,
            0.436130078366610,
            0.327740170655563,
            0.821202297447584,
            0.560493185321629,
            0.018157128751305,
            0.872757585477675,
            0.652495601506189,
        ],
    ),
    (
        0,
        [
            0.170828036106290,
            0.749901980484964,
            0.096371655623567,
            0.870465227027076,
            0.577303506795108,
            0.785799258839674,
            0.692194153458640,
            0.368766269920421,
            0.873904076861809,
            0.745095098450065,
        ],
    ),
]

LRAND48_EXPECTATIONS = [
    (
        123456789,
        [
            112675174,
            54641039,
            213185015,
            936582211,
            703816657,
            1763518505,
            1203649950,
            38992137,
            1874232643,
            1401223634,
        ],
    ),
    (
        987654321,
        [
            131366428,
            634697485,
            1644080285,
            1257289969,
            1018916327,
            27342727,
            208616612,
            341242519,
            1619352249,
            1277550864,
        ],
    ),
    (
        123456789,
        [
            112675174,
            54641039,
            213185015,
            936582211,
            703816657,
            1763518505,
            1203649950,
            38992137,
            1874232643,
            1401223634,
        ],
    ),
    (
        0,
        [
            366850414,
            1610402240,
            206956554,
            1869309841,
            1239749840,
            1687491058,
            1486475625,
            791919534,
            1876694714,
            1600079540,
        ],
    ),
]

MRAND48_EXPECTATIONS = [
    (
        123456789,
        [
            225350349,
            109282078,
            426370030,
            1873164423,
            1407633314,
            -767930286,
            -1887667396,
            77984274,
            -546502010,
            -1492520027,
        ],
    ),
    (
        987654321,
        [
            262732857,
            1269394970,
            -1006806726,
            -1780387357,
            2037832654,
            54685454,
            417233224,
            682485038,
            -1056262798,
            -1739865567,
        ],
    ),
    (
        123456789,
        [
            225350349,
            109282078,
            426370030,
            1873164423,
            1407633314,
            -767930286,
            -1887667396,
            77984274,
            -546502010,
            -1492520027,
        ],
    ),
    (
        0,
        [
            733700828,
            -1074162815,
            413913109,
            -556347614,
            -1815467615,
            -919985179,
            -1322016045,
            1583839069,
            -541577867,
            -1094808216,
        ],
    ),
]


@pytest.mark.parametrize("seed,expected", DRAND48_EXPECTATIONS)
def test_drand48(seed, expected):
    prng = pyrand48.Rand48(seed)
    for n in range(10):
        assert prng.drand48() == pytest.approx(expected[n])


@pytest.mark.parametrize("seed", RAND48_SEEDS)
def test_drand48_bounds(seed):
    prng = pyrand48.Rand48(seed)
    for i in range(RAND48_MANY):
        value = prng.drand48()
        assert (value >= 0) and (value < 1)


@pytest.mark.parametrize("seed,expected", LRAND48_EXPECTATIONS)
def test_lrand48(seed, expected):
    prng = pyrand48.Rand48(seed)
    for n in range(10):
        assert prng.lrand48() == expected[n]


@pytest.mark.parametrize("seed", RAND48_SEEDS)
def test_lrand48_bounds(seed):
    prng = pyrand48.Rand48(seed)
    for i in range(RAND48_MANY):
        value = prng.lrand48()
        assert (value >= 0) and (value < (1 << 31))


@pytest.mark.parametrize("seed,expected", MRAND48_EXPECTATIONS)
def test_mrand48(seed, expected):
    prng = pyrand48.Rand48(seed)
    for n in range(10):
        assert prng.mrand48() == expected[n]


@pytest.mark.parametrize("seed", RAND48_SEEDS)
def test_mrand48_bounds(seed):
    prng = pyrand48.Rand48(seed)
    for i in range(RAND48_MANY):
        value = prng.mrand48()
        assert (value >= -(1 << 31)) and (value < (1 << 31))


@pytest.mark.parametrize("seed", RAND48_SEEDS)
def test_random_element_selection(seed):
    prng = pyrand48.Rand48(seed)
    d6 = [1, 2, 3, 4, 5, 6]
    for i in range(RAND48_MANY):
        d6_index = int(prng.drand48() * len(d6))
        assert (d6_index >= 0) and (d6_index < 6)


# See also
# https://www.nntp.perl.org/group/perl.perl5.porters/2012/11/msg196019.html
# https://github.com/Perl/perl5/blob/82c49390396382408fdafe8b813efdc28eb1ccdc/t/op/rand.t#L136-L140
def test_perl_conformance():
    prng = pyrand48.Rand48(1)
    assert int(prng.drand48() * 1000) == 41
    assert int(prng.drand48() * 1000) == 454
