package ex01

import org.cheese.ex01.checkValidMultiplication
import org.cheese.ex01.multiplyMatricesParallel
import org.cheese.ex01.multiplyMatricesSequential
import org.junit.jupiter.api.Test
import org.junit.jupiter.api.assertDoesNotThrow
import kotlin.test.assertEquals
import kotlin.test.assertFailsWith

class MultiplyMatricesTest {
    private val m1 = listOf(listOf(1, 2), listOf(3, 4)) //  2×2
    private val m2 = listOf(listOf(5, 6), listOf(7, 8)) //  2×2
    private val m3 = listOf(listOf(1, 2), listOf(3, 4), listOf(5, 6)) //  3×3

    private val nThreads = 4
    private val chunkSize = 2

    @Test
    fun `should throw IllegalArgumentException when checking validity due to wrong matrix dimensions`() {
        assertFailsWith<IllegalArgumentException>("Invalid matrix dimensions for multiplication") {
            checkValidMultiplication(m1,m3)
        }
    }

    @Test
    fun `should succeed when checking validity with correct matrix dimensions`() {
        assertDoesNotThrow<IllegalArgumentException> {
            return checkValidMultiplication(m1, m2)
        }
    }

    @Test
    fun `should succeed when multiplying matrices (sequential)`() {
        val result = arrayOf(arrayOf(19, 22), arrayOf(43, 50))

        assertEquals(
            multiplyMatricesSequential(m1, m2).contentDeepToString(),
            result.contentDeepToString()
        )
    }

    @Test
    fun `should succeed when multiplying matrices (parallel)`() {
        val result = arrayOf(arrayOf(19, 22), arrayOf(43, 50))

        assertEquals(
            multiplyMatricesParallel(m1, m2, nThreads, chunkSize).contentDeepToString(),
            result.contentDeepToString()
        )
    }
}