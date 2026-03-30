package sut;

import com.pholser.junit.quickcheck.Property;
import com.pholser.junit.quickcheck.runner.JUnitQuickcheck;
import org.jetbrains.annotations.NotNull;
import org.junit.Assume;
import org.junit.Test;
import org.junit.runner.RunWith;

import static org.hamcrest.Matchers.is;
import static org.junit.Assert.assertThat;

@RunWith(JUnitQuickcheck.class)
public class PutTest {
    @Property
    public void put_validKey_accepts(@NotNull String key, String value) {
        Assume.assumeTrue(!key.isEmpty());

        TST<String> st = new TST<>();
        st.put(key, value);
        assertThat(st.get(key), is(value));
    }

    @Test(expected = IllegalArgumentException.class)
    public void put_nullKeyInEmptyTrie_throwsIllegalArgumentException() {
        TST<String> st = new TST<>();
        st.put(null, "v");
    }

    @Test
    public void put_baseChoice_trieEmpty_acceptsNewKey() {
        TST<String> st = new TST<>();
        st.put("cat", "v");
        assertThat(st.get("cat"), is("v"));
    }

    @Test
    public void put_trieAlreadyIncludesKey_replacesValue() {
        TST<String> st = new TST<>();
        st.put("cat", "v1");
        st.put("cat", "v2");
        assertThat(st.get("cat"), is("v2"));
    }

    @Test
    public void put_trieIncludesPrefixOfNewKey_accepts() {
        TST<String> st = new TST<>();
        st.put("ca", "prefix");
        st.put("cat", "word");
        assertThat(st.get("cat"), is("word"));
    }

    @Test(expected = IllegalArgumentException.class)
    public void put_emptyKey_throwsIllegalArgumentException() {
        TST<String> st = new TST<>();
        st.put("", "root");
    }

    @Test
    public void put_newKeySmallest_accepts() {
        TST<String> st = new TST<>();
        st.put("m", "middle");
        st.put("z", "largest");

        st.put("a", "smallest");

        assertThat(st.get("a"), is("smallest"));
        assertThat(st.size(), is(3));
    }

    @Test
    public void put_newKeyLargest_accepts() {
        TST<String> st = new TST<>();
        st.put("a", "smallest");
        st.put("m", "middle");

        st.put("z", "largest");

        assertThat(st.get("z"), is("largest"));
        assertThat(st.size(), is(3));
    }

    @Test
    public void put_newKeyTypical_accepts() {
        TST<String> st = new TST<>();
        st.put("a", "smallest");
        st.put("z", "largest");

        st.put("m", "middle");

        assertThat(st.get("m"), is("middle"));
        assertThat(st.size(), is(3));
    }
}
