import pytest

import nb_tokenizer as nb


@pytest.fixture
def long_text():
    """Test input: A paragraph."""
    return """Velkommen inn!

Nasjonalbibliotekets vakre publikumlokaler ligger på Solli plass i Oslo.

I bygningen fra 1914 kan du oppleve norsk kulturhistorie gjennom foredrag, verksteder og konserter eller gå på en av våre faste eller skiftende utstillinger. I Kafé Å kan du drikke en god kopp kaffe, og på en av Oslos vakreste lesesaler kan du fordype deg i fred og ro.

Inngangspartiet er utsmykket med fresker av kunstnerne Emanuel Vigeland, Per Krohg og Axel Revold."""


@pytest.fixture
def short_text():
    """Test input: a single sentence."""
    return (
        "Inngangspartiet er utsmykket med fresker "
        "av kunstnerne Emanuel Vigeland, Per Krohg og Axel Revold."
    )


def test_tokenizer(short_text):
    """Check that the tokenizer handles a simple, single sentence correctly."""
    # given
    expected = [
        "Inngangspartiet",
        "er",
        "utsmykket",
        "med",
        "fresker",
        "av",
        "kunstnerne",
        "Emanuel",
        "Vigeland",
        ",",
        "Per",
        "Krohg",
        "og",
        "Axel",
        "Revold",
        ".",
    ]
    # when
    tokens = nb.tokenize(short_text)
    # then
    assert len(tokens) == len(expected)
    assert all(t == e for t, e in zip(tokens, expected))
