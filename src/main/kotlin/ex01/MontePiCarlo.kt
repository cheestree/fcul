package org.cheese.ex01

import java.util.concurrent.Executors
import java.util.concurrent.TimeUnit
import java.util.concurrent.atomic.AtomicInteger
import kotlin.math.pow
import kotlin.random.Random

private typealias Point = Pair<Double, Double>

private fun circleCenter(p1: Point, p2: Point): Pair<Double, Double> {
    require(p1 != p2) { "Points must not be identical" }
    require(p1.first.isFinite() && p1.second.isFinite() &&
            p2.first.isFinite() && p2.second.isFinite()) { "Coordinates must be finite numbers" }
    return Point((p1.first + p2.first) / 2, (p1.second + p2.second) / 2)
}

private fun squaredDistance(center: Point, point: Point): Double {
    return (point.first - center.first).pow(2) + (point.second - center.second).pow(2)
}

fun montePiCarloSequential(radius: Int, vertices: Pair<Point, Point>, samples: Int): Double {
    val center = circleCenter(vertices.first, vertices.second)
    val radiusSquared = radius * radius
    var inside = 0

    repeat(samples) {
        val x = Random.nextDouble(vertices.first.first, vertices.second.first)
        val y = Random.nextDouble(vertices.first.second, vertices.second.second)
        val point = Pair(x, y)

        if (squaredDistance(center, point) <= radiusSquared) {
            inside++
        }
    }

    return 4.0 * inside / samples
}

fun montePiCarloParallel(radius: Int, vertices: Pair<Point, Point>, samples: Int, nThreads: Int = Runtime.getRuntime().availableProcessors(), chunkSize: Int = samples / nThreads): Double {
    val center = circleCenter(vertices.first, vertices.second)
    val radiusSquared = radius * radius
    val inside = AtomicInteger(0)

    val pool = Executors.newFixedThreadPool(nThreads)

    (0 until samples).chunked(chunkSize).forEach { chunk ->
        pool.submit {
            var localInside = 0
            repeat(chunk.size) {
                val x = Random.nextDouble(vertices.first.first, vertices.second.first)
                val y = Random.nextDouble(vertices.first.second, vertices.second.second)
                if (squaredDistance(center, Point(x, y)) <= radiusSquared) {
                    localInside++
                }
            }
            inside.addAndGet(localInside)
        }
    }

    pool.shutdown()
    pool.awaitTermination(1, TimeUnit.MINUTES)

    return 4.0 * inside.get() / samples
}