plugins {
    id("me.champeau.jmh") version "0.7.3"
    kotlin("jvm") version "2.2.0"
}

group = "org.cheese"
version = "1.0-SNAPSHOT"

repositories {
    mavenCentral()
}

dependencies {
    jmh("org.openjdk.jmh:jmh-core:1.37")
    jmh("org.openjdk.jmh:jmh-generator-annprocess:1.37")

    testImplementation(kotlin("test"))
}

tasks.test {
    useJUnitPlatform()
}
kotlin {
    jvmToolchain(21)
}