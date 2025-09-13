package org.cheese.ex01

import java.util.concurrent.Executors
import java.util.concurrent.TimeUnit
import java.util.concurrent.atomic.DoubleAdder

fun trapezoidsRuleSequential(f: (Double) -> Double, a: Double, b: Double, h: Double): Float {
    val n = ((b - a) / h).toInt()
    val sum = (1 until n).sumOf { i -> f(a + i * h) }
    return (h * (0.5 * (f(a) + f(b)) + sum)).toFloat()
}

fun trapezoidsRuleParallelUnsafe(f: (Double) -> Double, a: Double, b: Double, h: Double, nThreads: Int = 4): Float {
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

fun main() {
    val method = {it: Double -> it * (it-1)}
    val lowerBound = 0.0
    val upperBound = 1.0
    val resolution = 10e-7

    val nThreads = 4
    val chunkSize = 1000

    val integralSequential = trapezoidsRuleSequential(method, lowerBound, upperBound, resolution)
    val trapezoidsRuleParallelUnsafe = trapezoidsRuleParallelUnsafe(method, lowerBound, upperBound, resolution, nThreads)
    val trapezoidsRuleParallelSafe = trapezoidsRuleParallelSafe(method, lowerBound, upperBound, resolution, chunkSize)

    println(integralSequential)
    println(trapezoidsRuleParallelUnsafe)
    print(trapezoidsRuleParallelSafe)
}