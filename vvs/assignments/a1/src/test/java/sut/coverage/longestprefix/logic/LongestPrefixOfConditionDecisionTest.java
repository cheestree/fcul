package sut.coverage.longestprefix.logic;

import org.junit.Test;
import sut.TST;

import static org.hamcrest.Matchers.is;
import static org.junit.Assert.assertNull;
import static org.junit.Assert.assertThat;

public class LongestPrefixOfConditionDecisionTest {

    @Test
    public void cdc_entryGuardEmptyQuery() {
        // Requirement: add guard-path coverage to improve mutation score for longestPrefixOf.
        assertNull(new TST<String>().longestPrefixOf(""));
    }

    @Test
    public void cdc_whileCondition_trueBecauseBothClausesTrue() {
        // Requirement: logic-based CDC for while predicate (x != null && i < query.length()).
        TST<String> trie = new TST<>();
        trie.put("cat", "v");

        assertThat(trie.longestPrefixOf("cat"), is("cat"));
    }

    @Test
    public void cdc_whileCondition_falseBecauseLeftClauseFalse() {
        // Requirement: logic-based CDC where x == null forces predicate false.
        TST<String> trie = new TST<>();

        assertThat(trie.longestPrefixOf("cat"), is(""));
    }

    @Test
    public void cdc_whileCondition_falseBecauseRightClauseFalse() {
        // Requirement: logic-based CDC where i < query.length() becomes false for single-char query after one step.
        TST<String> trie = new TST<>();
        trie.put("a", "v");
        trie.put("ab", "v2");

        assertThat(trie.longestPrefixOf("a"), is("a"));
    }

    @Test
    public void cdc_nestedDecision_onCharacterComparisonAndValuePresence() {
        // Requirement: logic-based coverage for nested decisions c<x.c, c>x.c, c==x.c and x.val!=null.
        TST<String> trie = new TST<>();
        trie.put("m", "m");
        trie.put("a", "a");
        trie.put("z", "z");

        assertThat(trie.longestPrefixOf("apple"), is("a"));
        assertThat(trie.longestPrefixOf("zebra"), is("z"));
    }
}


