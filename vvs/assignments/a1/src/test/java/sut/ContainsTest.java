package sut;

import org.junit.Test;

import static org.hamcrest.core.Is.is;
import static org.junit.Assert.assertThat;

public class ContainsTest {
    @Test
    public void contains_returnsCorrectValue() {
        TST<String> st = new TST<>();
        assertThat(st.contains("cat"), is(false));
    }

    @Test
    public void contains_returnsCorrectValue2() {
        TST<String> st = new TST<>();
        st.put("cat", "v");
        assertThat(st.contains("cat"), is(true));
    }

    @Test(expected = IllegalArgumentException.class)
    public void contains_throwsIllegalArgumentException() {
        TST<String> st = new TST<>();
        st.contains(null);
    }
}
