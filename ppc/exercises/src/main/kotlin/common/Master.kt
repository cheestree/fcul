package org.cheese.common

import jdk.internal.org.jline.utils.ShutdownHooks
import java.util.LinkedList
import java.util.concurrent.BlockingQueue
import java.util.concurrent.LinkedBlockingQueue

data class Master(val nWorkers: Int, val tasks: LinkedBlockingQueue<Task>) {
    private val threads: ArrayList<Thread> = arrayListOf()

    val finalRunnable = Task(null, TaskStatus.KILL)

    init {
        for (i in 0 until nWorkers) {
            val worker = Worker(tasks)
            val thread = Thread(worker)
            threads.add(thread)
            thread.start()
        }
    }

    fun addTask(runnable: Runnable) {
        val task = Task(runnable)
        tasks.add(task)
    }

    fun killThreads() {
        for (i in threads) {
            tasks  .add(finalRunnable)
        }
    }

    fun joinThreads() {
        for (i in threads) {
            i.join()
        }
    }
}