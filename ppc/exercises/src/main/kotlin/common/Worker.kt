package org.cheese.common

import java.util.concurrent.BlockingQueue
import java.util.concurrent.LinkedBlockingQueue

class Worker(val taskQueue: BlockingQueue<Task> = LinkedBlockingQueue()) : Runnable {
    override fun run() {
        println("Starting " + Thread.currentThread().name)
        try {
            while (!Thread.interrupted()) {
                val task = taskQueue.take()

                if (task.runnable == null || task.status == TaskStatus.KILL) {
                    println("Thread stopped via KILL")
                    break
                }

                task.runnable.run()
            }
        } catch (e: InterruptedException) {
            println("Thread interrupted " + Thread.currentThread().name)
            Thread.currentThread().interrupt()
        }
    }
}