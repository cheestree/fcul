package sut.generators;

import com.pholser.junit.quickcheck.generator.GenerationStatus;
import com.pholser.junit.quickcheck.generator.Generator;
import com.pholser.junit.quickcheck.random.SourceOfRandomness;
import sut.TST;

public class TSTGenerator extends Generator<TST<String>> {

    public TSTGenerator() {
        super((Class<TST<String>>) (Class<?>) TST.class);
    }

    @Override
    public TST<String> generate(SourceOfRandomness random, GenerationStatus status) {
        TST<String> tst = new TST<>();
        int entries = random.nextInt(0, 20);

        for (int i = 0; i < entries; i++) {
            String key = randomKey(random);
            String value = randomValue(random, i);
            tst.put(key, value);
        }

        return tst;
    }

    private String randomKey(SourceOfRandomness random) {
        int length = random.nextInt(1, 8);
        StringBuilder sb = new StringBuilder(length);
        for (int i = 0; i < length; i++) {
            sb.append((char) ('a' + random.nextInt(0, 25)));
        }
        return sb.toString();
    }

    private String randomValue(SourceOfRandomness random, int salt) {
        return "v" + salt + "_" + random.nextInt(0, Integer.MAX_VALUE);
    }
}

