package sut.generators;

import com.pholser.junit.quickcheck.generator.GenerationStatus;
import com.pholser.junit.quickcheck.generator.Generator;
import com.pholser.junit.quickcheck.random.SourceOfRandomness;
import sut.TST;

public class TSTGenerator extends Generator<TST<String>> {

    private static final String ALPHABET = "abcdef";

    public TSTGenerator() {
        super((Class<TST<String>>) (Class<?>) TST.class);
    }

    @Override
    public TST<String> generate(SourceOfRandomness random, GenerationStatus status) {
        TST<String> trie = new TST<>();
        int entries = random.nextInt(1, 30);

        String[] anchors = new String[] { randomSegment(random, 1, 2), randomSegment(random, 1, 2) };
        for (int i = 0; i < entries; i++) {
            String key = random.nextBoolean()
                    ? anchors[random.nextInt(0, anchors.length - 1)] + randomSegment(random, 0, 4)
                    : randomSegment(random, 1, 6);
            trie.put(key, randomValue(random, i));
        }

        return trie;
    }

    private String randomSegment(SourceOfRandomness random, int minLen, int maxLen) {
        int length = random.nextInt(minLen, maxLen);
        StringBuilder sb = new StringBuilder(length);
        for (int i = 0; i < length; i++) {
            sb.append(ALPHABET.charAt(random.nextInt(0, ALPHABET.length() - 1)));
        }
        return sb.toString();
    }

    private String randomValue(SourceOfRandomness random, int salt) {
        return "v" + salt + "_" + random.nextInt(0, Integer.MAX_VALUE);
    }
}
