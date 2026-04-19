package sut.coverage.linebranch;

import org.junit.Test;
import sut.TST;

import java.util.HashSet;
import java.util.Set;

import static org.hamcrest.Matchers.containsInAnyOrder;
import static org.hamcrest.Matchers.is;
import static org.junit.Assert.assertThat;

public class DeleteLineBranchTest {

    @Test(expected = IllegalArgumentException.class)
    public void deleteNullThrows() {
        // Requirement: dedicated delete tests file + line/branch exceptional branch for delete().
        new TST<String>().delete(null);
    }

    @Test(expected = IllegalArgumentException.class)
    public void deleteEmptyThrows() {
        // Requirement: line/branch exceptional branch for delete() empty key.
        new TST<String>().delete("");
    }

    @Test
    public void deleteMissingKeyLeavesTrieUnchanged() {
        // Requirement: line/branch branch where contains(key) is false.
        TST<String> trie = new TST<>();
        trie.put("cat", "v1");
        trie.put("dog", "v2");

        trie.delete("cow");

        assertThat(trie.size(), is(2));
        assertThat(trie.contains("cat"), is(true));
        assertThat(trie.contains("dog"), is(true));
    }

    @Test
    public void deleteExistingLeafRemovesKeyAndDecrementsSize() {
        // Requirement: line/branch path where delete() finds key and prunes leaf node.
        TST<String> trie = new TST<>();
        trie.put("cat", "v1");

        trie.delete("cat");

        assertThat(trie.size(), is(0));
        assertThat(toSet(trie.keys()).isEmpty(), is(true));
    }

    @Test
    public void deleteSharedPrefixPreservesOtherKeys() {
        // Requirement: line/branch path where delete() clears value but preserves internal branch nodes.
        TST<String> trie = new TST<>();
        trie.put("ca", "prefix");
        trie.put("cat", "word");
        trie.put("car", "word2");

        trie.delete("cat");

        assertThat(trie.size(), is(2));
        assertThat(toSet(trie.keys()), containsInAnyOrder("ca", "car"));
    }

    private Set<String> toSet(Iterable<String> iterable) {
        Set<String> result = new HashSet<>();
        for (String key : iterable) {
            result.add(key);
        }
        return result;
    }
}

