package ex01

import org.cheese.ex01.montePiCarloParallel
import org.cheese.ex01.montePiCarloSequential
import org.junit.jupiter.api.Assertions.assertTrue
import org.junit.jupiter.api.assertThrows
import kotlin.test.Test

class MontePiCarloTest {
    private val r = 1
    private val vertices = Pair(Pair(-1.0, -1.0), Pair(1.0, 1.0))
    private val samples = 1_000_000

    private val nThreads = 4
    private val chunkSize = 1000

    @Test
    fun `should throw IllegalArgumentException when checking circle center coordinates`() {
        val vertices = Pair(Pair(1.0, 1.0), Pair(1.0, 1.0))

        assertThrows<IllegalArgumentException>("Points must not be identical") {
            montePiCarloParallel(r, vertices, samples)
        }
    }

    @Test
    fun `should reasonably approximate pi value (sequential)`() {
        val piEstimate = montePiCarloSequential(r, vertices, samples)

        assertTrue(piEstimate in 3.13..3.15) // Allow a reasonable tolerance
    }

    @Test
    fun `should reasonably approximate pi value (parallel)`() {
        val piEstimate = montePiCarloParallel(r, vertices, samples, nThreads, chunkSize)

        assertTrue(piEstimate in 3.13..3.15) // Allow a reasonable tolerance
    }
}