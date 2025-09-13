package org.cheese.ex01

import java.util.concurrent.Executors
import java.util.concurrent.TimeUnit

fun checkValidMatrix(m1: List<List<Int>>): Boolean {
    val mainRow = m1.first().size
    return m1.all { row -> mainRow == row.size }
}

fun checkValidMatricesCombination(m1: List<List<Int>>, m2: List<List<Int>>) =
    m1.first().size == m2.size

fun checkValidMultiplication(m1: List<List<Int>>, m2: List<List<Int>>): Boolean {
    return checkValidMatrix(m1) &&
            checkValidMatrix(m2) &&
            checkValidMatricesCombination(m1, m2)
}

fun multiplyMatricesSequential(m1: List<List<Int>>, m2: List<List<Int>>): Array<Array<Int>> {
    require(checkValidMultiplication(m1, m2)) { "Invalid matrix" }

    val rows = m1.size
    val cols = m2.first().size
    val common = m1.first().size
    val result = Array(rows) { Array(cols) { 0 } }

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
    m1: List<List<Int>>,
    m2: List<List<Int>>,
    nThreads: Int,
    chunkSize: Int
): Array<Array<Int>> {
    require(checkValidMultiplication(m1, m2)) { "Invalid matrix" }

    val rows = m1.size
    val cols = m2.first().size
    val common = m1.first().size
    val result = Array(rows) { Array(cols) { 0 } }

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

fun main(){
    val m1 = listOf(listOf(1, 2), listOf(3, 4)) //  2×2
    val m2 = listOf(listOf(5, 6), listOf(7, 8)) //  2×2

    val nThreads = 4
    val chunkSize = 2

    val multipliedSequential = multiplyMatricesSequential(m1, m2)
    val multipliedParallel = multiplyMatricesParallel(m1, m2, nThreads, chunkSize)

    println(multipliedSequential.contentDeepToString())
    println(multipliedParallel.contentDeepToString())
}