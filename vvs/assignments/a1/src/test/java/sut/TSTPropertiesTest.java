package sut;

import com.pholser.junit.quickcheck.From;
import com.pholser.junit.quickcheck.Property;
import com.pholser.junit.quickcheck.generator.InRange;
import com.pholser.junit.quickcheck.runner.JUnitQuickcheck;
import org.junit.Assume;
import org.junit.runner.RunWith;
import sut.generators.TSTGenerator;

import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

@RunWith(JUnitQuickcheck.class)
public class TSTPropertiesTest {

    @Property
    public void insertionOrderOfDifferentKeysDoesNotChangeFinalTreeValue(@From(TSTGenerator.class) TST<String> trie) {
        List<String> keys = new ArrayList<>();
        for (String key : trie.keys()) {
            keys.add(key);
        }

        TST<String> first = new TST<>();
        for (String key : keys) {
            first.put(key, trie.get(key));
        }

        TST<String> second = new TST<>();
        for (int i = keys.size() - 1; i >= 0; i--) {
            String key = keys.get(i);
            second.put(key, trie.get(key));
        }

        assertEquals(first, second);
    }

    @Property
    public void removeAllKeysLeavesTreeEmpty(@From(TSTGenerator.class) TST<String> trie) {
        List<String> keys = new ArrayList<>();
        for (String key : trie.keys()) {
            keys.add(key);
        }

        for (String key : keys) {
            trie.delete(key);
        }

        assertEquals(0, trie.size());
    }

    @Property
    public void insertThenRemoveSameKeyValueKeepsInitialTree(@From(TSTGenerator.class) TST<String> trie,
                                                             @InRange(minInt = 0, maxInt = 1000) int suffix) {
        TST<String> before = copyOf(trie);

        String key = "extra" + suffix;
        while (trie.contains(key)) {
            key = key + "x";
        }

        trie.put(key, "tempValue");
        trie.delete(key);

        assertEquals(before, trie);
    }

    @Property
    public void stricterPrefixReturnsSubset(@From(TSTGenerator.class) TST<String> trie,
                                            @InRange(minInt = 1, maxInt = 5) int cut) {
        List<String> keys = new ArrayList<>();
        for (String key : trie.keys()) {
            if (key.length() >= 2) {
                keys.add(key);
            }
        }

        Assume.assumeTrue(!keys.isEmpty());

        String key = keys.get(Math.abs(cut) % keys.size());
        int split = Math.min(Math.max(1, cut), key.length() - 1);

        String broadPrefix = key.substring(0, split);
        String strictPrefix = key.substring(0, split + 1);

        Set<String> broad = toSet(trie.keysWithPrefix(broadPrefix));
        Set<String> strict = toSet(trie.keysWithPrefix(strictPrefix));

        assertTrue(broad.containsAll(strict));
    }

    private TST<String> copyOf(TST<String> trie) {
        TST<String> copy = new TST<>();
        for (String key : trie.keys()) {
            copy.put(key, trie.get(key));
        }
        return copy;
    }

    private Set<String> toSet(Iterable<String> values) {
        Set<String> result = new HashSet<>();
        for (String value : values) {
            result.add(value);
        }
        return result;
    }
}

