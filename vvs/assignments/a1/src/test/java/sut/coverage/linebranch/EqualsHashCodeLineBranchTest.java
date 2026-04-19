package sut.coverage.linebranch;

import org.junit.Test;
import sut.TST;

import static org.hamcrest.Matchers.is;
import static org.junit.Assert.assertThat;

public class EqualsHashCodeLineBranchTest {

    @Test
    public void equalsIsReflexiveAndHashCodeStable() {
        // Requirement: line/branch coverage for equals() this==other branch and hashCode().
        TST<String> trie = new TST<>();
        trie.put("cat", "v1");

        assertThat(trie.equals(trie), is(true));
        assertThat(trie.hashCode(), is(trie.hashCode()));
    }

    @Test
    public void equalsReturnsFalseForNullAndDifferentType() {
        // Requirement: line/branch coverage for equals() instanceof false branch.
        TST<String> trie = new TST<>();
        trie.put("cat", "v1");

        assertThat(trie.equals(null), is(false));
        assertThat(trie.equals("not a trie"), is(false));
    }

    @Test
    public void equalsTrueForSameMappingsDifferentInsertionOrder() {
        // Requirement: line/branch coverage for equals() full successful comparison path.
        TST<String> left = new TST<>();
        left.put("cat", "1");
        left.put("dog", "2");

        TST<String> right = new TST<>();
        right.put("dog", "2");
        right.put("cat", "1");

        assertThat(left.equals(right), is(true));
        assertThat(left.hashCode(), is(right.hashCode()));
    }

    @Test
    public void equalsFalseWhenSizesDiffer() {
        // Requirement: line/branch coverage for equals() size mismatch branch.
        TST<String> left = new TST<>();
        left.put("cat", "1");

        TST<String> right = new TST<>();

        assertThat(left.equals(right), is(false));
    }

    @Test
    public void equalsFalseWhenSameSizeButDifferentValues() {
        // Requirement: line/branch coverage for equals() Objects.equals value mismatch branch.
        TST<String> left = new TST<>();
        left.put("cat", "1");

        TST<String> right = new TST<>();
        right.put("cat", "2");

        assertThat(left.equals(right), is(false));
    }

    @Test
    public void equalsFalseWhenSameSizeButDifferentKeys() {
        // Requirement: line/branch coverage for equals() !that.contains(key) branch.
        TST<String> left = new TST<>();
        left.put("cat", "1");

        TST<String> right = new TST<>();
        right.put("dog", "1");

        assertThat(left.equals(right), is(false));
    }
}

