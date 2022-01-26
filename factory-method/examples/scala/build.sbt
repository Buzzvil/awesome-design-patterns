ThisBuild / version := "0.1.0-SNAPSHOT"

ThisBuild / scalaVersion := "2.13.8"

lazy val root = (project in file("."))
  .settings(
    name := "factory_method"
  )

libraryDependencies += "org.scalatest" %% "scalatest" % "3.2.10" % "test"
libraryDependencies += "org.scalactic" %% "scalactic" % "3.2.10"

resolvers += "Artima Maven Repository" at "https://repo.artima.com/releases"