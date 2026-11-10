#' Convert Celsius temperatures to Fahrenheit
#'
#' @param celsius A numeric vector of temperatures in degrees Celsius.
#' @Author -
#' @returns A numeric vector of temperatures in degrees Fahrenheit.
#' @export
#' @examples
#' celsius_to_fahrenheit(c(0, 100))
celsius_to_fahrenheit <- function(celsius) {
  celsius * 9 / 5 + 32
}