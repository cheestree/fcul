package org.cheese.common

class Task(val runnable: Runnable? = null, val status: TaskStatus = TaskStatus.STANDARD)