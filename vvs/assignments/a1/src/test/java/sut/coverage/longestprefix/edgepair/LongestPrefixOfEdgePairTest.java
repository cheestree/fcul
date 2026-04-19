package sut.coverage.longestprefix.edgepair;

import org.junit.Test;
import sut.TST;

import static org.hamcrest.Matchers.is;
import static org.junit.Assert.assertNull;
import static org.junit.Assert.assertThat;

public class LongestPrefixOfEdgePairTest {

    @Test(expected = IllegalArgumentException.class)
    public void nullQueryThrows() {
        // Requirement: edge-pair coverage for entry guard edge query == null.
        new TST<String>().longestPrefixOf(null);
    }

    @Test
    public void emptyQueryReturnsNull() {
        // Requirement: edge-pair coverage for entry guard edge query.length() == 0.
        assertNull(new TST<String>().longestPrefixOf(""));
    }

    @Test
    public void whileConditionFalseBecauseRootNullReturnsEmptyString() {
        // Requirement: edge-pair coverage for while decision edge x == null at first check.
        assertThat(new TST<String>().longestPrefixOf("abc"), is(""));
    }

    @Test
    public void traversalTakesLeftAndRightEdges() {
        // Requirement: edge-pair coverage through both c < x.c and c > x.c branches.
        TST<String> trie = new TST<>();
        trie.put("m", "m");
        trie.put("a", "a");
        trie.put("z", "z");

        assertThat(trie.longestPrefixOf("apple"), is("a"));
        assertThat(trie.longestPrefixOf("zebra"), is("z"));
    }

    @Test
    public void equalEdgeUpdatesLengthWhenNodeHasValue() {
        // Requirement: edge-pair coverage for c == x.c edge then x.val != null edge.
        TST<String> trie = new TST<>();
        trie.put("cat", "v");

        assertThat(trie.longestPrefixOf("catalog"), is("cat"));
    }

    @Test
    public void equalEdgeWithoutValueDoesNotUpdateLength() {
        // Requirement: edge-pair coverage for c == x.c edge then x.val == null edge.
        TST<String> trie = new TST<>();
        trie.put("car", "v");

        assertThat(trie.longestPrefixOf("ca"), is(""));
    }
}

