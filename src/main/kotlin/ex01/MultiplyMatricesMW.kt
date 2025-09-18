package org.cheese.ex01

import org.cheese.common.Master
import org.cheese.common.Task
import java.util.concurrent.Executors
import java.util.concurrent.BlockingQueue
import java.util.concurrent.LinkedBlockingQueue

fun multiplyMatricesParallelMW(
    m1: List<List<Int>>,
    m2: List<List<Int>>,
    nThreads: Int,
    chunkSize: Int
): Array<Array<Int>> {
    checkValidMultiplication(m1, m2)

    val rows = m1.size
    val cols = m2.first().size
    val common = m1.first().size
    val result = Array(rows) { Array(cols) { 0 } }

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