package sut.coverage.linebranch;

import org.junit.Test;
import sut.TST;

import java.util.HashSet;
import java.util.Set;

import static org.hamcrest.Matchers.containsInAnyOrder;
import static org.hamcrest.Matchers.empty;
import static org.hamcrest.Matchers.is;
import static org.junit.Assert.assertNull;
import static org.junit.Assert.assertThat;

public class TSTCoreLineBranchCoverageTest {

    @Test
    public void sizeCountsOnlyDistinctKeys() {
        // Requirement: line/branch coverage for public methods size() and put().
        TST<String> trie = new TST<>();
        assertThat(trie.size(), is(0));

        trie.put("cat", "v1");
        trie.put("cat", "v2");
        trie.put("car", "v3");

        assertThat(trie.size(), is(2));
    }

    @Test
    public void containsCoversPresentAndMissing() {
        // Requirement: line/branch coverage for contains() true and false outcomes.
        TST<String> trie = new TST<>();
        trie.put("cat", "v1");

        assertThat(trie.contains("cat"), is(true));
        assertThat(trie.contains("dog"), is(false));
    }

    @Test(expected = IllegalArgumentException.class)
    public void containsNullThrows() {
        // Requirement: line/branch coverage for contains() exceptional branch.
        new TST<String>().contains(null);
    }

    @Test
    public void getCoversFoundAndNotFound() {
        // Requirement: line/branch coverage for get() normal branches and null return.
        TST<Integer> trie = new TST<>();
        trie.put("apple", 1);

        assertThat(trie.get("apple"), is(1));
        assertNull(trie.get("banana"));
    }

    @Test(expected = IllegalArgumentException.class)
    public void getNullThrows() {
        // Requirement: line/branch coverage for get() null-argument guard.
        new TST<Integer>().get(null);
    }

    @Test(expected = IllegalArgumentException.class)
    public void getEmptyThrows() {
        // Requirement: line/branch coverage for get() empty-key guard.
        new TST<Integer>().get("");
    }

    @Test(expected = IllegalArgumentException.class)
    public void putNullThrows() {
        // Requirement: line/branch coverage for put() null-argument guard.
        new TST<String>().put(null, "x");
    }

    @Test
    public void keysEnumeratesStoredKeys() {
        // Requirement: line/branch coverage for keys() and collect() traversal.
        TST<String> trie = new TST<>();
        trie.put("cat", "v");
        trie.put("car", "v");
        trie.put("dog", "v");

        Set<String> keys = toSet(trie.keys());

        assertThat(keys, containsInAnyOrder("cat", "car", "dog"));
    }

    @Test
    public void keysWithPrefixCoversMatchAndNoMatch() {
        // Requirement: line/branch coverage for keysWithPrefix() branches x==null and x.val!=null.
        TST<String> trie = new TST<>();
        trie.put("ca", "prefix");
        trie.put("cat", "v1");
        trie.put("car", "v2");

        Set<String> matching = toSet(trie.keysWithPrefix("ca"));
        Set<String> missing = toSet(trie.keysWithPrefix("zz"));

        assertThat(matching, containsInAnyOrder("ca", "cat", "car"));
        assertThat(missing, empty());
    }

    @Test(expected = IllegalArgumentException.class)
    public void keysWithPrefixNullThrows() {
        // Requirement: line/branch coverage for keysWithPrefix() exceptional branch.
        new TST<String>().keysWithPrefix(null);
    }

    @Test
    public void keysThatMatchSupportsWildcardAndNoMatch() {
        // Requirement: line/branch coverage for keysThatMatch() including wildcard and empty result.
        TST<String> trie = new TST<>();
        trie.put("cat", "v");
        trie.put("car", "v");
        trie.put("dog", "v");

        Set<String> wildcard = toSet(trie.keysThatMatch(".a."));
        Set<String> none = toSet(trie.keysThatMatch("z.."));

        assertThat(wildcard, containsInAnyOrder("cat", "car"));
        assertThat(none, empty());
    }

    private Set<String> toSet(Iterable<String> iterable) {
        Set<String> set = new HashSet<>();
        for (String item : iterable) {
            set.add(item);
        }
        return set;
    }
}

