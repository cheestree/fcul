package sut;

import org.junit.Test;

import static org.hamcrest.core.Is.is;
import static org.junit.Assert.assertNull;
import static org.junit.Assert.assertThat;

public class GetTest {
    @Test
    public void get_returnsCorrectValue() {
        TST<Integer> tst = new TST<>();
        tst.put("apple", 1);
        tst.put("banana", 2);

        assertThat(tst.get("apple"), is(1));
        assertThat(tst.get("banana"), is(2));
    }

    @Test
    public void get_returnsNullIfKeyDoesNotExist() {
        TST<Integer> tst = new TST<>();
        assertNull(tst.get("apple"));
    }

    @Test(expected = IllegalArgumentException.class)
    public void get_nullThrowsIllegalArgumentException() {
        TST<Integer> tst = new TST<>();
        tst.get(null);
    }

    @Test(expected = IllegalArgumentException.class)
    public void get_emptyKeyThrowsIllegalArgumentException() {
        TST<Integer> tst = new TST<>();
        tst.get("");
    }
}
