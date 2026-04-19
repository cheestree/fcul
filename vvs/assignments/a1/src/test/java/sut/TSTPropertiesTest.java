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
        // Property 1: insertion order of distinct keys must not change the final trie value.
        List<String> keys = keysOf(trie);

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
        // Property 2: deleting every stored key must leave the trie empty.
        for (String key : keysOf(trie)) {
            trie.delete(key);
        }

        assertEquals(0, trie.size());
    }

    @Property
    public void insertThenRemoveSameKeyValueKeepsInitialTree(@From(TSTGenerator.class) TST<String> trie,
                                                             @InRange(minInt = 0, maxInt = 1000) int suffix) {
        // Property 3: adding and then removing the same fresh key should restore the initial trie.
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
    public void stricterPrefixReturnsStrictSubset(@From(TSTGenerator.class) TST<String> trie,
                                                  @InRange(minInt = 0, maxInt = 20) int indexHint) {
        // Property 4: keysWithPrefix(stricter) is a subset of keysWithPrefix(broader), and strict when distinguishable.
        List<String> keys = keysOf(trie);
        Assume.assumeTrue(!keys.isEmpty());

        String key = keys.get(indexHint % keys.size());
        Assume.assumeTrue(key.length() >= 2);

        int split = 1 + (indexHint % (key.length() - 1));
        String broadPrefix = key.substring(0, split);
        String strictPrefix = key.substring(0, split + 1);

        Set<String> broad = toSet(trie.keysWithPrefix(broadPrefix));
        Set<String> strict = toSet(trie.keysWithPrefix(strictPrefix));

        assertTrue(broad.containsAll(strict));

        boolean hasBroadOnlyKey = false;
        for (String candidate : broad) {
            if (!strict.contains(candidate)) {
                hasBroadOnlyKey = true;
                break;
            }
        }

        // Only enforce proper-subset when the generated trie has keys that separate both prefixes.
        Assume.assumeTrue(hasBroadOnlyKey);
        assertTrue(broad.size() > strict.size());
    }

    private List<String> keysOf(TST<String> trie) {
        List<String> keys = new ArrayList<>();
        for (String key : trie.keys()) {
            keys.add(key);
        }
        return keys;
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
