package benchmarks.ex01

import org.cheese.ex01.multiplyMatricesParallel
import org.cheese.ex01.multiplyMatricesSequential
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
import kotlin.random.Random

@Warmup(iterations = 1)
@Measurement(iterations = 2, time = 500, timeUnit = TimeUnit.MILLISECONDS)
@Fork(1)

@OutputTimeUnit(TimeUnit.MILLISECONDS)
@State(Scope.Thread)
open class MultiplyMatricesBenchmark {

    private lateinit var m1: Array<IntArray>
    private lateinit var m2: Array<IntArray>

    @Param("2", "100", "500", "1000")
    var size: Int = 0

    @Param("1", "2", "4", "8", "16")
    var chunkSize: Int = 0

    @Setup(Level.Iteration)
    fun setup() {
        m1 = Array(size) { IntArray(size) { Random.Default.nextInt(0, 10) } }
        m2 = Array(size) { IntArray(size) { Random.Default.nextInt(0, 10) } }
    }

    //  Sequential
    @Benchmark
    @BenchmarkMode(Mode.Throughput)
    fun sequentialThroughput(): Array<IntArray> =
        multiplyMatricesSequential(m1, m2)

    @Benchmark
    @BenchmarkMode(Mode.AverageTime)
    fun sequentialAvgTime(): Array<IntArray> =
        multiplyMatricesSequential(m1, m2)

    //  Parallel
    @Benchmark
    @BenchmarkMode(Mode.Throughput)
    fun parallelThroughput(): Array<IntArray> =
        multiplyMatricesParallel(m1, m2, Runtime.getRuntime().availableProcessors(), chunkSize)

    @Benchmark
    @BenchmarkMode(Mode.AverageTime)
    fun parallelAvgTime(): Array<IntArray> =
        multiplyMatricesParallel(m1, m2, Runtime.getRuntime().availableProcessors(), chunkSize)

    //  Master/Worker
    @Benchmark
    @BenchmarkMode(Mode.Throughput)
    fun parallelThroughputMW(): Array<IntArray> =
        multiplyMatricesParallel(m1, m2, Runtime.getRuntime().availableProcessors(), chunkSize)

    @Benchmark
    @BenchmarkMode(Mode.AverageTime)
    fun parallelAvgTimeMW(): Array<IntArray> =
        multiplyMatricesParallel(m1, m2, Runtime.getRuntime().availableProcessors(), chunkSize)
}