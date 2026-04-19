package sut.coverage.longestprefix.primepath;

import org.junit.Test;
import sut.TST;

import static org.hamcrest.Matchers.is;
import static org.junit.Assert.assertNull;
import static org.junit.Assert.assertThat;

public class LongestPrefixOfPrimePathTest {

    @Test
    public void primePath_entryGuardEmptyQuery() {
        // Requirement: add guard-path coverage to improve mutation score for longestPrefixOf.
        assertNull(new TST<String>().longestPrefixOf(""));
    }

    @Test
    public void primePath_leftThenEqualThenMid() {
        // Requirement: prime-path candidate that combines left branch and later equality progression.
        TST<String> trie = new TST<>();
        trie.put("m", "m");
        trie.put("cat", "cat");

        assertThat(trie.longestPrefixOf("catalog"), is("cat"));
    }

    @Test
    public void primePath_rightThenEqualThenMid() {
        // Requirement: prime-path candidate that combines right branch and later equality progression.
        TST<String> trie = new TST<>();
        trie.put("m", "m");
        trie.put("zoo", "zoo");

        assertThat(trie.longestPrefixOf("zoology"), is("zoo"));
    }

    @Test
    public void primePath_multipleEqualTransitionsWithIntermediateValues() {
        // Requirement: prime-path candidate with repeated equal edges and multiple length updates.
        TST<String> trie = new TST<>();
        trie.put("c", "v1");
        trie.put("ca", "v2");
        trie.put("cat", "v3");

        assertThat(trie.longestPrefixOf("catalog"), is("cat"));
    }

    @Test
    public void primePath_exitsWhenQueryEndsBeforeTriePath() {
        // Requirement: prime-path candidate where loop exits due to i < query.length() becoming false.
        TST<String> trie = new TST<>();
        trie.put("abcd", "v");

        assertThat(trie.longestPrefixOf("ab"), is(""));
    }

    @Test
    public void primePath_exitsWhenSearchFallsOffTrie() {
        // Requirement: prime-path candidate where traversal exits because x becomes null.
        TST<String> trie = new TST<>();
        trie.put("cat", "v");

        assertThat(trie.longestPrefixOf("caz"), is(""));
    }
}


