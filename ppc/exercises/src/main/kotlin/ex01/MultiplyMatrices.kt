package org.cheese.ex01

import org.cheese.common.Master
import org.cheese.common.Task
import java.util.concurrent.Executors
import java.util.concurrent.LinkedBlockingQueue
import java.util.concurrent.TimeUnit

fun checkValidMatrix(
    m1: Array<IntArray>
): Boolean {
    val mainRow = m1.first().size
    return m1.all { row -> mainRow == row.size }
}

fun checkValidMultiplication(
    m1: Array<IntArray>,
    m2: Array<IntArray>
) {
    require(checkValidMatrix(m1)) { "Invalid matrix m1" }
    require(checkValidMatrix(m2)) { "Invalid matrix m2" }
    require(m1.first().size == m2.size) { "Invalid matrix dimensions for multiplication" }
}

fun multiplyMatricesSequential(
    m1: Array<IntArray>,
    m2: Array<IntArray>
): Array<IntArray> {
    checkValidMultiplication(m1, m2)

    val rows = m1.size
    val cols = m2.first().size
    val common = m1.first().size
    val result = Array(rows) { IntArray(cols) { 0 } }

    for (i in 0 until rows) {
        for (j in 0 until cols) {
            for (k in 0 until common) {
                result[i][j] += m1[i][k] * m2[k][j]
            }
        }
    }

    return result
}

fun multiplyMatricesParallel(
    m1: Array<IntArray>,
    m2: Array<IntArray>,
    nThreads: Int,
    chunkSize: Int
): Array<IntArray> {
    checkValidMultiplication(m1, m2)

    val rows = m1.size
    val cols = m2.first().size
    val common = m1.first().size
    val result = Array(rows) { IntArray(cols) { 0 } }

    val pool = Executors.newFixedThreadPool(nThreads)

    (0 until rows).chunked(chunkSize).forEach { rowChunk ->
        pool.submit {
            for (i in rowChunk) {
                for (j in 0 until cols) {
                    var sum = 0
                    for (k in 0 until common) {
                        sum += m1[i][k] * m2[k][j]
                    }
                    result[i][j] = sum
                }
            }
        }
    }

    pool.shutdown()
    pool.awaitTermination(1, TimeUnit.MINUTES)

    return result
}

fun multiplyMatricesParallelMW(
    m1: Array<IntArray>,
    m2: Array<IntArray>,
    nThreads: Int,
    chunkSize: Int
): Array<IntArray> {
    checkValidMultiplication(m1, m2)

    val rows = m1.size
    val cols = m2.first().size
    val common = m1.first().size
    val result = Array(rows) { IntArray(cols) { 0 } }

    val tasks = LinkedBlockingQueue<Task>()

    (0 until rows).chunked(chunkSize).forEach { rowChunk ->
        for (i in rowChunk) {
            tasks += Task( {
                for (j in 0 until cols) {
                    var sum = 0
                    for (k in 0 until common) {
                        sum += m1[i][k] * m2[k][j]
                    }
                    result[i][j] = sum
                }
            })
        }
    }

    val master = Master(nThreads, tasks)

    master.killThreads()
    master.joinThreads()

    return result
}