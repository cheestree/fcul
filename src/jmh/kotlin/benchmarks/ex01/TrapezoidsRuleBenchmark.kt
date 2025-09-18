package benchmarks.ex01

import org.cheese.ex01.trapezoidsRuleParallelSafe
import org.cheese.ex01.trapezoidsRuleParallelSafeMW
import org.cheese.ex01.trapezoidsRuleSequential
import org.openjdk.jmh.annotations.Benchmark
import org.openjdk.jmh.annotations.BenchmarkMode
import org.openjdk.jmh.annotations.Fork
import org.openjdk.jmh.annotations.Level
import org.openjdk.jmh.annotations.Measurement
import org.openjdk.jmh.annotations.Mode
import org.openjdk.jmh.annotations.OutputTimeUnit
import org.openjdk.jmh.annotations.Param
import org.openjdk.jmh.annotations.Scope
import org.openjdk.jmh.annotations.Setup
import org.openjdk.jmh.annotations.State
import org.openjdk.jmh.annotations.Warmup
import java.util.concurrent.TimeUnit

@Warmup(iterations = 1)
@Measurement(iterations = 2, time = 500, timeUnit = TimeUnit.MILLISECONDS)
@Fork(1)

@OutputTimeUnit(TimeUnit.MILLISECONDS)
@State(Scope.Thread)
open class TrapezoidsRuleBenchmark {

    @Param("0.0")
    var lowerBound: Double = 0.0

    @Param("1.0")
    var upperBound: Double = 1.0

    @Param("1e-7", "1e-6", "1e-5")
    var resolution: Double = 1e-7

    @Param("1", "2", "4", "8", "16")
    var chunkSize: Int = 1

    private lateinit var f: (Double) -> Double

    @Setup(Level.Iteration)
    fun setup() {
        f = { x -> x * (x - 1) }
    }

    //  Sequential
    @Benchmark
    @BenchmarkMode(Mode.Throughput)
    fun sequentialThroughput(): Float =
        trapezoidsRuleSequential(f, lowerBound, upperBound, resolution)


    @Benchmark
    @BenchmarkMode(Mode.AverageTime)
    fun sequentialAvgTime(): Float =
        trapezoidsRuleSequential(f, lowerBound, upperBound, resolution)

    //  Parallel
    @Benchmark
    @BenchmarkMode(Mode.Throughput)
    fun parallelThroughput(): Float =
        trapezoidsRuleParallelSafe(f, lowerBound, upperBound, resolution, chunkSize)

    @Benchmark
    @BenchmarkMode(Mode.AverageTime)
    fun parallelAvgTime(): Float =
        trapezoidsRuleParallelSafe(f, lowerBound, upperBound, resolution, chunkSize)

    //  Master/Worker
    @Benchmark
    @BenchmarkMode(Mode.Throughput)
    fun parallelThroughputMW(): Float =
        trapezoidsRuleParallelSafeMW(f, lowerBound, upperBound, resolution, chunkSize)

    @Benchmark
    @BenchmarkMode(Mode.AverageTime)
    fun parallelAvgTimeMW(): Float =
        trapezoidsRuleParallelSafeMW(f, lowerBound, upperBound, resolution, chunkSize)
}