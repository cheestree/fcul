package benchmarks.ex01

import org.cheese.ex01.montePiCarloParallel
import org.cheese.ex01.montePiCarloParallelMW
import org.cheese.ex01.montePiCarloSequential
import org.openjdk.jmh.annotations.*
import java.util.concurrent.TimeUnit

private typealias Point = Pair<Double, Double>

@Warmup(iterations = 1)
@Measurement(iterations = 2, time = 500, timeUnit = TimeUnit.MILLISECONDS)
@Fork(1)

@OutputTimeUnit(TimeUnit.MILLISECONDS)
@State(Scope.Thread)
open class MontePiCarloBenchmark {

    @Param("1")
    var radius: Int = 0

    @Param("1000", "10000", "100000")
    var samples: Int = 0

    @Param("1", "2", "4", "8", "16")
    var nThreads: Int = 0

    @Param("10", "100", "1000")
    var chunkSize: Int = 0

    private lateinit var vertices: Pair<Point, Point>

    @Setup(Level.Iteration)
    fun setup() {
        vertices = Pair(Pair(-1.0, -1.0), Pair(1.0, 1.0))
    }

    //  Sequential
    @Benchmark
    @BenchmarkMode(Mode.Throughput)
    fun sequentialThroughput(): Double =
        montePiCarloSequential(radius, vertices, samples)

    @Benchmark
    @BenchmarkMode(Mode.AverageTime)
    fun sequentialAvgTime(): Double =
        montePiCarloSequential(radius, vertices, samples)

    //  Parallel
    @Benchmark
    @BenchmarkMode(Mode.Throughput)
    fun parallelThroughput(): Double =
        montePiCarloParallel(radius, vertices, samples, nThreads, chunkSize)

    @Benchmark
    @BenchmarkMode(Mode.AverageTime)
    fun parallelAvgTime(): Double =
        montePiCarloParallel(radius, vertices, samples, nThreads, chunkSize)

    //  Master/Worker
    @Benchmark
    @BenchmarkMode(Mode.Throughput)
    fun parallelThroughputMW(): Double =
        montePiCarloParallelMW(radius, vertices, samples, nThreads, chunkSize)

    @Benchmark
    @BenchmarkMode(Mode.AverageTime)
    fun parallelAvgTimeMW(): Double =
        montePiCarloParallelMW(radius, vertices, samples, nThreads, chunkSize)

}