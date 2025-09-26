package ex01

import org.cheese.ex01.trapezoidsRuleParallelSafe
import org.cheese.ex01.trapezoidsRuleSequential
import org.junit.jupiter.api.Test
import kotlin.test.assertEquals
import kotlin.test.assertFailsWith

class TrapezoidsRuleTest {
    private val method = { x: Double -> x * (x - 1) }
    private val lowerBound = 0.0
    private val upperBound = 1.0
    private val resolution = 1e-7

    private val nThreads = 4
    private val chunkSize = 1000

    //  Tolerance for floating-point comparison
    private val tolerance = 1e-6f

    @Test
    fun `should throw IllegalArgumentException when checking validity due to incorrect bounds`() {
        assertFailsWith<IllegalArgumentException>("Bounds must be positive.") {
            trapezoidsRuleSequential(method, upperBound, lowerBound, resolution)
        }
    }

    @Test
    fun `should throw IllegalArgumentException when checking validity due to incorrect resolution`() {
        assertFailsWith<IllegalArgumentException>("Bounds must be positive.") {
            trapezoidsRuleSequential(method, lowerBound, upperBound, 0.0)
        }
    }

    @Test
    fun `should compute correct integral (sequential)`() {
        val expected = -1.0 / 6.0f  //  integral of x*(x-1) from 0 to 1
        val result = trapezoidsRuleSequential(method, lowerBound, upperBound, resolution)
        assertEquals(expected.toFloat(), result, tolerance, "Sequential trapezoid computation is incorrect")
    }

    @Test
    fun `should compute correct integral (safe parallel)`() {
        val expected = -1.0 / 6.0f
        val result = trapezoidsRuleParallelSafe(method, lowerBound, upperBound, resolution, nThreads, chunkSize)
        assertEquals(expected.toFloat(), result, tolerance, "Parallel safe trapezoid computation is incorrect")
    }
}