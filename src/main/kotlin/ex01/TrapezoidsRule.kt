package org.cheese.ex01

import java.util.concurrent.Executors
import java.util.concurrent.TimeUnit
import java.util.concurrent.atomic.DoubleAdder


fun checkValidTrapezoid(
    a: Double, b: Double, h: Double,
) {
    require(a < b) { "Bounds must be positive." }
    require(h > 0) { "Resolution must be positive." }
}

fun trapezoidsRuleSequential(f: (Double) -> Double, a: Double, b: Double, h: Double): Float {
    checkValidTrapezoid(a, b, h)

    val n = ((b - a) / h).toInt()
    val sum = (1 until n).sumOf { i -> f(a + i * h) }
    return (h * (0.5 * (f(a) + f(b)) + sum)).toFloat()
}

fun trapezoidsRuleParallelUnsafe(f: (Double) -> Double, a: Double, b: Double, h: Double, nThreads: Int = 4): Float {
    checkValidTrapezoid(a, b, h)

    val n = ((b - a) / h).toInt()
    var sum = 0.0

    val pool = Executors.newFixedThreadPool(nThreads)

    (1 until n).forEach { i ->
        pool.submit {
            sum += f(a + i * h)
        }
    }

    pool.shutdown()
    pool.awaitTermination(1, TimeUnit.MINUTES)

    return (h * (0.5 * (f(a) + f(b)) + sum)).toFloat()
}

fun trapezoidsRuleParallelSafe(
    f: (Double) -> Double,
    a: Double,
    b: Double,
    h: Double,
    nThreads: Int = Runtime.getRuntime().availableProcessors(),
    chunkSize: Int = ((b - a) / h).toInt() / nThreads
): Float {
    checkValidTrapezoid(a, b, h)

    val n = ((b - a) / h).toInt()
    val sum = DoubleAdder()
    val pool = Executors.newFixedThreadPool(nThreads)

    (1 until n).chunked(chunkSize).forEach { chunk ->
        pool.submit {
            var localSum = 0.0
            for (i in chunk) {
                localSum += f(a + i * h)
            }
            sum.add(localSum)
        }
    }

    pool.shutdown()
    pool.awaitTermination(1, TimeUnit.MINUTES)

    return (h * (0.5 * (f(a) + f(b)) + sum.toDouble())).toFloat()
}