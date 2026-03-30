package sut;

import org.junit.Test;

import static org.hamcrest.core.Is.is;
import static org.junit.Assert.assertThat;

public class SizeTest {
    @Test
    public void size_returnsCorrectValue() {
        TST<String> st = new TST<>();
        assertThat(st.size(), is(0));

        st.put("cat", "v");
        assertThat(st.size(), is(1));

        st.put("cat", "v2");
        assertThat(st.size(), is(1));

        st.put("ca", "prefix");
        assertThat(st.size(), is(2));
    }
}
