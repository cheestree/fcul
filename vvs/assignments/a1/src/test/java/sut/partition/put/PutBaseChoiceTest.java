package sut.partition.put;

import org.junit.Test;
import sut.TST;

import static org.hamcrest.Matchers.is;
import static org.junit.Assert.assertThat;

public class PutBaseChoiceTest {

    @Test
    public void baseChoice_emptyTrie_typicalKey_notPresent_noPrefix() {
        // Requirement: Base Choice for put() with trie empty + typical key.
        TST<String> trie = new TST<>();

        trie.put("m", "v");

        assertThat(trie.get("m"), is("v"));
        assertThat(trie.size(), is(1));
    }

    @Test
    public void variation_trieAlreadyIncludesNewKey_updatesValueWithoutGrowingSize() {
        // Requirement: ISP/Base Choice variation for characteristic "trie already includes new key".
        TST<String> trie = new TST<>();
        trie.put("m", "v1");

        trie.put("m", "v2");

        assertThat(trie.get("m"), is("v2"));
        assertThat(trie.size(), is(1));
    }

    @Test
    public void variation_trieIncludesPrefixOfNewKey() {
        // Requirement: ISP/Base Choice variation for characteristic "trie includes some prefix of new key".
        TST<String> trie = new TST<>();
        trie.put("ca", "prefix");

        trie.put("cat", "word");

        assertThat(trie.get("ca"), is("prefix"));
        assertThat(trie.get("cat"), is("word"));
        assertThat(trie.size(), is(2));
    }

    @Test
    public void variation_smallestLexicographicKey() {
        // Requirement: ISP/Base Choice variation for key-position characteristic: smallest key.
        TST<String> trie = new TST<>();
        trie.put("m", "mid");
        trie.put("z", "high");

        trie.put("a", "low");

        assertThat(trie.get("a"), is("low"));
        assertThat(trie.size(), is(3));
    }

    @Test
    public void variation_largestLexicographicKey() {
        // Requirement: ISP/Base Choice variation for key-position characteristic: largest key.
        TST<String> trie = new TST<>();
        trie.put("a", "low");
        trie.put("m", "mid");

        trie.put("z", "high");

        assertThat(trie.get("z"), is("high"));
        assertThat(trie.size(), is(3));
    }

    @Test
    public void variation_typicalLexicographicKeyInNonEmptyTrie() {
        // Requirement: ISP/Base Choice variation for key-position characteristic: typical key.
        TST<String> trie = new TST<>();
        trie.put("a", "low");
        trie.put("z", "high");

        trie.put("m", "mid");

        assertThat(trie.get("m"), is("mid"));
        assertThat(trie.size(), is(3));
    }

    @Test(expected = IllegalArgumentException.class)
    public void nullKeyThrows() {
        // Requirement: put() input validation guard for null keys.
        new TST<String>().put(null, "x");
    }
}

