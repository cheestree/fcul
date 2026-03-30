package sut;

import org.junit.Test;

import java.util.HashSet;
import java.util.Set;

import static org.hamcrest.Matchers.containsInAnyOrder;
import static org.hamcrest.Matchers.empty;
import static org.hamcrest.core.Is.is;
import static org.junit.Assert.assertNull;
import static org.junit.Assert.assertThat;

public class KeysTest {
    @Test
    public void keys_returnsCorrectValue() {
        TST<String> st = new TST<>();
        st.put("cat", "v");
        st.put("car", "v");
        st.put("dog", "v");

        Set<String> keys = new HashSet<>();
        for (String key : st.keys()) {
            keys.add(key);
        }

        assertThat(keys.size(), is(3));
        assertThat(keys, containsInAnyOrder("cat", "car", "dog"));
    }

    @Test
    public void keysWithPrefix_returnsCorrectValue() {
        TST<String> st = new TST<>();
        st.put("cat", "v");
        st.put("car", "v");
        st.put("dog", "v");

        Set<String> keys = new HashSet<>();
        for (String key : st.keysWithPrefix("ca")) {
            keys.add(key);
        }

        assertThat(keys.size(), is(2));
        assertThat(keys, containsInAnyOrder("cat", "car"));
    }

    @Test(expected = IllegalArgumentException.class)
    public void keysWithPrefix_throwsIllegalArgumentException() {
        TST<String> st = new TST<>();
        st.keysWithPrefix(null);
    }

    @Test
    public void keysWithPrefix_prefixNotInTrie_returnsEmptyIterable() {
        TST<String> st = new TST<>();
        st.put("cat", "v");
        st.put("dog", "v");

        Set<String> keys = new HashSet<>();
        for (String key : st.keysWithPrefix("zz")) {
            keys.add(key);
        }

        assertThat(keys, empty());
    }

    @Test
    public void keysWithPrefix_prefixIsCompleteKey_includesPrefixItself() {
        TST<String> st = new TST<>();
        st.put("ca", "prefixValue");
        st.put("cat", "v1");
        st.put("car", "v2");

        Set<String> keys = new HashSet<>();
        for (String key : st.keysWithPrefix("ca")) {
            keys.add(key);
        }

        assertThat(keys.size(), is(3));
        assertThat(keys, containsInAnyOrder("ca", "cat", "car"));
    }

    @Test
    public void keysThatMatch_returnsCorrectValue() {
        TST<String> st = new TST<>();
        st.put("cat", "v");
        st.put("car", "v");
        st.put("dog", "v");

        Set<String> keys = new HashSet<>();
        for (String key : st.keysThatMatch(".a.")) {
            keys.add(key);
        }

        assertThat(keys.size(), is(2));
        assertThat(keys, containsInAnyOrder("cat", "car"));
    }

    @Test
    public void keysThatMatch_noMatch_returnsEmpty() {
        TST<String> st = new TST<>();
        st.put("cat", "v");
        st.put("car", "v");

        Set<String> keys = new HashSet<>();
        for (String key : st.keysThatMatch("z..")) {
            keys.add(key);
        }

        assertThat(keys, empty());
    }

    @Test
    public void keysThatMatch_terminalNodeWithoutValue_isNotAdded() {
        TST<String> st = new TST<>();
        st.put("ca", "v");

        Set<String> keys = new HashSet<>();
        for (String key : st.keysThatMatch("c")) {
            keys.add(key);
        }

        assertThat(keys, empty());
    }

    @Test
    public void longestPrefixOf_returnsCorrectValue() {
        TST<String> st = new TST<>();
        st.put("cat", "v");
        st.put("car", "v");
        st.put("dog", "v");
        assertThat(st.longestPrefixOf("cat"), is("cat"));
    }

    @Test(expected = IllegalArgumentException.class)
    public void longestPrefixOf_throwsIllegalArgumentException() {
        TST<String> st = new TST<>();
        st.longestPrefixOf(null);
    }

    @Test
    public void longestPrefixOf_emptyStringReturnsNull() {
        TST<String> st = new TST<>();
        assertNull(st.longestPrefixOf(""));
    }

    @Test
    public void longestPrefixOf_longerQuery_returnsLongestStoredPrefix() {
        TST<String> st = new TST<>();
        st.put("c", "v1");
        st.put("ca", "v2");
        st.put("cat", "v3");

        assertThat(st.longestPrefixOf("catalog"), is("cat"));
    }

    @Test
    public void longestPrefixOf_noMatchingPrefix_returnsEmptyString() {
        TST<String> st = new TST<>();
        st.put("cat", "v");
        st.put("dog", "v");

        assertThat(st.longestPrefixOf("zzz"), is(""));
    }

    @Test
    public void longestPrefixOf_traversesLeftAndRightBeforeMatch() {
        TST<String> st = new TST<>();
        st.put("m", "mid");
        st.put("a", "left");
        st.put("z", "right");

        assertThat(st.longestPrefixOf("apple"), is("a"));
        assertThat(st.longestPrefixOf("zoo"), is("z"));
    }

    @Test
    public void longestPrefixOf_exactVsPartialPrefersLongest() {
        TST<String> st = new TST<>();
        st.put("a", "v1");
        st.put("ab", "v2");
        st.put("abc", "v3");

        assertThat(st.longestPrefixOf("abacus"), is("ab"));
        assertThat(st.longestPrefixOf("abc"), is("abc"));
    }

    @Test
    public void longestPrefixOf_doesNotUpdateLengthWhenMatchedNodeHasNullValue() {
        TST<String> st = new TST<>();
        st.put("ca", "v");

        assertThat(st.longestPrefixOf("cx"), is(""));
    }
}
