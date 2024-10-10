import json
from pathlib import Path

import pytest

from pyrand48.rand48 import Rand48


@pytest.fixture
def get_conformance_data():
    contents = (
        Path(__file__).parent / "data" / "rand48_conformance_data.json"
    ).read_text()
    return json.loads(contents)


def test_drand48(get_conformance_data):
    data = get_conformance_data
    for expectation in data["drand48_expectations"]:
        prng = Rand48(expectation["seed"])
        for precomputed_number in expectation["sequence"]:
            assert prng.drand48() == pytest.approx(precomputed_number)


def test_drand48_bounds(get_conformance_data):
    data = get_conformance_data
    for seed in data["seeds"]:
        prng = Rand48(seed)
        for i in range(data["extended_sequence_length"]):
            value = prng.drand48()
            assert (value >= 0) and (value < 1)


def test_lrand48(get_conformance_data):
    data = get_conformance_data
    for expectation in data["lrand48_expectations"]:
        prng = Rand48(expectation["seed"])
        for precomputed_number in expectation["sequence"]:
            assert prng.lrand48() == precomputed_number


def test_lrand48_bounds(get_conformance_data):
    data = get_conformance_data
    for seed in data["seeds"]:
        prng = Rand48(seed)
        for i in range(data["extended_sequence_length"]):
            value = prng.lrand48()
            assert (value >= 0) and (value < (1 << 31))


def test_mrand48(get_conformance_data):
    data = get_conformance_data
    for expectation in data["mrand48_expectations"]:
        prng = Rand48(expectation["seed"])
        for precomputed_number in expectation["sequence"]:
            assert prng.mrand48() == precomputed_number


def test_mrand48_bounds(get_conformance_data):
    data = get_conformance_data
    for seed in data["seeds"]:
        prng = Rand48(seed)
        for i in range(data["extended_sequence_length"]):
            value = prng.mrand48()
            assert (value >= -(1 << 31)) and (value < (1 << 31))


def test_random_element_selection(get_conformance_data):
    data = get_conformance_data
    for seed in data["seeds"]:
        prng = Rand48(seed)
        d6 = [1, 2, 3, 4, 5, 6]
        for i in range(data["extended_sequence_length"]):
            d6_index = int(prng.drand48() * len(d6))
            assert (d6_index >= 0) and (d6_index < 6)


# See also
# https://www.nntp.perl.org/group/perl.perl5.porters/2012/11/msg196019.html
# https://github.com/Perl/perl5/blob/82c49390396382408fdafe8b813efdc28eb1ccdc/t/op/rand.t#L136-L140
def test_perl_conformance():
    prng = Rand48(1)
    assert int(prng.drand48() * 1000) == 41
    assert int(prng.drand48() * 1000) == 454
